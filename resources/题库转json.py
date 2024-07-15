# https://miap.cc:8494/app/xcube/index.html#/login
# {
#     "题目": "客户网电脑使用过程中，说法是不正确的(  )",
#     "A": "A. 严禁将公安信息网上的计算机连接到因特网等其他网络外联行为",
#     "B": "B. 严禁将公安信息网上各种信息数据在互联网存储编辑查看",
#     "C": "C. 严禁将手机接入客户网上的计算机USB",
#     "D": "D. 客户网电脑退出客户网，不需要格式化，直接可以退出客户网使用",
#     "标准答案":"D"
# }
# 打开题库文件
with open("题库.txt", "r", encoding="utf-8") as question_bank_file:
    question_bank_text = question_bank_file.read()

# 解析输入文件
def parsing_input_files(text):
    import re
    topics = re.split(r'\n+\d+\n', text)

    topic_cache = []
    num=0
    for topic in topics:
        topic_dic = {}
        if topic.strip() == "":
            continue
        lines = topic.split("\n")
        for line in lines:


            if line.startswith("A"):
                line = line.strip()
                topic_dic["A"] = line
            elif line.startswith("B"):
                line = line.strip()
                topic_dic["B"] = line
            elif line.startswith("C"):
                line = line.strip()
                topic_dic["C"] = line
            elif line.startswith("D"):
                line = line.strip()
                topic_dic["D"] = line
            elif line.startswith("用户答案："):
                continue
            elif line.strip() == "":
                continue
            elif line.startswith("标准答案："):
                line = line.replace("标准答案：", "")
                line = line.strip()
                topic_dic["标准答案"] = line
            else:
                line = line.strip()
                topic_dic["题目"] = line
        num += 1
        topic_dic["题号"] = str(num)
        topic_cache.append(topic_dic)
    return topic_cache


topics_cache = parsing_input_files(question_bank_text)
import json
json.dump(topics_cache, open("config.json", "w", encoding="utf-8"), ensure_ascii=False)