from common import Common


class SearchKey:
    id = None
    age = None
    gender = None
    education = None
    query_list = []

    def __repr__(self):
        return "SearchKeys[{0}]: {1}".format(self.id, {
            'age': self.age,
            'gender': self.gender,
            'education': self.education,
            'query_list': len(self.query_list),
        })

    # 构造函数
    def __init__(self, data):
        data = data.split('	')
        self.id = data[0]
        self.age = Common.age_map[int(data[1])]
        self.gender = Common.gender_map[int(data[2])]
        self.education = Common.education_map[int(data[3])]
        self.query_list = data[4:]

    # 判断是否包含种子关键词
    def have_word(self, word):
        count = 0
        # 遍历query_list搜索词列表 cnt表示该query_list中包含该关键词的次数
        for query in self.query_list:
            if word in query:
                count += 1
        return count
