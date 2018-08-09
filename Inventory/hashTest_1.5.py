"""
Ideas:
- Change from binary file to cvs file so it can be opened in excel.

Daniel Diaz Santiago
6/21/2018

This is a module used to add, remove, save, load,
and print information from a file (hash.csv).

*Main calls the menu function to test each other function.

*Functions still need to be modified to be used.
"""

import csv
import pickle
from subprocess import call
HASH_FILE = "hash.csv"

def main():
	menu()



### CSV Functions
	
## Read data from "hash.csv"
def _read(FILE):
    try:
        inv_list = []
        with open(FILE, newline = "") as f:
            reader = csv.reader(f)

            for i in reader:
                inv_list.append(i)
        return inv_list

    ## If "hash.csv" is not found, create an empty one.
    except FileNotFoundError:
        print("Could not find " + FILE + " file!")
        print("Starting new " + FILE + " file...\n")
        _write(inv_list)
        
    ## Failsafe exception handling
    except Exception as e:
        print(type(e), e)
        print("\nEncountered error, terminating program...")
        sys.exit()

## Write data into "hash.csv"
def _write(inv_list, FILENAME):
    try:
        with open(FILENAME, "w", newline = "") as f:
            write = csv.writer(f)
            write.writerows(inv_list)
            
    ## Failsafe exception handling
    except Exception as e:
        print(type(e), e)
        print("\nEncountered error, terminating program...")
        sys.exit()

def printData(FILE):
        print("\nFormatted output")

        for i in range(0,len(FILE)):
                for j in range(0, 1):
                        print("Sku: " + str(FILE[i][j]) + "\tQty. " + str(FILE[i][j+1]))
        print("\n")

### CSV Functions


"""
Testing functions
"""
def options():        
	print("""rm\t\t Remove entry
add\t\t Insert entry
cat\t\t Print \"hash.csv\" file
cls\t\t Clear \"hash.csv\" file
find\t\t find
help, h\t\t help
exit\t\t Exit\n""")
def header():
	print("Inventory hasing module test\n")
	options()
	
def menu():
	_hash = _read(HASH_FILE)
	header()
	while True:
		choice = str(input("inv> "))
		
		if choice.lower() == "rm":
			pass
			
		elif choice.lower() == "add":
			test()
			header()
			
		elif choice.lower() == "cat":
			printData(_hash)
			
		elif choice.lower() == "cls":
			pass
			
		elif choice.lower() == "find":
			pass

		elif choice.lower() == "help" or choice.lower() == "h":
			options()

		elif choice.lower() == "exit":
			exit()

		elif choice.lower() == None:
			pass
			
		else:
			print("\n[-] invalid choice")


# Add to "hash.csv" file
def test():
	print("Current data in \"hash.csv\":")
	hash = _read(HASH_FILE)
	printData(hash)
	print("\n")
	
	while True:
		sku = str(input("    Sku: "))
		if sku.lower() == "done":
			_write(hash, HASH_FILE)
			return False
			
		
		"""
		elif sku.lower() == "clear":
			hash = {}
			save(hash, HASH_FILE)
			print("Printing hash.csv to verify...")
			printData(HASH_FILE)
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
		save(hash, HASH_FILE)
		printData(HASH_FILE)

if __name__ == "__main__":
 	main()




"""
Module functions start

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
	save(hash, FILENAME)
	print("Printing hash.csv to verify...")
	printData(FILENAME)
	print()
	
def removeKey():
	while True:
		hash = load(FILENAME)
		r = dict(hash)

		print("hash.csv:")
		printData(FILENAME)
			
		key = str(input("    Remove key: "))
		if key.lower() == "done":
			return False
	
		del r[key]
		hash = r
		save(hash, FILENAME)

		print("\n\nNew \"hash.csv\":")
		#printData(FILENAME)

def find():
	while True:
		hashList = load(FILENAME)
		print("Enter a SKU to find it\'s amount: ")
		key = str(input("    SKU: "))
		if key in hashList:
			print("    Qty. " + str(hashList[key]))
		elif key.lower() == "done":
			return False
		else:
			print("\n[-]Sku not found")

Module functions end
"""
