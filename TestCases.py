import searchAlgor

class Test_Linear_Search():
    def test_small_range(self):
        result = searchAlgor.LinearSearchAlgor(2, range(1,3))
        assert result, 1