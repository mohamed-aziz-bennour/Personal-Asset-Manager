import pandas as pd
import numpy as np
from pandas_datareader import data
from datetime import date
from portfolio.models import Portfolio, Asset


class RiskAnalysis:

    def __init__(self):
        self.start_date = None
        self.end_date = None
        self.period = None
        self.stock_returns = None
        self.sp_returns = None
        self.beta = None
        self.alpha = None
    
    def run_analysis(self, symbol):
        self.start_date = date(2013,12,31)
        self.end_date = date(2015,12,31)
        self.period = 12
        self.stock_returns = self.calculate_stock_returns(symbol)

        self.sp_returns = self.calculate_sp_returns()
        self.beta = self.calculate_beta()
        self.alpha = self.calculate_alpha()
        return self.risk_report()

    def get_data(self, symbol):
        stock = data.DataReader(symbol,'yahoo',self.start_date, self.end_date)
        return stock

    def adjust_date_range(self, stock):
        self.start_date = stock.index.min().date()  
        self.end_date = stock.index.max().date()

    def get_sp_data(self):
        sp = data.DataReader('^GSPC','yahoo',self.start_date, self.end_date)
        return sp


    def calculate_stock_returns(self, symbol):
        stock = self.get_data(symbol)
        self.adjust_date_range(stock)

        data = pd.DataFrame({'stock_adj_close':stock['Adj Close']}, index=stock.index)
        data[['stock_returns']] = data[['stock_adj_close']]/data[['stock_adj_close']].shift(1)-1 
        stock_return = data.dropna()
        return stock_return
    
    def calculate_sp_returns(self):
        sp = self.get_sp_data()
        data = pd.DataFrame({'sp_adj_close':sp['Adj Close']}, index=sp.index)
        data[['sp_returns']] = data[['sp_adj_close']]/data[['sp_adj_close']].shift(1)-1 
        sp_return = data.dropna()
        return sp_return


    def compute_covariance(self):
        covariance = np.cov(self.stock_returns['stock_returns'], self.sp_returns['sp_returns'])
        return covariance

    def calculate_beta(self):
        covariance = self.compute_covariance()
        beta = covariance[0,1]/covariance[1,1]
        return beta

    def calculate_alpha(self):
        alpha = np.mean(self.stock_returns['stock_returns'])-self.beta*np.mean(self.sp_returns['sp_returns'])
        return alpha
        
    def annualized_alpha(self):
        annualized_alpha = self.alpha*self.period
        return annualized_alpha

    def calculate_r_squared(self):
        covariance = self.compute_covariance()
        ypred = self.alpha+self.beta*self.sp_returns['sp_returns']
        ss_res = np.sum(np.power(ypred-self.stock_returns['stock_returns'],2))
        ss_tot = covariance[0,0]*(len(self.stock_returns)-1)
        r_squared = 1.-ss_res/ss_tot
        return r_squared

    def calculate_volatility(self):
        covariance = self.compute_covariance()
        volatility = np.sqrt(covariance[0,0])
        volatility = volatility*np.sqrt(self.period)
        return volatility

    def calculate_moment(self):
        momentum = np.prod(1+self.stock_returns['stock_returns'].tail(12).values)-1
        return momentum

    def risk_report(self):
        beta = self.beta
        annualized_alpha = self.annualized_alpha()
        r_squared = self.calculate_r_squared()
        volatility = self.calculate_volatility()
        risk_report = {'beta':round(beta,2), 
                        'alpha': round(annualized_alpha * 100,2), 
                        'r_squared':round(r_squared,2),
                        'volatility':volatility}
        return risk_report

class Analysis_portfolio():

    def anlaysis_portfolio(self,id):
        portfolio_object = Portfolio.objects.get(id=id)
        # bond = ContentType.objects.get_for_model(Bond)
        assets= Asset.objects.raw('''SELECT *, cost_basis * quantity as value 
            FROM portfolio_asset
            WHERE portfolio_asset.portfolio_id = %s ''',(id,))
        # print(assets)
        portfolio_value = 0 
        for asset in assets:
            portfolio_value += asset.value
        
        assets = [ asset.to_json(asset.value,portfolio_value)for asset in assets ]

        # assets = portfolio_object.asset_set.exclude(content_type=bond)

        print(assets)
        risk = RiskAnalysis()
        # print(risk)

        context = {}
        alpha = 0
        beta = 0
        r_squared = 0 
        for asset in assets:
            if asset["content_type"] != "bond":
               symbol = asset["content_object"]["symbol"]
               print(symbol)
               stock = risk.run_analysis(symbol)
            else:
               stock  = {'beta':0, 
                        'alpha':0, 
                        'r_squared':0,
                        'volatility':0}
            # context[symbol] = stock
            asset['analysis']=stock
            asset['analysis_total'] = {'beta':round(stock["beta"] * asset['weight'] /100,2), 
                                      'alpha':round(stock["alpha"] * asset['weight'] /100,2), 
                                      'r_squared':round(stock["r_squared"] * asset['weight'] / 100,2)
                                        }
            alpha += stock["alpha"] * asset['weight'] /100
            beta += stock["beta"] * asset['weight'] /100
            r_squared += stock["r_squared"] * asset['weight'] / 100 
            asset['weight'] =  round (asset['weight'],2)


        totals = {'portfolio_value' :portfolio_value,
                    'alpha': round(alpha,2), 
                    'beta' : round(beta,2),
                    'r_squared' : round(r_squared,2)

                    }

         
        # return JsonResponse({'response':assets,'total':totals,'portfolio':portfolio_object.to_json()})
        return dict(response = assets ,total = totals ,portfolio = portfolio_object.to_json())
























