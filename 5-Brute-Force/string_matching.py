import time

idx = []
pattern = ['어', '린', ' ', '왕', '자']

with open("TheLittlePrince.txt", "r") as f:
    text = f.read()

text = list(text)

start = time.time()

for i in range(len(text)):
    if text[i] == pattern[0]:
        if text[i + 1] == pattern[1]:
            if text[i + 2] == pattern[2]:
                if text[i + 3] == pattern[3]:
                    if text[i + 4] == pattern[4]:
                        idx.append(i)

print("Located index:", idx)
print("Total:", len(idx))
print("Running time: %.9f seconds" % (time.time() - start))