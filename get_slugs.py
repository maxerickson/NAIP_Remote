#! /usr/bin/env python3

import json
import urllib.request

naipurl="https://gis.apfo.usda.gov/arcgis/rest/services/NAIP?f=pjson"

with urllib.request.urlopen(naipurl) as url:
	js=json.loads(url.read())
	with open('slugs', 'w') as f:
		for s in js['services']:
			f.write(s['name'][5:]+'\n')