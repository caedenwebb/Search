import unittest
import SearchName

class MyTestCase(unittest.TestCase):
    def test_SearchString(self):
        print('Testing SearchString()...')
        self.assertEqual(SearchName.SearchString("Test String", "Test"), True)
        self.assertEqual(SearchName.SearchString("Test String", "t Str"), True)
        self.assertEqual(SearchName.SearchString("Test String", "String"), True)
        self.assertEqual(SearchName.SearchString("Test String", "Tef"), False)
        self.assertEqual(SearchName.SearchString("Test String", "string"), False)
        self.assertEqual(SearchName.SearchString("Test String", "TestString"), False)
        self.assertEqual(SearchName.SearchString("Google Chrome.lnk", "Google"), True)
        self.assertEqual(SearchName.SearchString("Google Drive.lnk", "Google"), True)
        self.assertEqual(SearchName.SearchString("Discord", "cord"), True)

        print('Test of SearchString() complete!')



if __name__ == '__main__':
    unittest.main()
