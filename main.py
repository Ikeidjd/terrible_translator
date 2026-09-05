import sys
import json


def translate(s: str) -> str:
    with open("words.json") as file:
        words = json.load(file)

    out = ""
    prev = 0

    for n, c in enumerate(s):
        if c.isalpha():
            continue

        word = s[prev:n]
        prev = n + 1

        if word not in words:
            words[word] = input(f"{word}: ")

        out += words[word] + c

    word = s[prev:len(s)]

    if word not in words:
        words[word] = input(f"{word}: ")

    out += words[word]

    with open("words.json", "w") as file:
        json.dump(words, file)

    return out


def main() -> None:
    if len(sys.argv) != 3:
        print("Incorrect usage")
        print("Correct usage: python main.py <input_file> <output_file>")
        sys.exit(-1)

    with open(sys.argv[1]) as file:
        s = file.read()

    with open(sys.argv[2], "w") as file:
        file.write(translate(s))


if __name__ == "__main__":
    main()
