import unittest

class TestMain(unittest.TestCase):
    
    def test_location(self):
        a = 'red'
        b = 'red'
        self.assertEqual(a,b) # True b/c strings take up same memory

if __name__ == '__main__':
    unittest.main()




