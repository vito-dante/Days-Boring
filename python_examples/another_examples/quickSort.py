from typing import List

def quick_sort(array_bad: List[int]):
    i = -1
    for j in range(len(array_bad) - 1):
        if array_bad[j] < array_bad[-1]:
            i += 1
            array_bad[j], array_bad[i] = array_bad[i],array_bad[j]
    # shift i+1 -->
    for tal in range(i+1,len(array_bad)):
        array_bad[tal+1] = array_bad(tal)
    array_bad[i+1] = array_bad[-1]
