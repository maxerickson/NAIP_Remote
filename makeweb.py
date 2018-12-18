#! /usr/bin/env python3

head='''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
</head>
<body>
<p>NAIP has altered the service at <a href="https://gis.apfo.usda.gov/arcgis/rest/services/NAIP">https://gis.apfo.usda.gov/arcgis/rest/services/NAIP</a>
to use a single layer, making this project unnecessary.</p>
'''

foot='''
</body>
</html>'''


s=head
s+=foot
with open("docs/index.html", "w") as f:
	f.write(s)

