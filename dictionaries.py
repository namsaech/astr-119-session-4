#efine dta structure
#dictionaries have key : value for elements
example_dict = {
"class"  :   "astr 119",
"prof"   :   "Brant",
"awesomeness"   : 10
}
print(type(example_dict)) 

#change value via key
example_dict["awesomeness"] += 1 
print(example_dict)

#iterate 
for x in example_dict.keys():
	print(x,example_dict[x])