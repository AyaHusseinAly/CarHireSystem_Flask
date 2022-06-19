create database CAR_HIRE_SYSTEM;
use CAR_HIRE_SYSTEM;

CREATE TABLE customers(
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    country VARCHAR(30) NOT NULL,
    city VARCHAR(30) NOT NULL,
    street VARCHAR(30) NOT NULL,
    building VARCHAR(30) NOT NULL,
    register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


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
    hire_date TIMESTAMP NOT NULL,
    return_date TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	customer_id INT(6),
	vehicle_id INT(6),
	FOREIGN KEY (customer_id) REFERENCES customers (id) ,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles (id)

);