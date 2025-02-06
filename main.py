# print("hello world")


def main (book):
    with open("./books/"+book) as f:
        file_contents = f.read()
        # print (file_contents)
    return file_contents


def wrd_cnt_v1(text):
    cnt=1
    # CNT starts from 1 because I increase the cnt on every space (or tab or new line) that is followed by a character
    # However this would not include the very last word therefore I need to increase the sum by one.
    # Therefore, this code would be faulty if you give a text with zero words. I could make it check for that but I dont feel like it.
    for i in range( len(text)-1):
        # if (text[i]==" " or text[i]=="\n" or text[i]=="\t") and text[i+1]!=" ":
        if (text[i]==" " or text[i]=="\n" or text[i]=="\t") and (text[i+1]!=" " and text[i+1]!="\n" and text[i+1]!="\t"):

            cnt+=1
    return(cnt)

def wrd_cnt_v2(text):
    cnt=0
    words= text.split()
    return(len(words))
    # print(type(words))



def char_cnt(text):
    dict_a={}
    for i in text:
        if i.lower() in dict_a:
            dict_a[i.lower()]+=1
            # print("KK")
            # dict_a.append(i.lower())
        else:
            dict_a[i.lower()]=1


    return(dict_a) 

book=main("frankenstein.txt")
# print(type(book))
word_count=wrd_cnt_v2(book)
char_count=char_cnt(book)
print("--- Begin report of books/frankenstein.txt ---")
print(str(word_count)+ " words found in the document\n")

for i in char_count:
    if i.isalpha():
        # print(i+ " fasd")
        print ("The '"+i+"' character was found "+str(char_count[i])+" times")