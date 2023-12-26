requests.exceptions.ConnectionError: HTTPSConnectionPool(host='www.google.com', port=443): Max retries exceeded with url: /maps/place/Ah+Thae+coffee+shop/data=!4m7!3m6!1s0x30e50b7d2d652d37:0x27e261b71695965!8m2!3d14.0803033!4d98.208837!16s%2Fg%2F11s5ml4561!19sChIJNy1lLX0L5TARZVlpcRsmfgI?authuser=0&hl=zh-TW&rclk=1 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x0000026355A0A690>: Failed to establish a new connection: [WinError 10055] An operation on a socket could not be performed because the system lacked sufficient buffer space or because a queue was full'))
  File "C:\Users\antop\Documents\Development\temp_holding\google-maps-scraper\venv\Lib\site-packages\cloudscraper\__init__.py", line 259, in request
    self.perform_request(method, url, *args, **kwargs)
  File "C:\Users\antop\Documents\Development\temp_holding\google-maps-scraper\venv\Lib\site-packages\cloudscraper\__init__.py", line 192, in perform_request
    return super(CloudScraper, self).request(method, url, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\antop\Documents\Development\temp_holding\google-maps-scraper\venv\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\antop\Documents\Development\temp_holding\google-maps-scraper\venv\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\antop\Documents\Development\temp_holding\google-maps-scraper\venv\Lib\site-packages\requests\adapters.py", line 519, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='www.google.com', port=443): Max retries exceeded with url: /maps/place/Dawei/data=!4m7!3m6!1s0x30e50bad6add31f1:0x82a2318863a01af0!8m2!3d14.1130173!4d98.1964237!16s%2Fg%2F11ty2v2_8y!19sChIJ8THdaq0L5TAR8BqgY4gxooI?authuser=0&hl=zh-TW&rclk=1 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x0000026355A08C90>: Failed to establish a new connection: [WinError 10055] An operation on a socket could not be performed because the system lacked sufficient buffer space or because a queue was full'))