# from portfolio import Portfolio


class Model_portfolio:

	def __init__(self, score):
		self.score = score
		self.recommended = self.recommended_portfolio()
		self.result = None

	def recommended_portfolio(self):

		if self.score in [16, 17, 18, 19, 20]:
			return "agressive"

		elif self.score in [11, 12, 13, 14, 15]:
			return "moderatly_aggressive"

		elif self.score in [6, 7, 8, 9, 10]:
			return "moderate"

		else:
			return "conservative"


	def call_portfolio(self, portfolio):

		if self.portfolio == '1':
			return_portfolio = Portfolio.objects.get(id=1)
		elif self.portfolio == '2':
			return_portfolio = Portfolio.objects.get(id=2)	
		elif self.portfolio = '3':
			return_portfolio = Portfolio.objects.get(id=3)
		else:
			return_portfolio = Portfolio.objects.get(id=4)

		return return_portfolio

	
	def call_text(self, portfolio):

		if self.portfolio = '1':
			with open('agressive.txt', 'r') as myfile:
				data=myfile.read().replace('\n', '')
		elif self.portfolio = '2':
			with open('moderatly_aggressive.txt', 'r') as myfile:
				data=myfile.read().replace('\n', '')
		elif self.portfolio = '2':
			with open('moderate.txt', 'r') as myfile:
				data=myfile.read().replace('\n', '')
		else:
			with open('moderate.txt', 'r') as myfile:
				data=myfile.read().replace('\n', '')
		return data

	def craete_context(self):
		return_portfolio = call_portfolio()
		data = call_text()
		self.result = dict(portfolio=return_portfolio, portfolio_description=data)
		return self.result




# p = Model_portfolio(2)




