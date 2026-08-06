WORDS = ("python""jojo""coik""jdfame")
import random
word = random.choice(WORDS)
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position]+ word[(position+1):]
print("乱序后的单词:",jumble)