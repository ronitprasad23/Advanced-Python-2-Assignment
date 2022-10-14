str = "In the process of writing, create interesting subheadings to give your paragraphs an identity. Also, they make your text look ordered and clear."
list1 = list(filter(lambda x: True if x.lower()in"a,e,i,o,u" else False,str))
print(list1)