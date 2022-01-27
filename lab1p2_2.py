


def main():
    
    while True: 

        print("Enter the file name you would like to read in to determine if the file contains a palindrome")

        file_name = input()
        print(" ")
        with open(file_name) as f: # Opens file
            lines = f.readlines()
            
        listtostr = " ".join([str(elem) for elem in lines]) # Converts sentence read in to a string
        rmnonalnum = list([val for val in listtostr if val.isalpha() or val.isnumeric()]) # removes non-alphnumericals
        result = "".join(rmnonalnum)
        encoded_str = result.encode("ascii", "ignore") # Removes lingering special letters
        decode_string = encoded_str.decode()
        palin = decode_string.lower()  ##String with only non-alphanumericals 
        palin_len = len(palin) # Non changing value for range in the for loops 
        len1 = len(palin) -2 # Changing value for index in creating the palindrome string
        len2 = len(palin) -1 # Non changing length for the for loop ranage for the string that has a letter removed 
        len3 = len(palin) -2 # Non changing length to reset value of len1 because its changing when it decrements in the for loop of the palindrome string with a letter removed
        palin_len2 = len(palin) - 1 # Changing length for the first check of the read in sentence is a palindrome before removing a letter
        palinlist = list(palin) # original string before removing a letter converted to a list because strings are immutable
        
        for i in range(palin_len): # For loop that creates palindrome for string that has no removed letters
            palinlist[i] = palin[palin_len2]
            palin_len2 = palin_len2 - 1
        newpalinstr = ''.join(palinlist) # String for the original string without removing a letter


        if newpalinstr == palin:
            print("Yes, no need to delete")
            print(" ")
        else:
            print("No, we need to see if deleting a maximum of one character will make the sentence into a palindrome")
            print(" ") 

            ## Gotta delete one letter then check if it is a palindrome 
            list2 = list(palin) # Changing list that accounts for removing a letter
            list3 = list(palin) # This is non changing list so that when a letter we removed doesnt work to create a palindrome we can use it to put the original letter back 

            print(" ")
            for n in range(palin_len): # Loop that removes a letter at a specific index
                list2[n] = ""         ## Removes the letter at the index of the sentence               
                str2 = ''.join(list2)     ## Puts it back into a string and str2 is now the original string before making it backwards but with a removed letter 
                list1 = list(str2) # Create a list from the string that has a letter removed so that we can turn into the needed palindrome string
                
                for i in range(len2): ## Loop takes the sentence with a removed letter and turns it into the palindrome string 
                    list1[i] = str2[len1]
                    len1 = len1 - 1
                palinstr = ''.join(list1) ## Backwards string of the string we removed a letter from
                
                if str2 == palinstr:
                    indexvalue = n + 1
                    print("Yes, delete " + list3[n] + " at position " + str(indexvalue))
                    print(" ")
                    len1 = len3
                    list2[n] = list3[n] # Substitutes the original letter back into the list thats removing letters to continue verifying every letter
                else:

                    print("No")
                    print(" ")
                    len1 = len3
                    list2[n] = list3[n] # Substitutes the original letter back into the list thats removing letters to continue searching to see if a palindrome works
    

if __name__ == "__main__":
    main()
