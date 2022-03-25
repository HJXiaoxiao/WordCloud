# coding:utf-8
from os import path
from remove import cut_word
from remove import out_stopword
#from statistics import read_file
#from statistics import main
#from statistics import clear_account
#from statistics import sort_1
import word
import plat
import os


if __name__ == '__main__':
    print("----------------------一、用户输入-----------------------")
    root_path = path_doc = r'D:\Python\word_cloud\venv\doc'
    n = 0
    k = 1
    for i in os.walk(root_path):
        for j in i[2]:
            path_doc = os.path.join(i[0], j)
    for i in os.listdir(root_path):
        print("{}---{}".format(k, i))
        k = k + 1
    # print(k)
    flag = int(input("请输入你想要查看的文件："))
    while (flag > k - 1 or flag <= 0):
        print("输入错误，要提示重新输入，直到输入正确为止")
        flag = int(input("请输入你想要查看的文件："))
    for i in os.listdir(root_path):
        n = n + 1
        if n == flag:
            print("{}".format(i))
            break
    print("你选择将要查看的词云图是：{}".format(i))


    print("----------------------二、屏蔽无用词-----------------------")
    d = path.dirname(__file__)
    Rawdata = open(path.join(d, 'doc', i),'r+', encoding='utf-8')
    text_1 = Rawdata.read()
    cut_word(text_1)
    Rawdata.close()

    print("----------------------三、排序并计数-----------------------")
    # print(d)
    #text = open(path.join(d, 'doc//report.txt'),'rb').read()
    text = open(path.join(d, 'resource', 'userdict.txt'), 'rb').read()
    #text = open(path.join(d, 'doc//alice.txt')).read()
    text = word.word_segment(text)
    delete = int(input("你想要查看count.txt里的内容吗？(1表示是，0表示否)："))
    if (delete == 1):
        con = open(r'resource/count.txt')
        for i in range(10):
            print(con.readline().strip())
        #s = con.read()
        #print(s)
    else:
        with open('resource/userdict.txt', 'a+', encoding='utf-8') as test:
            test.truncate(0)


    print("----------------------四、绘画词云图-----------------------")
    plat.generate_wordcloud(text)



