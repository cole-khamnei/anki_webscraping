import io
import time
import requests
import re

from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup as bsoup
from tqdm.notebook import tqdm
# from tqdm import tqdm


REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/39.0.2171.95 Safari/537.36'
}
ANTI_DOS_DELAY = 0.1


def safe_request(url: str, headers: dict = REQUEST_HEADERS,
                 anti_dos_delay: float = ANTI_DOS_DELAY):
    """"""
    time.sleep(anti_dos_delay)
    try:
        data = requests.get(url, headers=headers)
        return data
    except requests.exceptions.ConnectionError as e:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return requests.get(url, headers=headers, verify=False)

        
def get_html(url: str):
    """"""
    request_content = safe_request(url)
    return bsoup(request_content.content, features="html.parser")


def str_remover(string: str, *tokens):
    """"""
    for token in tokens:
        string = string.replace(token, "")
    return string


def get_box_legends(html):
    """"""
    return html.find_all(attrs={"class":"boxlegend"})


def process_box_legend(boxlegend_html):
    """"""
    description = str(boxlegend_html).split('boxlegend">')[1]
    return description


def get_image_urls(html):
    """"""
    return re.findall("\((.*?)\)", html.find('style').text)


def get_images_from_url(url: str):
    """"""
    response = safe_request(url)
    img = Image.open(BytesIO(response.content))
    width, height = img.size
    show_image = img.crop(box=(0, 0, width // 2, height))
    teach_image = img.crop(box=(width // 2, 0, width, height))
    return show_image, teach_image


def get_gallery_image_links(gallery_url: str):
    """"""
    gallery_html = get_html(gallery_url)
    gallery_elements = gallery_html.find(attrs={"id": "breadcrumb"}).findAll('a')[2:]
    gallery_links = [gallery_element.attrs["href"] for gallery_element in gallery_elements]
    return [gallery_url] + gallery_links


def get_gallery_info(gallery, tag_prefix):
    """"""
    tags = [tag_prefix + "::" + gallery.contents[0].replace(" ", "_").lower().replace("_-_", "::")]
    url = gallery.attrs["href"]
    links = get_gallery_image_links(url)
    return tags, links


class ProtoCardData:
    def __init__(self, desc: str, image_url: str):
        self.desc = desc.replace("<li>", "<br> &#x2022; ").replace("</li>", "")
        self.name = desc.split("</h4>")[0].replace("<h4>", "")
        self.image_url = image_url
        self.show_image, self.teach_image = get_images_from_url(image_url)
        self.tags = []
        
    def add_tags(self, tags):
        self.tags = self.tags + list(tags)
        
    def __repr__(self):
        s = self.desc.split("\n")[0]
        s += f":\n{self.image_url}\n"
        return s


def scrape_card_info(url: str, pbar_desc: str = ""):
    """"""
    
    if isinstance(url, (tuple, list)):
        pbar =  tqdm(url, unit="url", desc=f"Scraping {pbar_desc} URLs")
        return [card for url_i in pbar for card in scrape_card_info(url_i)]
        
    request_content = safe_request(url)
    url_html = bsoup(request_content.content, features="html.parser")

    box_legends = get_box_legends(url_html)
    descriptions = [process_box_legend(box_legend) for box_legend in box_legends]

    image_urls = get_image_urls(url_html)
    
    return [ProtoCardData(desc, image_url) for desc, image_url in zip(descriptions, image_urls)]


def get_deck_cards(url):
    """"""
    base_html = get_html(url)

    deck_cards = []
    deck_tag = "#radiology"
    topics = base_html.find_all(attrs={"class": "gallinfo"})
    for topic in topics:
        galleries = topic.findAll('a')
        for gallery in galleries:
            gallery_tags, gallery_links = get_gallery_info(gallery, tag_prefix=deck_tag)
            gallery_cards = scrape_card_info(gallery_links, pbar_desc=gallery_tags[0])

            for gallery_card in gallery_cards:
                gallery_card.add_tags(gallery_tags)

            deck_cards += gallery_cards

    return deck_cards

