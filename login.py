#!/usr/bin/env python

import kf5py

conn = kf5py.connection('http://localhost:8080/kforum/','you','yourpassword')
if conn.is_valid():
    print "Ok!"
else:
    print "Error!"
