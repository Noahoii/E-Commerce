import csv


def clean_query(query):
    # 清洗查询字符串 字符串包含http的数据直接丢掉
    if 'http' in query:
        return ''
    else:
        return query


with open("data/data.txt", 'r', encoding='utf-8', errors='replace') as infile, \
        open("data/trainKey.txt", 'w', encoding='utf-8', newline='') as test:

    count = 0
    for line in infile:
        # 去除行末的换行符
        line = line.strip()
        # 分割行数据
        parts = line.split('\t')
        # 提取前四个字段
        ID, age, gender, education = parts[:4]
        # 将剩余部分作为查询列表
        queries = parts[4:]
        # 清洗查询列表中的每个元素
        queries = [clean_query(query) for query in queries]
        # 把queries 转换为字符串格式
        # queries = '\t'.join(queries)
        # test.write(ID+'\t'+age+'\t'+gender+'\t'+education+'\t'+queries + '\n')
        for i in range(len(queries)):
            if queries[i] != '':
                test.write(queries[i]+'\n')
        count += 1
    print(count)
