# 🚆 TR_Counter

**台灣鐵路進出站數據分析工具**

## 📖 專案簡介
TR_Counter 是基於 **政府資料開放平台** 提供的台灣鐵路進出站數據的專案，旨在分析各車站的流量變化並進行可視化呈現，以協助交通規劃和趨勢分析。

## 📊 數據來源
本專案的數據來自 **政府資料開放平台**：
- [🚉 台鐵進出站人數統計](https://data.gov.tw/dataset/33425)
- [📈 車站基本資訊](https://data.gov.tw/dataset/8792?page=1)

## 🛠️ 功能特色
✅ **車站流量分析**：基於進出站人數資料，分析各站的客流量趨勢  
✅ **數據可視化**：使用 Matplotlib 生成視覺化圖表  
✅ **站點查詢**：根據 `stationCode` 查找對應的車站資訊  
✅ **易於擴展**：可添加更多數據分析與預測功能  

## 📜 授權與遵循條款
本專案遵循 **MIT License**，你可以自由使用與修改，但請標示來源。  
此外，本專案所使用的政府開放資料亦遵循 **[政府資料開放授權條款](https://data.gov.tw/license)**，並妥善引用與標示原始出處。

## 🚀 安裝與使用方法
### **環境需求**
- Python 3.x
- 相關套件 (`json`, `matplotlib`)
