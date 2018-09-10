# -*- coding: utf-8 -*-
from clog import Clog
from selenium import webdriver
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
            div_slide = d.find_element_by_class_name('slideWrap')
            iframe = div_slide.find_element_by_tag_name('iframe')
            d.switch_to.frame(iframe)

            next_btn = d.find_element_by_class_name('swiper-button-next')
            try:
                for _ in range(0, 20):
                    # Probably, the site prohibits to click if the item invisible.
                    # We should click only visible items.
                    sp_list = d.find_elements_by_class_name('swiper-slide-visible')
                    for sp in sp_list:
                        btn_point = sp.find_element_by_class_name('btn_point')
                        if 'after' not in btn_point.get_attribute('class'):
                            sp.click()
                            clog.info('Get the points.')
                            break
                    next_btn.click()
                    time.sleep(random.randrange(5, 30) / 10.0)
            except Exception, e:
                clog.info('Probably we got the all points !')
                pass
            time.sleep(1)
            # switch original frame
            d.switch_to.default_content()

            clog.info('Try Logout')
            usermenu = d.find_element_by_class_name('usermenu')
            lis = usermenu.find_elements_by_tag_name('li')
            lis[0].click()
            time.sleep(1)
        clog.info('INFO: Finish !')
    except Exception, e:
        clog.error('Exception: %s' % str(e))
        clog.error('TRACEBACK: %s' % traceback.format_exc())
    finally:
        d.close()


if __name__ == '__main__':
    auction()
