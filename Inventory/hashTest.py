"""
Daniel Diaz Santiago
6/21/2018

This is a module used to add, remove, save, load,
and print information from a file (hash.inv).
*Main calls the menu function to test each other function.

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

def printData(filename = ""):
	with open(filename, "rb") as fp:
		_data = pickle.load(fp)
	print(_data)

def clear():
	hash = {}
	save(hash, "hash.inv")
	print("Printing hash.inv to verify...")
	printData("hash.inv")
	print()
	
def removeKey(key):
	hash = load("hash.inv")
	r = dict(hash)
	del r[key]
	return r
"""
Module functions end
"""

"""
Testing functions
"""
def header():
	print("Inventory hasing module test\n")
	print("""(rm) Remove entry
(add) Insert entry
(cat) Print \"hash.inv\" file
(cls) Clear \"hash.inv\" file
(find) find
(exit) Exit\n""")
	
def menu():
	hash = load("hash.inv")
	header()
	while True:
		choice = str(input("#: "))
		
		if choice.lower() == "rm":
			print("hash.inv:")
			printData("hash.inv")
			
			key = str(input("Remove key: "))
			hash = removeKey(key)
			save(hash, "hash.inv")
			
			print("New \"hash.inv\":")
			printData("hash.inv")
			
		elif choice.lower() == "add":
			test()
			call("clear")
			header()
			
		elif choice.lower() == "cat":
			printData("hash.inv")
			
		elif choice.lower() == "cls":
			clear()
			
		elif choice.lower() == "find":
			while True:
				hashList = load("hash.inv")
				print("Enter a SKU to find it\'s amount: ")
				key = str(input("SKU: "))
				if key in hashList:
					print("Qty. " + str(hashList[key]))
				elif key.lower() == "done":
					break
				else:
					print("\n[-]Sku not found")

		elif choice.lower() == "exit":
			exit()
			
		else:
			print("\nInvalid choice...")


# Add to "hash.inv" file
def test():
	print("Current data in \"hash.inv\":")
	printData("hash.inv")
	hash = load("hash.inv")
	print()
	
	while True:
		sku = str(input("Sku: "))
		if sku.lower() == "done":
			save(hash, "hash.inv")
			#printData("hash.inv")
			return False
			
		elif sku.lower() == "rm":
			key = str(input("Remove key: "))
			hash = removeKey(key)
			save(hash, "hash.inv")
			sku = str(input("\nSku: "))
		
		"""
		elif sku.lower() == "clear":
			hash = {}
			save(hash, "hash.inv")
			print("Printing hash.inv to verify...")
			printData("hash.inv")
			return False
		"""
		qty = int(input("Qty: "))
		
		# Add new entry to hash dictionary
		hash[str(sku)] = qty
		
		# Save and print for confirmation
		save(hash, "hash.inv")
		printData("hash.inv")

if __name__ == "__main__":
 	main()
