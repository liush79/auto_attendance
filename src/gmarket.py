# -*- coding: utf-8 -*-

from selenium import webdriver
from id_const import GMARKET

import time
import traceback


def gmarket():
    print ('INFO: Load Firefox')
    d = webdriver.Firefox()
    try:
        for idpw in GMARKET['IDs']:
            print ('INFO: Move to login page')
            try:
                d.set_page_load_timeout(10)
                d.get(GMARKET['login_path'])
            except:
                d.set_page_load_timeout(30)
            print ('INFO: Try to login: \'%s\'' % idpw[0])
            id = d.find_element_by_id("id")
            id.click()
            id.send_keys(idpw[0])
            pw = d.find_element_by_id("pwd")
            pw.click()
            pw.send_keys(idpw[1])
            div_btn = d.find_element_by_class_name('btn-login')
            btn = div_btn.find_element_by_tag_name('span')
            btn.click()
            print ('INFO: Wait to login')
            time.sleep(2)
            print ('INFO: Move attendance page')
            d.get(GMARKET['attendance_path'])

            # Change to iFrame
            d.switch_to_frame('AttendRulletFrame')
            button_start = d.find_element_by_class_name('button_start')
            button_start.click()
            time.sleep(3)
            try:
                # Change to parent frame.
                d.switch_to_default_content()
            except Exception as e:
                print ('INFO: You already to attend this site.')
            print ('INFO: Logout')

            d.get('http://www.gmarket.co.kr/')
            time.sleep(1)
            logout = d.find_element_by_xpath('//a[@href="https://signinssl.gmarket.co.kr/logout/logoutproc"]')
            try:
                d.set_page_load_timeout(5)
                logout.click()
            except:
                pass
            time.sleep(1)
        print ('INFO: Finish !')
    except Exception as e:
        print ('ERROR: ', str(e))
        print ('TRACEBACK: ', traceback.format_exc())
    finally:
        d.close()
        d.quit()


if __name__ == '__main__':
    gmarket()
