"""
https://github.com/amitupreti/Email-Crawler-Lead-Generator
This is a 2nd version of the Emai crawler project. Here we choose scrapy because it provides multithreading, handles duplicates and other features.
-------------
“Rather than trying to reinvent the wheel, build on to that which is already excellent.”
― Auliq Ice
"""

import gc
import os
from datetime import datetime

import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class EmailCrawler(scrapy.Spider):

    def __init__(self, *args, **kwargs):

        self.name = "EmailCrawlerv2"
        self.allowed_domains = ["google.com"]
        self.start_urls = []
        # add start urls from the input.

        # basic settings
        self.output_format = kwargs.get('output_format', 'csv').lower()
        self.filename = kwargs.get(
            'output_filename', 'Email_data_dump') + '.' + self.output_format
        self.output_name = f"{datetime.now().strftime('%Y_%m_%d__%H_%M')}_{self.filename}"

        self.concurrent_requests = kwargs.get('concurrent_requests', 2)
        self.download_delay = kwargs.get('download_delay', 0)
        self.retry_times = kwargs.get('retry_times', 2)
        self.custom_settings = {
            'DOWNLOAD_DELAY': self.download_delay,
            'CONCURRENT_REQUESTS': self.concurrent_requests,
            # 'JOBDIR': './crawls',   # uncomment this to save memory. Data will be saved on the disk.
            'RETRY_TIMES': self.retry_times,
            'FEED_FORMAT': 'csv',
            'FEED_URI':  self.output_name,
        }

        self.base_headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        super(EmailCrawler, self).__init__(*args, **kwargs)

    # the crawler will execute start_requests function at first.
    def parse(self, response):
        gc.collect()

        print(f'processing  listing: {response.url}')
        if response.status == 429:
            url = response.meta['url']
            print(f'Bot detected on listing page: {url}.Retrying')
            # import ipdb
            # ipdb.set_trace()

            yield scrapy.Request(url, self.load_listings, dont_filter=True, meta={'url': url,
                                                                                  'keyword': response.meta['keyword'],

                                                                                  })

        else:
            ei = response.xpath('//*[@name="ei"]/@value').get()
            tbm = response.xpath('//*[@name="tbm"]/@value').get()
            query = response.xpath(
                '//*[@title="Search"]/@value').get(default='').replace(' ', '+')
            data_divs = response.xpath('//*[@id="rso"]//a')
            counter = 0
            for data_div in data_divs:
                # data_rtid = data_div.xpath('./@data-rtid').get(default='')
                datacid = data_div.xpath(
                    './@data-cid').get(default='')  # use with @asyjc

                if datacid:
                    counter += 1
                    detail_url = f'https://www.google.com/async/lcl_akp?ei={ei}&hl=en&yv=3&lei={ei}&tbm={tbm}&q={query}&async=ludocids:{datacid},f:rlni,lqe:false,_id:akp_tsuid2,_pms:s,_fmt:pc'
                    print(f'Detail_url: {detail_url}')
                    yield scrapy.Request(detail_url, self.load_detail,
                                         meta={'url': detail_url, 'keyword': response.meta['keyword'],
                                               })

                    print(f'{counter} places found.')

                    next_page = response.xpath(
                        '//*[@id="pnnext"]/@href').get(default='')
                    if next_page:
                        next_page = response.urljoin(next_page)
                    print(f'Next: {next_page}')
                    yield scrapy.Request(
                        next_page,
                        self.load_listings,
                        meta={
                            'url': next_page,
                            'keyword': response.meta['keyword'],

                        }
                    )

    def load_detail(self, response):
        gc.collect()
        print(f'processing detail: {response.url}')
        if response.status == 429:
            url = response.meta['url']
            print(f'Bot detected on Detail page: {url}.Retrying')
            # import ipdb
            # ipdb.set_trace()

            yield scrapy.Request(url, self.load_detail, dont_filter=True,
                                 meta={'url': url, 'keyword': response.meta['keyword'],
                                       })

        else:

            name = response.xpath(
                '//*[@data-attrid="title"]/span/text()').get(default='')
            website = response.xpath(
                '//a[contains(.,"Website")]/@href').get(default='')
            no_of_reviews = response.xpath('//a[contains(.,"Google reviews")]//text()').get(default='').replace(
                'Google reviews', '').strip().replace(',', '')
            rating = response.xpath('//div[@class="kp-header"]//g-review-stars/preceding-sibling::span/text()').get(
                default='')
            address = ''.join(
                response.xpath('//div[@data-attrid="kc:/location/location:address"]//text()').getall()).replace(
                'Address:',
                '').strip()
            phone = ''.join(response.xpath(
                '//div[@data-attrid="kc:/collection/knowledge_panels/has_phone:phone"]//text()').getall()).replace(
                'Phone:',
                '').strip()

            # for price_level and type of restaurant
            '''//*[@class="kp-header"]//*[@class="YhemCb"]'''
            data = response.xpath(
                '//*[@class="kp-header"]//*[@class="YhemCb"]/text()').getall()
            place_type = ''
            price_level = ''
            for d in data:
                if '$' in d:
                    price_level = len(d)
                else:
                    place_type = d

            try:
                state = address.split(',')[-1].strip().split()[0]
            except:
                state = ''

            yield {
                'state': state,
                'address': address,
                'business_name': name,
                'no_of_reviews': no_of_reviews,
                'phone': phone,
                'place_type': place_type,
                'price_level': price_level,
                'rating': rating,
                'website': website,
                'search_keyword': response.meta['keyword'],




            }


# settings = get_project_settings()
# process = CrawlerProcess(settings)
# process.crawl(EmailCrawler)
# process.start()  # the script will block here until the crawling is finished
