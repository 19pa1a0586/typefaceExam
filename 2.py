from gtts import gTTS
def getSound(word):
    mytext = word
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("newSound.mp3")
    
file_name = input()
req_file = file_name+".txt"
wd = getSound(wd)
rel_words = []
with open(req_file,'r') as file:
    for line in file:
        for word in line.split():
            if getSound(word) == wd:
                rel_words.append(word)
print(rel_words)
