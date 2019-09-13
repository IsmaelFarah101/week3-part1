import string
import re

def special(sentence):
    ##added a regex function to search for special characters
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    ##if there is a regex character found it will just return the sentence
    if(regex.search(sentence)):
        return True
    else:
        return False
        
def camel_case(sentence):
    ##checking if the sentence is empty
    if(len(sentence) > 0):
        ##checking if the sentence contains special characters
        if(special(sentence)):
            return sentence
        else:
            #fetches user input and using capwords to capitlize the first letter of each word and lower case the rest
            newsentence = string.capwords(sentence).replace(" ","")
            ## this lowercases the first letter of the word
            newsentence = newsentence[0].lower() + newsentence[1:]
            return newsentence
    else:
        return ''

def main():
    sentence = input('Enter a sentence: ')
    camelcased = camel_case(sentence)
    print(camelcased)

if __name__ == '__main__':
    main()



