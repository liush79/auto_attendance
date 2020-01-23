# -*- coding: utf-8 -*-

from clog import Clog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from id_const import AUCTION as TARGET

import random
import time
import traceback

clog = Clog()


def auction():
    clog.info('Load Firefox')
    d = webdriver.Firefox()
    d.implicitly_wait(10)
    try:
        for idpw in TARGET['IDs']:
            clog.info('Move to login page')
            d.get(TARGET['login_path'])
            clog.info('Try to login: \'%s\'' % idpw[0])
            id = d.find_element_by_id("id")
            id.click()
            # id.send_keys(idpw[0].decode('utf8'))  # python 2.x, python3 default str is unicode
            id.send_keys(idpw[0])
            pw = d.find_element_by_id("password")
            pw.click()
            pw.send_keys(idpw[1])
            btn = d.find_element_by_id('Image1')
            btn.click()
            clog.info('Wait to login')
            time.sleep(2)
            clog.info('Move attendance page')
            d.get(TARGET['attendance_path'])

            # find iframe
            # --------------------------------------------------------------------
            # by class name don't find double underscore class name... why ?
            # div_slide = div_container.find_element_by_class_name('content_slot content_slot__point_save')
            # --------------------------------------------------------------------
            # =============================== 2020-01-02 출석이 바뀜..===============================
            # div_slide = d.find_element_by_xpath('//div[@class="content_slot content_slot__point_save"]')
            # iframe = div_slide.find_element_by_tag_name('iframe')
            # d.switch_to.frame(iframe)
            #
            # next_btn = d.find_element_by_class_name('swiper-button-next')
            # try:
            #     cnt = 0
            #     for _ in range(0, 20):
            #         # Probably, the site prohibits to click if the item invisible.
            #         # We should click only visible items.
            #         sp_list = d.find_elements_by_class_name('swiper-slide-visible')
            #         for sp in sp_list:
            #             btn_point = sp.find_element_by_class_name('btn_point')
            #             if 'after' not in btn_point.get_attribute('class'):
            #                 cnt = 0
            #                 sp.click()
            #                 clog.info('Get the points.')
            #                 break
            #         cnt += 1
            #         if cnt >= 4:
            #             clog.info('Stopped to gathering.')
            #             break
            #         next_btn.click()
            #         time.sleep(random.randrange(5, 30) / 10.0)
            # except Exception as e:
            #     clog.info('Probably we got the all points !')
            #     pass
            # ===============================
            content_slot = d.find_element_by_id('contentSlot01')
            iframe = content_slot.find_element_by_tag_name('iframe')
            d.switch_to.frame(iframe)
            try:
                goods = d.find_element_by_class_name('goods_price')
                price = goods.find_element_by_tag_name('dd')
                clog.info(price.text)
                last_price = int(price.text[:-1].replace(',', '')) - 37000
                if last_price <= 0:
                    last_price = 0
                clog.info('최종 가격: ' + str(last_price))
                txt_answer = d.find_element_by_id('txtAnswer')
                time.sleep(random.randrange(2, 15))
                txt_answer.send_keys(str(last_price))
                time.sleep(0.5)
                submit_button = d.find_element_by_xpath('//button[@onclick="doApply(); return false;"]')
                submit_button.click()
            except Exception as e:
                clog.info('Probably you already get the points !')
                pass
            time.sleep(1)
            # switch original frame
            d.switch_to.default_content()

            clog.info('Go to home page.')
            d.get('http://www.auction.co.kr/')
            clog.info('Try Logout')
            usermenu = d.find_element_by_class_name('usermenu')
            lis = usermenu.find_elements_by_tag_name('li')
            lis[0].click()
            time.sleep(1)
        clog.info('INFO: Finish !')
    except Exception as e:
        clog.error('Exception: %s' % str(e))
        clog.error('TRACEBACK: %s' % traceback.format_exc())
    finally:
        d.close()


if __name__ == '__main__':
    auction()
