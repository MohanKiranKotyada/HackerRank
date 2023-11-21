'''Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies.
 Alice wants to minimize the total number of candies she must buy.'''

def candies(n, arr):
    result=[1 for i in range(n)] #giving 1 candi to each person
    for i in range(1,n):
        if(arr[i]>arr[i-1]):
            result[i]=result[i-1]+1 #adding one extra candi from the previous person if the next person has a higher score
    print(result)
    for i in range(n-1,0,-1):
        if(arr[i-1]>arr[i] and result[i-1]<=result[i]):
            result[i-1]=result[i]+1 
    return sum(result)