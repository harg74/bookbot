def count_words(get_text):    
    split = get_text.split()
    num_words = 0
    for i in split:
        num_words+=1
    return num_words

def count_char(get_text):
    count_dict = {}
    for i in range(len(get_text)):
        if get_text[i].lower() not in count_dict:
            count_dict[get_text[i].lower()] = 1
        else:
            count_dict[get_text[i].lower()] += 1
    #print(count_dict)
    return count_dict

def add_key_value(get_dictionary):
    container_list = []
    for key in get_dictionary.keys(): #para cada uno de los elementos en la lista
        create_dict = {}
        create_dict["char"] = key
        create_dict["num"] = get_dictionary[key]
        container_list.append(create_dict)
    container_list.sort(reverse=True, key=get_sorted)
    return container_list

def get_sorted(items):
    return items["num"]


