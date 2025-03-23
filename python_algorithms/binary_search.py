from math import ceil

def binary_search(myList, item):
    lowValue = 0
    highValue = len(myList) - 1
    
    while lowValue <= highValue:
        middleValue = ceil((lowValue + highValue) / 2)
        guess = myList[middleValue]
        
        if guess == item:
            return middleValue
        if guess > item:
            highValue = middleValue - 1
        else:
            lowValue = middleValue + 1
    return None
    
if __name__ == "__main__":
    myList = [1,3,5,7,9]
    print( 'List index ' + str(binary_search(myList, 5)))
    print( 'List index ' + str(binary_search(myList, -1)))
    