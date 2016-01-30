from .securities_models import ExchangeTradedFund



def file_opener():
	etfs = []
	with open('securities/etf.csv','r',errors='replace') as etf_data:
		for line in etf_data.readlines():
			split_line = line.strip().split(',')
			name, symbol, type_ = split_line

			if parse_symbol(symbol):
				parent, etf_name = parse_name(name)
				new_etf = [name, parent,  symbol, type_]
				etfs.append(new_etf)
		return etfs

def parse_name(name):
	parent, *name = name.split(' ')
	return parent, ' '.join(name)


def parse_symbol(symbol):
	if symbol.startswith('$'):
		return False
	elif symbol.startswith('.'):
		return False
	elif symbol.startswith('^'):
		return False
	else:
		return True
			



def insert_data_in_db():
		data = file_opener()
		for name, family_name, symbol, type_ in data:	
			etf = ExchangeTradedFund(
				symbol=symbol,
				name=name,
				category=type_,
				fund_family=family_name,
			)
			etf.save()

		