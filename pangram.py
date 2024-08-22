def is_pangram(sentence):
    sentence = sentence.lower()
    sentence = "".join(sentence.split())
    processing = list(sentence)
    processing = list(dict.fromkeys(processing))
    processing = sorted(processing)
    
    processing = [char for char in processing if char.isalpha() and not char.isdigit()]
    
    if len(processing) == 26:
        return "This is a pangram."
    else:
        return "This is not a pangram."
        
intext = input("Enter your sentence here: ")
print(is_pangram(intext))
