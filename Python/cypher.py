word = input("Enter a string to encrypt: ")
word = word.lower()
word = list(word)

enOrDe = input("Would you like to Encrpyt or Decrypt? (E or D) ")

def switch_cypher(test):
    switcher = {
        "a": "c",
        "b": "d",
        "c": "e",
        "d": "f",
        "e": "g",
        "f": "h",
        "g": "i",
        "h": "j",
        "i": "k",
        "j": "l",
        "k": "m",
        "l": "n",
        "m": "o",
        "n": "p",
        "o": "q",
        "p": "r",
        "q": "s",
        "r": "t",
        "s": "u",
        "t": "v",
        "u": "w",
        "v": "x",
        "w": "y",
        "x": "z",
        "y": "a",
        "z": "b"
    }
    return switcher.get(test, "INV")
def switch_decrypt(decryp):
    switcher = {
        "a": "y",
        "b": "z",
        "c": "a",
        "d": "b",
        "e": "c",
        "f": "d",
        "g": "e",
        "h": "f",
        "i": "g",
        "j": "h",
        "k": "i",
        "l": "j",
        "m": "k",
        "n": "l",
        "o": "m",
        "p": "n",
        "q": "o",
        "r": "p",
        "s": "q",
        "t": "r",
        "u": "s",
        "v": "t",
        "w": "u",
        "x": "v",
        "y": "w",
        "z": "x"
    }
    return switcher.get(decryp, "INV")


if enOrDe.lower() == "e":
    str1 = ""
    for i in range(0, len(word)):
        word[i] = switch_cypher(word[i])
        str1 += word[i]
    print(str1)
elif enOrDe.lower() == "d":
    str2 = ""
    for j in range(0, len(word)):
        word[j] = switch_decrypt(word[j])
        str2 += word[j]
    print(str2)

input()