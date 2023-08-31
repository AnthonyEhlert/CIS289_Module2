import re
"""
Program Name: regexing_ehlert.py
Author: Tony Ehlert
Date: 8/31/2023

Program Description: This program takes a passage and uses Regex to answer queries about the passage
"""
search_passage = ("\"I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. "
                 "I will face my fear. I will permit it to pass over me and through me. And when it has gone past I "
                 "will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will "
                 "remain.\" – Frank Herbert, Dune")

# How many words contain the letter f (case insensitive)? ... This includes Frank
contain_f_list = re.findall("f", search_passage, flags=re.IGNORECASE)
# print(contain_f_list)
# print(len(contain_f_list))

# How many words start with the letter f (case insensitive)? ... This includes Frank
start_with_f_list = re.findall(r"\bf", search_passage, flags=re.IGNORECASE)
# print(start_with_f_list)
# print(len(start_with_f_list))

# How many times the word "not" appears (whole word only)?
times_not_appears = re.findall(r"\bnot ", search_passage, flags=re.IGNORECASE)
# print(times_not_appears)
# print(len(times_not_appears))

# Update the passage to change every "I" word to "You", "my" to "your", and "me" to "you".
# print(search_passage)

updated_search_passage = re.sub("I ", "You ", search_passage)
# print(updated_search_passage)

updated_search_passage = re.sub("my ", "your ", updated_search_passage)
# print(updated_search_passage)

updated_search_passage = re.sub("me ", "you ", updated_search_passage)
# print(updated_search_passage)

updated_search_passage = re.sub("me.", "you.", updated_search_passage)
print(updated_search_passage)