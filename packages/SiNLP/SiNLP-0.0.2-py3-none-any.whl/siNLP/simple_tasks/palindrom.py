

def palindrom(word: str) -> dict:
    """
    'Racecar' and 'Racecar' is a classic palindrom in the English language.
     By definition, a palindrom is word that is spelled the same way - forwards
     or backwards. However, it does not have to necessarily be a word,
     it can also be a sentence even if these types of palindrom are less common.

    :param word:
        The string as passed in by the user.

    :return:
        :rtype res
        the palindrom string of the inputted string by the user.
        with the boolean value.

    """

    raw_forward = word
    raw_backward = word[::-1]

    post_forward = raw_forward.lower()
    post_backward = raw_backward.lower()

    # No result
    no_result = {"bool": False, "Result": "This is not a palindrom."}

    # preprocessed variant
    if raw_forward == raw_backward:
        res = {"bool": True, "preprocessing": raw_backward}
        return res

    elif post_forward == post_backward:
        res = {"bool": True, "postprocessing": post_backward}
        return res

    else:
        return no_result


if __name__ == "__main__":
   r = palindrom("hss")

