import string

eng2pir = {
    "sir":"matey",
    "hotel":"fleabag inn",
    "student":"swabbie",
    "boy":"matey",
    "madam":"proud beauty",
    "professor":"foul blaggart",
    "restaurant":"gallery",
    "your":"yer",
    "excuse":"arr",
    "students":"swabbies",
    "are":"be",
    "lawyer":"foul blaggart",
    "the":"th'",
    "restroom":"head",
    "my":"me",
    "hello":"avast",
    "is":"be",
    "man":"matey"
}

def translate(text):
    new_text = text
    words = text.split()
    
    for word in words:
        new_word = word
        punctuation = ""
        if word[-1] in string.punctuation:
            punctuation = word[-1]
            new_word = word.replace(punctuation, "")
        if new_word in eng2pir.keys():
            new_word = eng2pir[new_word]
        new_word = new_word + punctuation
        new_text = new_text.replace(word, new_word)
    return(new_text)

def main():
    words = "hello my man, please excuse your professor to the restroom!"
    print(translate(words))

if __name__ == "__main__":
    main()