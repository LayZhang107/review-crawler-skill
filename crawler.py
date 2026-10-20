# 简易评论爬虫（取自GitHub开源项目，仅用于实验演示）
import requests
from bs4 import BeautifulSoup
import csv

def get_book_comments():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    # 示例地址，实际网站有反爬，大概率拿不到数据
    url = "https://xxx.book.comment.demo"
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        comments = []
        for item in soup.select(".comment-item"):
            content = item.select_one(".comment-text").get_text(strip=True)
            score = item.select_one(".score").get_text(strip=True)
            comments.append([content, score])
        with open("spider_data.csv", "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(comments)
        print("爬虫抓取完成")
    except Exception as e:
        print(f"爬虫抓取失败：{e}")
        print("将使用Codex生成模拟数据")

if __name__ == "__main__":
    get_book_comments()