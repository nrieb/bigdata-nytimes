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
    url = "http://api.nytimes.com/svc/news/v3/content/all/all/.json"
    return (url, payload)

#   section_request :: (URL, {String:String})
def section_request():
    """Section request url / payload"""
    payload = {"api-key":API_KEY}
    url = "http://api.nytimes.com/svc/news/v3/content/section-list.json"
    return (url, payload)

# data StoredRecord = StoredRecord String String String
StoredRecord = namedtuple("StoredRecord", ["title", "created_date", "url"])

# handle_response :: JSON -> [StoredRecord]
# -> (Maybe [JSON], [StoredRecord])
def handle_response(response, stored_records):
    """Handle the response from the nytimes request"""
    storage = list(stored_records)
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
                storage.append(record)
                lines.append(result)

        return (lines, storage)

#   main :: IO()
def main():
    """main program"""
    stored_records = []
    next_request_time = 0 # start right away
    article_offset = 0
    retry_count = 0
    logging.basicConfig(level=logging.INFO)

    while len(stored_records) < 50000:

        #Time for another request
        if time.time() > next_request_time:
            # make the request
            (url, payload) = nyt_request(article_offset)
            req = requests.get(url, params=payload)
            logging.debug("request to {0}".format(req.url))
            # handle server errors
            if req.status_code != requests.codes.ok:
                retry_count += 0
                if retry_count < RETRY_LIMIT:
                    logging.debug("bad status code.  retrying")
                    next_request_time = time.time() + RETRY_TIME
                    continue
                else:
                    error_msg = "bad status code. more than {0} retrys. ending"
                    logging.info(error_msg.format(RETRY_LIMIT))
                    return

            # reset consecutive count
            retry_count = 0
            response = req.json()
            (json_records, stored_records) = handle_response(response,
                                                             stored_records)

            #print record
            if json_records:
                logging.debug("writing {0} records".format(len(json_records)))
                for line in json_records:
                    print(line)
            else:
                logging.warning("got an error response")

            if len(stored_records) % 1000 == 0:
                logging.info("Wrote {0} record".format(len(stored_records)))
            article_offset += 20 # each response should have 20 in it.
            next_request_time = time.time() + REQUEST_TIME
        else:
            time.sleep(TWENTY_FIVE_MS)

'''-------------------------------------------------------------------------'''
if __name__ == "__main__":
    main()
