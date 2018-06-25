# -*- coding: utf-8 -*-
from selenium import webdriver
from id_const import KYOBO

import time
import traceback


def kyobo():
    print ('INFO: Load Firefox')
    d = webdriver.Firefox()
    d.implicitly_wait(10)
    try:
        for idpw in KYOBO['IDs']:
            print ('INFO: Move to login page')
            d.get(KYOBO['login_path'])
            print ('INFO: Try to login: \'%s\'' % idpw[0])
            id = d.find_element_by_id("memid")
            id.click()
            id.send_keys(idpw[0])
            pw = d.find_element_by_id("pw")
            pw.click()
            pw.send_keys(idpw[1])
            btn = d.find_element_by_class_name('btn_submit')
            btn.click()
            print ('INFO: Wait to login')
            time.sleep(2)
            print ('INFO: Move attendance page')
            d.get(KYOBO['attendance_path'])
            div_stamp = d.find_element_by_class_name('daily_stamp_info')
            try:
                print ('INFO: Click attendance')
                btn_stamp = div_stamp.find_element_by_tag_name('a')
                btn_stamp.click()
                d.switch_to.alert.accept()
            except:
                print ('INFO: You already to attend this site.')
            print ('INFO: Logout')
            logout = d.find_element_by_xpath('//li[@class="button"]/a[@href="javascript:logout();"]')
            logout.click()
            time.sleep(1)
        print ('INFO: Finish !')
    except Exception, e:
        print ('ERROR: ', str(e))
        print ('TRACEBACK: ', traceback.format_exc())
    finally:
        d.close()


if __name__ == '__main__':
    kyobo()
