'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    n = len(arr)
    
    # Base case:
    if (n==1):
        print(0)
        return
    
    # Make temporary lists left and right
    left = [0]*n
    right = [0]*n

    # Make a new list to return at the end (product)
    prod = [0]*n

    # There are two constants, left-most element is ALWAYS 1
    # right-most element is ALWAYS 1
    left[0] = 1
    right[n-1] = 1

    # Make the temporary left list
    # range(1, n) --> start at position 1(inclusive) 
    # and end at position n(exclusive)
    for i in range(1, n):
        left[i] = arr[i-1] * left[i-1]
    
    # Make the right list
    # range(n-2, -1, -1) --> start at position n-2(inclusive, or [:-1])
    # end at -1(exclusive, 0)
    # last -1 dictates which direction to go in, -1, basically go right to left <-- (start at -1 and move towards 0)
    for j in range(n-2, -1, -1):
        right[j] = arr[j+1] * right[j+1]
    
    # Make the prod list to save the values
    # Use left[] and right[] to populate the prod list
    # range(n) --> start at position 0(inclusive) and end at n(exclusive)
    for i in range(n):
        prod[i] = left[i]*right[i]

    # Print the prod list to see
    print(f"\n {prod}")
    # for i in range(n):
    #     print(prod[i], end=" ")
    
    return prod

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

product_of_all_other_numbers([1, 2, 4, 5])

""" Questions """
# What can I use?
# arr[i]
# remove()
# loop through 
