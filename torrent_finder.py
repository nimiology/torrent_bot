import requests
from bs4 import BeautifulSoup
import telepot

bot = telepot.Bot('your token')

def GetDetail(LINK,chat_id):
    LINK_TEXT = requests.get(LINK).text
    BS4 = BeautifulSoup(LINK_TEXT,'html.parser')
    NAME = BS4.find(id = "title").string
    TYPE = BS4.find(title = 'More from this category').string
    FILES = BS4.find(title='Files').string
    DETAIL = BS4.find(class_='col2').text
    NUM = BS4.text.find('Size:')
    SIZE = BS4.text[NUM:NUM+40]
    SIZEE = SIZE.find("(")
    SIZE = SIZE[:SIZEE]
    DES = BS4.find("pre").text
    TORRENT_LINK = BS4.find(title="Get this torrent").get("href")
    MESSTGE = f"{NAME}\n\nproperties:\n\n\n\n\nType:\n{TYPE}\nFiles:\n{FILES}\n{SIZE}\n{DETAIL}\n\ndescription:\n****************\n{DES}\n****************\nLINK TORRENT:\n\n{TORRENT_LINK}\n\n**********************************"
    try:
        bot.sendMessage(chat_id,MESSTGE)
    except:
        MESSTGE = '{NAME}\n\nproperties:\n\n\n\n\nType:\n{TYPE}\nFiles:\n{FILES}\n{SIZE}\n{DETAIL}\n\ndescription:\n****************\n{DES}\n****************'
        bot.sendMessage(chat_id, MESSTGE)
        bot.sendMessage(chat_id, f"torrent link:\n\n{TORRENT_LINK}")


def FINDLINKS(INPUT, filter, page,chat_id):
    LINK_SEARCH = requests.get(f"https://thepiratebay10.org/search/{INPUT}/{page}/99/{filter}").text
    BS4 = BeautifulSoup(LINK_SEARCH,'html.parser')
    FINDER = BS4.find_all(class_="detLink")
    for LINK in FINDER:
        GetDetail(LINK.get("href"),chat_id)

