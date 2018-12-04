from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# <--- Setting up scraper -->

def log_error(e):
    """
    PRINTS ERRORS TO CONSOLE
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def is_good_response(resp):
    """
    CHECKS FOR 200 RESPONSE ON ASSET
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return resp.status_code == 200 and content_type is not None and content_type.find('html') > -1


def simple_get(url):
    """
    GRABS CONTENT FROM ASSET
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during request to {0} : {1}'.format(url, str(e)))
        return None

# <---- Actual Math Man Finding --->

def get_names():
    """
    GRAB RAW ASSETS
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician

    Names are returned as a list with no duplicates to be passed into get_hits_on_name
    """
    url = 'http://www.fabpedigree.com/james/mathmen.htm'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        # print(names)
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))



def get_hits_on_name(name):
    """
    GETS NUMBER OF HITS ON NAME BY NAME BASIS

    Accepts a `name` of a mathematician and returns the number
    of hits that mathematician's Wikipedia page received in the
    last 60 days, as an `int`

    This isn't working as we're getting the entire list that we've provided in

    Should I abstract the name checking stuff out of this function?
    """
    # url_root is a template string that is used to build a URL.
    url_root = 'https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/{}'
    # name = name[0].replace(" ", "%20")
    print(url_root.format(name.replace(" ", "%20")))

    response = simple_get(url_root.format(name))

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')

        # This if statement does not work at all
        if html.get_text(name):
            hit_link = [a for a in html.select('a') if a['href'].find('latest-60') > -1]
            print("LIST: {}, TYPE: {}".format(hit_link, type(hit_link)))
            print(len(hit_link))
        else:
            log_error("{} could not be found".format(name))


        if len(hit_link) > 0:
            # Strip commas
            hit_number = hit_link[0].text.replace(',', '')
            try:
                # Convert to integer
                print(int(hit_number))
                return int(hit_number)
            except:
                log_error("Couldn't parse {} as an int".format(link_text))

    log_error("No pageviews found for {}".format(name))
    return None


def rank_names_by_hit():
    """
    ACCEPTS LIST OF NAMES AND STORES BOTH THE NAME AND THE NUMBER OF HITS, THEN RANKS THEM

    """
    pass

# In file testing

names = get_names()
# print(names[1])
# get_hits_on_name(names[1])
get_hits_on_name("Isaac Newton")
# get_hits_on_name("gkufgsdkfusgadfa")


# """
# Print message which shows the number of mathematicians that were left out of the ranking.
# """
#
# if __name__ == '__main__':
#     print("Getting the list of names...")
#     names = get_names()
#     print("...done! =^.^=")
#
#     results = []
#
#     print("Getting stats for each name...")
#
#     for name in names:
#         try:
#             hits = get_hits_on_name(names)
#             if hits is None:
#                 hits = -1
#             results.append((hits, name))
#
#         except:
#             results.append((-1, name))
#             log_error("Error encountered while processing {}, skipping".format(name))
#
#     print("...done =^.^=")
#
#     results.sort()
#
#     results.reverse()
#
#     if len(results) > 5:
#         top_marks = results[:5]
#     else:
#         top_marks = results
#
#     print("\nThe most popular mathematicians are:\n")
#
#     for (mark, mathematician) in top_marks:
#         print("{} with {} pageviews".format(mathematician, mark))
#
#     no_results = len([res for res in results if res[0] == -1])
#     print("But we did not find results for {}".format(no_results))
