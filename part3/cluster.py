#!/usr/bin/env python

# Code heavily influed by:
# http://dev.bizo.com/2012/01/clustering-of-sparse-data-using-python.html
import csv
from scipy.sparse import lil_matrix
from sklearn.cluster import KMeans, SpectralClustering, MiniBatchKMeans
import logging
import sys
import json
import math

def extract_nonzero(fname):
    """
    extracts nonzero entries from a csv file
    input: fname (str) -- path to csv file
    output: generator<(int, int, float)> -- generator
    producing 3-tuple containing (row-index, column-index, data)
    """
    with open(fname, "r") as f:
        for (doc, _, word, tfidf) in csv.reader(f):
            yield (int(doc, 16), int(word, 16), float(tfidf))

def get_dimensions(fname):
    """
    determines the dimension of a csv file
    input: fname (str) -- path to csv file
    output: (nrows, ncols) -- tuple containing row x col data
    """
    with open(fname, "r") as f:
        colsize = 0
        rowsize = 0
        for (doc_id, _, word_id, _) in csv.reader(f):
            row = int(doc_id, 16)
            col = int(word_id, 16)
            if row > rowsize:
                rowsize = row
            if col > colsize:
                colsize = col

    return (rowsize+1, colsize+1)

# obtain dimensions of data
(rdim, cdim) = get_dimensions("word_id.csv")
logging.basicConfig(level=logging.INFO)
logging.info("rdim {0}, cdim {1}".format(rdim, cdim))
# allocate a lil_matrix of size (rdim by cdim)
# note: lil_matrix is used since we be modifying
#       the matrix a lot.
S = lil_matrix((rdim, cdim))
CP = lil_matrix((rdim, cdim))

def normalize(s, rdim):
    
    for rowid in xrange(0, rdim):
        row = s.getrowview(rowid)
        _, colidx = row.nonzero()
        sum = 0
        for i in colidx:
            sum += row[0, i]**2

        _, colidx = row.nonzero()
        
        for i in colidx:
            row[0,i] /= math.sqrt(sum)

# add data to S
for (i, j, d) in extract_nonzero("word_id.csv"):
    S[i, j] = d

for (i, j, d) in extract_nonzero("word_id.csv"):
    CP[i, j] = d

normalize(S, rdim)

"""
      1 Afternoon Update 
   1391 Arts 
x    470 Arts Art & Design
     10 Arts Arts
    306 Arts Dance
    132 Arts International Arts
    759 Arts Music
    455 Arts Television
     20 Arts Video Games
x    322 Automobiles 
      2 Automobiles Automobiles
     42 Automobiles Collectible Cars
     61 Automobiles New Cars
      6 Blogs 
x    223 Books 
    560 Books Sunday Book Review
   1147 Business Day 
x   1844 Business Day Dealbook
     15 Business Day DealBook
    130 Business Day Economy
     83 Business Day Energy & Environment 
    545 Business Day International Business
    655 Business Day Media
     17 Business Day Mutual Funds
     11 Business Day Retirement
    274 Business Day Small Business
    319 Corrections 
      1 Crosswords & Games 
x    215 Crosswords/Games 
     70 Crosswords & Games Bridge
     22 Crosswords & Games Chess
      1 Crosswords & Games Premium
x    440 Dining & Wine 
     33 Education 
     19 Education Education Life
x    784 Fashion & Style 
      1 Fashion & Style Trends
x    857 Fashion & Style Weddings/Celebrations
      2 Feeds 
     10 Great Homes and Destinations 
     90 Great Homes & Destinations 
x    583 Health 
      1 Health Research
x    249 Home & Garden 
     37 Job Market 
    453 Magazine 
x    856 Movies 
     24 Movies DVD
    242 Multimedia 
    368 Multimedia/Photos 
   2846 N.Y. / Region 
      6 Obituaries 
      8 Open 
   3585 Opinion 
      1 Opinion International Opinion
    403 Opinion Sunday Review
     47 Opinion The Public Editor
      9 Public Editor 
x    287 Real Estate 
     82 Real Estate Commercial Real Estate
      1 Real Estate Communities
x    405 Science 
     22 Science Environment
     35 Science Space & Cosmos
x    713 Sports 
    144 Sports Auto Racing
x    801 Sports Baseball
     23 Sports College Basketball
    150 Sports College Football
      4 Sports Cricket
     87 Sports Cycling
    265 Sports Golf
    233 Sports Hockey
      1 Sports International Sports
     26 Sports Olympics
    365 Sports Pro Basketball
x    482 Sports Pro Football
     19 Sports Rugby
      3 Sports Skiing
x    362 Sports Soccer
    340 Sports Tennis
    332 Sports World Cup
      6 Style 
     64 Style Fashion &amp; Style
     12 Style Fashion & Style
      3 Style International Style
      3 Style T Magazine
     44 Sunday Review 
x    806 Technology 
    169 Technology Personal Tech
x    446 Theater 
     23 Theater Tony Awards
    767 The Upshot 
     73 T Magazine 
    507 Travel 
    462 T:Style 
x   2765 U.S. 
    518 U.S. Education
    761 U.S. Politics
    124 World 
x    403 World Africa
    244 World Americas
x   1553 World Asia Pacific
x   1097 World Europe
x   1164 World Middle East
    148 Your Money 
      1 Your Money Annuities
      6 Your Money Asset Allocation
      2 Your Money Auto Insurance
      2 Your Money Credit and Debit Cards
      3 Your Money Estate Planning
      2 Your Money Financial Planners
      2 Your Money Health Insurance
      1 Your Money Home Insurance
      2 Your Money Household Budgeting
      1 Your Money Individual Retirement Accounts (IRA's)
      1 Your Money Life and Disability Insurance
      2 Your Money Paying for College
      1 Your Money Stocks and Bonds
      2 Your Money Student Loans
"""

# perform clustering
labeler = KMeans(n_clusters=24)
#labeler = MiniBatchKMeans(n_clusters=8)
#labeler = SpectralClustering(n_clusters=8)
# convert lil to csr format
# note: Kmeans currently only works with CSR type sparse matrix
labeler.fit(S.tocsr())



# print cluster assignments for each row
print "docid,label,wordid,tfidf"
for (rowidx, label) in enumerate(labeler.labels_):
    row = CP.getrow(rowidx)
    _ , colidxs = row.nonzero()
    for colidx in colidxs:
        print "{docid:x},{label},{wordid:x},{tfidf}".format(docid=rowidx,
                                                        label=label,
                                                        wordid=colidx,
                                                        tfidf=row[0,colidx])
