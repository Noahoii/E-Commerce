from search_key import SearchKey


class SeedKey:
    keyword = None
    count = 0
    age = None
    gender = None
    education = None
    search_id = None

    def __repr__(self):
        return "SeedKey[{0}]: {1}".format(self.keyword, {
            'count': self.count,
            'age': self.age,
            'gender': self.gender,
            'education': self.education,
            'search_id': self.search_id,
        })

    # 构造函数 初始化种子关键词对象
    def __init__(self, keyword, count, search_key:SearchKey):
        self.keyword = keyword
        self.count = count
        self.age = search_key.age
        self.gender = search_key.gender
        self.education = search_key.education
        self.search_id = search_key.id

    # 将种子关键词对象 转化为csv数据
    def to_csv_data(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}\n".format(
            self.keyword, self.count, self.age, self.gender, self.education, self.search_id
        )

    # 将一个种子关键词对象保存为csv文件的一行
    def save_to_file(self):
        with open('processed_data.csv', 'a', encoding='utf-8') as file:
            file.write(self.to_csv_data())
