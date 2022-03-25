import jieba


def cut_word(Test):
    # 默认启用了HMM（隐马尔科夫模型）进行中文分词
    seg_list = jieba.cut(Test, cut_all=True)

    #返回一个以分隔符'/'连接各个元素后生成的字符串
    line = "/".join(seg_list)
    word = out_stopword(line)
    #print(line)
    #列出关键字
    print("\n关键字：\n"+word)

#去除停用词
def out_stopword(seg):
    #打开写入关键词的文件
    keyword = open('resource/userdict.txt', 'w+', encoding='utf-8')
    print("去停用词：\n")
    wordlist = []

    # 获取停用词表
    stop = open('resource/stop.txt', 'r+', encoding='utf-8')
    #用‘\n’去分隔读取，返回一个一维数组
    stopword = stop.read().split("\n")
    #遍历分词表
    for key in seg.split('/'):
        #print(key)
        #去除停用词，去除单字，去除重复词
        if not(key.strip() in stopword) and (len(key.strip()) > 1):
            wordlist.append(key)
            print(key)
            keyword.write(key+"\n")

    stop.close()
    keyword.close()
    return '/'.join(wordlist)

'''if __name__ == '__main__':
    #打开txt文本
    Rawdata = open('doc/report.txt','r+',encoding='utf-8')
    #将文本读取并存储到text中
    text = Rawdata.read()
    #调用分词，将待分词的文本作为参数传入方法中
    cut_word(text)
    #关闭文本
    Rawdata.close()
'''