def count_words(sentence):
    print(sentence)
    sentence= sentence.lower()
    sentence = sentence.replace(".","")
    sentence= sentence.replace(","," ")
    sentence = sentence.replace("_", " ")
    sentence = sentence.replace(":", "")
    sentence = sentence.replace("!!&@$%^&", "")
    sentence=sentence.replace("\n", "")
    sentence= sentence.replace("''","")
    list_sentence= sentence.split()
    print(list_sentence)
    strip_list=[]
    for x in list_sentence:
        ah=x.strip("'")
        strip_list.append(ah)
    print(strip_list)
    b={}
    for count_item in strip_list:
        b[count_item] = strip_list.count(count_item)
    return b
