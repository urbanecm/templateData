#!/usr/bin/env python
#-*- coding: utf-8 -*-

from wmflabs import db
conn = db.connect("cswiki")

query_file = open("sql_y", "r")
query = query_file.readlines()[0]
cur = conn.cursor()
with cur:
	cur.execute(query)
	data = cur.fetchall()

print "<ol>"
for item in data:
	print "<li>"+item[0] + "</li>"
print "</ol>"
