import unittest
from AliceCardsBinarySearch import locate_card_binary
from Decorators import time_it

class LocateCardsBinaryTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(locate_card_binary([0,1,3,4,7,10,11,13],1),1)
    def test_2(self):
        self.assertEqual(locate_card_binary([-1,1,2,4],4),3)      
    def test_3(self):
        self.assertEqual(locate_card_binary([-127,-9,-1,3],-127),0)
    def test_4(self):
        self.assertEqual(locate_card_binary([6],6),0)
    def test_5(self):
        self.assertEqual(locate_card_binary([-9, 2, 5, 7, 9],4),-1)
    def test_6(self):
        self.assertEqual(locate_card_binary([],7),-1)
    def test_7(self):
        self.assertEqual(locate_card_binary([ 1, 3, 3, 5, 8, 8, 11, 11, 14, 14, 18, 19],5),3)
    def test_8(self):
        self.assertEqual(locate_card_binary([ 1, 3, 3, 5, 7, 7, 7, 8, 11, 11, 14, 18, 19],7),4) 
    @time_it
    def test_9(self):
        self.assertEqual(locate_card_binary(list(range(0,10000000,1)),9999998),9999998) # test_9 took 482.49197006225586 mille seconds

if __name__ == '__main__':
    unittest.main()