from .securities_models import Stock
import re
from decimal import *


def file_opener():
        data = [line.split("\n")[0].split('","') for line in open('securities/companylist.csv','r')]
        return data

def inser_data_in_db():
        data = file_opener()
        print(data[1])
        for symbol, name, _, marketcap, _, sector, industry, _ in data[1:]:
            # line = line[:-1]
            symbol = symbol[1:]
            marketcap = parse_marketcap(marketcap)
            stock = Stock(
                symbol=symbol,
                company_name=name,
                market_capitalization=marketcap,
                sector=sector,
                industry=industry
            )
            stock.save()

def parse_marketcap(mp):
    mp_M = re.match(r'^\$.*M$',mp)
    mp_B = re.match(r'^\$.*B$',mp)
    if mp_M is not None:
        return Decimal(mp_M.group()[1:-1])
    elif mp_B is not None:
        return  Decimal(mp_B.group()[1:-1])*1000
    else:
        return Decimal('0.00')



