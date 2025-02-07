def find_missing_numbers(arr):
    if not arr:
        return []  
    start = arr[0]
    end = arr[-1]
    missing_numbers = []
    num = start
    while num <= end:
        if num not in arr:
            missing_numbers.append(num)
        num += 1
    return missing_numbers