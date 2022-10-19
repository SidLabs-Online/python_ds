import unittest
import CC_Hide.CC_Hide_challenge as ccHide


class TestIfList(unittest.TestCase):
    
    # Returns 'ok' if the scanner returns a string.
    def test_the_scanner(self):
        
        self.assertEqual( type(ccHide.mask_cc()), str)
        


if __name__ == '__main__':
   unittest.main()