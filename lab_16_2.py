import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def preprocess_text(input_text):

    words = word_tokenize(input_text)

    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]

    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in lemmatized_words if word.lower() not in stop_words]

    no_punctuation = [word for word in filtered_words if word not in string.punctuation]

    processed_text = ' '.join(no_punctuation)

    return processed_text

input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla a urna id enim fermentum vehicula. In pulvinar dignissim justo vel pellentesque. Nunc rhoncus est vitae sagittis sagittis. Mauris condimentum sollicitudin massa id fringilla. Aliquam ultrices, sapien in iaculis aliquet, nulla orci tempus tellus, nec fermentum diam ligula et justo. Curabitur vitae enim et enim euismod euismod. Praesent tortor felis, blandit sed finibus pharetra, euismod ac turpis. Ut feugiat magna ac malesuada consectetur. Aliquam erat volutpat. Suspendisse ut cursus tellus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ultricies mi et feugiat dignissim. Duis ut velit ac tortor ullamcorper accumsan.."

with open("original_text.txt", 'w', encoding='utf-8') as file:
    file.write(input_text)

processed_text = preprocess_text(input_text)

with open("processed_text.txt", 'w', encoding='utf-8') as file:
    file.write(processed_text)

print("Оригінальний текст:")
print(input_text)
print("\nОброблений текст:")
print(processed_text)