# Standard
None

# Pip
None

# Custom
None


class Gram:

    def __init__(self):
        pass

    @staticmethod
    def simple_unigram(string: str, separator: str) -> list:
        """
        This function creates unigrams from the entered string.

        :param string:
            The string as passed in by the user.

        :param separator:
            the symbol according to which the entered string should be split.

        :return:
            :rtype list
            A collection of the unigrams.
        """

        tokens = string.split(separator)
        unigrams = list()

        # Creating unigrams via indexing
        for i in range(len(tokens)):
            unigrams.append([tokens[i]])

        return unigrams

    @staticmethod
    def simple_bigram(string: str, separator: str)-> list:
        """
            This function creates padded bigrams from the string passed in by the user.

            :param string:
                The string as passed in by the user.

            :return:
                :rtype list
                A list of the padded bigrams
            """

        # Simple tokens using white space
        tokens = string.split(separator)
        bigrams = list()

        # Padding
        tokens.insert(0, "<START>")
        tokens[-1] = "<END>"

        # Creating bigrams via indexing
        for i in range(len(tokens) - 1):
            bigrams.append((tokens[i], tokens[i + 1]))

        return bigrams


if __name__ == "__main__":

    res = Gram.simple_unigram("This is not my house")
    print(res)