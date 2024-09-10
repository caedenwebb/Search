import unittest
import utils

class MyTestCase(unittest.TestCase):
    def test_SearchString(self):
        print('Testing SearchString()...')
        self.assertEqual(utils.SearchString("Test String", "Test"), True)
        self.assertEqual(utils.SearchString("Test String", "t Str"), True)
        self.assertEqual(utils.SearchString("Test String", "String"), True)
        self.assertEqual(utils.SearchString("Test String", "Tef"), False)
        self.assertEqual(utils.SearchString("Test String", "string"), False)
        self.assertEqual(utils.SearchString("Test String", "TestString"), False)
        self.assertEqual(utils.SearchString("Google Chrome.lnk", "Google"), True)
        self.assertEqual(utils.SearchString("Google Drive.lnk", "Google"), True)
        self.assertEqual(utils.SearchString("Discord", "cord"), True)

        print('Test of SearchString() complete!')



if __name__ == '__main__':
    unittest.main()
