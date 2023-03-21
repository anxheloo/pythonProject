#Make a transalor -> #shkruajm nje shprehje dhe cdo zanore e zevendesojm me 'g'

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":       #-> same as if letter in "AEIOUaeiou":
                if letter.isupper():
                    translation = translation + "G"
                else:
                    translation = translation + "g"
        else:
            translation = translation + letter

    return translation


print(translate(input("Enter a phrase: ")))

phrase = input("Enter second phrase: ")
print(translate(phrase))