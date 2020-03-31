def get_raw_document_data(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def get_possibilities(status):
    markers = []
    possibilities = word_dict[len(status)][:]
    for character in status:
        if character not in ['#', '*']:
            markers.append((character, status.index(character)))

    for possibility in possibilities[:]:
        for marker in markers:
            if possibility[marker[1]] != marker[0]:
                possibilities.remove(possibility)
                break
    return possibilities

words = get_raw_document_data('words.txt')

word_list = words.split(", ")
word_dict = {}
for word in word_list:
    word_dict[len(word)] = word_dict.get(len(word), []) + [word]

last_input = ''
while True:
    text = input()
    if text == '^':
        text = last_input
    print(get_possibilities(text))
    last_input = text