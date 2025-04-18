import json
data=[]
with open("data_list.json", "r") as file:
    data = json.load(file)
target_date=str(input("輸入想要Sort的日期(Ex:20250101)\n"))
tmp=int(input("查詢進站輸入1,出站輸入0\n"))
file_name="data_list_"+target_date
if tmp:
    sort_text="gateInComingCnt"
    file_name+="進站"
else:
    sort_text="gateOutGoingCnt"
    file_name+="出站"
file_name+=".json"
file_name="data_list_"+target_date+".json"
filtered_data = list(filter(lambda x: x["trnOpDate"] == target_date, data))
sorted_data = sorted(filtered_data, key=lambda x: int(x[sort_text]),reverse=True)

with open(file_name, "w") as file:
    json.dump(sorted_data, file, indent=4)
print("Process finised,open",file_name,"to see the result")