import re
import os

if not os.path.exists("mydir"):
	print("\n\n'mydir' is not exist.\nMake a folder with name 'mydir' and copy all test files in the folder.\nThen run the file again\n\n")
else:
	for root, dirs, files in os.walk("mydir"):
		for file in files:
			if file.endswith(".py"):
				py_file = os.path.join(root, file)
				f = open(py_file, 'r')
				data = f.readlines()
				f.close()

				new_data = []
				for line in data:
					temp = line
					if re.findall("print ", temp):
						if re.findall("print \(", temp):
							pass
						else:
							print(temp)
							temp = re.sub("print ", "print(", temp)
							temp = temp[:-1] + ")\n"
					elif re.findall("print", temp):
						if re.findall("print\(", temp):
							pass
						else:
							print(temp)
							temp = re.sub("print", "print(", temp)
							temp = temp[:-1] + ")\n"
					new_data.append(temp)

				f = open(py_file, 'w')
				for line in new_data:
					f.write(line)
				f.close