import re

class UserInputError(Exception):
    pass

def filter_title_words(title):
    stopwords = {
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
        'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was',
        'were', 'will', 'with'
    }

    words = title.split()
    lista = []
    for word in words:
        if word.lower() not in stopwords:
            lista.append(word.capitalize())
    return lista[:3]

def clean_text(text):
    return re.sub(r'[^a-zA-Z ]', '', text).strip()

def generate_citekey(i):
    cleaned_author = clean_text(i["author"])
    cleaned_title = clean_text(i["title"])
    year = i["year"]

    author_last_name = cleaned_author.split()[-1][:15].capitalize()
    filtered_title = filter_title_words(cleaned_title)
    title_part = "".join(filtered_title)[:15]

    return f"{author_last_name}{year}{title_part}"

def raise_error(message):
    raise UserInputError(message)

def format_inproceedings(reference):
    citekey = reference.citekey if reference.citekey else "None"
    bibtex_entry = f"@inproceedings{{{citekey},\n"
    for key, value in reference.field_values.items():
        if value is not None:
            bibtex_entry += f"    {key} = {{{value}}},\n"
    bibtex_entry = bibtex_entry.rstrip(",\n") + "\n}"
    return bibtex_entry
