import unittest
from GenericBinarySearch import locate_cards_gen
from Decorators import time_it

class LocateCardsGenericTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(locate_cards_gen([0,1,3,4,7,10,11,13],1),1)
    def test_2(self):
        self.assertEqual(locate_cards_gen([-1,1,2,4],4),3)      
    def test_3(self):
        self.assertEqual(locate_cards_gen([-127,-9,-1,3],-127),0)
    def test_4(self):
        self.assertEqual(locate_cards_gen([6],6),0)
    def test_5(self):
        self.assertEqual(locate_cards_gen([-9, 2, 5, 7, 9],4),-1)
    def test_6(self):
        self.assertEqual(locate_cards_gen([],7),-1)
    def test_7(self):
        self.assertEqual(locate_cards_gen([ 1, 3, 3, 5, 8, 8, 11, 11, 14, 14, 18, 19],5),3)
    def test_8(self):
        self.assertEqual(locate_cards_gen([ 1, 3, 3, 5, 7, 7, 7, 8, 11, 11, 14, 18, 19],7),4) 
    @time_it
    def test_9(self):
        self.assertEqual(locate_cards_gen(list(range(0,10000000,1)),9999998),9999998) #test_9 took 328.366756439209 mille seconds


if __name__ == '__main__':
    unittest.main()