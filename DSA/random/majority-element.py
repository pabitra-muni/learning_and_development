# given an arry of integers, find the majority element or highest frequency element.
# the highest frequency item is more than n/2

def majorityElement(numbers: list[int]):
    numbers.sort()
    print(numbers)
    majorityElement = numbers[0]
    maxCount = 0
    curCount = 1

    for i in range(len(numbers) - 1):
        if numbers[i] != numbers[i+1]:
            if maxCount < curCount:
                majorityElement = numbers[i]
                maxCount = curCount
                curCount = 1
        else:
            curCount += 1

    # below condition handles edge case where the largest value is the majority.
    # In this case condition at line #13 will always be false
    if maxCount < curCount:
        majorityElement = numbers[-1]
        maxCount = curCount
    print('majority element is', majorityElement, 'with count', maxCount)


arr = [1, 3, 2, 2, 2,2,3]
majorityElement(arr)


## also see Moore's algorithm for O(n) complexity