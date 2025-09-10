# We use the defaultdict from the collections module to simplify the process of grouping anagrams
# Because defaultdict creates a list of values for each key
from collections import defaultdict

print("----Anagram Checker----")

# We create a function which receives a list of words and returns a list of lists

def find_anagrams(word_list: list):
    # We create a dictionary where the keys are  the letter of the word sorted alphabetically
    # And the values are lists of the words which match that key, from the original list
    anagram_dict: dict = defaultdict(list)

    for word in word_list:
        # Here the key is the word in lowercase with its letters sorted alphabetically
        key: str = "".join(sorted(word.lower()))
        # And the original word is appended to the list of values for that key
        anagram_dict[key].append(word)

    # Finally, we return a list, which contain the other lists(or in this case groups of anagrams)
    return [group for group in anagram_dict.values() if len(group) > 1]

original_list: list = ["Amor", "roma", "ramo", "carro", "arroc", "perro", "rEpro", "python"]
print(find_anagrams(original_list))
