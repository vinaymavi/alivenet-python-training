import json
print "PROGRAM START"
try:
    json_file = open('data_1.json')
    json_str = json_file.read()
    data = json.loads(json_str)
    print data
except ValueError as e:
    print "Value Error = {}".format(e)
except IOError as e:
    print "IO {}".format(e)
finally:
    print "FINALLY"

print "PROGRAM COMPLETED"