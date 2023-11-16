import requests
from lxml import etree
from urllib.parse import urljoin
import re
import pandas as pd


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


def get_food_label(page_number):
    page_url = f'https://www.ewg.org/foodscores/products/?category_group=&page={page_number}&per_page=48&type=products'
    resp = get_response(page_url)
    a_labels = etree.HTML(resp.text).xpath('//div[@class="ind_result_text fleft"]/a')
    return a_labels

def get_food_info(a):
    try:
        nutrition_fact = {}
        detail_url = urljoin('https://www.ewg.org/foodscores/products/', a.get('href'))
        resp_text = get_response(detail_url) .text
        resp = etree.HTML(resp_text)
        name = resp.xpath('//h1[@class="truncate_title_specific_product_page"]')[0].text
        clr = resp.xpath('//div[@id="nut_calories_value"]')[0].text
        nutrition_fact['name'] = name
        nutrition_fact['link'] = detail_url
        size_opt = resp.xpath('//option[@selected]')
        nutrition_fact['size'] = size_opt[0].text if size_opt else None
        nutrition_fact['Calories'] = clr
        pattern = r'score_(\d+)_(\d+)'
        matches = re.findall(pattern, resp_text)
        score = '.'.join(matches[0]) if matches else None
        for i in resp.xpath('//span[@class="normal_title" or @class="med_title"]'):
            name_n_value = i.xpath('string(./..)').strip()
            element_name = i.xpath('string(.)').strip()
            element_kv = name_n_value.split(element_name)
            element_value_detail = element_kv[-1].strip() if len(element_kv) > 1 else ''
            nutrition_fact[element_name] = element_value_detail
        return nutrition_fact
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    all_data_list = []
    ct = 20000000
    start_url = 'https://www.ewg.org/foodscores/products/?category_group=&page=1&per_page=48&type=products'
    pages = int(etree.HTML(requests.get(start_url).text).xpath('//a[@aria-label]')[-1].text)
    for page_number in range(1, pages+1):
        food_labels = get_food_label(page_number)
        for a in food_labels:
            nutrition_fact = get_food_info(a)
            if nutrition_fact:
                nutrition_fact['uid'] = ct
                ct += 1
                all_data_list.append(nutrition_fact)
            else:
                continue

    all_data_df = pd.DataFrame(all_data_list)
    all_data_df.to_csv('ewg_data.csv', index=False)
