from collections import deque

with open("AAliD9/.idea/tekst.txt", "r", encoding="utf-8") as file:
    words = file.read().split()

sorted_words = sorted(words)

queue = deque(sorted_words)

for i in range(100, 201):
    if i < len(queue):
        del queue[i - (i - 100)]

for word in queue:
    print(word)
