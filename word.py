# coding:utf-8
from collections import Counter
from os import path
import jieba
jieba.load_userdict(path.join(path.dirname(__file__), r'D:\学习文件\软件\WordCloud\resource\userdict.txt'))

def word_segment(text):
    '''
    通过jieba进行分词并通过空格分隔,返回分词后的结果
    '''

    # 计算每个词出现的频率，并存入txt文件
    jieba_word = jieba.cut(text, cut_all=False)
    data = []
    for word in jieba_word:
        data.append(word)
    temp = Counter(data)
    dataDict_temp = sorted(temp.items(),key = lambda x: x[1],reverse=True)
    dataDict = dict(dataDict_temp)
    with open('resource/count.txt', 'w') as fw:
        for k, v in dataDict.items():
            if k == '\r\n':
                continue
            else:
                fw.write("'%s' 出现：%d次\n" % (k, v))
            #fw.write("%s"%dataDict)


    # 返回结果
    jieba_word = jieba.cut(text, cut_all=False)
    seg_list =' '.join(jieba_word)
    return seg_list
