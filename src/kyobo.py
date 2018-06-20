# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from id_const import KYOBO_ID

import time
import traceback

LOGIN_PATH = 'https://www.kyobobook.co.kr/login/login.laf'
ATTENDANCE_PATH = 'http://www.kyobobook.co.kr/prom/2017/book/170103_dailyCheck.jsp?orderClick=c1j'
# RAND_TEXT = ['출쳌', '출석', '출첵', '출석합니다', 'ㅊㅊ']


def kyobo():
    print ('INFO: Load Firefox')
    d = webdriver.Firefox()
    d.implicitly_wait(10)
    try:
        # d = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
        #                      desired_capabilities=DesiredCapabilities.FIREFOX)
        for idpw in KYOBO_ID:
            print ('INFO: Move to login page')
            d.get(LOGIN_PATH)
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
            d.get(ATTENDANCE_PATH)
            div_stamp = d.find_element_by_class_name('daily_stamp_info')
            try:
                print ('INFO: Click attendance')
                btn_stamp = div_stamp.find_element_by_tag_name('a')
                btn_stamp.click()
                d.switch_to.alert.accept()
            except:
                print ('INFO: You already to attend this site.')
            # print ('INFO: Start reply')
            # div_reply = d.find_element_by_class_name('write_wrap event_reply')
            # reply = div_reply.find_element_by_tag_name('textarea')
            # reply.click()
            # print ('INFO: Select random text')
            # text = RAND_TEXT[int(time.time()) % len(RAND_TEXT)]
            # reply.send_keys(text)
            # btn = d.find_element_by_xpath('//button[@onclick="javascript:regComment();"]')
            # btn.click()
            # d.switch_to.alert.accept()
            # d.switch_to.alert.accept()
            print ('INFO: Logout')
            logout = d.find_element_by_xpath('//a[@href="javascript:logout();"]')
            logout.click()
            time.sleep(2)
        print ('INFO: Finish !')
    except Exception, e:
        print ('ERROR: ', str(e))
        print ('TRACEBACK: ', traceback.format_exc())
    finally:
        d.close()


if __name__ == '__main__':
    kyobo()
