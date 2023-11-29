import requests
from lxml import etree
from urllib.parse import urljoin, urlparse, urlsplit
import re
import json
import time
from math import ceil


def author():
    """
    Returns:
       author name in list
    """
    return ['Mingjun Shen']


def get_response(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'}
    resp = requests.get(url, headers=headers, timeout=15)
    return resp


def get_pages(url):
    resp = get_response(url)
    page = etree.HTML(resp.text).xpath('//span[@automation-id="totalProductsOutputText"]')[0].text
    page_total = ceil(int(page.split('of')[-1].strip()) / 24)
    return page_total


def get_detail_labels(page_url):
    resp = get_response(page_url)
    detail_labels = etree.HTML(resp.text).xpath(
        '//div[@automation-id="productList"]//a[contains(@automation-id,"productDescriptionLink")]')
    return detail_labels


def parse_detail_page(label):
    time.sleep(1)
    pd_name = label.text.strip()
    detail_url = label.get('href')
    detail_page = etree.HTML(get_response(detail_url).text)
    img_src = detail_page.xpath('//meta[@property="og:image"]')[0].get('content')
    pattern = r"profileId=(\d+)&imageId=(\d+-?\d*)"
    match = re.search(pattern, img_src)
    if match:
        profile_id = match.group(1)
        image_id = match.group(2)
        return pd_name, detail_url, profile_id, image_id
    else:
        return None, None, None, None


def download_images(profile_id, image_id):
    img_base = f'https://richmedia.ca-richimage.com/ViewerDelivery/productXmlService?profileid={profile_id}&itemid={image_id}&viewerid=1068&callback='
    img_page = get_response(img_base).text.strip('()')
    try:
        img_json = json.loads(img_page)
        imgs = img_json['product']['views']
        for img in imgs:
            if 'nf' in img.get('@name'):
                nf_url = img['swatches'][0]['images'][0]['@path']
                img_file = get_response(nf_url).content
                with open(f'{uid}.jpg', 'wb') as f:
                    f.write(img_file)
                return True
            else:
                continue
        return False
    except:
        return False


if __name__ == "__main__":
    costco = 'https://www.costco.com/grocery-household.html'
    start_list = [
        '/snacks.html',
        "/coffee-sweeteners.html",
        "/candy.html",
        "/pantry.html",
        "/breakfast.html",
        "/beverages.html",
        "/emergency-kits-supplies.html",
        "/organic-groceries.html",
        "/cheese.html",
        "/deli.html",
        "/cakes-cookies.html",
    ]

    uid = 1000000

    with open('costco_food_img.csv', 'w') as f:
        f.write('uid\tname\tlink\n')

    for start_url in start_list:
        page_total = get_pages(urljoin(costco, start_url))
        for i in range(0, page_total):
            page_url = f'https://www.costco.com{start_url}?currentPage={i + 1}&pageSize=24'
            detail_labels = get_detail_labels(page_url)
            for label in detail_labels:
                pd_name, detail_url, profile_id, image_id = parse_detail_page(label)
                uid += 1
                if profile_id and image_id:
                    down_img = download_images(profile_id, image_id)
                    if down_img:
                        with open('costco_food_img.csv', 'a') as f:
                            f.write(f'{uid}\t{pd_name}\t{detail_url}\n')
                else:
                    continue
