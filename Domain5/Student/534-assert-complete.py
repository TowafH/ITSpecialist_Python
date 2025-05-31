import unittest

class TestMain(unittest.TestCase):
    
    def test_location(self):
        a = 'red'
        b = 'red'
        self.assertEqual(a,b) # Checks if (a == b), will raise an AssertionErorr if (a != b)

    def test_truth(self):
        self.assertTrue((2 + 5) * 3 == 21) # Checks if the conditional expression evaluates to True, if not an AssertionError

    def test_is(self):
        a = 'red'
        b = 'red'
        self.assertIs(a,b) # Checks if a and b are the same object that takes up the SAME memory, doesn't create new memory

    def test_in(self):
        a = 'red'
        b = ['red','green','blue']
        self.assertIn(a,b) # Checks if a is in b

    #def test_is_instance(self):
        #city = City()
        #self.assertIsInstance(city, City)

if __name__ == '__main__':
    unittest.main()





