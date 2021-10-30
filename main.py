import pyttsx3
from assignment1.pdf2mp3 import str_to_mp3
from assignment1.text_prepocessing import text_preprocessing, lm_find_unchinese, de_numbers

if __name__ == '__main__':
    with open('/Users/cherriechenieth/Desktop/研究生课程/NLP/assignment1/Simon Writing.txt') as read_file:
        content = read_file.read()
        # print(content)
    read_file.close()
    content = de_numbers(lm_find_unchinese(content))

    """Convert into voices"""
    str_to_mp3(content, 1, save_as="cherry_test2.mp3")
