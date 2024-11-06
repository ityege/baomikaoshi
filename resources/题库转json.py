import subprocess
import re
import json

process = subprocess.Popen(
    [
        "awk",
        'BEGIN {OFS="\t";} /^[0-9]+$/ {question_number = $0;getline question_content;} /^A/{option_a = $0;}/^B/{option_b = $0;}/^C/{option_c = $0;}/^D/{option_d = $0;}/^标准答案/{standard_answer = $0;gsub(/标准答案：/, "", standard_answer);print question_number , question_content , option_a , option_b , option_c , option_d , standard_answer;}',
    ],
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=open("题库.txt", "r"),
    text=True,
)
stdout, stderr = process.communicate()
if process.returncode == 0:
    topic_cache = []
    for line in stdout.splitlines():
        fields = line.split("\t")
        topic_obj = {
            "题目": re.sub(r'[^\u4e00-\u9fa5]', '', fields[1].strip()),
            "A": fields[2].strip(),
            "B": fields[3].strip(),
            "C": fields[4].strip(),
            "D": fields[5].strip(),
            "标准答案": fields[6].strip(),
        }
        topic_cache.append(topic_obj)
        json.dump(topic_cache, open("config.json", "w", encoding="utf-8"), ensure_ascii=False)

else:
    print(stderr)