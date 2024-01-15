import nltk
from nltk.corpus import gutenberg
import matplotlib.pyplot as plt
from collections import Counter

# Завантаження тексту "austen-emma.txt" з Project Gutenberg
nltk.download('gutenberg')
nltk.download('punkt')
emma = gutenberg.words('austen-emma.txt')

# Визначення кількості слів у тексті
total_words = len(emma)
print(f"Кількість слів у тексті: {total_words}")

# Визначення 10 найбільш вживаних слів та побудова стовпчастої діаграми
word_freq = Counter(emma)
top_words = word_freq.most_common(10)
top_words_labels, top_words_values = zip(*top_words)

plt.bar(top_words_labels, top_words_values)
plt.title('10 найбільш вживаних слів у тексті')
plt.xlabel('Слова')
plt.ylabel('Кількість')
plt.show()

# Видалення стоп-слів та пунктуації
stop_words = set(nltk.corpus.stopwords.words('english'))
emma_cleaned = [word.lower() for word in emma if word.isalnum() and word.lower() not in stop_words]

# Визначення 10 найбільш вживаних слів після видалення стоп-слів та пунктуації
word_freq_cleaned = Counter(emma_cleaned)
top_words_cleaned = word_freq_cleaned.most_common(10)
top_words_cleaned_labels, top_words_cleaned_values = zip(*top_words_cleaned)

# Побудова стовпчастої діаграми після видалення стоп-слів та пунктуації
plt.bar(top_words_cleaned_labels, top_words_cleaned_values)
plt.title('10 найбільш вживаних слів у тексті після видалення стоп-слів та пунктуації')
plt.xlabel('Слова')
plt.ylabel('Кількість')
plt.show()
