"""
Quickly hacked-together script for pulling Konrad's citations from Google
Scholar, and formatting them according to the Markdown shown on http://kordinglab.com/publication/

requests-html used to avoid captcha/violating Google ToS.
"""
from requests_html import HTMLSession
from datetime import datetime


def get_citation_links(session, profile_url):
    """
    From the given url to Google scholar page, extract all absolute links to
    paper citations.

    Args:
       session (HTMLSession)
       profile_url (str): a url to a person's Google Scholar page.

    Returns:
        list: list of absolute URLs to paper cites.

    """
    r = session.get(profile_url)

    links = r.html.absolute_links

    assert len(links) > 0, "No paper cites, did we hit a captcha?"

    paper_links = [link for link in links if "view_citation" in link]

    return paper_links


"""Hard coded strings to extract from the Google Scholar "View article" page"""
AUTHOR = "Authors"
PUB_DATE = "Publication date"
JOURNAL = "Journal"
SOURCE = "Source"
TITLE = "Scholar articles"
URL = 'url'

def get_paper_data(session, paper_url):
    """
    Extracts paper citation data from the detailed citation page.

    Args:
        session (HTMLSession)
        paper_url (str): detailed citation url page

    Returns:
        dict: dictionary containing author, publication date, dournal, link

    """
    paper_dict = {}

    r = session.get(paper_url)
    divs = r.html.find('div')

    table_text = ""
    link_div = None
    for div in divs:
        attrs = div.attrs
        # the gsc_oci_table has newline separated key/value information
        # where the next element is the value
        if 'id' in attrs:
            if attrs['id'] == 'gsc_oci_table':
                table_text = div.text
            if attrs['id'] == 'gsc_oci_title_gg':
                link_div = div

    table_list = table_text.split("\n")

    if AUTHOR in table_list:
        paper_dict[AUTHOR] = table_list[table_list.index(AUTHOR) + 1]

    if TITLE in table_list:
        paper_dict[TITLE] = table_list[table_list.index(TITLE) + 1]

    if PUB_DATE in table_list:
        paper_dict[PUB_DATE] = table_list[table_list.index(PUB_DATE) + 1]
        #paper_dict[PUB_DATE] = datetime.strptime(paper_dict[PUB_DATE], "%Y/%m/%d")

    if JOURNAL in table_list:
        paper_dict[JOURNAL] = table_list[table_list.index(JOURNAL) + 1]
    elif SOURCE in table_list:
        paper_dict[JOURNAL] = table_list[table_list.index(SOURCE) + 1]

    if link_div:
        paper_dict[URL] = link_div.absolute_links.pop()
    else:
        paper_dict[URL] = paper_url

    return paper_dict


def print_markdown(paper_dict):
    """
    Formats the markdown from the information provided in paper_dict.

    Prints to stdout.

    Args:
        paper_dict (dict): output from get_paper_data()

    Returns:
        None
    """

    # it appears that only patents are missing author/journal
    if AUTHOR in paper_dict and JOURNAL in paper_dict:
        print("_{}_<br>".format(paper_dict[TITLE]))
        print("{}<br>".format(paper_dict[AUTHOR]))
        print("{}, {} ([Article]({}))".format(
            paper_dict[JOURNAL],
            paper_dict[PUB_DATE].split("/")[0],
            paper_dict[URL],
        ))

if __name__ == "__main__":
    konrad_profile_url = "https://scholar.google.com/citations?hl=en&user=MiFqJGcAAAAJ&view_op=list_works&sortby=pubdate"
    session = HTMLSession()
    citation_links = get_citation_links(session, konrad_profile_url)

    paper_data = [get_paper_data(session, url) for url in citation_links]

    # sort by recency, so reversed
    paper_data.sort(key=lambda x: x[PUB_DATE] if PUB_DATE in x else "", reverse=True)
    for paper in paper_data:
        print_markdown(paper)
        print()