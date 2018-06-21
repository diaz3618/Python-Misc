import pickle

def save(data = [], filename = ""):
        with open(filename, "wb") as fp:
                pickle.dump(data, fp)
        with open(filename, "rb") as fp:
                _data = pickle.load(fp)
        print(_data)
      
def load(filename = ""):
        try:
                with open(filename, "rb") as fp:
                        _data = pickle.load(fp)
                return _data
        except:
                return None
#def clear(filename = ""):


def _hash():
        hashVar = load("hash.inv")
        sku = []
        qty = []
        last = int(len(sku) + 1)
        
        aSku = str(input("Sku: "))
        sku.insert(last, aSku)

        aQty = str(input("Qty: "))
        qty.insert(last, aQty)
                
        addHash = {k:v for k, v in zip(sku, qty)}
        hashVar.insert(last, addHash)
        save(hashVar, "hash.inv")
        
def main():
        _hash()
##        sku = load("sku.inv")
##        last = int(len(sku) + 1)
##        print(last)
##        qty = [56, 52, 34, 12, 56, 12]
##
##        """
##        Insert to lists.
##        """
##        aSku = str(input("Sku: "))
##        if aSku not in qty:
##                sku.insert(last, aSku)
##        else:
##                aSku = 0
##
##        aQty = str(input("Qty: "))
##        if aQty in qty == True:
##                _insert(qty, aQty)
##
##
##        """
##        Save to files, and print to verify.
##        """
##        save(sku, "sku.inv")
##        save(qty, "qty.inv")
##        print("Sku: " + str(sku))
##        print("Qty: " + str(qty))
##
##
##        """
##        Hash
##        """
##        hash = {k:v for k, v in zip(sku, qty)}
##        print("Hash: " + str(hash['111-222']))

def _insert(var, val):
        last = int(len(var+1))
        var.insert(last, str(val))

if __name__ == "__main__":
        main()
