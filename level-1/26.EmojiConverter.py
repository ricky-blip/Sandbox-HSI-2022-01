kalimat = input(" >>> ")

emoji_mapping = {
    ":)": "🙂",
    ":D": "😀",
    ":|": "😐"
}

words = kalimat.split(" ")

print(kalimat)
print(words)

output = ""
for w in words:
    output = output + emoji_mapping.get(w, w) + " "
    
print(output)