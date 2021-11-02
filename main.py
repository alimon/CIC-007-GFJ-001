#!/usr/bin/env python3

import os
import sys

CURRENT_DIR = os.getcwd()
DATABASE_FILE = os.path.join(CURRENT_DIR, "main.db")

diagnostics_supported = { 
        "Influenza" : os.path.join(CURRENT_DIR, "diagnostics/cold_influenza")
}
diagnostics_list = [ "Influenza" ]

if __name__ == '__main__':
    sys.path.append(diagnostics_supported["Influenza"])
    import driver
    driver.run()
