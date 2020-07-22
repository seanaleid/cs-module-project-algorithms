'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    mainC = 0
    window = []
    exLen = mainC + k
    n = len(nums)
    result = []
    stop = n - k

    if mainC == stop :
        return
    else:
        for i in nums:
            # print(nums[mainC:exLen])
            window.append(nums[mainC:exLen])
            # print(window)
            mainC+=1
            exLen+=1
            # window[i] = nums[i]
            # mainC+=1
            # result.append(max(window))
            # print(window)
            # print(result)
        
        for i in window:
            if len(i) == k:
                # print(max(i))
                result.append(max(i))
    print(result)
    return result

sliding_window_max([1,7,5,9,3,6,2], 3)

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

""" Pseudo code """
# Recipe, I need:
# - a secondary array that'll be the window of the len(k)
# - counter to move the secondary array 
# - result [], to append the answers
# - logic to move the 2nd array, increment the counter, 
# and to find the max value inside the 2nd array (max(list_name))

# Method:
# initialize the main index counter at 0, mainC = 0
# initialize the 2nd array with, window = [0]*n
# use k for length of window
# initialize length of the arr, n = len(arr)
# initialize exclusive length for ranges, exLen = (mainC + n)
# while mainC is not n
    # for loop using range(mainC, exLen)
        # for i in range(mainC, exLen):
            # window[i] = arr[i]
            # increment the mainC, mainC+=1
            # return max(window)