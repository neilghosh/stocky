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

import webapp2
from google.appengine.api import urlfetch
import re
import json
import urllib
import csv, io
import logging
from auth import Auth

class MainPage(webapp2.RequestHandler):
    def get(self):
        if not Auth().validate_key(self.request):
            self.response.status = 401
            return
        name = self.request.get("name")
        url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxCompanySearch.jsp?search='+name.replace(" ", "%20")
        logging.info(url)
        try:
            result = urlfetch.fetch(url)
            logging.info(result)
            if result.status_code == 200:
            	# regex = "itpFlag=0(.*?)<span class='symbol'"
            	regex = "(symbol=.*?&illiquid).*?(itpFlag=0'>.*?<span)"
            	pattern = re.compile(regex)
            	companies = {}
                for (x,y) in re.findall(pattern, result.content):
                	companies[x[7:][:-9]] = y[11:].replace('<b >','').replace('</b>','')[:-5]
                	## names.append(name[6:].replace('<b >','').replace('</b>',''))
                self.response.write(json.dumps(companies))
            else:
                self.response.status_code = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')
        self.response.headers['Content-Type'] = 'application/json'

class QuotePage(webapp2.RequestHandler):
    def get(self):
        if not Auth().validate_key(self.request):
            self.response.status = 401
            return
        name = self.request.get("name")
        ## url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp?symbol='+name.replace(" ", "%20")+'&series=EQ'
        url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+name.replace(" ", "%20")+'&illiquid=0&smeFlag=0&itpFlag=0'
        logging.info(url)
        try:
            result = urlfetch.fetch(url)
            logging.info(result)
            if result.status_code == 200:
                regex = '{"futLink".*'
                pattern = re.compile(regex)
                data = re.findall(pattern, result.content)
                jsonData = json.loads(data[0])
                logging.info(jsonData)
                self.response.write(json.dumps(jsonData['data'][0]))
            else:
                self.response.status_code = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')
        self.response.headers['Content-Type'] = 'application/json'

class HistoricalDataPage(webapp2.RequestHandler):
    def get(self):
        if not Auth().validate_key(self.request):
            self.response.status = 401
            return
        name = self.request.get("name")
        startDate = self.request.get("startdate")
        endDate = self.request.get("enddate")
        datePeriod = self.request.get("dateperiod")
        ## url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp?symbol='+name.replace(" ", "%20")+'&series=EQ'
        ##         url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol='+name+'&series=EQ&fromDate='+startDate+'&toDate='+endDate+''
        ## url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol='+name+'&series=EQ&fromDate=undefined&toDate=undefined&datePeriod=3months&hiddDwnld=true'
        ##url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol='+name+'&series=EQ&fromDate=01-Jul-2017&toDate=13-Jul-2017'
        url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol='+name+'&series=EQ&fromDate='+startDate+'&toDate='+endDate+'&datePeriod='+datePeriod+''
        ## http://localhost:8080/getdata?name=TCS&startdate=01-07-2016&enddate=18-07-2017&dateperiod=3months
        logging.info(url)
        try:
            result = urlfetch.fetch(url)
            logging.info(result)
            if result.status_code == 200:
                regex = '"Date".*:'
                pattern = re.compile(regex)
                data = re.findall(pattern, result.content)[0].replace(':','\n')
                logging.info(data)
                ##fieldnames = ("Date","Symbol","Series","Open Price","High Price","Low Price","Last Traded Price ","Close Price","Total Traded Quantity","Turnover (in Lakhs)")
                reader = csv.DictReader(io.StringIO(unicode(data)))
                json_data = json.dumps(list(reader))
                self.response.write(json_data)
            else:
                self.response.status_code = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')
        self.response.headers['Content-Type'] = 'application/json'



app = webapp2.WSGIApplication([
    ('/api/companysearch', MainPage),
    ('/api/getquote', QuotePage),
    ('/api/getdata', HistoricalDataPage),
], debug=True)
