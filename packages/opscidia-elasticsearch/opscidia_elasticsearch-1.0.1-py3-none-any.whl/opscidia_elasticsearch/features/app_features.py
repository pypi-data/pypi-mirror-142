# @copyright  Copyright (c) 2018-2020 Opscidia
from elasticsearch_dsl import connections, Search, Q

from typing import List, Optional, Dict, Union


def search(
    index: str = 'articles',
    field: str = 'content',
    query: Q = None,
    sources: List = [],
    highlight: Dict = {},
    extras: Dict = {}
):

    """
    Pull articles from index using keywords query
    
    keywords: (list) of keywords
    field: (str) field name to quieried
    index: (str) ES index name
    review: (bool) Filter for reviews only. Default False
    date_start: (str) Filter article from YYYY-MM-DD. Default None
    date_end: (str) Filter article until YYYY-MM-DD. Defaut None
    source: (list) of fields to be returned
    page_start: (int) Index article to start. Default 0
    page_end: (int) Index article to end > start. Default 10
    total_hits: (bool, int) If true, stops when all the documents are scanned.
        If int, stops if the limit is reached. Default 500
    
    :return: Dict[stats, hits]
    """

    _s = Search(index = index).extra(**extras).query(query)

    if len(highlight.keys()) > 0:
        _s = _s.highlight(field, **highlight)
    if len(sources) > 0:
        _s = _s.source(sources)

    resp = _s.execute()
    
    # resp = Search(index = index).extra(**extras).query(query).highlight(
    #     field, **highlight).source(sources).execute()
    
    return resp