import json
import chardet
from bs4 import BeautifulSoup
from scan.common import logger


class Response:
    def __init__(self, req_resp):
        self.req_resp = req_resp
        self.status_code = req_resp.status_code
        self.content = req_resp.content

    def json(self):
        try:
            return json.loads(self.content)
        except Exception as e:
            logger.error(f'格式化json异常:{e}, 数据:{self.content}')

    def soup(self):
        try:
            soup = BeautifulSoup(self.content, 'lxml')
            return soup
        except Exception as e:
            logger.error(f'格式化soup异常:{e}, 数据:{self.content}')

    def text(self):
        try:
            encoding = chardet.detect(self.content).get('encoding')
            return self.content.decode(encoding)
        except Exception as e:
            logger.error(f'格式化text异常:{e}, 数据:{self.content}')



