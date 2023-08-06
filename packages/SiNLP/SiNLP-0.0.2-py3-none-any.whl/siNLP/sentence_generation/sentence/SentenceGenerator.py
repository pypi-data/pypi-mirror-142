# Standard
import pickle

from typing import Type

# Pip
None

# Custom



class SentenceGenerator:

    def __init__(self, model: dict):
        self.model = model

    def open_model(self):
        model = self.model
        with open(model, mode="rb") as pickle_file:
            return pickle.load(pickle_file)

    def generate_basic_sentence(self):
        pass


if __name__ == "__main__":
    pass