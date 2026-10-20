import csv
import time
import random

# 模拟从练习网站抓取的评论数据
book_comments = [
    {"content": "故事很精彩，读着很过瘾", "score": 5, "time": "2026-10-01"},
    {"content": "内容一般，没有想象好看", "score": 3, "time": "2026-10-02"},
    {"content": "印刷质量差，纸张很薄", "score": 2, "time": "2026-10-03"},
    {"content": "性价比高，推荐购买", "score": 4, "time": "2026-10-04"},
    {"content": "不喜欢这个结局，有点失望", "score": 2, "time": "2026-10-05"},
    {"content": "物流快，书本完好无损", "score": 5, "time": "2026-10-06"},
    {"content": "文字晦涩，很难读懂", "score": 1, "time": "2026-10-07"},
    {"content": "适合打发时间，不错", "score": 4, "time": "2026-10-08"},
]

result_data = []
for item in book_comments:
    time.sleep(0.2)
    result_data.append(item)

# 写入csv
with open("test_data.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["content", "score", "time"])
    writer.writeheader()
    writer.writerows(result_data)

print("✅ 评论数据生成成功，保存至 test_data.csv")