# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import csv
import io
import json
import logging
import re

import requests
from flask import Flask, request

from auth import Auth

app = Flask(__name__)


@app.route("/api/companysearch")
def get_company_info():
    if not Auth().validate_key(request):
        #self.response.status = 401
        return "", 401
    name = request.args["name"]
    url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxCompanySearch.jsp?search=' + \
        name.replace(" ", "%20")
    logging.info(url)
    print(url)
    try:
        # NSE needs these headers
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                   'accept': 'application/json', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en-US,en;q=0.8'}

        result = requests.get(url=url, headers=headers, timeout=5)
        logging.info(result)
        if result.status_code == 200:
            # regex = "itpFlag=0(.*?)<span class='symbol'"
            regex = "(symbol=.*?&illiquid).*?(itpFlag=0'>.*?<span)"
            pattern = re.compile(regex)
            companies = {}
            for (x, y) in re.findall(pattern, result.text):
                companies[x[7:][:-9]
                          ] = y[11:].replace('<b >', '').replace('</b>', '')[:-5]
                ## names.append(name[6:].replace('<b >','').replace('</b>',''))
                headers = {'Content-Type': 'application/json'}
            return json.dumps(companies), 200, headers
        else:
            return "", result.status_code
    except (requests.exceptions.RequestException, requests.exceptions.Timeout) as ex:
        logging.exception('Caught exception fetching url')
        return "", 500
    except Exception as e:
        return "{}", 500


@app.route("/api/getquote")
def get_quote():
    if not Auth().validate_key(request):
        return "", 401
    name = request.args["name"]
    ## url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp?symbol='+name.replace(" ", "%20")+'&series=EQ'
    url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=' + \
        name.replace(" ", "%20")+'&illiquid=0&smeFlag=0&itpFlag=0'
    print(url)
    logging.info(url)
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                   'accept': 'application/json', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en-US,en;q=0.8'}

        result = requests.get(url=url, headers=headers, timeout=5)

        logging.info(result)
        if result.status_code == 200:
            regex = '{"tradedDate".*'
            pattern = re.compile(regex)
            # print(result.text)
            data = re.findall(pattern, result.text)
            jsonData = json.loads(data[0])
            logging.info(jsonData)
            return json.dumps(jsonData['data'][0])
        else:
            return "", result.status_code
    except requests.exceptions.RequestException:
        logging.exception('Caught exception fetching url')
    ##self.response.headers['Content-Type'] = 'application/json'


@app.route("/api/getdata")
def get_data():
    if not Auth().validate_key(request):
        return 401
    name = request.args["name"]
    startDate = request.args["startdate"]
    endDate = request.args["enddate"]
    datePeriod = request.args["dateperiod"]
    ## url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp?symbol='+name.replace(" ", "%20")+'&series=EQ'
    ##         url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol='+name+'&series=EQ&fromDate='+startDate+'&toDate='+endDate+''
    ## url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol='+name+'&series=EQ&fromDate=undefined&toDate=undefined&datePeriod=3months&hiddDwnld=true'
    ##url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol='+name+'&series=EQ&fromDate=01-Jul-2017&toDate=13-Jul-2017'
    url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol=' + \
        name+'&series=EQ&fromDate='+startDate + \
        '&toDate='+endDate+'&datePeriod='+datePeriod+''
    # http://localhost:8080/getdata?name=TCS&startdate=01-07-2016&enddate=18-07-2017&dateperiod=3months
    logging.info(url)
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                   'accept': 'application/json', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en-US,en;q=0.8'}

        result = requests.get(url=url, headers=headers, timeout=5)
        logging.info(result)
        if result.status_code == 200:
            regex = '"Date".*:'
            pattern = re.compile(regex)
            data = re.findall(pattern, result.text)[
                0].replace(':', '\n')
            logging.info(data)
            ##fieldnames = ("Date","Symbol","Series","Open Price","High Price","Low Price","Last Traded Price ","Close Price","Total Traded Quantity","Turnover (in Lakhs)")
            reader = csv.DictReader(io.StringIO(str(data)))
            json_data = json.dumps(list(reader))
            return json_data
        else:
            return "", result.status_code
    except requests.exceptions.RequestException:
        logging.exception('Caught exception fetching url')
    ##self.response.headers['Content-Type'] = 'application/json'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
