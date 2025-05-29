def soundex(name):
    name = name.upper()
    soundex_dict = {
        "B": "1", "F": "1", "P": "1", "V": "1",
        "C": "2", "G": "2", "J": "2", "K": "2", "Q": "2", "S": "2", "X": "2", "Z": "2",
        "D": "3", "T": "3",
        "L": "4",
        "M": "5", "N": "5",
        "R": "6"
    }

    first_letter = name[0]
    tail = name[1:]
    digits = [soundex_dict.get(char, "0") for char in tail]

    filtered_digits = []
    previous = ""
    for digit in digits:
        if digit != previous:
            filtered_digits.append(digit)
        previous = digit

    filtered_digits = [d for d in filtered_digits if d != "0"]
    code = first_letter + "".join(filtered_digits)
    return code[:4].ljust(4, "0")


def levenshtein(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            insertions = previous_row[j] + 1
            deletions = current_row[j - 1] + 1
            substitutions = previous_row[j - 1] + (a[j - 1] != b[i - 1])
            current_row[j] = min(insertions, deletions, substitutions)

    return current_row[n]


# wczytanie danych z pliku 
imiona = []
nazwiska = []

with open("AAliD10/.idea/dane.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) >= 2:
            imiona.append(parts[0])
            nazwiska.append(" ".join(parts[1:]))


print("=== SoundEx – imiona ===")
for i in range(len(imiona)):
    for j in range(i + 1, len(imiona)):
        print(f"{imiona[i]} vs {imiona[j]}: {soundex(imiona[i])} vs {soundex(imiona[j])}")

print("\n=== Levenshtein – imiona ===")
for i in range(len(imiona)):
    for j in range(i + 1, len(imiona)):
        print(f"{imiona[i]} vs {imiona[j]}: {levenshtein(imiona[i], imiona[j])}")

print("\n=== SoundEx – nazwiska ===")
for i in range(len(nazwiska)):
    for j in range(i + 1, len(nazwiska)):
        print(f"{nazwiska[i]} vs {nazwiska[j]}: {soundex(nazwiska[i])} vs {soundex(nazwiska[j])}")

print("\n=== Levenshtein – nazwiska ===")
for i in range(len(nazwiska)):
    for j in range(i + 1, len(nazwiska)):
        print(f"{nazwiska[i]} vs {nazwiska[j]}: {levenshtein(nazwiska[i], nazwiska[j])}")
