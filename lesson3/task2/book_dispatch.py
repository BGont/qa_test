import csv
from contextlib import contextmanager
import json


@contextmanager
def custom_file_context_manager(*args, **kwargs):
    f = None
    try:
        f = open(*args, **kwargs)
        yield f
    except OSError as err:
        print('Oops. Something went wrong!')
        raise
    finally:
        if f is not None:
            f.close()


def dict_slice(dct, keys):
    return {key: dct[key] for key in keys if key in dct}


def dict_keys_lower(dct):
    return {key.lower(): val for key, val in dct.items()}


def main(users_file_path, user_fields, books_file_path, book_fields, result_file_path):

    result = []

    with custom_file_context_manager(users_file_path, mode="r", encoding="utf-8") as users_file:
        users_list = json.load(users_file)

    with custom_file_context_manager(books_file_path, mode="r", encoding="utf-8") as books_file:
        books_iterator = csv.DictReader(books_file)

        for user in users_list:
            result_item = dict_slice(user, user_fields)
            result_item['books'] = []
            try:
                current_book = next(books_iterator)
                result_item['books'].append(dict_keys_lower(dict_slice(current_book, book_fields)))
            except StopIteration:
                pass

            result.append(result_item)

    with custom_file_context_manager(result_file_path, mode="w", encoding="utf-8") as result_file:
        json.dump(result, result_file, indent=2)


if __name__ == "__main__":

    user_fields = ['name', 'gender', 'address']
    book_fields = ['Title', 'Author', 'Height']
    books_file_path = 'books.csv'
    users_file_path = 'users.json'
    result_file_path = 'result.json'

    main(users_file_path,
         user_fields,
         books_file_path,
         book_fields,
         result_file_path)
