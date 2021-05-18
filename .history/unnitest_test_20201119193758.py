import unittest
class search:
    def search_fun(self):
        print("search")
        return True

class TestCase(unittest.TestCase):
    # def setUp(self):
    #     self.Search = search()
    @classmethod
    def setUpClass(cls) -> None:
        print("setup cal")
        cls.Search = search()

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

if __name__ == '__main__':
    unittest.main()
    