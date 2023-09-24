"""
Create a python file named number_to_words, Write a program that can convert user entered number (from 0~9) to words.

    NOTE: MUST use ternary
"""

num_word = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']


def num_to_word(num: int = 0):
    result = num_word[num] if 0 <= num <= 9 else 'Invalid number'
    print(result)

num_to_word(12)
