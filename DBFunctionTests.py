import unittest
from DBFunction import createCustomer, createOrder, retrieveAll

#dummy testing failing parameter 
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_dummy_case(self):
        print("testing parameter")
        self.assertEqual(createOrder("Fifteen", "Twelve"), "broken")

class testDBFunctions(unittest.TestCase):
    #stub
    def test_stub_insertion(self):
         print("testing insertion of stub")
         self.assertEqual(createCustomer("Johny", 15), 0)

    #mock
    #tests the retrieve function after the test of insertion to make sure insert was sucessfull
    def test_retrieve(self):
        print("testing retrieve")
        self.assertEqual(retrieveAll(), [(6, 'Albert', 13), (7, 'James', 3), (8, 'Kevin', 5), (9, 'Eric', 16), (10, 'David', 21), (24, 'Johny', 15)])
        
if __name__ == '__main__':
    unittest.main()