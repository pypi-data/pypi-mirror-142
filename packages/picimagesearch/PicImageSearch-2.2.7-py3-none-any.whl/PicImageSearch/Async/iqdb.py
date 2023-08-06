from loguru import logger
from .network import HandOver
from PicImageSearch.Utils.iqdb import IqdbResponse
from ..Utils import get_error_message


class AsyncIqdb(HandOver):
    """
    Iqdb and Iqdb 3d
    -----------
    Reverse image from https://www.iqdb.org\n


    Params Keys
    -----------
    :param **requests_kwargs: proxy settings
    """

    def __init__(self, **requests_kwargs):
        super().__init__(**requests_kwargs)
        self.requests_kwargs = requests_kwargs
        self.url = 'https://www.iqdb.org/'
        self.url_3d = 'https://3d.iqdb.org/'

    async def search(self, url) -> IqdbResponse:
        """
        Iqdb
        -----------
        Reverse image from https://www.iqdb.org\n


        Return Attributes
        -----------
        • .origin = Raw data from scrapper\n
        • .raw = Simplified data from scrapper\n
        • .saucenao = e.g.  https://saucenao.com/search.php?db=999&dbmaski=32768&url=https://iqdb.org/thu/thu_ccb14a40.jpg
        • .ascii2d = e.g.  https://ascii2d.net/search/url/https://iqdb.org/thu/thu_ccb14a40.jpg
        • .tineye = e.g.  https://tineye.com/search?url=https://iqdb.org/thu/thu_ccb14a40.jpg
        • .google = e.g.   https://www.google.com/searchbyimage?image_url=https://iqdb.org/thu/thu_ccb14a40.jpg&safe=off
        • .more = other (low similarity) Simplified data from scrapper\n
        • .raw[0].content = First index of content <Index 0 `Best match` or Index 1 etc `Additional match`>\n
        • .raw[0].source = First index of source website that was found\n
        • .raw[0].other_source = other index of source website that was found\n
        • .raw[0].url = First index of url source that was found\n
        • .raw[0].thumbnail = First index of url image that was found\n
        • .raw[0].similarity = First index of similarity image that was found\n
        • .raw[0].size = First index detail of image size that was found

        """
        try:

            if url[:4] == 'http':  # 网络url
                datas = {
                    "url": url
                }
                res = await self.post(self.url, _data=datas)
            else:  # 是否是本地文件
                res = await self.post(self.url,
                                      _files={'file': open(url, 'rb')})
            if res.status_code == 200:
                # logger.info(res.text)
                return IqdbResponse(res.content)
            else:
                logger.error(get_error_message(res.status_code))
        except Exception as e:
            logger.error(e)

    async def search_3d(self, url) -> IqdbResponse:
        """
        Iqdb 3D
        -----------
        Reverse image from https://3d.iqdb.org\n


        Return Attributes
        -----------
        • .origin = Raw data from scrapper\n
        • .raw = Simplified data from scrapper\n
        • .raw[0].content = First index of content <Index 0 `Best match` or Index 1 etc. `Additional match`>\n
        • .raw[0].title = First index of title that was found\n
        • .raw[0].url = First index of url source that was found\n
        • .raw[0].thumbnail = First index of url image that was found\n
        • .raw[0].similarity = First index of similarity image that was found\n
        • .raw[0].size = First index detail of image size that was found
        """
        try:
            if url[:4] == 'http':  # 网络url
                datas = {
                    "url": url
                }
                res = await self.post(self.url_3d, _data=datas)
            else:  # 是否是本地文件
                res = await self.post(self.url_3d,
                                      _files={'file': open(url, 'rb')})
            if res.status_code == 200:
                return IqdbResponse(res.content)
            else:
                logger.error(get_error_message(res.status_code))
        except Exception as e:
            logger.error(e)
