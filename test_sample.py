import searchAlgor

class Test_Linear_Search:
    def test_small_range(self):
        result = searchAlgor.LinearSearchAlgor(2, range(1,3))
        assert result, 1

    def test_large_range(self):
        result = searchAlgor.LinearSearchAlgor(88, range(23, 125))
        assert result, 65