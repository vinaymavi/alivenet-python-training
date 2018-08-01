import json
#import numpy
json_file = open('data.json')
json_str = json_file.read()
data = json.loads(json_str)
print data