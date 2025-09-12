from stats import count_words, count_char, add_key_value
import sys

if len(sys.argv) == 2:

    def get_book_text(filepath):
        with open(filepath) as f:
            content = f.read()
            return content
        
    def main():
        get_text =  get_book_text(sys.argv[1])
        words = count_words(get_text)
        count_char(get_text)
        sorted_list = add_key_value(count_char(get_text))

        final_list = []
        for dict in sorted_list:
            if dict['char'].isalpha() != False:
                final_list.append(dict)
        print('============ BOOKBOT ============')
        print('Analyzing book found at books/frankenstein.txt...')
        print('----------- Word Count ----------')
        print(f'Found {words} total words')
        print('--------- Character Count -------')
        for dict in final_list:
            print(f'{dict['char']}: {dict['num']}')
    main()
else:
    print("bad request: While running your main.py in CLI, you need to include your <path_to_book>: Usage: python3 main.py <path_to_book>")
    sys.exit(1)