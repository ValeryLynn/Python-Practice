

#Define the function
def pig_latin(line):
    '''
    This function takes in word or sentence and returns it in piglatin.
    Numbers are not converted.
    If the word starts with a vowel, it only adds 'ay' at the end.
    '''

#Clean any spaces from the front and end of the line.   
    line = line.strip()
    myArray = line.split(' ')

#Convert the line to a list to iterate.
    newArray = list(myArray)

#Enumerate the line and iterate over each item, checking for numbers and
#words that start in vowels. Then convert accordingly.    
    for i,item in enumerate(newArray):
        first_letter = item[0]
        if not item.isnumeric():
            if first_letter in 'aeiou':
                newArray[i] = item + 'ay'
            else:
                newArray[i] = item[1:len(item)] + item[0] + 'ay'
        else:
            newArray[i] = item
            
    myString = ' '
    for item in newArray:
        myString = myString + item + ' '
      
    myString.strip()
    return myString.lower()

line = input()
print (pig_latin(line))


