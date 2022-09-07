def find_and_replace(file_name, old_word, new_word):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            text = text.replace(old_word, new_word)
            with open(file_name, 'w') as file:
                file.write(text)
    except FileNotFoundError:
        print('File not found')


find_and_replace('test.txt', 'Yes', 'YES')
