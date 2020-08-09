
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # Python Exercise.# # # # # # # # # # # # # #
#                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


def element_indexes(listOfElements, element):
    ''' Returns the indexes of all occurrences of given element in
    the list- listOfElements '''
    indexPosList = []
    indexPos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            indexPos = listOfElements.index(element, indexPos)
            # Append the index position into a list
            indexPosList.append(indexPos)
        except ValueError as e:
            break
 
    return indexPosList
    

def capital_indexes(string):
    '''
        Returns the indexes of all occurrences of UPPERCASE elements in a
        given string.
    '''
    # Create empty list.
    index_post_list = []
    index_pos = 0

    # Start of try and except.
    try:
        # Loop through string.
        for s in string:
            # Check for elements that meets uppercase condition.
            if s == s.upper():
                # Search for item in list from indexPos to the end of list
                index_pos = string.index(s, index_pos)
                # Append the index position into a list
                index_post_list.append(index_pos)
               
    except Exception as e:
        print(e)

    return index_post_list


def cap_dict_indexes(string):
    index_dict = {}
    index_pos = 0
    try:
        for s in string:
            if s == s.upper():
                index_pos = string.index(s, index_pos)
                index_dict[s] = index_pos
                index_pos += 1
    except Exception as e:
        print(e)

    return index_dict
