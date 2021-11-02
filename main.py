#!/usr/bin/env python3

import os
import sys
import sqlite3
import getpass

CURRENT_DIR = os.getcwd()
DATABASE_FILE = os.path.join(CURRENT_DIR, "main.db")

diagnostics_supported = { 
        "Influenza" : os.path.join(CURRENT_DIR, "diagnostics/cold_influenza"),
        "Fiebre tifoidea" : os.path.join(CURRENT_DIR, "diagnostics/typhoid_fever")
}
diagnostics_list = [ "Influenza", "Fiebre tifoidea" ]

def _validate_user(db_conn, username, password):
    cur = db_conn.cursor()
    user_cur = cur.execute("SELECT user.name, user.last_name, user.active, user_type.description FROM user JOIN user_type ON user.id_type = user_type.id WHERE user.user_name = '{}' and user.password = '{}';".format(username, password))
    user_data = user_cur.fetchall()
    if len(user_data):
        return user_data[0]

    return None

if __name__ == '__main__':
    db_conn = sqlite3.connect(DATABASE_FILE)

    print("Sistema experto de diagnostico de enfermedades")
    print("")

    username = input("Ingresa el nombre de usuario: ")
    password = getpass.getpass("Ingresa la contrasena: ")

    user = _validate_user(db_conn, username, password)
    if not user:
        print("Usuario o contrasena invalidos")
        sys.exit(1)
    # Is user active?
    if not user[2]:
        print("Usuario inactivo")
        sys.exit(1)

    print("Usuario: {} {}, Tipo {}".format(user[0], user[1], user[3]))

    print()
    print("Selecciona la posible enfermedad a diagnosticar:")
    idx = 1
    for diagnostic in diagnostics_list:
        print("{}. {}".format(idx, diagnostic))
        idx = idx + 1
    print()

    idx = int(input())
    if idx < 0 or idx > len(diagnostics_list) + 1:
        print("Enfermedad a diagnosticar invalida")
        sys.exit(1)

    sys.path.append(diagnostics_supported[diagnostics_list[idx - 1]])
    import driver
    driver.run()
    sys.exit(0)
