import jieba
from common import Common

with open('data/cn_stopwords.txt', 'r', encoding='utf-8') as f:
    stop_words = set([line.strip() for line in f.readlines()])


def clean_and_filter(text):
    # 使用jieba进行分词
    words = jieba.lcut(text)
    # 去除停用词
    filtered_words = [word for word in words if word not in stop_words]
    # 去掉空格
    filtered_words = [word for word in filtered_words if word != ' ']
    # 检查是否包含关键词
    has_keyword = any(keyword in filtered_words for keyword in Common.seed_keys)
    return ''.join(filtered_words), has_keyword


# 读取原始txt文件
input_file = 'data/trainKey.txt'
output_file = 'data/trainKeyCleaned.txt'

with open(input_file, 'r', encoding='utf-8') as infile, \
        open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        cleaned_line, has_keyword = clean_and_filter(line.strip())
        if has_keyword:  # 只保存含有关键词的行
            outfile.write(cleaned_line + '\n')
