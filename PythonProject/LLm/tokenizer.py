from collections import Counter
import re

class BytePairEncoder:
    def __init__(self):
        self.ws_token = '_'
        self.unk_token = '<UNK>'

        self.corpus = {}
        self.word_count = {}
        self.vocab = Counter()

        self.id_tokens = {}
        self.token_ids = {}

    def preprocess(self, text):
        return re.sub('\s+',' ', text)

    def process_sentence(self, sentence):
        words = sentence.split()
        for word in words:
            word = self.ws_token + word
            if word not in self.corpus:
                self.corpus[word] = [ch for ch in word]
                self.word_count[word] = 1
            else:
                self.word_count[word] += 1

    def _dump_init(self):
        print("=" * 12 + " dump initial state " + "=" * 12)
        print("--> dump corpus <--")
        for word, text in self.corpus.items():
            print(f"{word} => {text}")
        print('-.' * 20)
        print("==> dump wordcnt <==")
        for word, count in self.word_count.items():
            print(f"{word} => {count}")
        print('-.' * 20)
        print("==> dump vocab <==")
        for token, count in self.vocab.items():
            print(f"{token} => {count}")
        print('-.' * 40)

    def init_state(self, content):
        for line in content:
            sentence = self.preprocess(line.strip())
            self.process_sentence(sentence)
        alphabet = {}
        for word, chrs in self.corpus.items():
            for ch in chrs:
                alphabet[ch] = alphabet.get(ch, 0) + self.word_count(word)
        self.vocab.update(alphabet)

    def merge_pair(self):
        top_bigram, top_count = self.gen_bigrams().most_comm

    def train(self, text, steps=1):
        self.init_state(text)
        self._dump_init()
        pass

    def encode(self, text):
        pass

    def decode(self, text):
        pass
