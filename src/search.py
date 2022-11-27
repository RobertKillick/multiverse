import math

def search(search_list: list, search_number: int, start_index=0, end_index=None):

    if search_list == [] or search_number < 0:
        return

    if end_index == None:
        end_index = len(search_list)-1
    
    search_index = math.floor((end_index-start_index)/2+start_index)

    if search_list[search_index] == search_number:
        return search_index

    if end_index == start_index:
        return
    
    if search_list[search_index] < search_number:
        return search(search_list, search_number, search_index+1, end_index)
    else:
        return search(search_list, search_number, start_index, search_index-1)
