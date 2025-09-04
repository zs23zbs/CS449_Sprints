#Needed Imports 
from datetime import datetime #setting execution time 
import random #generating a random list 

#parameters for generating a random list 
min_size = 10 #mini number of elements a list could have 
max_size = 2000 #max number of elements a list could have 
min_value = 1 #smallest number an element could be 
max_value = 1999 #largest number an element could be 

#function for creating random list  
def generate_random_list (min_size, max_size, min_value, max_value):
    size = random.randint(min_size, max_size) #returns a random size integers from specified range 
    return [random.randint(min_value, max_value) for _ in range(size)] #create a random list of integers depending on the random size

#generate the random list 
random_list = generate_random_list(min_size, max_size, min_value, max_value)

#pick a random interger as target to search 
key = random.choice(random_list)

'''Linear Search Algorithm: Iterates through array and searches one by one for the desired key'''
def LinearSearchAlgor(key, random_list):
    iterations = 0 #keep track of passes to search for key 
    for i in range(len(random_list)): #iterate through the length of list 
        if random_list[i] == key: #if element in list equals the key
            return i #return index of key in list 
        else:
            iterations += 1
    return None


'''Binary Search Algorithm: Divides the array by the midpoint until it arrives at the desired key'''
def BinarySearchAlgor(sort_list, key, low, high):
    if low > high: #if first index is greater than last index 
        return None
    else: 
        midpoint = ((low+high) //2 ) 
        #find the lower ceiling midpoint (index)
        if sort_list[midpoint] == key: #if midpoint equals the key 
            return midpoint #return the index of the found key
        elif key not in sort_list: #if key is not in list 
            return None
        elif key < sort_list[midpoint]: #if the key is less than midpoint in list 
            return BinarySearchAlgor(sort_list, key, low, midpoint - 1) #recursively call function 
        else:
            return BinarySearchAlgor(sort_list, key, midpoint + 1, high)
        
        
if __name__ == '__main__':
    print()

    # Source code from GeeksForGeeks (Execution Time)
    #timer for LinearSearchAlgor
    start_time_linear = datetime.now()
    linear_result = LinearSearchAlgor(key, random_list)
    end_time_linear = datetime.now()
    linear_execution = (end_time_linear - start_time_linear).total_seconds() * 10**3 

    #print linear search algorithm out and execution time
    print(f"Array Size: {len(random_list)}\n")

    print(f"The key algorithms search for: {key}\n")
    
    print(f"Linear Search Result: {linear_result}")
    print(f"Execution time for Linear Search Algorithm: {linear_execution:.03} ms\n")


    #timer for sorting BinarySearchAlgor
    start_time_sort = datetime.now()

    #set parameters for Binary Search Algorithm 
    low = 0 #get index of the first elemetn in list 
    high = len(random_list) - 1 #get index of the last element in the list 
    sort_list = sorted(random_list)  # Sorting the list


    end_time_sort = datetime.now()
    sort_time = (end_time_sort - start_time_sort).total_seconds() * 10**3  


    #timer for BinarySearchAlgor
    start_time_binary = datetime.now()
    binary_result = BinarySearchAlgor(sort_list, key, low, high)
    end_time_binary = datetime.now()
    binary_execution = (end_time_binary - start_time_binary).total_seconds() * 10**3

    # Total time for Binary Search (including sorting)
    total_binary_time = sort_time + binary_execution

    #print binary search algorithm out and execution time
    print(f"Binary Search Result: {binary_result}")
    print(f"Execution time for Sorting: {sort_time:.03f} ms")
    print(f"Execution time for Binary Search Algorithm: {binary_execution:.03f} ms\n")
    print(f"Total time for Binary Search (including sorting): {total_binary_time:.03f} ms\n")

    # Source code from GeeksForGeeks (Execution Time)
    #timer for program execution time 
    start = datetime.now()
    a = 0
    for i in range(1000):
        a += (i * 100)
    end = datetime.now()
    time = (end - start).total_seconds() * 10**3
    print(f"Timer of Program Execution is: {time:.03f} ms\n")