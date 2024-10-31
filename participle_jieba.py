import os

import jieba
import thulac
from snownlp import SnowNLP

with open('data/cn_stopwords.txt', 'r', encoding='utf-8') as f:
    stop_words = set([line.strip() for line in f.readlines()])

# seg = thulac.thulac(seg_only=True)
# 遍历data/key目录下的文件
for file in os.listdir("data/key"):
    # 读取文件
    with open("data/key/" + file, "r", encoding="utf-8") as f:
        # 清空文件
        open("data/jieba_seg/" + file, "w", encoding="utf-8").close()
        # 读取文件内容
        for line in f:
            # 分词
            # jieba分词
            words = jieba.lcut(line.strip())

            # snownlp分词
            # words = SnowNLP(line.strip()).words

            #thulac分词
            # words = thulac_seg(line.strip())
            # words = [word for word, pos in words]

            #去掉file里的.txt字符串
            key =file
            key = key.replace(".txt", "")
            # 去掉种子关键词
            words = [word for word in words if word != key]
            # 去除停用词
            words = [word for word in words if word not in stop_words]
            # print(words)
            # 写入到文件
            with open("data/jieba_seg/" + file, "a", encoding="utf-8") as f2:
                f2.write("\n".join(words))