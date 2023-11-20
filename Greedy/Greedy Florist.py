'''A group of friends want to buy a bouquet of flowers. The florist wants to maximize
his number of new customers and the money he makes. To do this, he decides he'll
multiply the price of each flower by the number of that customer's previously
purchased flowers plus 1. The first flower will be original price,
(O + 1) x original price, the next will be (1 + 1) x original price and so on.
Given the size of the group of friends, the number of flowers they want to purchase
and the original prices of the flowers, determine the minimum cost to purchase all
of the flowers. The number of flowers they want equals the length of the c array.'''

def getMinimumCost(k, c):
    c.sort(reverse=True)
    Previous_purchase = 0
    cost =0 
    for i in range(len(c)):
        cost+=(1+Previous_purchase)*c[i]
        if((i+1)%k==0):  # for every k people purchased the counter is increased by 1
            Previous_purchase+=1
    return cost
        