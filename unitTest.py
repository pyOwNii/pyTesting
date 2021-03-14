
import unittest

# Testar en simpel addition

def addition(x,y):
    z = x + y
    return z

class testAddition(unittest.TestCase):
    def testAddition(self):
        # Viktigt att komma ihåg att vid unittest så testar vi mot en expected outcome.
        # Addition, the inputs against the expected outcome
        self.assertEqual(addition(50,50), 100)

if __name__ == '__main__':
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#Integration Test

#End to End tests

#Larger Automated Tests