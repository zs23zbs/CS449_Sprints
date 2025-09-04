import searchAlgor

"""Notes to Self:
* Using Python 3.9.6 for pytest to work, DON'T CHANGE Python: Select Interpreter 
* command specifically for interpreter, executing the pytests is "pytest" itsef. 
* command+Shift+P for fast track on terminal """

class Test_Linear_Search: # Pass
    def test_small_range(self):
        result = searchAlgor.LinearSearchAlgor(2, range(1,3))
        assert result, 1

    def test_large_range(self): # Pass
        result = searchAlgor.LinearSearchAlgor(88, range(23, 125))
        assert result, 65

    def test_key_not_found(self): # Pass
        result = searchAlgor.LinearSearchAlgor(67, range(78, 170))
        assert result == print(result)

class Test_Binary_Search:
    def test_small_(self): # Pass
        list = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        first_element = list[0]
        sort_list = sorted(list)
        low = list.index(first_element)
        high = len(list) - 1

        result = searchAlgor.BinarySearchAlgor(sort_list, 20, low, high)
        assert result, 5
    
    def test_large_range(self): # Pass
        list = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 34, 45, 67, 89, 94, 101, 120, 495, 283, 596, 294, 300, 319, 314, 3, 6, 8]
        first_element = list[0]
        sort_list = sorted(list)
        low = list.index(first_element)
        high = len(list) - 1

        result = searchAlgor.BinarySearchAlgor(sort_list, 596, low, high)
        assert result, 32
    
    def test_no_key_found(self):  # Pass
        list = [45, 684, 283, 749, 8, 10, 293]
        first_element = list[0]
        sort_list = sorted(list)
        low = list.index(first_element)
        high = len(list) - 1

        result = searchAlgor.BinarySearchAlgor(sort_list, 1, low, high)
        assert result == print(result)