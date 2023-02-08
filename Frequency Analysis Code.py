string = str(input("Please enter the string to count the frequency of the letters: "))
string = string.lower()   #converts string to lower case to prevent missing out capital letters.
alphabetslst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
emplst = []    #final list that will have the frequency of all the letters.


def frequencyanalysis(emplst, string):
    for i in string:
        if i.isalpha() == False:
            continue
        else:
            if i in alphabetslst:
                freq = string.count(i)
                freqtuple = (i, freq)
                emplst.append(freqtuple)
                alphabetslst.remove(i)
    return emplst
    
print(frequencyanalysis(emplst,string))
