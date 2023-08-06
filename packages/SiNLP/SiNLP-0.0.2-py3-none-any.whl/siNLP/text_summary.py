# Standard
from collections import Counter
import textwrap

# Pip
None

# Custom
None


class TextSummary:

    def __init__(self, text: str, summary_len=5, threshold=30):
        self.text = text
        self.summary_len = summary_len
        self.threshold = threshold

    def open_text(self) -> list:
        file = self.text
        text_sentences = list()

        with open(file, mode="r", encoding="utf-8") as open_file:
            for line in open_file:
                if not line.isspace():
                    strip = line.strip()
                    text_sentences.append(strip)

        return text_sentences

    @staticmethod
    def __find_sentence_end(sentence: str, text_end="."):

        tokens = sentence.split()
        end_of_line = "<END OF LINE>"
        tokens.append(end_of_line)

        sentence_split = " "
        vocab = list()

        sentence_split += "<START>"

        for i in range(len(tokens)-1):
            tok = tokens[i]
            vocab.append(tok)
            sentence_split += f"{tok} "
            pre_tok = tokens[i-1]
            post_tok = tokens[i+1]

            if text_end in tok:
                if tok.islower() and post_tok.istitle():
                    sentence_split += "<END>"
                    sentence_split += "<START>"

        sen = sentence_split.replace("<START>", "").split("<END>")

        return {"sen": sen, "vocab": vocab}

    def get_sentences(self) -> dict:
        text: list = self.open_text()
        vocab = list()
        sentences = list()

        for line in text:
            sen_break = self.__find_sentence_end(line)
            sentences.extend(sen_break.get("sen"))
            vocab.extend(sen_break.get("vocab"))

        results = {"vocab": vocab, "sentences": sentences}

        return results

    @staticmethod
    def __calculate_score(sen: str, vocab: dict):

        score = 0
        for word in sen.split():
            vocab.get(word)
            score += vocab.get(word)

        return score

    def get_score(self):

        sentences_results = self.get_sentences()
        sentences = sentences_results.get("sentences")
        vocab = Counter(sentences_results.get("vocab"))
        total_scores = dict()
        for sentence_number, sen in enumerate(sentences):
            score = self.__calculate_score(sen, vocab)
            total_scores[sentence_number] = score
        return total_scores

    def get_summary(self):

        sentences = self.get_sentences().get("sentences")
        sentence_scores = self.get_score()
        threshold = self.threshold
        sum_len = self.summary_len
        threshold_texts = list()

        for sen_num, sen_text in enumerate(sentences):
            score = sentence_scores.get(sen_num)
            if score >= threshold:
                threshold_texts.append(sen_text)

        summary = textwrap.fill(''.join(threshold_texts[:sum_len]), 100)

        return summary


if __name__ == "__main__":
    file = "test.txt"

    text = TextSummary(text=file, summary_len=4, threshold=20).get_score()
    print(text)
