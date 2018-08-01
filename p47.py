def set_age(age):
    if age < 18:
        raise Exception("Age should be greter then 18")

try:
    set_age(1)
except Exception as e:
    print "EXCEPTION {}".format(e)


