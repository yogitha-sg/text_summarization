from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

print("=" * 60)
print("             TEXT SUMMARIZATION SYSTEM")
print("=" * 60)

text = input("\nEnter a paragraph:\n")

parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LsaSummarizer()

sentences = summarizer(parser.document, 2)

print("\n--- SUMMARY ---")

if sentences:
    for sentence in sentences:
        print(sentence)
else:
    print("Text is too short to summarize.")