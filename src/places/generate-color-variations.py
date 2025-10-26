#!/usr/bin/python3
import os

# This script uses src.svg and generates svg files for each defined color
# It uses the following color table to do so:

SRC = {"folder":"eeca8f","backfolder":"c89e6b","paper":"e8e8e8","emblem":"575757"}
VARIANTS = []

# Blue
VARIANTS.append({"name":"Pear","folder":"96ad52","backfolder":"6d941e","paper":"e4e4e4","emblem":"2f3e1f"})

for filename in os.listdir("."):
    if filename.endswith(".svg"):
        if filename not in ["extra.svg", "src.svg"]:
            os.remove(filename)

for variant in VARIANTS:
    name = variant["name"]
    os.system(f"cp src.svg {name}.svg")
    for key in SRC.keys():
        src_color = SRC[key]
        color = variant[key]
        if src_color != color:
            os.system("sed -i 's/%s/%s/g' %s.svg" % (src_color, color, name))
