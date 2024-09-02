#!/usr/bin/python

import subprocess
import os

user = subprocess.getoutput("whoami")

if user != "root":
    print("run this file as root")
else:
    with open("encryptor.py", "rb") as app:
        kapp = app.read()

    with open('/usr/bin/dsaencryptor', "wb") as mapp:
        mapp.write(kapp)

    os.system("chmod 755 /usr/bin/dsaencryptor")
    print("installed successfully as dsaencryptor")