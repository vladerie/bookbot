def main():
    book_path="books/frankenstein.txt"
    text=get_book_text(book_path)
    num_words= get_num_words(text)
    character_count=get_characters(text)
    print(f"Analyzing {book_path}")
    print("")
    print(f"{num_words} words are present within the text")
    for char in character_count:
        print(f"{char} occurs {character_count[char]} times")
    print("end of report")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    alphabet_dict = {chr(letter): 0 for letter in range(ord('a'), ord('z') + 1)}
    lctext=text.lower()
    for char in lctext:
        if char in alphabet_dict:
            alphabet_dict[char] += 1
    return alphabet_dict




main()