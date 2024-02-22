def top_n (items, n):
    """ Returns top n items in an array, in desc order.
    Args:
        items(array): list or array-like object
        n (int): Number of items to return
        
    Return:
        array: top n items, in desc order.
        
    Egs: 
        >>> top_n([8,4,2,3,9], 3)
        [9,8,4]
    """
    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]: # if this item is bigger than the next one
                items[j], items[j+1] = items[j+1], items[j] # swap the two!

    # get last two items
    top_n = items[-n:]

    # return in desc order
    return top_n[::-1]