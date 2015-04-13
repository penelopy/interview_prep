""" From interview cake

Write a function that, given:
    an amount of money
    a list of coin denominations
computes the number of ways to make amount of money with coins of the available denominations.
"""

def change_possibiilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)   #creates an array of len amount + 1
    ways_of_doing_n_cents[0] = 1
    # print ways_of_doing_n_cents

    for coin in denominations: # 1, 3, 5
        print "hey"
        for higher_amount in xrange(coin, amount + 1): # 1, 2, 3, 4, 5
            print ways_of_doing_n_cents
            print coin
            print higher_amount
            higher_amount_remainder = higher_amount - coin
            # print ways_of_doing_n_cents[higher_amount]

            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
            print ways_of_doing_n_cents
            print "*****"

    return ways_of_doing_n_cents[amount]

print change_possibiilities_bottom_up(5, [1, 3, 5])

###########
# ways_of_doing_n_cents = [1, 0, 0, 0, 0, 0]

# coin = 1
# higher_amount_remainder = 0
