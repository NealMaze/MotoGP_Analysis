# import necessary modules
import requests
from bs4 import BeautifulSoup
import time
from collections import defaultdict
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 1) function return a soup object
def soup_special(url):
    """Returns a BeautifulSoup object for the provided url"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# 2) functions to get various datapoints from a soup object
def get_date(soup):
    """ Returns the date of the race, or 'n/a' if
        information does not exist in the provided soup """
    find = soup.find(class_='padbot5')
    if find is None:
        r = 'n/a'
    else:
        r = ','.join(find.text.replace(',',' ').split()[-3:])
    return r

def get_tr_con(soup):
    """ Returns the track condition during a race, or 'n/a' if
        information does not exist in the provided soup """
    find = soup.find(class_='sprite_weather track_condition')
    if find is None:
        r = 'n/a'
    else:
        r = find.findNext().text.split()[2]
    return r

def get_tr_tmp(soup):
    """ Returns the track temperature during a race, or 'n/a' if
        information does not exist in the provided soup """
    find = soup.find(class_='sprite_weather ground')
    if find is None:
        r = 'n/a'
    else:
        r = find.findNext().text.split()[1]
    return r

def get_air_tmp(soup):
    """ Returns the air temperature during a race, or 'n/a' if
        information does not exist in the provided soup """
    find = soup.find(class_='sprite_weather air')
    if find is None:
        r = 'n/a'
    else:
        r = find.findNext().text.split()[1]
    return r

def get_humidity(soup):
    """ Returns the track humidity during a race, or 'n/a' if
        information does not exist in the provided soup """
    find = soup.find(class_='sprite_weather humidity')
    if find is None:
        r = 'n/a'
    else:
        r = find.findNext().text.split()[1]
    return r

def get_all_cats(soup):
    """ Returns all the different categories (MotoGP, Moto2, etc.)
        that took place at a particular track in the provided soup """
    find = soup.find(id='category')
    if find is None:
        r = []
    else:
        r = find.find_all('option')
    return r

def get_all_sessions(soup):
    """ Returns all the different sessions (RACE, RACE2, etc.)
        that took place at a particular track in the provided
        soup, (modified to include practices and qualifying """
    find = soup.find(id='session')
    r = []
    if find is None:
        print(f"\n - - - - - No Sessions Found - - - - - ")
    else:
        r2 = find.find_all('option')
        for s in r2:
            r.append(s.text)
    return r

def getOffSeasonTests(soup):
    hrefLinks = []
    links = soup.find_all("a", {"class": ["bold"]})
    for link in links:
        if "Results" in link.text:
            hrefLinks.append(link["href"])
    return hrefLinks

def get_GP_info_additional(track_url_str):
    """
    Returns MotoGP average speed, MotoGP distance, Moto2 distance,
    and Moto3 distance for the particular track. If data does not exist,
    it returns 'n/a' in place of a float or int.
    """
    url = 'http://www.motogp.com/en/event/' + track_url_str + '#info-track'
    soupy = soup_special(url)

    # MotoGP average speed
    avg_speed_str = soupy.find(class_='c-statistics__speed-item').text
    if avg_speed_str == '-':
        avg_speed = 'n/a'
    else:
        avg_speed = float(avg_speed_str)

    attributes = soupy.find(class_='c-laps__content').find_all(class_='c-laps__item')

    # MotoGP distance
    GP_dist = float(attributes[9].text.split()[0])
    if GP_dist == 0: GP_dist = 'n/a'

    # Moto2 distance
    m2_dist = float(attributes[10].text.split()[0])
    if m2_dist == 0: m2_dist = 'n/a'

    # Moto3 distance
    m3_dist = float(attributes[11].text.split()[0])
    if m3_dist == 0: m3_dist = 'n/a'

    return [avg_speed, GP_dist, m2_dist, m3_dist]

def get_GP_info(track_url_str):
    """
    Returns a list with track length, number of left corners, number of right corners,
    track width, and length of longest straight. For any unavailable values, it returns
    'n/a' instead of a float or int.
    """
    url = 'http://www.motogp.com/en/event/' + track_url_str + '#info-track'
    soupy = soup_special(url)
    attributes = soupy.find(id='circuit_numbers').find_all(class_='circuit_number_content')
    strs = []
    list_data = []

    for s in range(len(attributes)):
        strs.append(attributes[s].text)

    if float(strs[0].split()[0]) == 0:
        list_data.append('n/a')
    else:
        list_data.append(float(strs[0].split()[0]))

    if strs[1] == '':
        list_data.append('n/a')
    else:
        list_data.append(int(strs[1]))

    if strs[2] == '':
        list_data.append('n/a')
    else:
        list_data.append(int(strs[2]))

    if len(strs[3].split()) == 1:
        list_data.append('n/a')
    else:
        list_data.append(float(strs[3].split()[0]))

    if len(strs[4].split()) == 1:
        list_data.append('n/a')
    else:
        list_data.append(float(strs[4].split()[0]))

    return list_data

def getAllRounds(soup):
    """ Returns all the rounds that took place in a particular season
        for which the soup was passed in """
    find = soup.find(id='event')
    if find is None:
        r = []
    else:
        r = find.find_all('option')
    return r

########################################################################################################################
# 3) function to get testing sessions
# def changeHandleSeason():


def getAllTests(soup, yr):
    """ Returns all the tests that took place during the season
        of the soup object it's passed"""
    find = soup.find(id = f"testoffseason{yr}")
    if find is None:
        r = []
        print(f"no tests were found in {yr}")
    else:
        r = find.find_all(href = True)
    return r

########################################################################################################################

def get_date(soup):
    """ Returns the date of the race, or 'n/a' if
        information does not exist in the provided soup """
    find = soup.find(class_='padbot5')
    if find is None:
        r = 'n/a'
    else:
        r = ','.join(find.text.replace(',',' ').split()[-3:])
    return r

def get_tr_con(soup):
    """ Returns the track condition during a race, or 'n/a' if
        information does not exist in the provided soup """
    find = soup.find(class_='sprite_weather track_condition')
    if find is None:
        r = 'n/a'
    elif len(find) < 3:
        r = "n/a"
    else:
        r = find.findNext().text.split()[2]
    return r

def get_tr_tmp(soup):
    """ Returns the track temperature during a race, or 'n/a' if
        information does not exist in the provided soup """
    find = soup.find(class_='sprite_weather ground')
    if find is None:
        r = 'n/a'
    else:
        r = find.findNext().text.split()[1]
    return r

def get_air_tmp(soup):
    """ Returns the air temperature during a race, or 'n/a' if
        information does not exist in the provided soup """
    find = soup.find(class_='sprite_weather air')
    if find is None:
        r = 'n/a'
    else:
        r = find.findNext().text.split()[1]
    return r

def get_humidity(soup):
    """ Returns the track humidity during a race, or 'n/a' if
        information does not exist in the provided soup """
    find = soup.find(class_='sprite_weather humidity')
    if find is None:
        r = 'n/a'
    else:
        r = find.findNext().text.split()[1]
    return r

def getAllStats(soup, year, trk, track, cat, ssn):
    rHeaders = ["Year", "Number", "Name", "Nation", "Team", "Manufacturer"]
    rdrs = []
    wthr = []

    if soup.find('tbody') is None:
        return "failed Weather", "failed Rider"
    else:
        riders = soup.find('tbody').find_all('a')

        # raceday stats
        date = get_date(soup)
        trCon = get_tr_con(soup)
        trTmp = get_tr_tmp(soup)
        airTmp = get_air_tmp(soup)
        humid = get_humidity(soup)

        wthr.append(year)
        wthr.append(date)
        wthr.append(track)
        wthr.append(cat)
        wthr.append(ssn)
        wthr.append(trCon)
        wthr.append(trTmp)
        wthr.append(airTmp)
        wthr.append(humid)

        # rider stats
        for r in riders:
            pos = r.findPrevious().findPrevious().findPrevious().findPrevious().text
            if pos == '':
                pos = 'crash'
            points = r.findPrevious().findPrevious().findPrevious().text
            if points == '':
                points = 0
            else:
                points = float(points)
            r_num = r.findPrevious().findPrevious().text
            if r_num != '':
                r_num = int(r_num)
            r_nam = r.text
            r_nat = r.findNext().text
            team = r.findNext().findNext().text
            bike = r.findNext().findNext().findNext().text
            avgspd = r.findNext().findNext().findNext().findNext().text
            time = r.findNext().findNext().findNext().findNext().findNext().text

            rdr = [year, cat, r_num, r_nam, r_nat, team, bike]
            rdrs.append(rdr)

        return wthr, rdrs













########################################################################################################################

def getSessPDFs(soup):
    """ Returns all the PDFs associated with the selected session"""
    links = []
    find = soup.find(id="results_menu")

    if find is None:
        links = []
        print("no PDFs Found")
        find = soup.find_all(href=True)
        for i in find:
            x = i["href"]
            if "resources" in x:
                print(x)
    else:
        q = find.find_all(href=True)
        for i in q:
            x = i["href"]
            if "https" in x:
                links.append(x)
    return links

def getPDFs(soup):
    """ Returns all the PDFs associated with the selected session"""
    links = []
    find = soup.find(id="results_menu")

    if find is None:
        links = []
        print("no PDFs Found")
        find = soup.find_all(href=True)
        for i in find:
            x = i["href"]
            if "resources" in x:
                print(x)
    else:
        q = find.find_all(href=True)
        for i in q:
            x = i["href"]
            if "https" in x:
                links.append(x)
    return links

def saveCSV(mat, file):
    # """accepts a matrix, and a file destination, and saves
    # the matrix as a csv file"""

    df = pd.DataFrame(mat)
    df.to_csv(file, index = False)
