#!/usr/bin/python3
import os
import datetime
database =""
day      = datetime.datetime.now().strftime("%d-%m-%y")
nameDump = "dumpe"+day


var = "mysqldump  {0} > {1}.sql".format(database,nameDump)


os.system(var)