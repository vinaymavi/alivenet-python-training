import unittest

class Person(object):
    def set_name(self,name):
        self.name = name

class TestCaseFixture(unittest.TestCase):
    person = None
    def setUp(self):
        print "SETUP CALLING..."
        TestCaseFixture.person = Person()
        TestCaseFixture.person.set_name("Alivenet")

    def test_name(self):
        self.assertEqual(TestCaseFixture.person.name, 'Alivenet')
    
    def tearDown(self):
        print "TEAR DOWN CALLIN...."

if __name__ == '__main__':
    unittest.main()