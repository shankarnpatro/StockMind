import csv

import requests

API_ENDPOINT = 'http://192.168.1.18:8000/api/equity_sells/create/'


def csv_f():
    fobj = open('API_Sell_Test_Execution_Status.csv', 'w')
    fobj.write('symbol_name' + ',' + 'sell_price' + ',' + 'Status_code' + ',' + 'Status_Message' + '\n')
    with open('Sell_Equity.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if 'symbol_name' not in row:
                print(row)
                status_code, status_msg = equity_sell_Apicall(API_ENDPOINT, row[0], row[1], row[2], row[3])
                fobj.write(row[0] + ',' + row[1] + ',' + str(status_code) + ',' + status_msg + '\n')
        fobj.close()
        print(f'Processed {line_count} lines.')


def equity_sell_Apicall(API_ENDPOINT, sname, sPrice, tPrice, achievement):
    data = {'symbol_name': sname, 'sell_price': int(sPrice), 'target_price': int(tPrice), 'achievement': achievement}
    print(data)
    r = requests.post(url=API_ENDPOINT, data=data)
    pastebin_url = r.status_code
    pastebin_msg = r.text
    print("The pastebin URL is:%s" % pastebin_url)
    print("The pastebin URL is:%s" % pastebin_msg)
    return pastebin_url, pastebin_msg


csv_f()
