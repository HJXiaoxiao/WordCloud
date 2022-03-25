def read_file():
    f = open(r'D:\Python\word_cloud\venv\resource\userdict.txt', encoding='utf-8')
    readline = f.readlines()
    word = []  # 存储单词

    # 得到文章的单词并且存入列表中：

    for line in readline:
        # 因为原文中每个单词都是用空格 或者逗号加空格分开的，
        line = line.replace(',', '')  # 除去逗号只要空格来分开单词
        line = line.strip()
        wo = line.split(' ')

        word.extend(wo)
    return word


def clear_account(lists):
    wokey = {}
    wokey = wokey.fromkeys(lists)

    word_1 = list(wokey.keys())
    for i in word_1:
        wokey[i] = lists.count(i)
    return wokey


def sort_1(wokey):
    del [wokey['']]
    wokey_1 = {}
    wokey_1 = sorted(wokey.items(), key=lambda d: d[1], reverse=True)
    wokey_1 = dict(wokey_1)
    return wokey_1


def main(wokey_1):
    i = 0
    for x, y in wokey_1.items():
        if i < 10:
            print('the word is "', '{}'.format(x), '"', ' and its amount is "', '{}'.format(y), '"')
            i += 1
            continue
        else:
            break


main(sort_1(clear_account(read_file())))