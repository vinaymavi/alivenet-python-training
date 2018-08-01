class MyError(Exception):
    def __init__(self,msg, *args, **kwargs):
        self.message = msg

    def __str__(self):
        return self.message

    
try:
    raise MyError("This is custom exception")
except Exception as e:
    print e
finally:
    print "Finally calling"