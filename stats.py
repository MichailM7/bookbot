# This version uses no built-in python solution
def wrd_cnt_v1(text):
    cnt=1
    # CNT starts from 1 because I increase the cnt on every space (or tab or new line) that is followed by a character
    # However this would not include the very last word therefore I need to increase the sum by one.
    # Therefore, this code would be faulty if you give a text with zero words. I could make it check for that but I dont feel like it.
    for i in range( len(text)-1):
        if (text[i]==" " or text[i]=="\n" or text[i]=="\t") and (text[i+1]!=" " and text[i+1]!="\n" and text[i+1]!="\t"):

            cnt+=1
    return(cnt)

# This version uses the .split() to split the string into a list of strings. Each split happens when the character in the parenthesis appears
# so in our case its empty space.
def wrd_cnt_v2(text):
    words= text.split()
    return(len(words))




def char_cnt(text):
    dict_a={}
    for i in text:
        if i.lower() in dict_a:
            dict_a[i.lower()]+=1
        else:
            dict_a[i.lower()]=1
    return(dict_a) 

def char_srt(dict):
    list_of_dicts=[]
    for i in dict:
        # print(i)
        # print(dict[i])
        list_of_dicts.append({"key":i,"num":dict[i]})
    list_of_dicts.sort(key=lambda d:d["num"], reverse=True)
    return list_of_dicts
    # for i in list_of_dicts:
    #     print(i)


    # list_of_dicts.sort(key=lambda d:d["num"])
        # if i.isalpha():
        #     print ("The '"+i+"' character was found "+str(char_count[i])+" times")