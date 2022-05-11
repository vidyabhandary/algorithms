'''
A vending machine has the following denominations: 1c, 5c, 10c, 25c, 50c, and $1.
Your task is to write a program that will be used in a vending machine to return change.
Assume that the vending machine will always want to return the least number of coins or
notes. Devise a function getChange(M, P) where M is how much money was inserted into the
machine and P the price of the item selected, that returns an array of integers
representing the number of each denomination to return.

 Example:

 getChange(5, 0.99) // should return [1,0,0,0,0,4]
 getChange(3.14, 1.99) // should return [0,1,1,0,0,1]
 getChange(3, 0.01) // should return [4,0,2,1,1,2]
 getChange(4, 3.14) // should return [1,0,1,1,1,0]
 getChange(0.45, 0.34) // should return [1,0,1,0,0,0]
 
'''


def get_change(M, P):

    denominations = [1, 5, 10, 25, 50, 100]
    res = {i: 0 for i in denominations}

    amt = (M * 100) - (P * 100)

    while amt:
        for c in denominations[::-1]:
            change = int(amt / c)
            res[c] = change
            amt -= (c * change)

    # res.values() return type would be dict_values object
    # so cast to a list

    return list(res.values())


assert get_change(5, 0.99) == [1, 0, 0, 0, 0, 4], '?'
assert get_change(3.14, 1.99) == [0, 1, 1, 0, 0, 1], '?'
assert get_change(3, 0.01) == [4, 0, 2, 1, 1, 2], '?'
assert get_change(4, 3.14) == [1, 0, 1, 1, 1, 0], '?'
assert get_change(0.45, 0.34) == [1, 0, 1, 0, 0, 0], '?'
