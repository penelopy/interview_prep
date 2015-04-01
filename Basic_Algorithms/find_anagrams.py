"""
Given a target word and a list of words, return list of words that are an anagram of the target word.
"""

def find_anagrams(target, wordlist):
    anagrams = []
    d = {}

    #creates a dictionary of letters using target word
    for letter in target:
        d[letter] = d.get(letter, 0) + 1

    # iterates through wordlist, places word/letters in dictionary and compares to 'd'
    for word in wordlist:
        temp_dict = {}
        for letter in word:
            temp_dict[letter] = temp_dict.get(letter, 0) + 1

        if d == temp_dict:
            anagrams.append(word)
    return anagrams


targ1 = "stop"
wordlist1 = ["tops", "spot", "pots", "monkey", "post"]


targ2 = "thomasalvaedison"
wordlist2 = ["dohavesalamisnot", "nerds", "darthvader"]

print find_anagrams(targ1, wordlist1)
print find_anagrams(targ2, wordlist2)