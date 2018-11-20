from bs4 import BeautifulSoup
import json
import requests


def first_call():
    cookies = {
        'cdnDown': '0',
        'PLAY_LANG': 'en-US',
        'PLAY_SESSION': '9d958df0bc59f42e37799f8f40c2f39e47043558-cadence_pSessionId=5d1mnv18bka3et70di8lk7ugq7&instance=wd1prvps0002a',
        'WorkdayLB_VPS': '3408308746.53810.0000',
        'wday_vps_cookie': '3408308746.53810.0000',
        'timezoneOffset': '240',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json,application/xml',
        'Referer': 'https://cadence.wd1.myworkdayjobs.com/en-US/External_Careers',
        'Connection': 'keep-alive',
        'X-Workday-Client': '2018.41.1184',
    }

    params = (
        ('clientRequestID', '38b5b27cdc31487c9fc15905e6942ea4'),
    )

    response = requests.get('https://cadence.wd1.myworkdayjobs.com/en-US/External_Careers', headers=headers,
                            params=params, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.text
    data = json.loads(soup)

    i = 0
    end_links = []
    for a in data["body"]["children"][0]["children"][0]["listItems"]:
        end = data["body"]["children"][0]["children"][0]["listItems"][i]["title"]["commandLink"]
        end_links.append(end)
        i += 1
    return end_links


def second_call():
    cookies = {
        'WorkdayLB_VPS': '3408308746.53810.0000',
        'cdnDown': '0',
        'PLAY_LANG': 'en-US',
        'PLAY_SESSION': '9d958df0bc59f42e37799f8f40c2f39e47043558-cadence_pSessionId=5d1mnv18bka3et70di8lk7ugq7&instance=wd1prvps0002a',
        'wday_vps_cookie': '3408308746.53810.0000',
        'timezoneOffset': '240',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json,application/xml',
        'Referer': 'https://cadence.wd1.myworkdayjobs.com/en-US/External_Careers',
        'Connection': 'keep-alive',
        'stats-perf': '38b5b27cdc31487c9fc15905e6942ea4,1263,,0',
        'X-Workday-Client': '2018.41.1184',
    }

    params = (
        ('clientRequestID', '593eed83ebd041f48d8f2c2662d23dcf'),
    )

    response = requests.get(
        'https://cadence.wd1.myworkdayjobs.com/External_Careers/fs/searchPagination/318c8bb6f553100021d223d9780d30be/50',
        headers=headers, params=params, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.text
    data = json.loads(soup)
    i = 0
    end_links = []
    for a in data["body"]["children"][0]["children"][0]["listItems"]:
        end = data["body"]["children"][0]["children"][0]["listItems"][i]["title"]["commandLink"]
        end_links.append(end)
        i += 1

    return end_links


def third_call():
    cookies = {
        'WorkdayLB_VPS': '3408308746.53810.0000',
        'cdnDown': '0',
        'PLAY_LANG': 'en-US',
        'PLAY_SESSION': '9d958df0bc59f42e37799f8f40c2f39e47043558-cadence_pSessionId=5d1mnv18bka3et70di8lk7ugq7&instance=wd1prvps0002a',
        'wday_vps_cookie': '3408308746.53810.0000',
        'timezoneOffset': '240',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json,application/xml',
        'Referer': 'https://cadence.wd1.myworkdayjobs.com/en-US/External_Careers',
        'Connection': 'keep-alive',
        'stats-perf': '593eed83ebd041f48d8f2c2662d23dcf,1131,0,',
        'X-Workday-Client': '2018.41.1184',
    }

    params = (
        ('clientRequestID', '6dbe4e390ee64ab8a3edf7d4f9829a7d'),
    )

    response = requests.get(
        'https://cadence.wd1.myworkdayjobs.com/External_Careers/24/searchPagination/318c8bb6f553100021d223d9780d30be/100',
        headers=headers, params=params, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.text
    data = json.loads(soup)
    i = 0
    end_links = []
    for a in data["body"]["children"][0]["children"][0]["listItems"]:
        end = data["body"]["children"][0]["children"][0]["listItems"][i]["title"]["commandLink"]
        end_links.append(end)
        i += 1

    return end_links


def fourth_call():
    cookies = {
        'WorkdayLB_VPS': '3408308746.53810.0000',
        'cdnDown': '0',
        'PLAY_LANG': 'en-US',
        'PLAY_SESSION': '9d958df0bc59f42e37799f8f40c2f39e47043558-cadence_pSessionId=5d1mnv18bka3et70di8lk7ugq7&instance=wd1prvps0002a',
        'wday_vps_cookie': '3408308746.53810.0000',
        'timezoneOffset': '240',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json,application/xml',
        'Referer': 'https://cadence.wd1.myworkdayjobs.com/en-US/External_Careers',
        'Connection': 'keep-alive',
        'stats-perf': '6dbe4e390ee64ab8a3edf7d4f9829a7d,1410,0,',
        'X-Workday-Client': '2018.41.1184',
    }

    params = (
        ('clientRequestID', 'e6f34d058f4047868e5527fd434c6fd8'),
    )

    response = requests.get(
        'https://cadence.wd1.myworkdayjobs.com/External_Careers/26/searchPagination/318c8bb6f553100021d223d9780d30be/150',
        headers=headers, params=params, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.text
    data = json.loads(soup)
    i = 0
    end_links = []
    for a in data["body"]["children"][0]["children"][0]["listItems"]:
        end = data["body"]["children"][0]["children"][0]["listItems"][i]["title"]["commandLink"]
        end_links.append(end)
        i += 1

    return end_links


def fifth_call():
    cookies = {
        'WorkdayLB_VPS': '3408308746.53810.0000',
        'cdnDown': '0',
        'PLAY_LANG': 'en-US',
        'PLAY_SESSION': '9d958df0bc59f42e37799f8f40c2f39e47043558-cadence_pSessionId=5d1mnv18bka3et70di8lk7ugq7&instance=wd1prvps0002a',
        'wday_vps_cookie': '3408308746.53810.0000',
        'timezoneOffset': '240',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json,application/xml',
        'Referer': 'https://cadence.wd1.myworkdayjobs.com/en-US/External_Careers',
        'Connection': 'keep-alive',
        'stats-perf': 'e6f34d058f4047868e5527fd434c6fd8,911,0,',
        'X-Workday-Client': '2018.41.1184',
    }

    params = (
        ('clientRequestID', 'd55948b5760b4d09a206327693f8e09e'),
    )

    response = requests.get(
        'https://cadence.wd1.myworkdayjobs.com/External_Careers/27/searchPagination/318c8bb6f553100021d223d9780d30be/200',
        headers=headers, params=params, cookies=cookies)

    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.text
    data = json.loads(soup)
    i = 0
    end_links = []
    for a in data["body"]["children"][0]["children"][0]["listItems"]:
        end = data["body"]["children"][0]["children"][0]["listItems"][i]["title"]["commandLink"]
        end_links.append(end)
        i += 1

    return end_links


def sixth_call():
    cookies = {
        'WorkdayLB_VPS': '3408308746.53810.0000',
        'cdnDown': '0',
        'PLAY_LANG': 'en-US',
        'PLAY_SESSION': '9d958df0bc59f42e37799f8f40c2f39e47043558-cadence_pSessionId=5d1mnv18bka3et70di8lk7ugq7&instance=wd1prvps0002a',
        'wday_vps_cookie': '3408308746.53810.0000',
        'timezoneOffset': '240',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json,application/xml',
        'Referer': 'https://cadence.wd1.myworkdayjobs.com/en-US/External_Careers',
        'Connection': 'keep-alive',
        'stats-perf': 'd55948b5760b4d09a206327693f8e09e,958,0,',
        'X-Workday-Client': '2018.41.1184',
    }

    params = (
        ('clientRequestID', '523fd69f99ab4f17ab99481ad60ee368'),
    )

    response = requests.get(
        'https://cadence.wd1.myworkdayjobs.com/External_Careers/28/searchPagination/318c8bb6f553100021d223d9780d30be/250',
        headers=headers, params=params, cookies=cookies)

    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.text
    data = json.loads(soup)
    i = 0
    end_links = []
    for a in data["body"]["children"][0]["children"][0]["listItems"]:
        end = data["body"]["children"][0]["children"][0]["listItems"][i]["title"]["commandLink"]
        end_links.append(end)
        i += 1

    return end_links


def seventh_call():
    cookies = {
        'WorkdayLB_VPS': '3408308746.53810.0000',
        'cdnDown': '0',
        'PLAY_LANG': 'en-US',
        'PLAY_SESSION': '9d958df0bc59f42e37799f8f40c2f39e47043558-cadence_pSessionId=5d1mnv18bka3et70di8lk7ugq7&instance=wd1prvps0002a',
        'wday_vps_cookie': '3408308746.53810.0000',
        'timezoneOffset': '240',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json,application/xml',
        'Referer': 'https://cadence.wd1.myworkdayjobs.com/en-US/External_Careers',
        'Connection': 'keep-alive',
        'stats-perf': '523fd69f99ab4f17ab99481ad60ee368,1477,0,',
        'X-Workday-Client': '2018.41.1184',
    }

    params = (
        ('clientRequestID', '9cf227ccebec4d1184dc68834cc05385'),
    )

    response = requests.get(
        'https://cadence.wd1.myworkdayjobs.com/External_Careers/29/searchPagination/318c8bb6f553100021d223d9780d30be/300',
        headers=headers, params=params, cookies=cookies)

    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.text
    data = json.loads(soup)
    i = 0
    end_links = []
    for a in data["body"]["children"][0]["children"][0]["listItems"]:
        end = data["body"]["children"][0]["children"][0]["listItems"][i]["title"]["commandLink"]
        end_links.append(end)
        i += 1

    return end_links


def eight_call():
    cookies = {
        'WorkdayLB_VPS': '3408308746.53810.0000',
        'cdnDown': '0',
        'PLAY_LANG': 'en-US',
        'PLAY_SESSION': '9d958df0bc59f42e37799f8f40c2f39e47043558-cadence_pSessionId=5d1mnv18bka3et70di8lk7ugq7&instance=wd1prvps0002a',
        'wday_vps_cookie': '3408308746.53810.0000',
        'timezoneOffset': '240',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json,application/xml',
        'Referer': 'https://cadence.wd1.myworkdayjobs.com/en-US/External_Careers',
        'Connection': 'keep-alive',
        'stats-perf': '9cf227ccebec4d1184dc68834cc05385,1333,0,',
        'X-Workday-Client': '2018.41.1184',
    }

    params = (
        ('clientRequestID', '58499934e26e48578819cd1a52a8d610'),
    )

    response = requests.get(
        'https://cadence.wd1.myworkdayjobs.com/External_Careers/30/searchPagination/318c8bb6f553100021d223d9780d30be/350',
        headers=headers, params=params, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.text
    data = json.loads(soup)
    i = 0
    end_links = []
    for a in data["body"]["children"][0]["children"][0]["listItems"]:
        end = data["body"]["children"][0]["children"][0]["listItems"][i]["title"]["commandLink"]
        end_links.append(end)
        i += 1

    return end_links


def ninth_call():
    cookies = {
        'WorkdayLB_VPS': '3408308746.53810.0000',
        'cdnDown': '0',
        'PLAY_LANG': 'en-US',
        'PLAY_SESSION': '9d958df0bc59f42e37799f8f40c2f39e47043558-cadence_pSessionId=5d1mnv18bka3et70di8lk7ugq7&instance=wd1prvps0002a',
        'wday_vps_cookie': '3408308746.53810.0000',
        'timezoneOffset': '240',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json,application/xml',
        'Referer': 'https://cadence.wd1.myworkdayjobs.com/en-US/External_Careers',
        'Connection': 'keep-alive',
        'stats-perf': '58499934e26e48578819cd1a52a8d610,1238,0,',
        'X-Workday-Client': '2018.41.1184',
    }

    params = (
        ('clientRequestID', '79475788f9f0445f8fdedeb2dc4c7a0c'),
    )

    response = requests.get(
        'https://cadence.wd1.myworkdayjobs.com/External_Careers/31/searchPagination/318c8bb6f553100021d223d9780d30be/400',
        headers=headers, params=params, cookies=cookies)

    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.text
    data = json.loads(soup)
    i = 0
    end_links = []
    for a in data["body"]["children"][0]["children"][0]["listItems"]:
        end = data["body"]["children"][0]["children"][0]["listItems"][i]["title"]["commandLink"]
        end_links.append(end)
        i += 1

    return end_links


def tenth_call():
    cookies = {
        'WorkdayLB_VPS': '3408308746.53810.0000',
        'cdnDown': '0',
        'PLAY_LANG': 'en-US',
        'PLAY_SESSION': '9d958df0bc59f42e37799f8f40c2f39e47043558-cadence_pSessionId=5d1mnv18bka3et70di8lk7ugq7&instance=wd1prvps0002a',
        'wday_vps_cookie': '3408308746.53810.0000',
        'timezoneOffset': '240',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json,application/xml',
        'Referer': 'https://cadence.wd1.myworkdayjobs.com/en-US/External_Careers',
        'Connection': 'keep-alive',
        'stats-perf': '79475788f9f0445f8fdedeb2dc4c7a0c,1021,0,',
        'X-Workday-Client': '2018.41.1184',
    }

    params = (
        ('clientRequestID', '8d7bdfcd67dd41c0a27ad7b23affaac5'),
    )

    response = requests.get(
        'https://cadence.wd1.myworkdayjobs.com/External_Careers/32/searchPagination/318c8bb6f553100021d223d9780d30be/450',
        headers=headers, params=params, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.text
    data = json.loads(soup)
    i = 0
    end_links = []
    for a in data["body"]["children"][0]["children"][0]["listItems"]:
        end = data["body"]["children"][0]["children"][0]["listItems"][i]["title"]["commandLink"]
        end_links.append(end)
        i += 1

    return end_links
