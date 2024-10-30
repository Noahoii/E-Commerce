from common import Common
from search_key import SearchKey
from seedkey import SeedKey


# 数据预处理
def process_data():
    with open('processed_data.csv', 'w', encoding='utf-8') as file:
        print("清空processed_data文件内容")
        # 写入表头
        file.write("keyword, count, age, gender, education, search_id\n")
    with open('data.txt', 'r', encoding='utf-8') as file:
        line_num = 1
        for line in file:
            line_num += 1
            # 类似构造函数，初始化参数
            search_keys = SearchKey(line)
            for keyword in Common.seed_keys:

                # 遍历关键词 判断是否包含关键词 count 表示一条query_list中包含该关键词几次
                count = search_keys.have_word(keyword)
                if count:
                    # 初始化种子关键词对象，
                    seed_keys = SeedKey(keyword, count, search_keys)
                    seed_keys.save_to_file()
                    print(seed_keys)
