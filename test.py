import re
import csv

CAPITALIZED_WORDS_PATTERN = r'\b[A-Z][a-zA-Z]*\b'
WORDS_BEFORE_COLON_PATTERN = r'\b\w+(?=:)'
CLOSING_TAGS_PATTERN = r'</(\w+)>'
IDS_PATTERN = r'(\d+)'
SURNAMES_PATTERN = r'([A-Za-zА-Яа-яЁё]+)'
EMAILS_PATTERN = r'(\w+@\w+\.\w+)'
REGISTRATION_DATES_PATTERN = r'(\d{1,2}[-/\s]\d{1,2}[-/\s]\d{4})'
WEBSITES_PATTERN = r'(https?://[^\s]+)'
DATE_PATTERN = r'\s(\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4}[-/.]\d{1,2}[-/.]\d{1,2})'
EMAIL_PATTERN = r'\s[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
URL_PATTERN = r'\s(https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?)'

def task1():
    with open('task1-en.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    capitalized_words = re.findall(CAPITALIZED_WORDS_PATTERN, content)
    print("Слова, начинающиеся с большой буквы:", capitalized_words)

    words_before_colon = re.findall(WORDS_BEFORE_COLON_PATTERN, content)
    print("Слова перед двоеточием:", words_before_colon)

def task2():
    with open('task2.html', 'r', encoding='utf-8') as file:
        content = file.read()

    closing_tags = set(re.findall(CLOSING_TAGS_PATTERN, content))
    print("Закрывающие теги без повторений:", closing_tags)

def task3():
    with open('task3.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    ids = re.findall(IDS_PATTERN, content)
    surnames = re.findall(SURNAMES_PATTERN, content)
    emails = re.findall(EMAILS_PATTERN, content)
    registration_dates = re.findall(REGISTRATION_DATES_PATTERN, content)
    websites = re.findall(WEBSITES_PATTERN, content)

    data = list(zip(ids, surnames, emails, registration_dates, websites))

    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Фамилия', 'Электронная почта', 'Дата регистрации', 'Сайт'])
        writer.writerows(data)

def add_task():
    def extract_useful_data(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        dates = re.findall(DATE_PATTERN, content)
        emails = re.findall(EMAIL_PATTERN, content)
        urls = re.findall(URL_PATTERN, content)

        results = {
            'Dates': dates,
            'Emails': emails,
            'URLs': urls
        }
        return results

    data = extract_useful_data('task_add.txt')
    for category, items in data.items():
        print(f'{category}:')
        for item in items:
            print(f'  - {item}')

task1()
task2()
task3()
add_task()