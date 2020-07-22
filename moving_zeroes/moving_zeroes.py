'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    """ Version 2 """
    # Set counter
    count = 0
    # Set the length of the list
    n = len(arr)

    # Loop through the list
    for i in range(n):
        # Check for the values that are not 0
        if arr[i] != 0:
            # If they are not 0, move the first non 0 int to arr[0]
            arr[count] = arr[i]
            # Increment the counter
            count+=1
            # It will move to the next num in the arr.
            # If it is 0, it'll skip it.
            # If it is not 0, it will take that num and put it at arr[1],
            # increment the counter to 2, and move tot he next num.
            # With example of [0,3,1,0,-2], the list now looks like
            # [3,1,-2,-,-]

    # Use a while loop to fill in the 0s at the end
    # In this example, count = 3
    # count < n --> 3 < 4 --> current position 3, length of list is 4
    while count < n:
        # arr[3] = 0
        arr[count] = 0
        # count = 4
        count+=1
        # Loop through again, count = 4
        # arr[4] = 0

    return arr
    # mutated list --> [3,1,-2,0,0]

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

 # Your code here

    """ Questions """
    # How can I move an item to the end of a list?
    # Are there methods that already exist?
    # Can I use one of the sorts?

    # Case #1 - all items are 0
    # Case #2 - empty list
    # Case #3 - there are no zero
    # Case #4 - everything else

""" Version 1 """
    # counter = arr.count(0)
    # print(arr.count(0))

    # if len(arr) == counter:
    #     return arr
    # elif arr == []:
    #     return arr
    # elif counter == 0:
    #     return arr
    # else:
    # # loop through the list
    #     while counter > 0:
    #         for item in arr:
    #             if item == 0:
    #                 arr.append(arr.pop(arr.index(item)))
    #                 counter-=1
    #                 print(arr)
    #                 moving_zeroes(arr)
    #             else:
    #                 return arr
    # check to see if each value is equal to 0
    # if zero, move to the end
    # if not, do nothing

# moving_zeroes([0,0,0,3,2,1,-4])
# moving_zeroes([0,1,0,0,2,0,-4])