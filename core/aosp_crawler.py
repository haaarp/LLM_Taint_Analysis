import json
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import multiprocessing as mp 
import time
import os

class PublicAPI:


    def __init__(self, name, arguments, retType, doc, class_name,package,class_description):
        self.package = package
        self.class_name = class_name
        self.class_description = class_description
        self.name = name
        self.arguments = arguments
        self.retTpye = retType
        self.doc = doc

def collect_results(res):
    global errors
    global output
    if 'error' in res.keys():
        errors.append(res['error'])
    elif 'success' in res.keys() and len(res['success']) > 0:
        output.extend(res['success'])
    return 

def parse_url(url):
    try:
        package = url.replace('https://developer.android.com/reference/','')
        class_name = url.split('/')[-1]
        tmp = []
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features="lxml")
        class_description = get_class_description(soup,url)

        for table in soup.find_all('table', attrs={"class":"responsive methods","id":"pubmethods"}):
            df = pd.read_html(str(table))[0]
            for idx, r in df.iterrows():
                retType = r['Public methods']
                s = re.split(r'\(|\) ', str(r['Public methods.1']), maxsplit=2)
                if len(s) < 3:
                    continue
                name = s[0]
                arguments = s[1].split(', ')
                doc = s[2]
                api = PublicAPI(name, arguments, retType, doc,class_name,package,class_description)
                tmp.append(api.__dict__)
    except Exception as e:
        return {'error':e}
    return {'success':tmp}

def parse_codes(url):
    try:
        tmp = []
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features="lxml")
        for table in soup.find_all('table', attrs={"class":"responsive methods","id":"pubmethods"}):
            codes = table.find_all('code')
            for code in codes:
                for link in code.find_all('a'):
                    tmp.append(link.text)
    except Exception as e:
        return {'error':e}
    return {'success':tmp}

def get_class_description(soup,url):
    try:
        ps = soup.find_all('p')
        if 'kotlin' in url:
            desc = ps[0].get_text().replace('\n','') if len(ps) > 2 and ps[0].text[0] != '\n'  else ''
        else:
            desc = ps[1].get_text().replace('\n','') if len(ps) > 2 and ps[1].text[0] != '\n' else ''
    except Exception:
        return ''
    return desc.strip()
    
def parse_class_description(url):
    try:
        name = url.split('/')[-1]
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features="lxml")
        ps = soup.find_all('p')
        if 'kotlin' in url:
            desc = ps[0].get_text().replace('\n','') if len(ps) > 2 and ps[0].text[0] != '\n'  else ''
        else:
            desc = ps[1].get_text().replace('\n','') if len(ps) > 2 and ps[1].text[0] != '\n' else ''
        tmp = f'{name},{desc}'
    except Exception as e:
        return {'error':f'{url}:{e}'}
    return {'success':tmp}


def star_crawling(urls,output_file):
    print('start script')
    pool = mp.Pool(mp.cpu_count() - 2) 
    for url in urls:
        pool.apply_async(parse_url,args=([url]),callback=collect_results)

    pool.close()
    pool.join()

    json_string = json.dumps(output, indent=4)
    with open(output_file, 'w') as outfile:
        outfile.write(json_string)

    if len(errors) > 0:
        print('Logging errors')
        for item in errors:
            print(item)



if __name__ == "__main__":
    start = time.time()
    errors = []
    output = []

    input_example = [
    "https://developer.android.com/reference/android/location/Address",
    "https://developer.android.com/reference/android/location/Criteria",
    "https://developer.android.com/reference/android/location/Geocoder",
    "https://developer.android.com/reference/android/location/GnssAntennaInfo",
    "https://developer.android.com/reference/android/location/GnssAntennaInfo.Builder",
    "https://developer.android.com/reference/android/location/GnssAntennaInfo.Listener",
    "https://developer.android.com/reference/android/location/GnssAntennaInfo.PhaseCenterOffset",
    "https://developer.android.com/reference/android/location/GnssAntennaInfo.SphericalCorrections"
    ]

    # read the list of urls from input file
    # with open(input) as f:
    #     urls = f.read().splitlines()
    #     urls = [x for x in urls if x.split('/')[-1][0].isupper()]

    absolute_dirpath = os.path.abspath(os.path.dirname(__file__))

    star_crawling(input_example, absolute_dirpath + '/../outputs/output_aosp.json')
    end = time.time()
    sec = end - start
    print(f'script finished. Processing took {sec} seconds')
