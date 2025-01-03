from pydantic import BaseModel
import requests
import json
from urllib.parse import urlencode

from _types import ICNAirplane


url = "https://www.airport.kr/arr/ap_ko/getArrPasSchList.do"
#params = "intg=&keyWord=&curDate=20250103&startTime=1700&airPort=&endTime=1759&todayDate=20250103&tomorrowDate=20250104&todayTime=1717&curStime=1700&curEtime=1759&layout=61705f6b6f40403837324040666e637432&siteId=ap_ko&langSe=ko&exitDoor2=&scheduleListLength=&termId=&exitDoor=&daySel=20250103&fromTime=1700&toTime=1759&airport=&airline=&airplane="

def _generate_parameters():
  from datetime import datetime, timedelta

  todayTime = datetime.now().strftime("%H%M")
  startTime = todayTime
  endTime = str(int(todayTime) + 59)
  curStime = todayTime
  curEtime = str(int(todayTime) + 59)
  fromTime = todayTime
  toTime = str(int(todayTime) + 59)


  curDate = datetime.now().strftime("%Y%m%d")
  tomorrowDate = (datetime.now() + timedelta(days=1)).strftime("%Y%m%d")

  layout = "61705f6b6f40403837324040666e637432"
  layout = ""
  params = {
  "intg": "",
  "keyWord": "",
  "curDate": curDate,
  "startTime": startTime,
  "airPort": "",
  "endTime": endTime,
  "todayDate": curDate,
  "tomorrowDate": tomorrowDate,
  "todayTime": todayTime,
  "curStime": curStime,
  "curEtime": curEtime,
  "layout": layout,
  "siteId": "ap_ko",
  "langSe": "ko",
  "exitDoor2": "",
  "scheduleListLength": "",
  "termId": "",
  "exitDoor": "",
  "daySel": curDate,
  "fromTime": fromTime,
  "toTime": toTime,
  "airport": "",
  "airline": "",
  "airplane": "",
  }

  print(urlencode(params))
  return urlencode(params)


def request():
  params = _generate_parameters()
  #exit(0)
  response = requests.post(url, data=params)
  answer = response.json()
  print(answer)

def parse():
    with open('response_sample.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    ap = ICNAirplane(**data["scheduleList"][0])
    print(ap)
    print(ap.to_str())
    return data

if __name__ == "__main__":
  parse()