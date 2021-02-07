import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 


#----------- BOT------------
class Bot:
	def __init__(self, data, name_stock):
		self.data = pd.read_csv(data)
		self.name = name_stock
		self.SMA15 = self.data['Close'].rolling(window=15).mean()
		self.SMA50 = self.data['Close'].rolling(window=50).mean()

	def strategy(self):
		buy_sign = []
		sell_sign = []
		flag = -1
		for i in range(len(self.data)):
        	#Sign to buy
			if self.SMA15[i] > self.SMA50[i] and flag != 1 :
				buy_sign.append(self.data['Close'][i])
				sell_sign.append(np.nan)
				flag = 1

        	#Sign to sell 
			elif self.SMA15[i] < self.SMA50[i] and flag != -1 :
				buy_sign.append(np.nan)
				sell_sign.append(self.data['Close'][i])
				flag = -1

        	#None of the two previous condition
			else:
				buy_sign.append(np.nan)
				sell_sign.append(np.nan)
			
		
		return (buy_sign, sell_sign)
	
	def plotgraph(self):
		plt.figure(figsize =(15, 8))
		plt.plot(self.data['Close'], label = self.name + ' stock')
		plt.plot(self.SMA15, label = 'SMA15')
		plt.plot(self.SMA50, label = 'SMA50')
		plt.plot(self.data.index , self.strategy()[0], 'g^', label = 'Buy')
		plt.plot(self.data.index , self.strategy()[1], 'rv', label = 'Sell')
		plt.title(self.name + " stock")
		plt.legend()
		plt.show()





#AAPL bot		
B = Bot("AAPL.csv", "AAPL")
B.strategy()
B.plotgraph()

#XOM bot
bo = Bot("XOM (1).csv", "XOM")
bo.strategy()
bo.plotgraph()
#Microsoft bot
b1 =  Bot("MSFT.csv", "MSFT")
b1.strategy()
b1.plotgraph()


