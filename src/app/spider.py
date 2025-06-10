import datetime
import json
import logging
import os
import random
from multiprocessing import Pool
from random import choice

from playwright._impl import _errors
from playwright.sync_api import sync_playwright

from src.core.db_conf import db_mongo_insert_one
from src.core.proxy import IparchitectProxy
from src.core.settings import DOWNLOAD_DIR
from src.core.utelites import not_big_sleep

def run_cian(url):
    with sync_playwright() as p:
        proxy = IparchitectProxy()

        proxys = random.choice(proxy.get_proxy_in_list())

        browser = p.chromium.launch(
            headless=False,
            args = [
                "--disable-blink-features=AutomationControlled",
                "--disable-extensions",
                "--disable-infobars",
                "--enable-automation",
                "--no-first-run",
                "--enable-webgl",
        ])
        context = browser.new_context(
            ignore_https_errors=False,
            locale='ru-RU',
            color_scheme='dark',
            permissions=["geolocation"],
            timezone_id='Europe/Moscow',
            viewport= { 'width': 1280, 'height': 720 },
            proxy=proxys,
        )
        page = context.new_page()
        page.route("**/*.{png,jpg,jpeg,webp}", lambda route: route.abort())

        page.goto(url=url, wait_until='domcontentloaded')
        # page.goto("https://www.browserscan.net/ru", wait_until='domcontentloaded')
        # page.goto("https://bot.sannysoft.com", wait_until='domcontentloaded')
        # resp = p.request.new_context(
        #     proxy=proxys
        # )
        page.pause()

        browser.close()

def run(self, cpu: int):
    urls = self.url_sub_category(dis_msk)
    with Pool(processes=cpu) as pool:
        pool.map(self.entrance_point_pw, urls)
        pool.close()
        pool.join()

if __name__ == '__main__':
    run_cian('https://www.cian.ru/')