create database CAR_HIRE_SYSTEM;
use CAR_HIRE_SYSTEM;

CREATE TABLE customers(
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    country VARCHAR(30) NOT NULL,
    city VARCHAR(30) NOT NULL,
    street VARCHAR(30) NOT NULL,
    building VARCHAR(30) NOT NULL,
    register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE INDEX email_indx ON customers(email);



CREATE TABLE vehicles(
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    category ENUM('small_car ', 'family_car', 'van') NOT NULL,      -- small_car / family_car / van
    plate_no VARCHAR(100) NOT NULL UNIQUE,
    model VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

);


CREATE TABLE bookings(
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    booking_type ENUM('in_advance', 'normal'),    -- in advance / normal
    hire_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    return_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	customer_id INT(6) UNSIGNED,
	vehicle_id INT(6) UNSIGNED,
	FOREIGN KEY (customer_id) REFERENCES customers (id) ,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles (id)
);
ALTER TABLE bookings ALTER COLUMN hire_date DROP DEFAULT;    
ALTER TABLE bookings ALTER COLUMN return_date DROP DEFAULT;

CREATE INDEX hire_date_indx ON bookings(hire_date);			-- as it will be used frequently for daily Reports
CREATE INDEX return_date_indx ON bookings(return_date);		-- as it will be used frequently for daily Reports
