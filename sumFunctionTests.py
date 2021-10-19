import unittest
from sumFunction import sumIntegers

#dummy testing failing parameter 
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_dummy_case(self):
        print("testing parameter")
        self.assertEqual(sumIntegers("C:\\Users\\Daniel Shin\\Desktop\\TestDoubles\\TestDoubles\\NonExistentFile.txt"), "broken")

class testSum(unittest.TestCase):
    #main case adds even numbers from 2 to 14
    def test_main_case(self):
        print("testing MainTest.txt")
        self.assertEqual(sumIntegers("C:\\Users\\Daniel Shin\\Desktop\\TestDoubles\\TestDoubles\\MainTest.txt"), 56)

    #stub case carries 6 ones
    def test_stub_case(self):
        print("testing Stub.txt")
        self.assertEqual(sumIntegers("C:\\Users\\Daniel Shin\\Desktop\\TestDoubles\\TestDoubles\\Stub.txt"), 6)

    #mock case will always pass as there is one value, therefore having the output equal the sum
    def test_mock_case(self):
        print("testing MainTest.txt")
        self.assertEqual(sumIntegers("C:\\Users\\Daniel Shin\\Desktop\\TestDoubles\\TestDoubles\\Mock.txt"), 28)
        
if __name__ == '__main__':
    unittest.main()