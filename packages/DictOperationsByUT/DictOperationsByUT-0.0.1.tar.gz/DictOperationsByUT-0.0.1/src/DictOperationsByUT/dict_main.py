def dictKeys(d):
    """
    Returns a list of keys in the dict

    """
    try:
        l = []
        for i in d:
            l.append(i)
        return l
    except Exception as e:
        print(f"Error Occurred: {e}")


def dictValues(d):
    """
    Returns a list of all values from the key

    """
    try:
        l = []
        for i in d:
            l.append(d[i])
        return l
    except Exception as e:
        print(f"Error Occurred: {e}")


def dictItems(d):
    """
    Returns the list of tuples of key value pair present in the dict

    """
    try:
        k = dictKeys(d)
        v = dictValues(d)
        res = []

        for key, val in zip(k, v):
            res.append((key, val))
        return res
    except Exception as e:
        print(f"Error Occurred: {e}")


