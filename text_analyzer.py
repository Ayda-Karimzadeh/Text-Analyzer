# کد به تابع‌های کوچیک تقسیم شده باشه
import re

# فایل رو با open و encoding="utf-8" بخون.
def read_file():

    file_path = input("\nEnter file path:")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return content

# علامت‌ها رو حذف کن و متن رو به کلمه‌ها بشکن.
def list_words(content):

    cleaned_content = re.sub(r'[^\w\s]', '', content)
    words = cleaned_content.lower().split()
    
    return words

# با دیکشنری یا collections.Counter تکرار هر کلمه رو بشمار.
def show_top_words(words):

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    top_words = sorted(word_count.items(),
    key=lambda item: item[1], reverse=True)[:10]
    print("Top 10 Most Frequent Words:")

    for word, count in top_words:
        print(word, ":", count)

def count_sentences(content):

    sentences = re.split(r'[.!?؟]+', content)
    sentences = [s for s in sentences if s.strip()]

    return len(sentences)

# نتیجه رو مرتب و تمیز چاپ کن.
try:
    content = read_file()
    words =list_words(content)
    print(f"Number of words : {len(words)}")
    print(f"Number of sentences : {count_sentences(content)}")
    # ۱۰ کلمه‌ی پرتکرار به ترتیب چاپ بشه
    show_top_words(words)

except FileNotFoundError:
    print("File not found!")