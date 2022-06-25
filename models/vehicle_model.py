from datetime import datetime
from app_config import mysql


class Vehicle():

    def __init__(self, id= None, category= None, plate_no= None, model= None, created_at= None, updated_at= None):
        self.id = id
        self.category = category
        self.plate_no = plate_no
        self.model = model
        self.created_at = created_at
        self.updated_at = updated_at


    @classmethod
    def find(cls, id):
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM VEHICLES WHERE id = {id}") 
        vehicle = cur.fetchone()
        cur.close()   
        if vehicle:
            return Vehicle(*vehicle)

        return None
    
    @classmethod
    def create(cls, data):
        cur = mysql.connection.cursor()
        vehicle = cls.find_by_plate_no(data['plate_no'])
        if not vehicle:
            cur.execute("INSERT INTO VEHICLES(category, model, plate_no) VALUES (%s,%s,%s)",
                        (data['category'], data['model'], data['plate_no'])
                        )     
            mysql.connection.commit()
            id = cur.lastrowid
            cur.close()
            return Vehicle(
                        id = id,
                        category = data['category'],
                        model = data['model'],
                        plate_no = data['plate_no'],
                        created_at = datetime.now(),
                        updated_at = datetime.now()
                        ) 
        
        return vehicle

    @classmethod
    def update(cls, id, data):
        cur = mysql.connection.cursor()
        q = "UPDATE VEHICLES SET "
        for k, v in data.items():
            q += f"{k} = '{v}' , "
        query = q[:-2]                    # remove last char => ","
        query += f"WHERE id = {id}"

        cur.execute(query) 
        mysql.connection.commit()
        affected_row = cur.rowcount
        cur.close()     
        if not affected_row:
            return None
        return 'updated'  


    @classmethod
    def delete(cls, id):
        cur = mysql.connection.cursor()
        cur.execute(f"DELETE FROM VEHICLES WHERE id = {id}") 
        mysql.connection.commit()
        affected_row = cur.rowcount
        cur.close()     
        if not affected_row:
            return None
        return 'deleted'  

    @classmethod
    def find_by_plate_no(cls, plate_no):
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM VEHICLES WHERE plate_no = '{plate_no}'") 
        vehicle = cur.fetchone()
        cur.close()  
        print(vehicle) 
        if vehicle:
            return Vehicle(*vehicle)

        return None

    @classmethod
    def find_by(cls, col_val_dict):
        cur = mysql.connection.cursor()
        q = "SELECT * FROM VEHICLES WHERE "
        for k, v in col_val_dict.items():
            q += f"{k} = '{v}' and "
        query = q[:-4]                    # remove last "and"
        cur.execute(query)         
        vehicles = cur.fetchall()
        vehicles_arr = [Vehicle(*vehicle) for vehicle in vehicles]
        cur.close()   
        if len(vehicles_arr) !=0:
            return vehicles_arr

        return []