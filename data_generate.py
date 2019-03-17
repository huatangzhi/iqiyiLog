import random
import time

url_path = [
    "www/1",
    "www/2",
    "www/3",
    "www/4",
    "www/6",
    "pianhua/130",
    "toukouxu/821"
]

# http statusCode 
status_code = [404, 302, 200]
# ip item
ip_slices = [132, 156, 124, 10, 29, 167, 143, 187, 30, 100]

http_refers = [
    "https://www.baidu.com/s?wd={query}",
    "https://www.sogou.com/web?query={query}",
    "http://cn.bing.com/search?q={query}",
    "https://search.yahoo.com/search?p={query}"
]

search_keyword = [
    "猎场",
    "快乐人生",
    "极限挑战",
    "我的体育老师",
    "幸福满院"
]


def sample_url():
    return random.sample(url_path, 1)[0]


def sample_ip():
    slice = random.sample(ip_slices, 4)
    return ".".join([str(item) for item in slice])


def sample_status():
    return random.sample(status_code, 1)[0]


def sample_refer():
    if random.uniform(0, 1) > 0.2:
        return "_"
    refer_str = random.sample(http_refers, 1)
    query_str = random.sample(search_keyword, 1)
    return refer_str[0].format(query=query_str[0])


def generate_log(count, logfile_path):
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f = open(logfile_path, "w+")
    while count >= 0:
        query_log = "{ip} \t {localtime} \t \"GET {url} HTTP/1.0\"\t {referece} \t {status}".format(ip=sample_ip(), localtime=time_str, url=sample_url(), referece=sample_refer(), status=sample_status())
        f.write(query_log + "\n")
        count = count - 1


if __name__ == "__main__":
    generate_log(10, "/Users/hp/001Code/001BigData/001Iqiyi/log/logs")
