# Standard
import nltk
import pickle

# Pip
from nltk.util import bigrams
from nltk.lm.preprocessing import pad_both_ends

# Custom
None


class Ngram:
    def __init__(self, training_file):
        self.training_file = training_file

        assert type(training_file) == str, "Enter the path name of the training file as a string."


    def open_file(self):
        file = self.training_file

        try:
            assert type(file) == str, "Enter the path name of the training file as a string"

            with open(file, mode="r", encoding="utf-8") as training_file:
                return training_file.readlines()

        except FileNotFoundError as error:
            print(error)

    def train_model(self):

        print("Das Ngram-Model wird trainiert...")
        training_file = open("../training_texts/text.txt", mode="r", encoding="utf-8").readlines()

        unigram_count = dict()
        bigrams_count = dict()
        maxliexp = dict()

        for line in training_file:
            # Satz tokenisieren
            tokens = nltk.word_tokenize(line, language='English')

            # Bigramme padden
            padded_bigrams = list(
                bigrams(pad_both_ends(tokens, n=2)))  # Padding

            # Unigramme erzeugen
            padded_unigrams = list(pad_both_ends(tokens, n=2))

            # Bigramme berechnen
            for gram in padded_bigrams:
                bigrams_count[gram] = bigrams_count.get(gram, 0) + 1

            # Unigramme berechnen
            for gram in padded_unigrams:
                unigram_count[gram] = unigram_count.get(gram, 0) + 1

        # MLE berechnen
        for bi in bigrams_count:
            word_1 = bi[0]
            maxliexp[bi] = bigrams_count.get(bi) / unigram_count.get(word_1)


    def save_model(self):
            save = "test.pickle"

            with open(save, mode="wb") as pickle_file:
                pickle.dump(self.maxliexp, pickle_file)
                pickle_file.close()


if __name__ == "__main__":
    Ngram(training_file=[])