msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))

def count_word(sen, word):
    cnt = 0
    for i in range(len(sen)):
        if sen[i] == 'L':
            tmp = sen[i: i + 4]
            if tmp == word:
                cnt += 1

    return cnt

print(count_word(msg, "Love"))