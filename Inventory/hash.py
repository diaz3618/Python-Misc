import pickle

def skuFile(data):
        data = []
        with open("sku.inv", "wb") as fp:
                pickle.dump(data, fp)
        with open("sku.inv", "rb") as fp:
                _data = pickle.load(fp)
        print(_data)

def main():
        sku = []
        with open('sku.inv') as f:
                sku = f.read().splitlines()
        print("[+]Loaded: " + str(sku))
                
        addSku = str(input("SKU: "))
        addQty = int(input("Qty: "))

                
        #sku = ['249-666', '256-276', '234-534']
        _insert(sku, addSku)
        
        qty = [56, 52, 34]
        _insert(qty, addQty)
        
        hash = {k:v for k, v in zip(sku, qty)}


        test(sku)


        """
        Print files
        """
        wFile(str(hash), "data.inv")
        wFile(str(qty), "qty.inv")







def test(sku):
        """
        Print to verify
        """
        print()
        print("In list: " + str(sku))

        """
        Write to files
        """
        for items in sku:
                sTest = sku.replace("[", "")
                wFile(str(sTest), "sku.inv")

        # Print file to verify
        f = open("sku.inv", "r")
        print
        if f.mode == "r":
                read = f.read()
                print("In file: " + str(read))






                
def wFile(data, fileName, append = False):
        if append == True:
                f = open(fileName, "a+")
        f = open(fileName, "w+")
        f.write(data)
        f.close()

def _insert(var, val):
        var.append(val)

if __name__ == "__main__":
        main()
