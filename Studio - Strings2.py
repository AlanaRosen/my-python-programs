phrase = "To answer your question, I don't believe that Miranda shot the sheep on purpose."

def counter(message):
    new_message = message.split(", ",1)
    print("After the introductory prepositional phrase, there are",len(new_message[1]),"characters.")  
    
print(counter(phrase))
