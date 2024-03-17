class KaroList:
	def __init__(self) -> None:
		# allocated space for our array
		self.array = []

		# this value represnts number of items in array 
		# for example: we might have an array with capacity 10, 
		# but with only two items in it (on index 0, 1)
		self.size = 0

		# this value is len of our array.
		# if we want to append a value to the array
		# we have to first check whether we're not exceeding the capacity.
		# if we are then, we need to create a new bigger array (2x size of the previous one),
		# copy elements from old array into the new one and then insert the new item.
		self.capacity = 0

	def append(self, item):
		# note, you are not allowed to use append(array)!
		pass

	def __getitem__(self, index):
		# should fail if trying to get an index >= self.size
		pass

	def __str__(self) -> str:
		return f'{{ array: {self.array}, capacity: {self.capacity}, size: {self.size} }}'


# let's create our list!
karo_list = KaroList()
print(karo_list)

# let's add a couple of values into our list!
karo_list.append(0)
karo_list.append(1)
print(karo_list)

# let's add some more values!
for i in range(2, 12):
	karo_list.append(i)

print(karo_list)

# let's if we can get a value at specified index
print(karo_list[2])

print(karo_list[5])

# and what happens if index is bigger than size?
try:
	print(karo_list[45])
except:
	print('error!')

# and what if index isn't even a number?
try:
	print(karo_list['karo'])
except:
	print('error!')
