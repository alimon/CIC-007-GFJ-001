CREATE TABLE IF NOT EXISTS appointment (
	id INTEGER PRIMARY KEY,
	id_patient INTEGER,
	id_user INTEGER,
	appt_datetime DATETIME NOT NULL,
	diagnostic TEXT NOT NULL,
	comments TEXT NOT NULL,
	FOREIGN KEY (id_patient) REFERENCES patient(id),
	FOREIGN KEY (id_user) REFERENCES user(id)
);
