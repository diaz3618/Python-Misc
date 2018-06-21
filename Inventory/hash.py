import pickle

def save(data = [], filename = ""):
        with open(filename, "wb") as fp:
                pickle.dump(data, fp)
##        with open(filename, "rb") as fp:
##                _data = pickle.load(fp)
##      print(_data)      

def load(filename = ""):
        try:
                with open(filename, "rb") as fp:
                        _data = pickle.load(fp)
                return _data
        except:
                return None
#def clear(filename = ""):
        
def main():
        sku = load("sku.inv")
        qty = [56, 52, 34, 56, 56]

        """
        Insert to lists.
        """
        aSku = str(input("Sku: "))
        if aSku in sku == False:
                _insert(sku, aSku)
        
        aQty = str(input("Qty: "))
        if aQty in qty == False:
                _insert(qty, aQty)


        """
        Save to files, and print to verify.
        """
        save(sku, "sku.inv")
        save(qty, "qty.inv")
        print("Sku: " + str(sku))
        print("Qty: " + str(qty))


        """
        Hash
        """
        hash = {k:v for k, v in zip(sku, qty)}
        print("Hash: " + str(hash['249-666']))

def _insert(var, val):
        var.append(val)

if __name__ == "__main__":
        main()
