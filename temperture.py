import requests,json
API_key="8104eaa58b20aa7137af538e9bf1d55a"
city="Taoyuan"
country="TW"
url="https://api.openweathermap.org/data/2.5/weather?"
url+="q="+city+","+country
url+="&units=metric&lang=zh_tw&"
url+="appid="+API_key

try:
    response=requests.get(url)
    data=json.loads(response.text);
except:
    data=None
if not data:
    print("沒有查詢到天氣資料")
else:
    print(city+" current weather report")
    print("----------------------------")
    weather=data["weather"][0]
    print("天氣描述: ",weather["description"])
    print("----------------------------")
    main=data["main"]
    print("目前溫度: ",main["temp"])
    print("大氣壓力: ",main["pressure"])
    print("目前濕度: ",main["humidity"])
    print("最低溫度: ",main["temp_min"])
    print("最高溫度: ",main["temp_max"])
    print("--------------------------")    



