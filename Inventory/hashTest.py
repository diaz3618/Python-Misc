import pickle

def main():
	printData("hash.inv")
	hash = load("hash.inv")
	
	while True:
		sku = str(input("Sku: "))
		if sku.lower() == "done":
			save(hash, "hash.inv")
			printData("hash.inv")
			return False
		elif sku.lower() == "clear":
			hash = {}
			save(hash, "hash.inv")
			print("Printing hash.inv to verify...")
			printData("hash.inv")
			return False
			
		qty = int(input("Qty: "))
		
		
		hash[str(sku)] = qty
		
		save(hash, "hash.inv")
		printData("hash.inv")

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

if __name__ == "__main__":
 	main()