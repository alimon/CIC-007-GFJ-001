CREATE TABLE IF NOT EXISTS user_type (
	id INTEGER PRIMERY KEY,
	description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS user (
	id INTEGER PRIMARY KEY,
	id_type INTEGER,
	name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	user_name TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
	active INTEGER NOT NULL DEFAULT 1,
	FOREIGN KEY (id_type) REFERENCES user_type(id)
);

INSERT INTO user_type VALUES(1, "Admin");
INSERT INTO user_type VALUES(2, "Physician");
INSERT INTO user_type VALUES(3, "Reviewer");

INSERT INTO user VALUES(1, 1, "Anibal", "Limon Belmares", "alimon_admin", "notcryptpass", 1);
INSERT INTO user VALUES(2, 2, "Anibal", "Limon Belmares", "alimon_phy", "notcryptpass", 1);
INSERT INTO user VALUES(3, 3, "Anibal", "Limon Belmares", "alimon_rev", "notcryptpass", 1);
