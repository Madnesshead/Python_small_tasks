from operator import itemgetter
from Task_1 import text


# 1. Count how many times every symbol appears in text and sort it by symbols in alphabetical order
def symbols_count():
    result_count = {}
    for symbol in text:
        if symbol in result_count:
            result_count[symbol] += 1
        else:
            result_count[symbol] = 1
    return result_count


result = symbols_count()
sorted_result_count = sorted(result)
print('Question_1')
for key in sorted_result_count:
    print(repr(f'{key} - {result[key]}'))


# 2. Sort the same info by amount of symbols frequency
print('\nQuestion_2')
sorted_result_count = sorted(result.items(), key=itemgetter(1))
for item in sorted_result_count:
    print(repr(f'{item[0]} - {item[1]}'))