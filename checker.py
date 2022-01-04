import urllib3
from urllib3 import request
import logging, coloredlogs

http = urllib3.PoolManager()
logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(message)s',level='DEBUG', logger=logger)

def check_availability(url):
    try:
        request = http.request('GET', url, timeout=10,retries=urllib3.Retry())
        
        if request.status == 200:
            return True
        else:
            return False
    except urllib3.exceptions.NewConnectionError:
        return False
    except urllib3.exceptions.ProtocolError:
        return False
    except urllib3.exceptions.ClosedPoolError:
        return False
    except urllib3.exceptions.ConnectTimeoutError:
        return False
    except urllib3.exceptions.MaxRetryError:
        return False
    except urllib3.exceptions.LocationValueError:
        return False
    except urllib3.exceptions.DecodeError:
        return False


web_page_url = input('Enter web url address : ')

if check_availability(web_page_url):
    print('success')
    logger.debug('Site is Working !')
else:
    logger.error('Not Working')
    