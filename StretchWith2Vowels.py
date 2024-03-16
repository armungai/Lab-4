def read_sentence():
    return input("Sentence: ")
    

def is_vowel(c):
    return c.lower() in 'aeiou'
    

def count_vowels(segment):
    return sum(is_vowel(char) for char in segment)

            
def matches(word):
    vowel_count = 0
    for i, char in enumerate(word):
        if char == 'z':
            if vowel_count == 2:
                return True
            vowel_count == 0
        else:
            if is_vowel(char):
                vowel_count += 1
        
        if i == len(word) - 1 and vowel_count == 2:
            return True
        
    return False
  

def count_matches(sentence):
    words = sentence.split()
    return sum(matches(word) for word in words)

  

if __name__ == "__main__":
    #Write your code here
    while True:
        sentence = read_sentence()
        if sentence == "*":
            break

        valid_word_count = count_matches(sentence)
        print ("Matching words =", valid_word_count)
    
    print("Done")
