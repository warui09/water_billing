DROP TABLES IF EXISTS user;
DROP TABLES IF EXISTS user_details;
DROP TABLES IF EXISTS readings;

CREATE TABLE user(
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	user_name TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL
);

CREATE TABLE user_details(
	id INTEGER PRIMARY KEY,
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	meter_number INTEGER NOT NULL,
	FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE readings(
	readings_id INTEGER PRIMARY KEY,
	user_id INTEGER,
	reading_date DATE,
	value DECIMAL(10, 2),
	FOREIGN KEY (user_id) REFERENCES user(user_id)
);

