'''
We want to randomly generate password characters and store them in a variable when this programme is run.

To solve this task i will use the settings of:
    2 uppercase letters from A to Z,
    2 lowercase letters from a to z,
    2 digits from 0 to 9,
    2 punctuation signs such as !, ?, “, # etc.
    And ASCII Characters

'''
import random
import datetime

starttime = datetime.datetime.now()

#A function do shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#Generating the needed pairs
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code
lowercaseLetter1=chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)
digit1=chr(random.randint(48,57)) #Generate a random digit (based on ASCII code)
digit2=chr(random.randint(48,57)) #Generate a random digit (based on ASCII code)
punctuationsign1=chr(random.randint(33,96)) #Generate a random punctuation sign (based on ASCII code)
punctuationsign2=chr(random.randint(33,96)) #Generate a random punctuation sign (based on ASCII code)

#Combining the generated pairs and calling the shuffle function
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationsign1 + punctuationsign2
password = shuffle(password)
print(password)

#Generating 50 passwords
for i in range(50):
    uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
    uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code
    lowercaseLetter1=chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)
    lowercaseLetter2=chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)
    digit1=chr(random.randint(48,57)) #Generate a random digit (based on ASCII code)
    digit2=chr(random.randint(48,57)) #Generate a random digit (based on ASCII code)
    punctuationsign1=chr(random.randint(33,96)) #Generate a random punctuation sign (based on ASCII code)
    punctuationsign2=chr(random.randint(33,96)) #Generate a random punctuation sign (based on ASCII code)

    #Combining the generated pairs and calling the shuffle function
    password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationsign1 + punctuationsign2
    password = shuffle(password)
    #Output
    print(password)

endtime = datetime.datetime.now()
#Time difference
totaltime = endtime - starttime
#Output
print(totaltime)