def stretch(text):
    new_text = 0
    for each in text:
        each = each+each
        new_text = new_text + each
    return(new_text)
    
text = "bland"

print(stretch(text))