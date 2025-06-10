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
        # page.get_by_test_id("SearchBlock").get_by_role("link", name="Купить").click()
        # #TODO Не всегда открывается меню, перекрывает объявление черная пятница
        # #решение увеличить ожидание
        # not_big_sleep()
        # not_big_sleep()
        #
        # page.get_by_role("button", name="Квартиру в новостройке и вторичке").click()
        #
        #
        #
        # not_big_sleep()
        #
        #
        # page.get_by_test_id("SearchBlock").get_by_text("Коммерческая").click()
        # not_big_sleep()
        #
        # page.get_by_role("textbox", name="Город, адрес, метро, район или шоссе").click()
        # not_big_sleep()
        #
        # page.get_by_role("textbox", name="Город, адрес, метро, район или шоссе").fill("санкт-петербург")
        # not_big_sleep()
        #
        # page.get_by_title("Санкт-Петербург", exact=True).first.click()
        # page.get_by_role("link", name="Найти").click()
        # page.get_by_test_id("SearchBlock").get_by_role("link", name="Купить").click()
        # not_big_sleep()
        #
        # page.get_by_role("button", name="Квартиру в новостройке и вторичке").click()
        # not_big_sleep()
        #
        # page.get_by_test_id("SearchBlock").get_by_text("Коммерческая").click()
        # not_big_sleep()

        # page.get_by_text("Торговая площадь").click()
        # page.get_by_test_id("SearchBlock").get_by_text("Склад").click()
        # page.get_by_text("Помещение свободного назначения").click()
        # page.get_by_text("Общепит").click()
        # page.get_by_text("Производство").click()
        # page.get_by_text("Автосервис").click()
        # page.get_by_text("Здание").click()
        # page.get_by_text("Бытовые услуги").click()
        # page.get_by_text("Арендный бизнес").click()
        # page.get_by_text("Готовый бизнес").click()
        # page.get_by_role("textbox", name="Город, адрес, метро, район или шоссе").fill("Санкт-Петербург")
        # page.get_by_text("Санкт-Петербург", exact=True).nth(1).click()
        # not_big_sleep()
        # count_pagin = page.get_by_role("heading", name="Найдено").inner_text()
        # print(count_pagin)

        # page.get_by_role("link", name="Найти").click()
        # with page.expect_download() as download1_info:
        #     with page.expect_popup() as page2_info:
        #         page.get_by_role("button", name="Сохранить файл в Excel").click()
        #     page2 = page2_info.value
        # download1 = download1_info.value
        # page2.close()
        # page.get_by_role("link", name="..").click()
        # page.get_by_role("link", name="..").click()

        # ---------------------
        page.pause()
        context.close()
        browser.close()

def run(self, cpu: int):
    urls = self.url_sub_category(dis_msk)
    with Pool(processes=cpu) as pool:
        pool.map(self.entrance_point_pw, urls)
        pool.close()
        pool.join()

if __name__ == '__main__':
    url = 'https://spb.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=offices&office_type[0]=1&office_type[1]=2&office_type[2]=3&office_type[3]=4&office_type[4]=5&office_type[5]=7&office_type[6]=9&office_type[7]=10&office_type[8]=11&office_type[9]=12&p=54&ready_business_types[0]=1&ready_business_types[1]=2&region=2'
    run_cian(url)