import unittest
"""
these black box unit tests are used when we don't know how the sys works
you just evaluate the input and the output
test driven development: first u make the tests and after you make the program
"""
class BlackBox(unittest.TestCase):
    def test_positive(self):
        num_1 = 10 
        num_2 = 5
        # u should make an instance of a func into a variable to test it
        cases = Case()
        res = cases.sum(num_1, num_2)
        # This is how it works, the variable and the result it should give u
        self.assertEqual(res, 15)  
        
    def test_neggative(self):
        num_1 = -10 
        num_2 = -7
        # u should make an instance of a func into a variable to test it
        cases = Case()
        res = cases.sum(num_1, num_2)
        # This is how it works, the variable and the result it should give u
        self.assertEqual(res, -17)      

class Case():
    def sum(self, n1,n2):
        return n1+n2

if __name__ =="__main__":
    
    unittest.main()