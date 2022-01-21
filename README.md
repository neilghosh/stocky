# stocky
## Setup
```
pip install -t lib -r requirements.txt
```
## Start Server 
```
python main.py
```
## APIs
### Get list of companies with their ticker symbol for a partial company name.
> api/companysearch?name=infosys
#### Example
```bash
curl -X GET \
  'https://trade-junky.appspot.com/api/companysearch?name=infosys' \
  -H 'api-key: 2246696acd8638f0fbfe5d6e4d515a3eaefed5c19b5a2c18'
```
##### Response
``` javascript
{
    "INFY": "Infosys Limited",
    "HCL-INSYS": "HCL Infosystems Limited"
}
```
### Get all the latest data for a specific ticker symbol.
> api/getquote?name=INFY
#### Example
``` bash
curl -X GET \
  'http://localhost:8080/api/getquote?name=INFY' \
  -H 'api-key: 2246696acd8638f0fbfe5d6e4d515a3eaefed5c19b5a2c18'
```
##### Response
``` javascript
{
    "sellPrice3": "-",
    "sellPrice2": "-",
    "sellPrice1": "-",
    "totalSellQuantity": "-",
    "sellPrice5": "-",
    "sellPrice4": "-",
    "ndEndDate": "-",
    "series": "EQ",
    "marketType": "N",
    "previousClose": "924.35",
    "bcEndDate": "-",
    "css_status_desc": "Listed",
    "priceBand": "No Band",
    "secDate": "19OCT2017",
    "cm_adj_low_dt": "22-AUG-17",
    "sellQuantity4": "-",
    "sellQuantity5": "-",
    "securityVar": "4.30",
    "high52": "1,050.70",
    "open": "930.00",
    "cm_ffm": "1,85,238.49",
    "sellQuantity2": "-",
    "sellQuantity3": "-",
    "closePrice": "926.95",
    "pricebandupper": "1,016.75",
    "extremeLossMargin": "5.00",
    "sellQuantity1": "-",
    "buyPrice4": "-",
    "buyPrice5": "-",
    "low52": "860.00",
    "deliveryToTradedQuantity": "69.54",
    "isExDateFlag": false,
    "buyPrice2": "-",
    "applicableMargin": "12.50",
    "buyQuantity1": "3,227",
    "recordDate": "01-NOV-17",
    "buyQuantity3": "-",
    "buyQuantity2": "-",
    "buyQuantity5": "-",
    "buyQuantity4": "-",
    "buyPrice1": "926.95",
    "totalBuyQuantity": "3,227",
    "lastPrice": "927.75",
    "companyName": "Infosys Limited",
    "bcStartDate": "-",
    "symbol": "INFY",
    "buyPrice3": "-",
    "deliveryQuantity": "3,79,479",
    "exDate": "31-OCT-17",
    "purpose": "BUYBACK",
    "indexVar": "-",
    "varMargin": "7.50",
    "change": "3.40",
    "surv_indicator": "-",
    "quantityTraded": "5,45,717",
    "totalTradedVolume": "5,45,717",
    "isinCode": "INE009A01021",
    "adhocMargin": "-",
    "pChange": "0.37",
    "faceValue": "5.00",
    "dayHigh": "932.00",
    "dayLow": "925.20",
    "ndStartDate": "-",
    "pricebandlower": "831.95",
    "averagePrice": "927.39",
    "cm_adj_high_dt": "20-OCT-16",
    "totalTradedValue": "5,060.92"
}
```
### get the historical data for specified date range / duration .
> /getdata?name=INFY&startdate=01-07-2016&enddate=18-07-2017&dateperiod=3months
#### Example
``` bash
curl -X GET \
  'https://trade-junky.appspot.com/api/getdata?name=INFY&startdate=01-07-2016&enddate=18-07-2017&dateperiod=3months' \
  -H 'api-key: 2246696acd8638f0fbfe5d6e4d515a3eaefed5c19b5a2c18'
```
##### Response
``` javascript
[
    {
        "High Price": "932.00",
        "Turnover (in Lakhs)": "5,060.94",
        "Close Price": "926.95",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "925.20",
        "Date": "19-Oct-2017",
        "Last Traded Price ": "        927.75",
        "Total Traded Quantity": "5,45,717",
        "Open Price": "930.00"
    },
    {
        "High Price": "930.00",
        "Turnover (in Lakhs)": "33,508.69",
        "Close Price": "924.35",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "922.95",
        "Date": "18-Oct-2017",
        "Last Traded Price ": "        925.00",
        "Total Traded Quantity": "36,15,926",
        "Open Price": "928.90"
    },
    {
        "High Price": "936.80",
        "Turnover (in Lakhs)": "26,216.12",
        "Close Price": "930.50",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "929.50",
        "Date": "17-Oct-2017",
        "Last Traded Price ": "        930.75",
        "Total Traded Quantity": "28,12,551",
        "Open Price": "936.80"
    },
    {
        "High Price": "942.00",
        "Turnover (in Lakhs)": "27,003.04",
        "Close Price": "939.00",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "933.00",
        "Date": "16-Oct-2017",
        "Last Traded Price ": "        939.00",
        "Total Traded Quantity": "28,79,375",
        "Open Price": "935.95"
    },
    {
        "High Price": "933.50",
        "Turnover (in Lakhs)": "33,379.68",
        "Close Price": "930.10",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "927.55",
        "Date": "13-Oct-2017",
        "Last Traded Price ": "        929.05",
        "Total Traded Quantity": "35,90,364",
        "Open Price": "932.80"
    },
    {
        "High Price": "934.35",
        "Turnover (in Lakhs)": "47,530.16",
        "Close Price": "927.30",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "919.55",
        "Date": "12-Oct-2017",
        "Last Traded Price ": "        928.35",
        "Total Traded Quantity": "51,40,486",
        "Open Price": "930.00"
    },
    {
        "High Price": "938.00",
        "Turnover (in Lakhs)": "27,886.48",
        "Close Price": "930.70",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "928.00",
        "Date": "11-Oct-2017",
        "Last Traded Price ": "        930.60",
        "Total Traded Quantity": "29,91,252",
        "Open Price": "935.45"
    },
    {
        "High Price": "939.95",
        "Turnover (in Lakhs)": "33,411.06",
        "Close Price": "935.45",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "929.55",
        "Date": "10-Oct-2017",
        "Last Traded Price ": "        935.15",
        "Total Traded Quantity": "35,71,610",
        "Open Price": "939.95"
    },
    {
        "High Price": "929.00",
        "Turnover (in Lakhs)": "16,187.46",
        "Close Price": "923.90",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "914.00",
        "Date": "09-Oct-2017",
        "Last Traded Price ": "        924.25",
        "Total Traded Quantity": "17,52,416",
        "Open Price": "920.00"
    },
    {
        "High Price": "922.00",
        "Turnover (in Lakhs)": "39,293.15",
        "Close Price": "920.15",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "903.95",
        "Date": "06-Oct-2017",
        "Last Traded Price ": "        920.50",
        "Total Traded Quantity": "42,87,154",
        "Open Price": "904.00"
    },
    {
        "High Price": "904.95",
        "Turnover (in Lakhs)": "38,870.64",
        "Close Price": "903.05",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "899.00",
        "Date": "05-Oct-2017",
        "Last Traded Price ": "        903.00",
        "Total Traded Quantity": "43,05,650",
        "Open Price": "900.00"
    },
    {
        "High Price": "905.40",
        "Turnover (in Lakhs)": "22,489.97",
        "Close Price": "899.60",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "897.15",
        "Date": "04-Oct-2017",
        "Last Traded Price ": "        901.45",
        "Total Traded Quantity": "24,95,746",
        "Open Price": "903.00"
    },
    {
        "High Price": "912.00",
        "Turnover (in Lakhs)": "22,403.92",
        "Close Price": "903.55",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "901.60",
        "Date": "03-Oct-2017",
        "Last Traded Price ": "        903.05",
        "Total Traded Quantity": "24,73,761",
        "Open Price": "910.10"
    },
    {
        "High Price": "902.40",
        "Turnover (in Lakhs)": "25,656.51",
        "Close Price": "899.90",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "895.00",
        "Date": "29-Sep-2017",
        "Last Traded Price ": "        899.00",
        "Total Traded Quantity": "28,52,916",
        "Open Price": "898.00"
    },
    {
        "High Price": "903.90",
        "Turnover (in Lakhs)": "78,716.66",
        "Close Price": "896.00",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "894.30",
        "Date": "28-Sep-2017",
        "Last Traded Price ": "        896.00",
        "Total Traded Quantity": "87,68,633",
        "Open Price": "896.10"
    },
    {
        "High Price": "907.90",
        "Turnover (in Lakhs)": "27,015.42",
        "Close Price": "899.80",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "895.10",
        "Date": "27-Sep-2017",
        "Last Traded Price ": "        895.90",
        "Total Traded Quantity": "30,00,069",
        "Open Price": "906.10"
    },
    {
        "High Price": "908.40",
        "Turnover (in Lakhs)": "33,154.16",
        "Close Price": "905.90",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "894.30",
        "Date": "26-Sep-2017",
        "Last Traded Price ": "        901.75",
        "Total Traded Quantity": "36,83,239",
        "Open Price": "897.00"
    },
    {
        "High Price": "901.95",
        "Turnover (in Lakhs)": "40,640.85",
        "Close Price": "895.35",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "889.10",
        "Date": "25-Sep-2017",
        "Last Traded Price ": "        901.00",
        "Total Traded Quantity": "45,44,350",
        "Open Price": "901.00"
    },
    {
        "High Price": "910.25",
        "Turnover (in Lakhs)": "78,982.73",
        "Close Price": "898.30",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "888.00",
        "Date": "22-Sep-2017",
        "Last Traded Price ": "        899.00",
        "Total Traded Quantity": "88,02,044",
        "Open Price": "908.15"
    },
    {
        "High Price": "915.25",
        "Turnover (in Lakhs)": "37,369.52",
        "Close Price": "909.55",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "908.15",
        "Date": "21-Sep-2017",
        "Last Traded Price ": "        911.00",
        "Total Traded Quantity": "41,02,076",
        "Open Price": "915.00"
    },
    {
        "High Price": "917.00",
        "Turnover (in Lakhs)": "26,271.53",
        "Close Price": "912.70",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "907.45",
        "Date": "20-Sep-2017",
        "Last Traded Price ": "        913.30",
        "Total Traded Quantity": "28,83,915",
        "Open Price": "917.00"
    },
    {
        "High Price": "916.00",
        "Turnover (in Lakhs)": "27,486.42",
        "Close Price": "912.25",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "903.50",
        "Date": "19-Sep-2017",
        "Last Traded Price ": "        912.70",
        "Total Traded Quantity": "30,16,665",
        "Open Price": "908.00"
    },
    {
        "High Price": "917.75",
        "Turnover (in Lakhs)": "38,685.13",
        "Close Price": "909.10",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "906.30",
        "Date": "18-Sep-2017",
        "Last Traded Price ": "        908.80",
        "Total Traded Quantity": "42,37,930",
        "Open Price": "910.00"
    },
    {
        "High Price": "913.25",
        "Turnover (in Lakhs)": "60,894.09",
        "Close Price": "908.25",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "892.20",
        "Date": "15-Sep-2017",
        "Last Traded Price ": "        908.60",
        "Total Traded Quantity": "67,29,730",
        "Open Price": "892.30"
    },
    {
        "High Price": "896.60",
        "Turnover (in Lakhs)": "61,053.28",
        "Close Price": "892.40",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "881.60",
        "Date": "14-Sep-2017",
        "Last Traded Price ": "        892.30",
        "Total Traded Quantity": "68,49,003",
        "Open Price": "884.50"
    },
    {
        "High Price": "887.60",
        "Turnover (in Lakhs)": "50,719.27",
        "Close Price": "883.75",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "881.00",
        "Date": "13-Sep-2017",
        "Last Traded Price ": "        884.50",
        "Total Traded Quantity": "57,39,114",
        "Open Price": "885.50"
    },
    {
        "High Price": "887.75",
        "Turnover (in Lakhs)": "76,032.70",
        "Close Price": "884.05",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "878.80",
        "Date": "12-Sep-2017",
        "Last Traded Price ": "        883.25",
        "Total Traded Quantity": "86,20,677",
        "Open Price": "882.55"
    },
    {
        "High Price": "891.80",
        "Turnover (in Lakhs)": "60,728.47",
        "Close Price": "878.70",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "873.65",
        "Date": "11-Sep-2017",
        "Last Traded Price ": "        879.95",
        "Total Traded Quantity": "68,93,821",
        "Open Price": "890.40"
    },
    {
        "High Price": "899.00",
        "Turnover (in Lakhs)": "38,206.96",
        "Close Price": "884.30",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "882.10",
        "Date": "08-Sep-2017",
        "Last Traded Price ": "        884.00",
        "Total Traded Quantity": "43,02,271",
        "Open Price": "899.00"
    },
    {
        "High Price": "900.50",
        "Turnover (in Lakhs)": "27,961.81",
        "Close Price": "895.75",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "892.35",
        "Date": "07-Sep-2017",
        "Last Traded Price ": "        894.65",
        "Total Traded Quantity": "31,20,596",
        "Open Price": "900.00"
    },
    {
        "High Price": "900.30",
        "Turnover (in Lakhs)": "34,594.75",
        "Close Price": "895.60",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "890.00",
        "Date": "06-Sep-2017",
        "Last Traded Price ": "        896.90",
        "Total Traded Quantity": "38,67,955",
        "Open Price": "900.00"
    },
    {
        "High Price": "905.00",
        "Turnover (in Lakhs)": "44,075.06",
        "Close Price": "901.90",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "897.25",
        "Date": "05-Sep-2017",
        "Last Traded Price ": "        901.00",
        "Total Traded Quantity": "48,91,696",
        "Open Price": "902.00"
    },
    {
        "High Price": "921.10",
        "Turnover (in Lakhs)": "46,007.18",
        "Close Price": "900.20",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "893.50",
        "Date": "04-Sep-2017",
        "Last Traded Price ": "        899.95",
        "Total Traded Quantity": "50,88,554",
        "Open Price": "921.00"
    },
    {
        "High Price": "925.90",
        "Turnover (in Lakhs)": "38,778.10",
        "Close Price": "919.95",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "910.00",
        "Date": "01-Sep-2017",
        "Last Traded Price ": "        919.85",
        "Total Traded Quantity": "42,16,961",
        "Open Price": "915.95"
    },
    {
        "High Price": "928.95",
        "Turnover (in Lakhs)": "68,861.39",
        "Close Price": "914.95",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "912.90",
        "Date": "31-Aug-2017",
        "Last Traded Price ": "        915.00",
        "Total Traded Quantity": "75,11,226",
        "Open Price": "928.80"
    },
    {
        "High Price": "939.00",
        "Turnover (in Lakhs)": "75,141.26",
        "Close Price": "926.65",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "924.10",
        "Date": "30-Aug-2017",
        "Last Traded Price ": "        926.70",
        "Total Traded Quantity": "80,74,832",
        "Open Price": "937.20"
    },
    {
        "High Price": "942.00",
        "Turnover (in Lakhs)": "62,401.10",
        "Close Price": "927.45",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "925.55",
        "Date": "29-Aug-2017",
        "Last Traded Price ": "        926.75",
        "Total Traded Quantity": "66,84,696",
        "Open Price": "941.45"
    },
    {
        "High Price": "953.95",
        "Turnover (in Lakhs)": "1,92,328.51",
        "Close Price": "941.00",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "938.00",
        "Date": "28-Aug-2017",
        "Last Traded Price ": "        940.30",
        "Total Traded Quantity": "2,03,56,054",
        "Open Price": "943.95"
    },
    {
        "High Price": "918.25",
        "Turnover (in Lakhs)": "1,92,984.33",
        "Close Price": "912.15",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "902.35",
        "Date": "24-Aug-2017",
        "Last Traded Price ": "        911.50",
        "Total Traded Quantity": "2,11,90,262",
        "Open Price": "910.00"
    },
    {
        "High Price": "903.70",
        "Turnover (in Lakhs)": "2,72,829.14",
        "Close Price": "892.80",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "873.90",
        "Date": "23-Aug-2017",
        "Last Traded Price ": "        893.40",
        "Total Traded Quantity": "3,06,42,095",
        "Open Price": "880.00"
    },
    {
        "High Price": "897.05",
        "Turnover (in Lakhs)": "2,15,755.53",
        "Close Price": "875.40",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "860.00",
        "Date": "22-Aug-2017",
        "Last Traded Price ": "        876.00",
        "Total Traded Quantity": "2,46,21,299",
        "Open Price": "895.20"
    },
    {
        "High Price": "924.00",
        "Turnover (in Lakhs)": "4,01,714.79",
        "Close Price": "873.40",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "870.00",
        "Date": "21-Aug-2017",
        "Last Traded Price ": "        870.15",
        "Total Traded Quantity": "4,52,03,588",
        "Open Price": "924.00"
    },
    {
        "High Price": "1,017.90",
        "Turnover (in Lakhs)": "7,66,250.24",
        "Close Price": "923.25",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "884.20",
        "Date": "18-Aug-2017",
        "Last Traded Price ": "        923.15",
        "Total Traded Quantity": "8,22,02,480",
        "Open Price": "1,017.90"
    },
    {
        "High Price": "1,029.25",
        "Turnover (in Lakhs)": "1,30,547.60",
        "Close Price": "1,020.85",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "998.05",
        "Date": "17-Aug-2017",
        "Last Traded Price ": "       1021.05",
        "Total Traded Quantity": "1,28,92,130",
        "Open Price": "1,005.00"
    },
    {
        "High Price": "986.10",
        "Turnover (in Lakhs)": "30,142.54",
        "Close Price": "975.20",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "969.00",
        "Date": "16-Aug-2017",
        "Last Traded Price ": "        979.35",
        "Total Traded Quantity": "30,89,040",
        "Open Price": "982.00"
    },
    {
        "High Price": "989.20",
        "Turnover (in Lakhs)": "18,731.63",
        "Close Price": "981.45",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "977.15",
        "Date": "14-Aug-2017",
        "Last Traded Price ": "        982.00",
        "Total Traded Quantity": "19,08,235",
        "Open Price": "988.00"
    },
    {
        "High Price": "997.00",
        "Turnover (in Lakhs)": "32,289.22",
        "Close Price": "987.70",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "969.60",
        "Date": "11-Aug-2017",
        "Last Traded Price ": "        986.50",
        "Total Traded Quantity": "32,72,078",
        "Open Price": "976.00"
    },
    {
        "High Price": "987.50",
        "Turnover (in Lakhs)": "44,880.73",
        "Close Price": "981.25",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "969.35",
        "Date": "10-Aug-2017",
        "Last Traded Price ": "        984.95",
        "Total Traded Quantity": "45,70,342",
        "Open Price": "969.90"
    },
    {
        "High Price": "973.90",
        "Turnover (in Lakhs)": "19,015.04",
        "Close Price": "969.35",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "964.55",
        "Date": "09-Aug-2017",
        "Last Traded Price ": "        970.70",
        "Total Traded Quantity": "19,61,205",
        "Open Price": "967.65"
    },
    {
        "High Price": "970.25",
        "Turnover (in Lakhs)": "28,925.79",
        "Close Price": "963.85",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "955.05",
        "Date": "08-Aug-2017",
        "Last Traded Price ": "        963.50",
        "Total Traded Quantity": "30,02,324",
        "Open Price": "968.50"
    },
    {
        "High Price": "983.75",
        "Turnover (in Lakhs)": "29,528.35",
        "Close Price": "968.25",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "965.70",
        "Date": "07-Aug-2017",
        "Last Traded Price ": "        966.50",
        "Total Traded Quantity": "30,36,872",
        "Open Price": "983.50"
    },
    {
        "High Price": "989.00",
        "Turnover (in Lakhs)": "26,251.09",
        "Close Price": "983.75",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "976.05",
        "Date": "04-Aug-2017",
        "Last Traded Price ": "        983.50",
        "Total Traded Quantity": "26,74,509",
        "Open Price": "988.00"
    },
    {
        "High Price": "998.75",
        "Turnover (in Lakhs)": "22,928.70",
        "Close Price": "984.00",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "980.25",
        "Date": "03-Aug-2017",
        "Last Traded Price ": "        981.80",
        "Total Traded Quantity": "23,20,174",
        "Open Price": "991.00"
    },
    {
        "High Price": "1,012.75",
        "Turnover (in Lakhs)": "21,267.81",
        "Close Price": "993.35",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "987.20",
        "Date": "02-Aug-2017",
        "Last Traded Price ": "        989.10",
        "Total Traded Quantity": "21,28,792",
        "Open Price": "1,006.00"
    },
    {
        "High Price": "1,017.00",
        "Turnover (in Lakhs)": "38,653.74",
        "Close Price": "1,005.55",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "998.35",
        "Date": "01-Aug-2017",
        "Last Traded Price ": "       1004.50",
        "Total Traded Quantity": "38,44,699",
        "Open Price": "1,011.00"
    },
    {
        "High Price": "1,021.70",
        "Turnover (in Lakhs)": "96,535.94",
        "Close Price": "1,011.20",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "986.75",
        "Date": "31-Jul-2017",
        "Last Traded Price ": "       1015.00",
        "Total Traded Quantity": "95,79,124",
        "Open Price": "991.90"
    },
    {
        "High Price": "1,003.00",
        "Turnover (in Lakhs)": "54,782.02",
        "Close Price": "997.35",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "962.30",
        "Date": "28-Jul-2017",
        "Last Traded Price ": "        995.70",
        "Total Traded Quantity": "55,49,214",
        "Open Price": "976.00"
    },
    {
        "High Price": "1,004.00",
        "Turnover (in Lakhs)": "62,220.56",
        "Close Price": "971.05",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "966.80",
        "Date": "27-Jul-2017",
        "Last Traded Price ": "        969.85",
        "Total Traded Quantity": "63,38,426",
        "Open Price": "996.00"
    },
    {
        "High Price": "999.00",
        "Turnover (in Lakhs)": "34,138.53",
        "Close Price": "994.05",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "990.40",
        "Date": "26-Jul-2017",
        "Last Traded Price ": "        994.00",
        "Total Traded Quantity": "34,35,012",
        "Open Price": "998.10"
    },
    {
        "High Price": "999.00",
        "Turnover (in Lakhs)": "35,471.55",
        "Close Price": "993.85",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "986.20",
        "Date": "25-Jul-2017",
        "Last Traded Price ": "        994.00",
        "Total Traded Quantity": "35,72,807",
        "Open Price": "990.00"
    },
    {
        "High Price": "994.00",
        "Turnover (in Lakhs)": "30,326.47",
        "Close Price": "990.55",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "982.60",
        "Date": "24-Jul-2017",
        "Last Traded Price ": "        990.50",
        "Total Traded Quantity": "30,64,588",
        "Open Price": "983.50"
    },
    {
        "High Price": "982.55",
        "Turnover (in Lakhs)": "29,259.22",
        "Close Price": "980.10",
        "Series": "EQ",
        "Symbol": "INFY",
        "Low Price": "971.40",
        "Date": "21-Jul-2017",
        "Last Traded Price ": "        979.90",
        "Total Traded Quantity": "29,90,377",
        "Open Price": "973.00"
    }
]
```
