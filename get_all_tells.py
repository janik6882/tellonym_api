# -*- coding: utf-8 -*-
import json
from Main_Wrapper import Wrapper
creds = json.load(open("creds.json", "r"))
poi = json.load(open("interest.json", "r"))
api = Wrapper(creds["token"])
x = api.get_details_name(poi["poi"][2], pos=0, limit=31)
print (x)
with open("out.json", "w") as f:
    json.dump(x, f)
