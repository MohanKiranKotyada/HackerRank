'''You will be given a list of integers, arr, and a single integer k. You must create an
array of length k from elements of arr such that its unfairness is minimized. Call
that array arri. Unfairness of an array is calculated as  max (arr') — min(arr') '''

def maxMin(k, arr):
    s= sorted(arr) # Sort the array 
    res = s[k-1]-s[0]  # result is the difference of the 1st and the kth value of the array until the end 
    for i in range(len(s)-k+1):
        if(s[i+k-1]-s[i]<res):
            res = s[i+k-1]-s[i]
    return res
