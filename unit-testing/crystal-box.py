import unittest
"""
these crystal box unit tests are used when we know how the sys works, useful for regration testing: find the bug when it was working
you evaluate everything: all the different ways(e.g.,if, recursion) that the program operates in its system 
crystal test assume there is alredycode written
"""
class CrystalBox(unittest.TestCase):
    def test_positive(self):
        indexation = Operate()
        result = indexation.is_adult(23)
        self.assertEqual(result,  True)

    def test_false(self):
        indexation = Operate()
        result = indexation.is_adult(12)
        self.assertEqual(result,  False)
        
class Operate():
    def is_adult(self, age):
        if age >=18:
            return True
        else:
            return False
    
if __name__=="__main__":
    unittest.main()