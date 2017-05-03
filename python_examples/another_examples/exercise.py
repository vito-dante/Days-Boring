from typing import List

def exchange_letter(message: str, letter_change_before: str,
                    letter_change_after: str) -> str:
    new_message = ""
    for letter in message:
        if letter == letter_change_before:
            new_message += letter_change_after
        else:
            new_message += letter
    return new_message

def order_bubble_sort(array_bad: List[int]) -> List[int]:
    sort = True
    while sort:
        sort = False
        for index in range(len(array_bad)-1): # becouse my number reach n-1
            if array_bad[index] > array_bad[index+1]:
                array_bad[index], array_bad[index+1] = array_bad[index+1], array_bad[index]
                sort = True
    return array_bad

