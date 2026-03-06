def bubble_sort(arr: List[Any]) -> List[Any]:
    """
    Bubble sort algorithm implementation.
    """
    # Step 1: Create a copy of the input array
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    # Step 2: Use nested loops to compare adjacent elements
    for i in range(n):
        for j in range(0, n - i - 1):
            
            # Step 3: Swap elements if they're in wrong order
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                
    # Step 4: Return the sorted array
    return arr_copy
