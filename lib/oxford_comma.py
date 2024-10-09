def oxford_comma(items):
    list_len = len(items)
    string_obj = ""
    counter = 1
    if list_len == 1:
        string_1 = items[0]
        return string_1
    elif list_len == 2:
        return f"{items[0]} and {items[1]}"
    elif list_len >2 :
        while counter != list_len:
            string_obj += f'{items[counter-1]}, '
            counter += 1
        string_obj += f'and {items[-1]}'
        
    return string_obj
