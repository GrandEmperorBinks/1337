# https://github.com/GrandEmperorBinks

import json
output = []     #create output list for use later on

def l33t():    #define the l33t function
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']     #list of encodable/decodable characters - the alphabet
    messageList = []
    newMessage = ''
    message = input('Enter text to be converted to l33tsp3@k (enter x to end program): ')      #prompt the user for input

    for character in message:   #convert the input (the message variable) to a list (the messageList) variable
        messageList.append(character.lower())

    for letter in messageList:  #iterate through messageList
        if letter in alphabet:  #if the letter is in our alphabet list, replace it with the character 13 positions away and add that new character to a string
            index = alphabet.index(letter)
            newMessage = newMessage + alphabet[index].upper()
        else:                   #if the character isn't encodeable/decodeable, add it without encoding to the string
            newMessage = newMessage + letter

    return newMessage           #return the new message newMessage

file = open('data.txt', 'w')    #open the file data.txt


while True:                     #forever repeat
    text = l33t()              #run the function and save the output as text
    if text == 'x':             #if the text is 'k' (encoded version of 'x'), break out of infinite loop (ending program)
        break
    else:                       #else add message to a list of encoded/decoded messages
        output.append(text)

json.dump(output, file, indent = 2)     #write list of messages to the file in JSON format
file.close()
