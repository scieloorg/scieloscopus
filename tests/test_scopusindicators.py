# coding: utf-8
import unittest
import os
import sys

PROJECT_PATH = os.path.abspath(os.path.dirname(''))
sys.path.append(PROJECT_PATH)

from scieloscopus import scopusindicators


class ScopusTest(unittest.TestCase):

    def test_load_issn_scielo(self):

        result = scopusindicators.get_indicators('2197-0025')

        expected = {
              '2015':
              {
                'cites_by_doc_2years': 0.41,
                'citescore': 0.6,
                'h_index': 4,
                'ipp': 0.409090909090909,
                'issn_scielo': '2197-0025',
                'scopus_id': 21100334898,
                'sjr': 0.172,
                'sjr_best_quartile': 'Q4',
                'snip': 0.187043499875161,
                'year': 2015},
              '2016':
              {
                'cites_by_doc_2years': 0.63,
                'citescore': 0.63,
                'h_index': 4,
                'ipp': 0.565217391304348,
                'issn_scielo': '2197-0025',
                'scopus_id': 21100334898,
                'sjr': 0.236,
                'sjr_best_quartile': 'Q3',
                'snip': 0.312834895072393,
                'year': 2016}}

        self.assertEqual(expected, result)

    def test_load_issn_scielo_year(self):

        result = scopusindicators.get_indicators('2197-0025', '2015')

        expected = {
                'cites_by_doc_2years': 0.41,
                'citescore': 0.6,
                'h_index': 4,
                'ipp': 0.409090909090909,
                'issn_scielo': '2197-0025',
                'scopus_id': 21100334898,
                'sjr': 0.172,
                'sjr_best_quartile': 'Q4',
                'snip': 0.187043499875161,
                'year': 2015}

        self.assertEqual(expected, result)

    def test_load_current_indicators(self):

        result = scopusindicators.get_current_indicators('2197-0025')

        expected = {
                'cites_by_doc_2years': 0.63,
                'citescore': 0.63,
                'h_index': 4,
                'ipp': 0.565217391304348,
                'issn_scielo': '2197-0025',
                'scopus_id': 21100334898,
                'sjr': 0.236,
                'sjr_best_quartile': 'Q3',
                'snip': 0.312834895072393,
                'year': 2016}

        self.assertEqual(expected, result)

    def test_load_update_indicators(self):

        result = scopusindicators.UPDATE_INDICATORS

        expected = '2017-06-27'

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
