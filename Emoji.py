emojis = {
    ":)": "😀",
    ":(": "🙁",
    "XD": "😆"

}

message = input(">")

words = message.split(" ")
print(words)

phrase = ""
for word in words:
    phrase += emojis.get(word, word).__add__(" ")

print(phrase)
