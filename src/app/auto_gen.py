# https://spb.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=offices&office_type[0]=1&office_type[1]=2&office_type[2]=3&office_type[3]=4&office_type[4]=5&office_type[5]=7&office_type[6]=9&office_type[7]=10&office_type[8]=11&office_type[9]=12&p=17&ready_business_types[0]=1&ready_business_types[1]=2&region=2


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cian.ru/")
    page.get_by_test_id("SearchBlock").get_by_role("link", name="Купить").click()
    page.get_by_role("button", name="Квартиру в новостройке и вторичке").click()
    page.get_by_test_id("SearchBlock").get_by_text("Коммерческая").click()
    page.get_by_role("textbox", name="Город, адрес, метро, район или шоссе").click()
    page.get_by_role("textbox", name="Город, адрес, метро, район или шоссе").fill("санкт-петербург")
    page.get_by_title("Санкт-Петербург", exact=True).first.click()
    page.get_by_role("link", name="Найти").click()
    page.get_by_test_id("SearchBlock").get_by_role("link", name="Купить").click()
    page.get_by_role("button", name="Квартиру в новостройке и вторичке").click()
    page.get_by_test_id("SearchBlock").get_by_text("Коммерческая").click()
    page.get_by_text("Торговая площадь").click()
    page.get_by_test_id("SearchBlock").get_by_text("Склад").click()
    page.get_by_text("Помещение свободного назначения").click()
    page.get_by_text("Общепит").click()
    page.get_by_text("Производство").click()
    page.get_by_text("Автосервис").click()
    page.get_by_text("Здание").click()
    page.get_by_text("Бытовые услуги").click()
    page.get_by_text("Арендный бизнес").click()
    page.get_by_text("Готовый бизнес").click()
    page.get_by_role("textbox", name="Город, адрес, метро, район или шоссе").click()
    page.get_by_role("textbox", name="Город, адрес, метро, район или шоссе").fill("Санкт-")
    page.get_by_text("Санкт-Петербург", exact=True).nth(1).click()
    page.get_by_role("link", name="Найти").click()
    with page.expect_download() as download1_info:
        with page.expect_popup() as page2_info:
            page.get_by_role("button", name="Сохранить файл в Excel").click()
        page2 = page2_info.value
    download1 = download1_info.value
    page2.close()
    page.get_by_role("link", name="..").click()
    page.get_by_role("link", name="..").click()

    # ---------------------
    context.close()
    browser.close()

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cian.ru/")
    page.get_by_test_id("SearchBlock").get_by_role("link", name="Купить").click()
    page.get_by_role("button", name="Квартиру в новостройке и вторичке").click()
    page.get_by_test_id("SearchBlock").get_by_text("Коммерческая").click()
    page.get_by_role("textbox", name="Город, адрес, метро, район или шоссе").click()
    page.get_by_role("textbox", name="Город, адрес, метро, район или шоссе").fill("санкт-петербург")
    page.get_by_title("Санкт-Петербург", exact=True).first.click()
    page.get_by_role("link", name="Найти").click()
    page1.close()
    page.get_by_test_id("SearchBlock").get_by_role("link", name="Купить").click()
    page.get_by_role("button", name="Квартиру в новостройке и вторичке").click()
    page.get_by_test_id("SearchBlock").get_by_text("Коммерческая").click()
    page.get_by_text("Торговая площадь").click()
    page.get_by_test_id("SearchBlock").get_by_text("Склад").click()
    page.get_by_text("Помещение свободного назначения").click()
    page.get_by_text("Общепит").click()
    page.get_by_text("Производство").click()
    page.get_by_text("Автосервис").click()
    page.get_by_text("Здание").click()
    page.get_by_text("Бытовые услуги").click()
    page.get_by_text("Арендный бизнес").click()
    page.get_by_text("Готовый бизнес").click()
    page.get_by_role("textbox", name="Город, адрес, метро, район или шоссе").click()
    page.get_by_role("textbox", name="Город, адрес, метро, район или шоссе").fill("Санкт-")
    page.get_by_text("Санкт-Петербург", exact=True).nth(1).click()
    page.get_by_role("link", name="Найти").click()
    with page.expect_download() as download1_info:
        with page.expect_popup() as page2_info:
            page.get_by_role("button", name="Сохранить файл в Excel").click()
        page2 = page2_info.value
    download1 = download1_info.value
    page2.close()
    page.get_by_role("link", name="..").click()
    page.get_by_role("link", name="..").click()
    page.get_by_text("1..101112131415161718192021222324..").click(button="right")
    page3 = context.new_page()
    page3.goto("https://api.cian.ru/commercial-search-offers/desktop/v1/offers/get-offers/")
    page3.close()
    page4 = context.new_page()
    page4.goto("https://api.cian.ru/ebc-analytics/event-enrichment/")
    page4.close()
    page.get_by_role("heading", name="Найдено 1 026 объявлений").click()
    page.get_by_role("link", name="36", exact=True).click()
    page.get_by_role("link", name="29", exact=True).click()
    expect(page.get_by_role("link", name="..", exact=True).nth(1)).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



#deal_type=sale&engine_version=2&offer_type=offices&office_type[0]=1&office_type[1]=2&office_type[2]=3&office_type[3]=4&office_type[4]=5&office_type[5]=7&office_type[6]=9&office_type[7]=10&office_type[8]=11&office_type[9]=12&p=9&ready_business_types[0]=1&ready_business_types[1]=2&region=2
#deal_type=sale&engine_version=2&offer_type=offices&office_type[0]=1&office_type[1]=2&office_type[2]=3&office_type[3]=4&office_type[4]=5&office_type[5]=7&office_type[6]=9&office_type[7]=10&office_type[8]=11&office_type[9]=12&p=25&ready_business_types[0]=1&ready_business_types[1]=2&region=2