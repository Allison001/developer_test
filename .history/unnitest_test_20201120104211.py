import unittest
from HTMLTestRunner import HTMLTestRunner

class search:
    def search_fun(self):
        print("search")
        return True

class TestCase(unittest.TestCase):
    # def setUp(self):
    #     self.Search = search()
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclseeee")
        cls.Search = search()
    @classmethod
    def tearDownClass(cls) -> None:
        print("the end")

    def test_001(self):
        print("test_001")
        # Search = search()
        assert True == self.Search.search_fun()

    def test_002(self):
        print("test_002")
        # Search = search()
        assert True == self.Search.search_fun()

    def test_003(self):
        print("test_003")
        # Search = search()
        assert True == self.Search.search_fun()

class TestCase1(unittest.TestCase):
    def test_case001(self):
        print("test_case--1")

if __name__ == '__main__':
    # unittest.main()

    suit= unittest.TestSuite()
    suit.addTest(TestCase("test_003"))
    unittest.TextTestRunner().run(suit)
    