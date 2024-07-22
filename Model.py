from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")

    def correct_spell(self, text):
        words = text.split()
        correct_words = []
        for word in words:
            correct_word = str(TextBlob(word).correct())
            correct_words.append(correct_word)
        return " ".join(correct_words)

    def correct_grammar(self, text):
        tokens = word_tokenize(text)
        tagged = pos_tag(tokens)
        grammar_mistakes = [word for word, tag in tagged if tag not in ['NN', 'VB', 'JJ', 'RB']]
        foundmistakes_count = len(grammar_mistakes)
        return grammar_mistakes, foundmistakes_count

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello World  I like mashine learnogn appple "
    print("Corrected Spelling:", obj.correct_spell(message))
    mistakes, count = obj.correct_grammar(message)
    print("Grammar Mistakes:", mistakes)
    print("Number of Grammar Mistakes:", count)
