str = "Capitalize the first letter of every word in the title, but do not capitalize pronouns, articles, prepositions, and conjunctions."
list1 = list(filter(lambda x: True if x in "0123456789"else False,str))
print(list1)