from fake_useragent import UserAgent
import random
import requests
#随机更换user-agent
class RandomUserAgentMiddlware(object):
    def __init__(self, crawler):
        super(RandomUserAgentMiddlware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)

        request.headers.setdefault('User-Agent', get_ua())
#更换随机ip
class RandomIPMiddleware:
    def __init__(self,url):
        self.url = url #第三方获取ip接口
        self.agentIP = self.get_ip()
    def get_ip(self):
        res = requests.get(self.url)
        ipArr = res.text.split('\r\n')
        randomNum = int(random.random() * len(ipArr))
        randomIP = ipArr[randomNum]
        return randomIP

    def process_request(self,request,spider):
        print(self.agentIP)
        request.meta['proxy'] = 'http://' + self.agentIP