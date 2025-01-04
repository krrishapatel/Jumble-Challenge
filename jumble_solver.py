import sys
from typing import List, Set


def load_words(word_file: str) -> Set[str]:
    """Load words from the given file into a set for fast lookups"""
    try:
        with open(word_file, 'r') as file:
            words = set(file.read().splitlines())
        return words
    except FileNotFoundError:
        print(f"Error: The file {word_file} was not found.")
        sys.exit(1)


def find_sub_anagrams(letters: str, word_list: Set[str]) -> List[str]:
    """
    Find all sub-anagrams of the given letters in the word list.
    
    Args:
        letters (str): The input letters to find sub-anagrams for
        word_list (Set[str]): The set of valid words to search against
    
    Returns:
        List[str]: A list of matching sub-anagrams
    """
    from collections import Counter

    input_counter = Counter(letters)

    def is_valid(word: str) -> bool:
        """Check if a word can be formed using the given letters"""
        word_counter = Counter(word)
        return all(word_counter[char] <= input_counter[char] for char in word_counter)

    return [word for word in word_list if is_valid(word)]


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 jumble_solver.py <word_list.txt> <letters>")
        sys.exit(1)

    word_file = sys.argv[1]
    letters = sys.argv[2].lower()

    word_list = load_words(word_file)
    matches = find_sub_anagrams(letters, word_list)

    print("\n".join(sorted(matches)))


if __name__ == "__main__":
    main()
