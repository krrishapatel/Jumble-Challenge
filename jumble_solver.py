from collections import Counter
from typing import List

def load_word_list(file_path: str) -> List[str]:
    """
    Load a word list from a file into a list of words.
    """
    with open(file_path, 'r') as file:
        return [line.strip().lower() for line in file]

def is_sub_anagram(word: str, letters: str) -> bool:
    """
    Check if a word is a sub-anagram of the given letters.
    """
    word_counter = Counter(word)
    letters_counter = Counter(letters)
    # Check if each letter in the word can be formed from the letters
    return all(word_counter[char] <= letters_counter[char] for char in word_counter)

def jumble_solver(word_list_path: str, letters: str) -> List[str]:
    """
    Find all sub-anagrams of the input letters from the word list.
    """
    # Load word list
    word_list = load_word_list(word_list_path)
    # Find matching sub-anagrams
    results = [word for word in word_list if is_sub_anagram(word, letters)]
    return sorted(results)  # Sort results alphabetically

if __name__ == "__main__":
    # Input: word list file and scrambled letters
    word_list_file = input("Enter the path to the word list file: ").strip()
    letters = input("Enter the letters: ").strip().lower()
    # Solve the jumble
    results = jumble_solver(word_list_file, letters)
    # Output results
    print("\nMatching sub-anagrams:")
    print("\n".join(results))
