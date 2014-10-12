#!/usr/bin/env python
"""Request and print out id,abstract,url from nytimes"""
from __future__ import print_function
import requests
from collections import namedtuple
import time
import logging

API_KEY = "1e9766d00a2b163e1bcaacab404321bf:9:69917539"
# TWENTY_FIVE_MS :: Sec 1
TWENTY_FIVE_MS = 25/1000.0
CHECK_TIME = TWENTY_FIVE_MS
REQUEST_TIME = TWENTY_FIVE_MS * 5
RETRY_TIME = 1 #sec

RETRY_LIMIT = 50

# type URL = String
#   nyt_request :: Int -> (URL, {String:String})
def nyt_request(offset):
    """Returns the url and payload for doc request from nytimes with starting
    at the offset"""
    payload = {"offset":"{0}".format(offset),
               "api-key":API_KEY}
    url = "http://api.nytimes.com/svc/news/v3/content/nyt/all/.json"
    return (url, payload)

#   section_request :: (URL, {String:String})
def section_request():
    """Section request url / payload"""
    payload = {"api-key":API_KEY}
    url = "http://api.nytimes.com/svc/news/v3/content/section-list.json"
    return (url, payload)

# data StoredRecord = StoredRecord String String String
StoredRecord = namedtuple("StoredRecord", ["title", "created_date", "url"])

# handle_response :: {String:String} -> [StoredRecord]
# -> (Maybe [String], [StoredRecord])
def handle_response(response, stored_records):
    """Handle the response from the nytimes request"""
    storage = list(stored_records)
    formatstr = "{abstract},{url}"
    lines = []
    if "error" in response or "results" not in response:
        return (None, storage)
    else:
        for result in response["results"]:
            record = StoredRecord(result["title"],
                                  result["created_date"],
                                  result["url"])
            if record in storage:
                continue
            else:
                storage.append(storage)
                lines.append(formatstr.format(abstract=result["abstract"],
                                              url=result["url"]))
        return (lines, storage)

#   main :: IO()
def main():
    """main program"""
    stored_records = []
    next_request_time = 0 # start right away
    offset = 0
    id_num = 0
    retry_count = 0
    logging.basicConfig(level=logging.DEBUG)
    
    while len(stored_records) < 40:
        if time.time() > next_request_time:
            (url, payload) = nyt_request(offset)
            req = requests.get(url, params=payload)
            logging.debug(r.status_code)
            if req.status_code != requests.codes.ok:
                retry_count += 0
                if retry_count < RETRY_LIMIT:
                    logging.info("bad status code.  retrying")
                    next_request_time = time.time() + RETRY_TIME
                    continue
                else:
                    error_msg = "bad status code. more than {0} retrys. ending"
                    logging.info(error_msg.format(RETRY_LIMIT))
                    return
            
            retry_count = 0
                
            response = req.json()
            (csv_records, stored_records) = handle_response(response,
                                                            stored_records)
            if csv_records:
                for line in csv_records:
                    print("{0},{1}".format(id_num, line))
                    id_num += 1
            else:
                logging.warning("got an error response")
            # print
            offset += 20 # each response should have 20 in it.
            next_request_time = time.time() + REQUEST_TIME
        else:
            time.sleep(TWENTY_FIVE_MS)


if __name__ == "__main__":
    main()
