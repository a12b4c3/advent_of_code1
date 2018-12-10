import d3p1v2
import d3p1
import unittest


class TestDay3Part1Methods(unittest.TestCase):

    def test_1(self):
        # expect 2 pieces to overlap
        print("running test 1...")
        print("exoect 2 pieces to overlap")
        d3p1v2.main("d3s1.txt")
        print()
        print()


    def test_2(self):
        # expect no pieces to overlap
        print("running test 2...")
        print("expect 0 pieces to overlap")
        d3p1v2.main("d3s2.txt")
        print()
        print()

    def test_3(self):
        # expect 2 pieces to overlap
        print("running test 3...")
        print("expect 2 pieces to overlap")
        d3p1v2.main("d3s3.txt")
        print()
        print()


    def test_4(self):
        # expect 3 pieces to overlap
        print("running test 4...")
        print("expect 3 pieces to overlap")
        d3p1v2.main("d3s4.txt")
        print()
        print()


    def test_overlap_checker(self):
        #no overlap adjacent
        self.assertFalse(d3p1.overlap_checker(1, 1, 3, 3, 1, 3, 3, 5))
        #no overlap not adjacent
        self.assertFalse(d3p1.overlap_checker(1, 1, 3, 3, 4, 4, 6, 6))
        #overlap on y
        self.assertTrue(d3p1.overlap_checker(1, 1, 3, 3, 1, 2, 3, 4))
        #overlap on x
        self.assertTrue(d3p1.overlap_checker(1, 1, 3, 3, 2, 2, 5, 5))




if __name__ == "__main__":
    unittest.main()