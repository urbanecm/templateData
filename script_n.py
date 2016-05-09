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

res = []
for item in data:
	res.append(item[0])

not_in = "("
for item in res:
	not_in += '"' + item + '"' + ", "
not_in = not_in[:len(not_in)-2]
not_in += ")"
query = 'select CONCAT("<li>Šablona:", page_title, "</li>") as title from page where page_title not in ' + not_in + ' and page_namespace=10 and page_title not like "%/doc";'
print query
