#! /usr/bin/env python3

head='''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
</head>
<body><p>Click below to add a layer to JOSM. Remote Control
must be enabled and setup for https.</p>
<p>To save a layer to the JOSM imagery menu, right click the 
layer in the JOSM "Layers" window and select "Set WMS Bookmark".</p>
<p>Visit <a href="https://gis.apfo.usda.gov/arcgis/rest/services/NAIP">https://gis.apfo.usda.gov/arcgis/rest/services/NAIP</a>
for more information about a given layer.</p>
'''

foot='''
<script>
handleClick=function(e){
  e.preventDefault();
  e.stopPropagation();
  req = new XMLHttpRequest();
  req.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200) {
      var pop=document.createElement('div');
      pop.style.position="fixed";
      pop.style.top="10px";
      pop.style.left="50%";
      pop.style.padding="10px";
      pop.style.backgroundColor="white";
      pop.style.outline="black solid thick";
      pop.innerHTML="Done";
      document.body.appendChild(pop);
      setTimeout(function(){document.body.removeChild(pop)}, 1500);
    };
  };
  req.open('GET', e.target.href, true);
  req.send(null);
};
links=document.getElementsByClassName("im");
for(var i=0; i<links.length; i++){
  links[i].addEventListener("click", handleClick, "false");
}
</script>
</body>
</html>'''

linktmpl='<a class="im" href="https://127.0.0.1:8112/imagery?title={slug}&type=wms&url=https://gis.apfo.usda.gov/arcgis/services/NAIP/{slug}/ImageServer/WMSServer?FORMAT=image/jpeg&VERSION=1.1.1&SERVICE=WMS&REQUEST=GetMap&LAYERS=0&STYLES=&SRS={{proj}}&WIDTH={{width}}&HEIGHT={{height}}&BBOX={{bbox}}">{slug}</a></br>'

s=head
with open("slugs") as f:
	for line in f:
		if line.startswith("NAIP"):
			pass
		else:
			s+=linktmpl.format(slug=line)
s+=foot
with open("docs/index.html", "w") as f:
	f.write(s)

