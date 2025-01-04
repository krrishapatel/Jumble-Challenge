import sys
from typing import List, Set

# Load words from the file
def load_words(word_file: str) -> Set[str]:
    with open(word_file, 'r') as file:
        words = {line.strip().lower() for line in file}
    return words

# Count the frequency of each letter in a string
def letter_count(word: str) -> dict:
    count = {}
    for char in word:
        count[char] = count.get(char, 0) + 1
    return count

# Find sub-anagrams based on the letters
def find_sub_anagrams(letters: str, word_list: Set[str]) -> List[str]:
    input_letter_count = letter_count(letters)
    sub_anagrams = []
    for word in word_list:
        word_letter_count = letter_count(word)
        
        # Check if the word can be formed using the given letters
        is_sub_anagram = True
        for char in word_letter_count:
            if word_letter_count[char] > input_letter_count.get(char, 0):
                is_sub_anagram = False
                break
        
        if is_sub_anagram:
            sub_anagrams.append(word)
    
    return sub_anagrams

# Main function to handle user input and call other functions
def main():
    if len(sys.argv) != 3:
        print("Usage: python3 jumble_solver.py <word_list_file> <letters>")
        sys.exit(1)
    
    word_file = sys.argv[1]
    letters = sys.argv[2].lower()
    
    word_list = load_words(word_file)
    sub_anagrams = find_sub_anagrams(letters, word_list)
    
    print("\n".join(sorted(sub_anagrams)))

# Program starts
if __name__ == "__main__":
    main()
