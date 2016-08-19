from bs4 import BeautifulSoup
import csv
import re
import os
import urllib2
import xlrd
import xlwt


path = os.getcwd()


def read_xls():
    urls = []
    file_location = os.path.join(path, 'broker.xls')
    workbook = xlrd.open_workbook(file_location, formatting_info=True)
    sheet = workbook.sheet_by_index(0)
    # print sheet.cell_value(0,0)
    # print sheet.nrows
    # print sheet.ncols
    a = 0
    for row in range(sheet.nrows):
        row_values = sheet.row_values(row, start_colx=0, end_colx=3)
        company_names = row_values[0]
        link = sheet.hyperlink_map.get((row, 0))
        # print company_names, link
        url = '(No URL)' if link is None else link.url_or_path
        a += 1
        clean_url = url.strip('(No URL)')

        urls.append(clean_url)
        # links.append(clean_url)
        # print a
        # print '{0}'.format(company_names)
        # links='{0}'.format(clean_url)
        # print '{0}'.format(company_names)
    return urls
# url='http://www.ncbfaa.org/Scripts/4Disapi.dll/4DCGI/directory/Member/detail.html?Action=NCBFAA&NCBFAA_Activity=DirectoryDetailComp&CID_W=35&AddressIDD_W=40&Time=-1780439465&SessionID=8709471ip9k9f78blq23547mq6t2vr19d26c0lyfug55tywb66n1933w9qw6hs17&MenuKey=members'
# url='http://www.ncbfaa.org/Scripts/4Disapi.dll/4DCGI/directory/Member/detail.html?Action=NCBFAA&NCBFAA_Activity=DirectoryDetailComp&CID_W=36&AddressIDD_W=42&Time=-1780439465&SessionID=8709471ip9k9f78blq23547mq6t2vr19d26c0lyfug55tywb66n1933w9qw6hs17&MenuKey=members'
# url='http://www.ncbfaa.org/Scripts/4Disapi.dll/4DCGI/directory/Member/detail.html?Action=NCBFAA&NCBFAA_Activity=DirectoryDetailComp&CID_W=37&AddressIDD_W=44&Time=-1780439465&SessionID=8709471ip9k9f78blq23547mq6t2vr19d26c0lyfug55tywb66n1933w9qw6hs17&MenuKey=members'
# url='http://www.ncbfaa.org/Scripts/4Disapi.dll/4DCGI/directory/Member/detail.html?Action=NCBFAA&NCBFAA_Activity=DirectoryDetailComp&CID_W=41&AddressIDD_W=52&Time=-1780439465&SessionID=8709471ip9k9f78blq23547mq6t2vr19d26c0lyfug55tywb66n1933w9qw6hs17&MenuKey=members'
# url='http://www.ncbfaa.org/Scripts/4Disapi.dll/4DCGI/directory/Member/detail.html?Action=NCBFAA&NCBFAA_Activity=DirectoryDetailComp&CID_W=42&AddressIDD_W=54&Time=-1780439465&SessionID=8709471ip9k9f78blq23547mq6t2vr19d26c0lyfug55tywb66n1933w9qw6hs17&MenuKey=members'
# url='http://www.ncbfaa.org/Scripts/4Disapi.dll/4DCGI/directory/Member/detail.html?Action=NCBFAA&NCBFAA_Activity=DirectoryDetailComp&CID_W=43&AddressIDD_W=56&Time=-1780439465&SessionID=8709471ip9k9f78blq23547mq6t2vr19d26c0lyfug55tywb66n1933w9qw6hs17&MenuKey=members'
# url='http://www.ncbfaa.org/Scripts/4Disapi.dll/4DCGI/directory/Member/detail.html?Action=NCBFAA&NCBFAA_Activity=DirectoryDetailComp&CID_W=44&AddressIDD_W=58&Time=-1780439465&SessionID=8709471ip9k9f78blq23547mq6t2vr19d26c0lyfug55tywb66n1933w9qw6hs17&MenuKey=members'
# url='http://www.ncbfaa.org/Scripts/4Disapi.dll/4DCGI/directory/Member/detail.html?Action=NCBFAA&NCBFAA_Activity=DirectoryDetailComp&CID_W=46&AddressIDD_W=61&Time=-1780439465&SessionID=8709471ip9k9f78blq23547mq6t2vr19d26c0lyfug55tywb66n1933w9qw6hs17&MenuKey=members'

url='http://www.ncbfaa.org/Scripts/4Disapi.dll/4DCGI/directory/Member/detail.html?Action=NCBFAA&NCBFAA_Activity=DirectoryDetailComp&CID_W=83&AddressIDD_W=133&Time=-1784431270&SessionID=8709168g6m9r84a9whqcgc314051a5622j6o9833ft2u2hr81dz0cp754ikhjkj2&MenuKey=members'
 # url=''
# url=''
# url=''
# url=''
# url=''
# url=''
# url=''
# url=''

def get_company_name(url):
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, 'lxml')
    company_name = soup.findAll('h2')
    return company_name[1].get_text()


def get_data(url):
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, 'lxml')
    contacts = []
    tables = soup.findAll('table')
    subtable = tables[3]
    tds = subtable.findAll('td')
    for td in tds:
        data = td.get_text()
        contacts.append(data)
    del contacts[::2]
    return contacts


def contacts():
    return list((get_company_name(url), get_data(url)))


with open('broker.csv', 'a') as outcsv:
    # configure writer to write standard csv file
    writer = csv.writer(outcsv,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    # writer.writerow(['Company Name', 'Primary Contact', 'Company Address','Broker License','Phone','Fax','Email','Web', 'Services'])
    if len(get_data(url)) ==8:
        writer.writerow([contacts()[0], contacts()[1][0], contacts()[1][1], contacts()[1][2], contacts()[
                        1][3], contacts()[1][4], contacts()[1][5], contacts()[1][6], contacts()[1][7]])
        print get_company_name(url)
        print contacts()[1][0]
        print contacts()[1][1]
        print contacts()[1][2]
        print contacts()[1][3]
        print contacts()[1][4]
        print contacts()[1][5]
        print contacts()[1][6]
        print contacts()[1][7]
    else:
        writer.writerow([contacts()[0], contacts()[1][0], contacts()[1][1], '', contacts()[
                        1][2], contacts()[1][3], contacts()[1][4], contacts()[1][5], contacts()[1][6]])


        print get_company_name(url)
        print contacts()[1][0]
        print contacts()[1][1]
        print contacts()[1][2]
        print contacts()[1][3]
        print contacts()[1][4]
        print contacts()[1][5]
        print contacts()[1][6]


