import unittest
import utils
import SearchDate

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

    def test_SearchDateCreated_TestDateForMatch(self):
        print('Testing TestDateForMatch()...')
        self.assertEqual(SearchDateCreated.TestDateForMatch([4, 3, 2015], ['4/3/2015-4/5/2017']), True)
        self.assertEqual(SearchDateCreated.TestDateForMatch([3, 8, 2019], ['1/1/1970-3/9/2019']), True)
        self.assertEqual(SearchDateCreated.TestDateForMatch([3, 8, 2019], ['4/3/2020-4/18/2025']), False)
        self.assertEqual(SearchDateCreated.TestDateForMatch([9, 4, 2016], ['9/5/2015-9/5/2016']), True)
        self.assertEqual(SearchDateCreated.TestDateForMatch([2, 19, 2024], ['3/15/2024-9/30/2024']), False)
        print('Test of TestDateForMatch() complete!')

if __name__ == '__main__':
    unittest.main()
