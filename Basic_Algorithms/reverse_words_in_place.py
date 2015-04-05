"""Write a function reverse_words() that takes a string message and reverses the order of the words in place """
# Strings are immutable in python - so i think this is the best you can do.

message = 'find you will pain only go you recordings security the into if'

# output = "if into the security recordings you go only pain will you find"

message_list = message.split()

for x in range(len(message_list) /2):
    temp = message_list[x]
    message_list[x] = message_list[-x - 1]
    message_list[-x -1] = temp

new_message = ' '.join(message_list)
print new_message