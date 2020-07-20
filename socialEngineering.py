"""
* author - Arvind Krishna
* github - github.com/ArvindAROO

* date - 13/07/2020 - 13:02:10
"""
#! DISCLAIMER - The author or any other related party is not responsible for the lossses incurred
#! either to the user or to the victim. Use at your own risk.
#! This activity might be illegal depending on the context, this is created for educational purposes only

class password:
	"""
    The class for creating all the possible guessable passwords
	by Social Engineering attack
	"""
	def getInfo(self):
		"""
		Get relevant info about the user
		"""
		self.d, self.m, self.y = input("Enter date of birth in format dd/mm/yyyy:").split('/')
		self.fName = input("Enter first name:").strip().capitalize()
		self.sName = input("Enter second name:").strip().capitalize()
		self.initial = input("Enter initials:").strip().upper()
		self.intd, self.intm, self.inty = str(int(self.d)), str(int(self.m)), str(int(self.y))

	def addNameAndNum(self, name, d, m, y):
		"""
		just concatenate the parameters in the particular way
		The parameters for name can be only firstName, only secondName or any of its combinations
		"""
		List = []
		List.append(name + y)
		List.append(name + y[2: ])
		List.append(name + d + m)
		List.append(name + d)
		List.append(name + '.' + d)
		List.append(name + '.' + d + m)
		List.append(name + '.' + d + m + y)
		List.append(name + '.' + d + m + y[2: ])
		List.append(name + '.' + y)
		return List

	def add123(self, name):
		List1 = []
		List1.append(name + '123')
		List1.append(name + '123')
		List1.append(name + '123')
		List1.append(name + '.')
		List1.append(name + '.123')
		List1.append(name + '.123')
		return List1

	def genPass(self):
		self.Default = ['12345678', '87654321', '123456789', '987654321', '11111111', 'abcdefgh', 'password', 'Password', 'iloveyou']
		self.List = []
		self.List.extend([self.fName, self.sName, self.fName + self.sName, self.sName + self.fName])

		self.List.append(self.d + self.m + self.y)
		self.List.append(self.d + self.m + self.y[2: ])
		self.List.append(self.y)

		# funccall		for using only fname
		List1 = self.addNameAndNum(self.fName, self.d, self.m, self.y)
		self.List.extend(List1)
		List1 = self.addNameAndNum(self.fName, self.intd, self.intm, self.inty)
		self.List.extend(List1)
		del List1

		# funccall		for using fname and sname
		List1 = self.addNameAndNum(self.fName + self.sName, self.d, self.m, self.y)
		self.List.extend(List1)
		List1 = self.addNameAndNum(self.fName + self.sName, self.intd, self.intm, self.inty)
		self.List.extend(List1)
		del List1

		# func call	for using only sName
		List1 = self.addNameAndNum(self.sName, self.d, self.m, self.y)
		self.List.extend(List1)
		List1 = self.addNameAndNum(self.sName, self.intd, self.intm, self.inty)
		self.List.extend(List1)
		del List1

		# func call for first name and initial and num
		List1 = self.addNameAndNum(self.fName + self.initial, self.d, self.m, self.y)
		self.List.extend(List1)
		List1 = self.addNameAndNum(self.fName + self.initial, self.intd, self.intm, self.inty)
		self.List.extend(List1)
		del List1

		# func call for first name and sName and initial and num
		List1 = self.addNameAndNum(self.fName + self.sName + self.initial, self.d, self.m, self.y)
		self.List.extend(List1)
		List1 = self.addNameAndNum(self.fName + self.sName + self.initial, self.intd, self.intm, self.inty)
		self.List.extend(List1)
		del List1

		# func call	for first name and initial and sname and num
		List1 = self.addNameAndNum(self.fName + self.initial + self.sName, self.d, self.m, self.y)
		self.List.extend(List1)
		List1 = self.addNameAndNum(self.fName + self.initial + self.sName, self.intd, self.intm, self.inty)
		self.List.extend(List1)
		del List1

		# func call	for adding random numbers for fname
		List1 = self.add123(self.fName)
		self.List.extend(List1)
		del List1

		# func call	for adding random numbers for fullname
		List1 = self.add123(self.fName + self.sName)
		self.List.extend(List1)
		del List1

		# func call for adding random numbers fname + initial
		List1 = self.add123(self.fName + self.initial)
		self.List.extend(List1)
		del List1

		# func call for adding random numbersf full name + initial
		List1 = self.add123(self.fName + self.sName + self.initial)
		self.List.extend(List1)
		del List1

		List1 = self.add123(self.fName + self.initial + self.sName)
		self.List.extend(List1)
		del List1

		self.List.append(self.fName + ' ' + self.sName)
		self.List.append(self.fName + '.' + self.sName)

		# donot edit below this line...These for case handling
		self.List2 = [i.lower() for i in self.List]
		self.List3 = [i.capitalize() for i in self.List2]
		self.FinalWithNoPunc = list(set(self.List + self.List2 + self.List3 + self.Default))
		del self.List, self.List2, self.List3, self.Default
		return self.FinalWithNoPunc

def main():
	P = password()
	P.getInfo()
	passwordList = sorted(P.genPass())
	fileName = open('possiblePasswords.txt', 'w')
	print(* passwordList, sep = '\n', file = fileName)

if __name__ == '__main__':
	try:
		main()
	except Exception as E:
		print(E)