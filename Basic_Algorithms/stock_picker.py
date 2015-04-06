
def stock_picker(array_of_stocks):
    highest_profit = array_of_stocks[1] - array_of_stocks[0]
    hp_dates = []

    for buy_date in range(len(array_of_stocks)):
        for sell_date in range(buy_date + 1,  len(array_of_stocks)):
            profit = array_of_stocks[sell_date] - array_of_stocks[buy_date]
            if profit > highest_profit: 
                highest_profit = profit
                hp_dates = [buy_date, sell_date]

    # print hp_dates
        

stock_picker([12, 20, 30, 28, 32, 26, 27])



# def stock_picker(array_of_stocks): 
#     min_price = array_of_stocks[0]
#     max_price = array_of_stocks[1]
#     max_profit = max_price - min_price

#     for current_price in array_of_stocks: 
#         if current_price < min_price: 
#             min_price = current_price
#             max(max_profit, max_price - min_price)
#         print max_profit

# stock_picker([12, 20, 30, 28, 32, 26, 27])



def get_max_profit(stock_prices_yesterday):

    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy /and/ sell at time 0. 
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be /negative/--we'd return 0!
        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit

print get_max_profit([12, 20, 30, 28, 32, 26, 27])