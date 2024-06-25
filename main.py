import time
from functions import *

def init_search_linear(file, word):
    with open(file, 'r') as f:
        text = f.read().replace('\n', '').replace('.', ' ').replace(',', '')
    
    list_words = text.split()
    len_list_word = len(list_words)
    print('LEN LEST WORD', len_list_word)

    index = search_linear(list_words)
    nb_occurence = count_linear(list_words, word)

    print(f"Le mot '{word}' apparaît {nb_occurence} fois dans le fichier '{file}'.")

def init_fibonnacci(n):
    print(f"Le nombre de Fibonacci à la position {n} est {fibonacci_iteratif(n)}")
    print(f"Le nombre de Fibonacci à la position {n} est {fibonacci_recursive(n)}")

def init_search_binary(file, word):
    with open(file, 'r') as f:
        text = f.read().replace('\n', '').replace('.', ' ').replace(',', '')
    
    list_words = text.split()
    len_list_word = len(list_words)
    print('LEN LEST WORD', len_list_word)

    nb_occurence = count_binary(word, list_words)

    print(f"Le mot '{word}' apparaît {nb_occurence} fois dans le fichier '{file}'.")

def handler(file):
    # init_search_linear(file, 'ipsum')
    # init_fibonnacci(10)
    init_search_binary(file, 'ipsum')


if __name__ == "__main__":
    handler('sample-13mb-text-file.txt')