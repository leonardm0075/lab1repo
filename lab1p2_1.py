


def main():
    
    while True:

        print("Enter the file name you would like to read in to determine if the file contains a palindrone without removing any letters")
        print(" ")
        file_name = input() # Takes user input to choose a file to read in during runtime

        with open(file_name) as f: # Opens file
            lines = f.readlines()
            
        listtostr = " ".join([str(elem) for elem in lines]) # Sentence thats read in from the file is stored as a list so this converts it to a string
        
        rmnonalnum = list([val for val in listtostr if val.isalpha() or val.isnumeric()]) # Gets rid of non-alphanumerics and converts to list because strings are immutable
        result = "".join(rmnonalnum) # Converts the above list back into a string
        encoded_str = result.encode("ascii", "ignore") # There are left over special letters so I use this to remove them
        decode_string = encoded_str.decode() 
        palin = decode_string.lower() # Forces string into all lowercase 
        
        palin_len = len(palin) - 1 # Adjusted length to correctly switch the indexes when creating palindrome string
        palin_len2 = len(palin) # Non changin length of string for the range in the for index
        list1 = list(palin) # Change back into a list because strings are immutable

        for i in range(palin_len2): # Loop creates palindrome string
            list1[i] = palin[palin_len]
            palin_len = palin_len - 1
        
        str1 = ''.join(list1) # List converted back into a string
        print(" ")
        print(str1)
        
        
        if str1 == palin:
            print("Yes")
            print(" ")

        else:
            print("No")
            print(" ")

        
        


if __name__ == "__main__":
    main()
