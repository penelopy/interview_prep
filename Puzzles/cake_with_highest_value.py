""" https://www.interviewcake.com/question/cake-thief"""

def duffel_value(cake_tuples, capacity):
    highest_value = cake_tuples[0][0]/ cake_tuples[0][1]
    for i in range(len(cake_tuples)):
        value = cake_tuples[i][0]/ cake_tuples[i][1]
        if value > highest_value: 
            highest_value = value

    remainder = capacity / 


cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

duffel_value(cake_tuples, capacity)


