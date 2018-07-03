"""
Ideas:
- Change from binary file to cvs file so it can be opened in excel.

Daniel Diaz Santiago
6/21/2018

This is a module used to add, remove, save, load,
and print information from a file (hash.inv).

*Main calls the menu function to test each other function.

*Functions still need to be modified to be used.
"""

import pickle
from subprocess import call

def main():
	menu()

"""
Module functions start
"""
def save(data = [], filename = ""):
	with open(filename, "wb") as fp:
		pickle.dump(data, fp)
		fp.close()
		
def load(filename = ""):
	with open(filename, "rb") as fp:
		_data = pickle.load(fp)
	return _data

def printData(filename = "", _type = "format"):
	with open(filename, "rb") as fp:
		_data = pickle.load(fp)
	if _type.lower() == "raw":
		print("Raw output: \n" + str(_data))

	if _type.lower() == "format":
		print("\nFormatted output")
		for i in range(0,len(_data)):
			print("Sku: " + str(list(_data.keys())[i]) + "\tQty. " + str(list(_data.values())[i]))

def clear():
	hash = {}
	save(hash, "hash.inv")
	print("Printing hash.inv to verify...")
	printData("hash.inv")
	print()
	
def removeKey():
	while True:
		hash = load("hash.inv")
		r = dict(hash)

		print("hash.inv:")
		printData("hash.inv")
			
		key = str(input("    Remove key: "))
		if key.lower() == "done":
			return False
	
		del r[key]
		hash = r
		save(hash, "hash.inv")

		print("\n\nNew \"hash.inv\":")
		#printData("hash.inv")

def find():
	while True:
		hashList = load("hash.inv")
		print("Enter a SKU to find it\'s amount: ")
		key = str(input("    SKU: "))
		if key in hashList:
			print("    Qty. " + str(hashList[key]))
		elif key.lower() == "done":
			return False
		else:
			print("\n[-]Sku not found")
"""
Module functions end
"""

"""
Testing functions
"""
def options():
	print("""rm\t\t Remove entry
add\t\t Insert entry
cat\t\t Print \"hash.inv\" file
cls\t\t Clear \"hash.inv\" file
find\t\t find
help, h\t\t help
exit\t\t Exit\n""")
def header():
	print("Inventory hasing module test\n")
	options()
	
def menu():
	hash = load("hash.inv")
	header()
	while True:
		choice = str(input("#: "))
		
		if choice.lower() == "rm":
			removeKey()
			
		elif choice.lower() == "add":
			test()
			#call("clear") ## ONLY ON LINUX (FOR SIMPLICITY)
			header()
			
		elif choice.lower() == "cat":
			printData("hash.inv", "raw")
			printData("hash.inv")
			
		elif choice.lower() == "cls":
			clear()
			
		elif choice.lower() == "find":
			find()

		elif choice.lower() == "help" or choice.lower() == "h":
			options()

		elif choice.lower() == "exit":
			exit()

		elif choice.lower() == None:
			pass
			
		else:
			print("\n[-] invalid choice")


# Add to "hash.inv" file
def test():
	print("Current data in \"hash.inv\":")
	printData("hash.inv")
	hash = load("hash.inv")
	print()
	
	while True:
		sku = str(input("    Sku: "))
		if sku.lower() == "done":
			save(hash, "hash.inv")
			return False
			
		
		"""
		elif sku.lower() == "clear":
			hash = {}
			save(hash, "hash.inv")
			print("Printing hash.inv to verify...")
			printData("hash.inv")
			return False
		"""

		# Add quantity
		qty = int(input("    Qty: "))
		if sku in hash:
			hash[str(sku)] += qty
		else:
			hash[str(sku)] = qty
		
		# Add new entry to hash dictionary
		###hash[str(sku)] = qty
		
		# Save and print for confirmation
		save(hash, "hash.inv")
		printData("hash.inv")

if __name__ == "__main__":
 	main()
