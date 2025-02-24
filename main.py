from stats import *
import sys
if len(sys.argv)!=2:
    print ( "Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main ():
    # book="frankenstein.txt"
    # file_path="books/"+book
    file_path=sys.argv[1]
    text=get_book_text(file_path)
    word_count=wrd_cnt_v2(text)
    char_count=char_cnt(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at "+file_path+"...")
    print("----------- Word Count ----------")
    print("Found "+str(word_count)+ " total words")
    print("--------- Character Count -------")
    sorted_chars=char_srt(char_count)

    for i in sorted_chars:
        # print(i["key"])
        if i["key"].isalpha():
            print(i["key"]+": "+str(i["num"]))
    #         print ("The '"+i+"' character was found "+str(char_count[i])+" times")
    print("============= END ===============")
    



def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        # print (file_contents)
    return file_contents






# book="frankenstein.txt"
# file_path="./books/"+book
main()
# word_count=wrd_cnt_v2(book)
# char_count=char_cnt(book)
# print("--- Begin report of books/frankenstein.txt ---")
# print(str(word_count)+ " words found in the document\n")

# for i in char_count:
#     if i.isalpha():
#         print ("The '"+i+"' character was found "+str(char_count[i])+" times")