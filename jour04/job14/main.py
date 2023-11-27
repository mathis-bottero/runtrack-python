def my_long_word (n, La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance):
    n = 3
    result = ""
    
    i = 0
    while i < len(words):
        result += " ".join(words[i:i+n]) + " "
        i += n
    
    return result.strip()

sentence = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
output = my_long_word(3, sentence)
print(output)