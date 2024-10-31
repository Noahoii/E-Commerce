import os

count = {}

for file in os.listdir("data/key"):
    # 读取文件
    with open("data/key_seg/" + file, "r", encoding="utf-8") as f:
        file = file.replace(".txt", ".csv")
        # 清空文件
        open("data/intermediary_key/" + file, "w", encoding="utf-8").close()
        with open("data/intermediary_key/" + file, "a", encoding="utf-8") as f2:
            f2.write("intermediary_key,count,weight"+"\n")
        # 读取文件内容
        for line in f:
            word = line.strip()
            if word in count:
                count[word] +=1
            else:
                count[word] = 1
        word_freq = []
        #遍历字典转换为元组  计算前十个的权重
        for word,freq in count.items():
            word_freq.append((freq,word))
        word_freq.sort(reverse = True)
        #遍历前十个输出
        for word,freq in word_freq[:10]:
            with open("data/intermediary_key/" + file, "a", encoding="utf-8") as f2:
                f2.write(str(freq)+','+str(word) +","+str(word/ len(word_freq))+"\n")