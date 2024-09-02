def select_word(sentence):
    words = sentence.split()
    
    index = sum(ord(char) for char in sentence) % len(words)
    return words[index]

def generate_sentence(sentence1, sentence2, sentence3):
    word1 = select_word(sentence1)
    word2 = select_word(sentence2)
    word3 = select_word(sentence3)
    return f"{word1}_{word2}_{word3}"

sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")
sentence3 = input("Enter the third sentence: ")


output_sentence = generate_sentence(sentence1, sentence2, sentence3)
print("Generated sentence:", output_sentence)
