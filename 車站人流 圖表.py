import json
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


zh_font = fm.FontProperties(fname="C:/Windows/Fonts/msjh.ttc")
fig = plt.figure(figsize=(19.2, 10.8), dpi=100)

data=[]
station_data=[]
with open("data_list.json", "r") as file:
    data = json.load(file)
with open("station_list.json", "r", encoding="utf-8") as file:
	station_data = json.load(file)

target_sta=str(input("輸入想要查詢的車站編號\n"))
tmp=int(input("查詢進站輸入1,出站輸入0\n"))

result = next((item["name"] for item in station_data if item["stationCode"] == target_sta), None)
title="車站 "+result+" 的進站人數"
file_name=title
if tmp:
    sort_text="gateInComingCnt"
    file_name+="進站"
else:
    sort_text="gateOutGoingCnt"
    file_name+="出站"

filtered_data = list(filter(lambda x: x["staCode"] == target_sta, data))
gate_in_counts = [int(item["gateInComingCnt"]) for item in filtered_data]
dates=[item["trnOpDate"] for item in filtered_data]
formatted_dates = [date[-4:] for date in dates]

plt.plot(formatted_dates, gate_in_counts)
plt.grid(True)
plt.title(title,fontproperties=zh_font)
plt.xticks(rotation=45,fontsize=8)
plt.xlabel("日期",fontproperties=zh_font)
plt.ylabel("人數",fontproperties=zh_font)
plt.savefig(title, dpi=100, bbox_inches='tight')
plt.show()
print("圖表已成功儲存為 plot.png")