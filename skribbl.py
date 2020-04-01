from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_raw_document_data(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def get_possibilities(status):
    markers = []
    possibilities = word_dict[len(status)][:]
    for character in status:
        if character not in ['#', '*', '_']:
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

print('LINK: ')
driver = webdriver.Chrome(executable_path='/Users/meganyang/skribble/chromedriver')
driver.get(input())
while True:
    command = input()
    if command == "GUESS":
        try:
            display_text = driver.find_element_by_id('currentWord').text
            possibilities = get_possibilities(display_text)
            chat_box = driver.find_element_by_id('inputChat')
            chat_box.click()
            counter = 0
            for possibility in possibilities:
                if counter > 5:
                    counter = 0
                    print('CONTINUE? ')
                    prompt = input()
                    if prompt == 'YES':
                        pass
                    else:
                        break
                chat_box.send_keys(possibility)
                chat_box.send_keys(Keys.ENTER)
                if driver.find_element_by_id('currentWord').text != display_text:
                    break
                counter += 1
                sleep(1.1)
        except:
            continue
    else:
        chat_box = driver.find_element_by_id('inputChat')
        chat_box.click()
        chat_box.send_keys(command)
        chat_box.send_keys(Keys.ENTER)