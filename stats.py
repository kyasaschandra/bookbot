def get_num_words(str_book):
    return len(str_book.split())

def count_characters(str_book):
    count={}
    for i in str_book.lower():
        if i in count.keys():
            count[i]+=1
        else:
            count[i]=1
    return dict(sorted(count.items(), reverse = True, key=lambda item: item[1]))