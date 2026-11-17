from typing import List



def sort_words(words: List[str]) -> List[str]:
    def length(words:str) -> int:
        return len(words)
    return sorted(words, key = length, reverse = True)
    pass


def sort_numbers(numbers: List[int]) -> List[int]:
    def a(numbers:list[int])->List[int]:
        return abs(numbers)
    return sorted(numbers, key= a, reverse = False)
    pass


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
