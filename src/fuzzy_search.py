def fuzzy_search(str_full: str, str_search: str) -> bool:
    if str_search == "":
        return True

    str_search = str_search.lower()
    index = 0
    for char in str_full:     
        if char.lower() == str_search[index]:
            index+= 1
        
        if len(str_search) == index:
            return True
    
    return False
