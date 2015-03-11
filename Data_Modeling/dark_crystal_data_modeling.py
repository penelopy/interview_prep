cage
prisoner
skeksis consumption
skeksis


Prisoner
ID - primary key
race - string
arrival date - datetime
cage - foreign key
start_HP - int
amount of remaining essence


Skeksis
ID - primary key
start_HP - int
current_HP - int (pulled from consumption)
ranking - int

which skekeis consumed essense
when essence was consumed
from which prisoner the essense was consumed
how much essence was consumed


Consumption
ID - primary key
skeksi - foreign key
prisoner - foreign key
date - datetime
essense - how much 

cage
ID - primary key
num_prisoners - int 

race
ID - 
race_name_1 = podling
race_name_2 = gefling
