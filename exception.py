#unexpected results, can use try statement to make trial statement
try:
	print(a) #have not defined a, will return exception
except:
		print("a is not defined!")
	#these are specific errors 
try:
	print(a) # a still not defined
except NameError:
	print("a is still not defined")
except:
	print("something else went wrong")
#will break program since is not defined
print(a)