from datetime import datetime
from db_config import mysql

class Customer():
    def __init__(self, id= None, full_name= None, phone= None, email= None, country= None, city= None, street= None, building= None, register_date= None, updated_at= None):
        self.id = id
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.country = country
        self.city = city
        self.street = street
        self.building = building
        self.register_date = register_date


    @classmethod
    def find(cls, id):
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM CUSTOMERS WHERE id = {id}") 
        customer = cur.fetchone()
        cur.close()   
        if customer:
            return Customer(*customer)

        return None
    
    @classmethod
    def create(cls, data):
        cur = mysql.connection.cursor()
        customer = cls.find_by_email(data['email'])
        if not customer:
            cur.execute("INSERT INTO CUSTOMERS(full_name, phone, email, country, city, street, building) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (data['full_name'], data['phone'], data['email'], data['country'],data['city'], data['street'], data['building'])
                        )     
            mysql.connection.commit()
            id = cur.lastrowid
            cur.close()
            
            return Customer(
                        id = id,
                        full_name = data['full_name'],
                        phone = data['phone'],
                        email = data['email'],
                        country = data['country'],
                        city = data['city'],
                        street = data['street'],
                        building = data['building'],
                        register_date = datetime.now(),
                        ) 
        
        return customer

    @classmethod
    def update(cls, id, data):
        cur = mysql.connection.cursor()
        q = "UPDATE CUSTOMERS SET "
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
        cur.execute(f"DELETE FROM CUSTOMERS WHERE id = {id}") 
        mysql.connection.commit()
        affected_row = cur.rowcount
        cur.close()     
        if not affected_row:
            return None
        return 'deleted'  

    @classmethod
    def find_by_email(cls, email):
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM CUSTOMERS WHERE email = '{email}'") 
        customer = cur.fetchone()
        cur.close()  
        print(customer) 
        if customer:
            return Customer(*customer)

        return None

    @classmethod
    def find_by(cls, col_val_dict):
        cur = mysql.connection.cursor()
        q = "SELECT * FROM CUSTOMERS WHERE "
        for k, v in col_val_dict.items():
            q += f"{k} = '{v}' and "
        query = q[:-4]                    # remove last "and"
        cur.execute(query)         
        customers = cur.fetchall()
        customers_arr = [Customer(*customer) for cutomer in customers]
        cur.close()   
        if len(customer) !=0:
            return customers_arr

        return []