# Binary Search 

list = [2, 4, 9, 10, 15, 50]

def binary_search(list, target):
    low = 0
    high = len(list) -1
    
    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else: 
            low = mid + 1
    return None

print(binary_search(list, 4))
