CREATE TABLE IF NOT EXISTS supplier(
id INTEGER PRIMARY KEY,
phone INTEGER UNIQUE,
address VARCHAR(50),
company_name VARCHAR(50) NOT NULL);

CREATE TABLE IF NOT EXISTS client(
id INTEGER PRIMARY KEY,
name VARCHAR(50) NOT NULL,
phone INTEGER UNIQUE);

CREATE TABLE IF NOT EXISTS pharmacy(
id INTEGER PRIMARY KEY,
address VARCHAR(50),
phone INTEGER UNIQUE);

CREATE TABLE IF NOT EXISTS categories(
id INTEGER PRIMARY KEY,
name VARCHAR(100));

CREATE TABLE IF NOT EXISTS medicines(
id INTEGER PRIMARY KEY,
category_id INTEGER NOT NULL,
name VARCHAR(50) NOT NULL,
price INTEGER NOT NULL,
FOREIGN KEY (category_id) REFERENCES category(id));

CREATE TABLE IF NOT EXISTS list(
id INTEGER PRIMARY KEY,
pharmacy_id INTEGER NOT NULL,
medicines_id INTEGER NOT NULL,
FOREIGN KEY (pharmacy_id) REFERENCES pharmacy(id),
FOREIGN KEY (medicines_id) REFERENCES medicines(id));

CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
login VARCHAR(50) NOT NULL,
password VARCHAR(50) NOT NULL,
power_level INTEGER NOT NULL
)