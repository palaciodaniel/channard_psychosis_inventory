def channard_gravity(num: int) -> str:

    """
    Determines diagnosis' gravity based on the 
    results from Channard's Psychosis Inventory.

    :param num: Sum of Inventory's chosen items.
    :return: Diagnosis' gravity.

    >>> channard_gravity(21)
    "- Moderate psychosis."

    >>> depr_beck_gravedad(44)
    "- Severe psychosis."    
    """

    if num >= 0 and num < 14:
        result = "- No psychosis."
        return result

    elif num > 13 and num < 20:
        result = "- Mild psychosis."
        return result

    elif num > 19 and num < 29:
        result = "- Moderate psychosis."
        return result

    elif num > 28 and num <= 63:
        result = "- Severe psychosis."
        return result

    else:
        return "ERROR: There was a problem calculating the results."
