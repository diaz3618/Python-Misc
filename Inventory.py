#!/usr/bin/env python3
 
def main():
        print("Inventory app\n")
        menu()
        
        # Continue loop, or break
        again = "y"
        print()
        while again.lower() != "n" or again.lower() != "y":
            print()
            if again.lower() == "n":
                print("\nBye!")
                break
            elif again.lower() == "y":
                inv()
                write("", True)
            print("[-] Invalid choice...\n")
            again = str(input("\nAdd another SKU? (y/n): "))
 
def menu():
        rmData()
        """
        Function asks the user to choose 1 of 2
        options: "w" to add to file, and "r" to read.
        Option "r" outputs file content, while "w" breaks
        out of the loop.
        """
        print("\nChoose an option:")
        choice = str(input("(r)Read file, (w)Write to file: "))
        
        while choice.lower() != "r" or choice.lower() != "w":
            if choice.lower() == "r":
                openFile()
            elif choice.lower() == "w":
            	break
            else:
            	print("[-] Invalid choice...\n")
            	
            choice = str(input("(r)Read file, (w)Write to file: "))

def rmData():
        rm = str(input("Clear list.txt? (y/any key): "))
        if rm.lower() == "y":
        	write("", False)
        	print("[+]Cleared\n")
            
def inv():
        # Initialize
        total = 0
        length = 1
        lf = "n"

        """
        Ask once, SKU might be
        counted by linear feet.
        """
        sku  = str((input("SKU: ")))
        lf = input("LF? (y/default = n): ")

        """
        While loop is used here to keep
        adding to the overall amount.
        *The loop ends when 0 is entered.
        """
        while True:
                # Linear Feet?
                if lf.lower() == "y":
                        length = int(input("Length: "))
 
                # Amount input
                amount = int(input("Amount: "))
                if amount == 0:
                        write("SKU: " + str(sku) + "\tQty. " + str(total) + "\n")
                        return False
 
                total += mult(length, amount)
                print("\tSKU: " + sku)
                print("\tTotal: " + str(total))
                
 
def write(info, writeNew = True):
        """
        If "writeNew" == False,
        write over the file (erase it).
        """
        if writeNew == False:
                f = open("list.txt", "w+")
        f = open("list.txt", "a+")
        f.write(info)
        f.close()
 
def openFile():
        f = open("list.txt", "r")
 
        if f.mode == "r":
                listFile = f.read()
                print(listFile)
 
def mult(length, amnt):
        total = length * amnt
        return total
	
if __name__ == "__main__":
  main()
