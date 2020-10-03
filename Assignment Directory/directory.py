import os
while True:
	print(os.listdir())
	directory = input("please name your new directory or use a previous one")
	parent_dir = 'C:\\users\\geral\\Desktop\\Assignment Directory\\'
	path = os.path.join(parent_dir, directory)
	try:
		os.mkdir(directory)
		print("directory created succesfully")
	except:
		print("utilizing existing file")

	logName = input("what do you wish to name your file?")+'.txt'
	Tpath = os.path.join(path, logName)
	os.chdir(path)
	Name = input("please enter your name")+','
	Number = input('please enter your number')+","
	Address = input('please enter your address')+','
	with open(Tpath, 'w+') as file_object:
		file_object.write(Name)
		file_object.write(Number)       #idk
		file_object.write(Address)
		file_object.close()

	print('your entered information is')
	with open(Tpath, 'w+') as file_object:
		contents = file_object.read()
		print(contents)

	redo = input("is this information correct? yes or no")
	if redo == 'yes':
		break
	else: 
		os.remove(Tpath)
		pass

	display = input("would you like to continue? Y/N")
	if display == "Y":
		pass
	else:
		break
