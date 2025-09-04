import searchAlgor

# Using Python 3.9.6 for pytest to work, DON'T CHANGE Python: Select Interpreter 
# command specifically for interpreter, executing the pytests is "pytest" itsef. 
# command+Shift+P for fast track on terminal 

class Test_Linear_Search: # Pass
    def test_small_range(self):
        result = searchAlgor.LinearSearchAlgor(2, range(1,3))
        assert result, 1

    def test_large_range(self): # Pass
        result = searchAlgor.LinearSearchAlgor(88, range(23, 125))
        assert result, 65

    def test_key_not_found(self):
        result = searchAlgor.LinearSearchAlgor(67, range(78, 170))
        assert "None"