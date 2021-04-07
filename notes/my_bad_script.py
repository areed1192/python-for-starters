
def split_full_name(string: str) -> list:
    """Takes a full name and splits it into first and last.

    Parameters
    ----------
    string : str
        The full name to be parsed.

    Returns
    -------
    list
        The first and the last name.
    """

    return string.split(" ")


# Test it out.
print(split_full_name(string=100000000))
