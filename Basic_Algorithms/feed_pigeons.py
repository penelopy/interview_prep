""" checkio(1) == 1
checkio(2) == 1
checkio(5) == 3
checkio(10) == 6 """

def checkio(feed):
    bird_array = [] # store incoming bird as zero, increment num when fed
    num_birds_arriving = 1
    fed_birds = 0

    while True: # Feeding loop
        for x in range(num_birds_arriving):
            bird_array.append(0)        # add bird to array
        for i in range(len(bird_array)):
            if feed > 0: 
                bird_array[i] += 1
                feed -= 1
            else:
                break 
        # print bird_array
        num_birds_arriving += 1

        if feed == 0: 
            break

    for bird in bird_array:
        if bird != 0: 
            fed_birds += 1

    return fed_birds

print checkio(10)

