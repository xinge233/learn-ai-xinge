import requests
from bs4 import BeautifulSoup

# 1. 伪装成一个更完整的浏览器环境
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    # 告诉服务器：我是从教务处主页点过来的，不是凭空钻出来的
    "Referer": "https://jwch.fzu.edu.cn/",
    # 告诉服务器：我接受中文网页
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

# 2. 使用 Session 保持会话
session = requests.Session()
session.headers.update(headers)

# 3. 先访问一下教务处首页，拿一下初始的 Cookie
print("正在访问首页获取Cookie...")
session.get("https://jwch.fzu.edu.cn/")

# 4. 再去请求你要爬的新闻页（改成具体的页码测试）
url = "https://jwch.fzu.edu.cn/jxtz.htm"
print(f"正在请求页面: {url}")

resp = session.get(url, timeout=10)

# 5. 检查状态码
if resp.status_code == 200:
    print("✅ 成功进入页面！")
    soup = BeautifulSoup(resp.content, "html.parser")
    document = soup.find_all("li")
    print(f"找到 {len(document)} 个 li 标签")
else:
    print(f"❌ 依然被拦截，状态码：{resp.status_code}")