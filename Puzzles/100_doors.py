
dict_doors = {}

for i in range (1, 101): 
    dict_doors[i] = "Open"

    for x in range (2, 101): 
        if i % x == 0: 
            door_change = dict_doors.get(i)
            if door_change == "Open": 
                dict_doors[i] = "Closed"
            else:
                dict_doors[i] = "Open"
print dict_doors



