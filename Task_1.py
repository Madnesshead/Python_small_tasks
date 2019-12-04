text = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


# 1. Get text length

print("Task 1 answer: " + str(len(text)))

# 2. Get amount of vowels in text

vowels = []
for letter in text.lower():
    if letter in 'aeiou':
        vowels.append(letter)
print("Task 2 answer, variant 1: " + str(len(vowels)))

# 2-2
vowels = [letter for letter in text.lower() if letter in 'aeiou']
print("Task 2 answer, variant 2: " + str(len(vowels)))

# 2-3
vowels_count = 0
for letter in text.lower():
    if letter in 'aeiou':
        vowels_count += 1
print("Task 2 answer, variant 3: " + str(len(vowels)))

# 3. Get every 18th symbol in text in reverse register with its index

every_18th = text[17::18]
print("Every 18th symbol in real case: " + str(every_18th))
print("Every 18th symbol in reverse case: " + str(every_18th.swapcase()))
print("Task 3 answer: ")
for idx, item in enumerate(text):
    if (idx + 1) % 18 == 0:
        print('{}{}'.format(idx + 1, item.swapcase()))





