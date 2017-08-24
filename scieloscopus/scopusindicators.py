# coding: utf-8

import os
import csv
import logging

logger = logging.getLogger(__name__)

_CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

JOURNALS = {}

CURRENT_INDICATORS = '2016'

UPDATE_INDICATORS = '2017-06-27'

with open(_CURRENT_DIR + '/data/scielo_scopus_indicators.csv', 'r') as csvfile:

    has_header = csv.Sniffer().has_header(csvfile.read())

    csvfile.seek(0)

    spamreader = csv.reader(csvfile, delimiter='\t')

    if has_header:
        next(spamreader)

    for line in spamreader:

        issn_scielo = line[0]

        year = line[1]

        if line[2]:
            scopus_id = int(line[2])
        else:
            scopus_id = None

        if line[3]:
            citescore = float(line[3])
        else:
            citescore = None

        if line[4]:
            sjr = float(line[4])
        else:
            sjr = None

        if line[5]:
            sjr_best_quartile = line[5]
        else:
            sjr_best_quartile = None

        if line[6]:
            cites_by_doc_2years = float(line[6])
        else:
            cites_by_doc_2years = None

        if line[7]:
            h_index = int(line[7])
        else:
            h_index = None

        if line[8]:
            snip = float(line[8])
        else:
            snip = None

        if line[9]:
            ipp = float(line[9])
        else:
            ipp = None

        JOURNALS.setdefault(issn_scielo, {})

        JOURNALS[issn_scielo][year] = {
            'issn_scielo': issn_scielo,
            'scopus_id': scopus_id,
            'citescore': citescore,
            'sjr': sjr,
            'sjr_best_quartile': sjr_best_quartile,
            'cites_by_doc_2years': cites_by_doc_2years,
            'h_index': h_index,
            'snip': snip,
            'ipp': ipp,
            'year': int(year)
        }


def get_indicators(issn_scielo, year=None):

    data = JOURNALS.get(issn_scielo, None)

    if data and year:
        return data.get(year, None)

    return data


def get_current_indicators(issn_scielo):

    return get_indicators(issn_scielo, CURRENT_INDICATORS)
