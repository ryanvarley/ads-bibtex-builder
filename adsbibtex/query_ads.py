""" queries ads using https://github.com/adsabs/adsabs-dev-api
"""

import ads


try:  # Temp version patch for ads module
    ads.SearchQuery
except AttributeError:
    ads.SearchQuery = ads.query


def bibcode_to_bibtex(bibcode):
    """ queries ads

    :param bibcode:
    :return:
    """

    query_result = ads.SearchQuery(bibcode=bibcode)

    papers = list(query_result)

    if len(papers) == 1:  # 0 failed, 2 is ambiguous
        return papers[0].bibtex



    print '{} failed :-('.format(bibcode)