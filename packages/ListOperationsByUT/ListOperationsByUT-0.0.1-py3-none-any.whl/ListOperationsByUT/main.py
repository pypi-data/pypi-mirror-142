def listIndex(l, val):
    """
    Returns the index of the first occurrence of the value passed if not present, return -1

    """
    try:
        if val in l:
            for i in range(len(l)):
                if l[i] == val:
                    return i
        return -1

    except Exception as e:
        print(f"Error Occurred: {e}")


def listLen(l):
    """
    Returns the length of the list

    """
    try:
        count = 0

        if l == []:
            return count

        for i in l:
            count += 1

        return count

    except Exception as e:
        print(f"Error Occurred: {e}")


def listCount(l, val):
    """
    Returns the occurrence of val passed
    """
    try:
        if val in l:
            count = 0
            for i in l:
                if i == val:
                    count += 1
            return count

        return 0
    except Exception as e:
        print(f"Error Occurred: {e}")
