class NotAValidAgeExeption(Exception):
    MESSGE = "Age should be Greter then "
    def __init__(self, age,*args, **kwargs):
        self.age = age

    def __str__(self):
        return "Alivenet Error code -2 : {}".format(NotAValidAgeExeption.MESSGE + str(self.age))

def set_age(age):
    if age <18:
        raise NotAValidAgeExeption(age)
try:
    set_age(10)
except NotAValidAgeExeption as e:
    print "Exception = {}".format(e)
