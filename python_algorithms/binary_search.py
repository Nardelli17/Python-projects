def binary_search(my_list, item):
    """
    Perform binary search on a sorted list.

    Args:
        my_list (list): A sorted list of elements.
        item (any): The element to search for.

    Returns:
        int: Index of the item if found, otherwise None.
    """
    low = 0
    high = len(my_list) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Integer division
        guess = my_list[mid]
        
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None  # Element not found

def run_tests():
    """Run test cases for binary_search."""
    test_cases = [
        ([1, 3, 5, 7, 9], 5, 2),  # Middle element
        ([1, 3, 5, 7, 9], 1, 0),  # First element
        ([1, 3, 5, 7, 9], 9, 4),  # Last element
        ([1, 3, 5, 7, 9], -1, None),  # Element smaller than min
        ([1, 3, 5, 7, 9], 10, None),  # Element greater than max
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, 5),  # Larger list
        ([1], 1, 0),  # Single-element list (found)
        ([1], 2, None),  # Single-element list (not found)
        ([], 5, None),  # Empty list
    ]

    for i, (lst, target, expected) in enumerate(test_cases, 1):
        result = binary_search(lst, target)
        assert result == expected, f"Test {i} failed: Expected {expected}, got {result}"
        print(f"Test {i} passed ✅")

if __name__ == "__main__":
    run_tests()

    