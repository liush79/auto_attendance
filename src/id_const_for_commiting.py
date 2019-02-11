# -*- coding: utf-8 -*-

KYOBO = {
    "name": "Kyobo",
    'login_path': 'https://www.kyobobook.co.kr/login/login.laf',
    'attendance_path': 'http://www.kyobobook.co.kr/event/dailyCheckSpci.laf?orderClick=c1j',
    "IDs": [
        ['Id', 'Password'],
    ]
}

AUCTION = {
    'name': 'Auction',
    'login_path': 'https://memberssl.auction.co.kr/Authenticate/?'
                  'url=http%3a%2f%2fwww.auction.co.kr%2f%3fredirect%3d1&return_value=0',
    'attendance_path': 'http://promotion.auction.co.kr/promotion/MD/eventview.aspx?txtMD=05F804C1E8',
    'IDs': [
        ['Id1', 'Password1'],
        ['Id2', 'Password2'],
    ]
}

GMARKET = {
    'name': 'Auction',
    'login_path': 'https://signinssl.gmarket.co.kr/login/login',
    'attendance_path': 'http://promotion.gmarket.co.kr/Event/PlusZone.asp',
    'IDs': [
        ['Id', 'Password'],
    ]
}
