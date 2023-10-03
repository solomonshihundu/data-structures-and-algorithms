import unittest
from AliceCards import locate_card
from Decorators import time_it

class LocateCardTest(unittest.TestCase):
  
   # Toggle between linear Search and binary search using appropriate method for Test Cases
    @time_it
    def test_1(self): 
        self.assertEqual(locate_card([13, 11, 10, 7, 4, 3, 1, 0],1),6)
    @time_it
    def test_2(self):
        self.assertEqual(locate_card([4, 2, 1, -1],4),0)      
    @time_it
    def test_3(self):
        self.assertEqual(locate_card([3, -1, -9, -127],-127),3)
    @time_it
    def test_4(self):
        self.assertEqual(locate_card([6],6),0)
    @time_it
    def test_5(self):
        self.assertEqual(locate_card([9, 7, 5, 2, -9],4),-1)
    @time_it
    def test_6(self):
        self.assertEqual(locate_card([],7),-1)
    @time_it
    def test_7(self):
        self.assertEqual(locate_card([ 19, 18,14, 14, 11, 11, 8, 8, 5, 3, 3, 1],5),8)
    @time_it
    def test_8(self):
        self.assertEqual(locate_card([ 19, 18, 14, 11, 11, 8, 7, 7, 7, 5, 3, 3, 1],7),6)
    @time_it
    def test_9(self):
        self.assertEqual(locate_card(list(range(0,10000000,1)),9999998),9999998) # test_9 took 1532.8707695007324 mille seconds
   

if __name__ == "__main__":
    unittest.main()