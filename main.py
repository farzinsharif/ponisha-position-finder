"""
better not to run in local machine due to cpu usage problem
for further use change config.py
"""
import requests as req
from bs4 import BeautifulSoup as bs
from config import *
import re
from datetime import datetime
import time
import pytz
import json


def chat_id_capture():
    """
    save new CHAT_ID if and send them to bot admin every 30 minute
    :return:None
    """

    # time.sleep(86400)
    chat_id = f"https://api.telegram.org/bot{API_KEY}/getUpdates"
    respnose = req.get(chat_id).text
    json_data = json.loads(respnose)
    listen = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHAT_ID}&text={respnose}"
    req.get(listen)
    # time.sleep(1800)


def time_now():
    """
    to run the bot in period you want
    :return: Current time for tehran
    """
    global current_time
    current_time = datetime.now(pytz.timezone('Asia/Tehran')).hour
    return current_time


def capture():
    """
    gather all the link and html file
    :return: html_list
    """

    for skill in desired_skill:
        URL = f'https://ponisha.ir/search/projects/skill-{skill}/status-open/page/1'

        response = req.get(URL)
        html_list.append(response.text)
    return html_list


def finder():
    """
    find all the job offer Title, Description, Link and Price
    :return: zip tuple of above list
    """

    global send
    price_list_tag = list()
    price_list = list()
    counter = 0

    for each_html in html_list:
        # Title finder
        motor = bs(each_html, "html.parser")
        each_job_tag = motor.find_all("h4")
        each_job_tag.pop()
        each_job_tag.pop()
        job_list_tag.append(each_job_tag)
        # Desc finder
        job_desc = motor.find_all("div", class_="desc hidden-xs height-50px")
        job_desc_tag_list.append(job_desc)
        job_desc.pop()
        job_desc.pop()
        # Price finder
        price_tag = motor.find_all("div", class_="budget")
        price_tag.pop()
        price_tag.pop()
        price_list_tag += price_tag

        # Link finder & ready to sail
        for a in motor.find_all("a", class_="absolute right0 left0 width-90 min-h-100 zx-900", href=True):
            link_list.append(a['href'])

    # Price ready to sail
    for each_tag in price_list_tag:
        price = re.findall(r'\d{6,}', str(each_tag))
        price_list += price
    # Title ready to sail
    for each_list in job_list_tag:
        for i in each_list:
            job_tag = i.string
            job_list.append(job_tag)
    # Desc ready to sail
    for each_list in job_desc_tag_list:
        for i in each_list:
            job_tag_desc = i.string
            job_tag_desc = job_tag_desc.strip()
            job_desc_list.append(job_tag_desc)
    # tuple ready to sail
    send = zip(price_list, job_list, job_desc_list, link_list)
    # in case you want the data on your local machine
    for each in send:
        counter += 1
        print(f'index :{counter}', each)
    print(f"Total open position count are : {counter}")
    return send


def sail():
    """
    Send data from bot to user according to CHAT_ID
    :return: None
    """
    counter = 0

    for message in send:
        url = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHAT_ID}&text={message}"
        req.get(url)
        counter += 1
    description_for_user = f"Total open position count is  : {counter} \n order of the message is as follows" \
                           f" 'budget amount' , 'position title' , 'position description' , 'position link' "
    sailor = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHAT_ID}&text={description_for_user}"
    req.get(sailor)
    # url = f"https://api.telegram.org/bot{API_KEY}/getUpdates"
    # print(req.get(url).json())


if __name__ == '__main__':
    while True:
        time_now()
        print(current_time)
        if current_time == 11:
            capture()
            finder()
            # sail()
        time.sleep(3600)

