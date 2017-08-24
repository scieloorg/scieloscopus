<<<<<<< HEAD


# scieloscopus
Library to delivery Scopus and Scimago indicators of SciELO Journals.


### How to install:

```
pip install scieloscopus
```

### How to use:
```
from scieloscopus import scopusindicators

scopusindicators.get_current_indicators('0036-3634')

#OUTPUT:
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
'year': 2016}
      

scopusindicators.get_indicators('2197-0025', '2015')

#OUTPUT:
{'cites_by_doc_2years': 0.41,
'citescore': 0.6,
'h_index': 4,
'ipp': 0.409090909090909,
'issn_scielo': '2197-0025',
'scopus_id': 21100334898,
'sjr': 0.172,
'sjr_best_quartile': 'Q4',
'snip': 0.187043499875161,
'year': 2015}


scopusindicators.UPDATE_INDICATORS
#OUTPUT: 
'2017-06-27'

```

## Badges
[![Build Status](https://travis-ci.org/scieloorg/scielojcr.svg?branch=master)](https://travis-ci.org/scieloorg/scielojcr)
[![PyPi version](https://img.shields.io/pypi/v/scielojcr.svg)](https://pypi.python.org/pypi/scielojcr)
[![Code Health](https://landscape.io/github/scieloorg/scielojcr/master/landscape.svg?style=flat)](https://landscape.io/github/scieloorg/scielojcr/master)
=======
# scieloscopus
Library to delivery Scopus and Scimago indicators of SciELO Journals.
>>>>>>> d3b9fb76b50759840b5c77caba9a8d29baef6744
