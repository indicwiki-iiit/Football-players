import pickle
import pandas as pd
import sweetviz as sv


def analyse(df,title):
	#generating sweetviz report
	report =sv.analyze([df,title])
	report.show_html()


def main():
	playerFile = './players.csv'
	playerDF = pd.read_csv(playerFile)

	#filling null values with nan string
	playerDF=playerDF.fillna('nan')
	#converting numerical attributes into strings
	playerDF['marking']=playerDF['marking'].astype(str)
	playerDF['value_euro']=playerDF['value_euro'].astype(str)
	playerDF['wage_euro']=playerDF['wage_euro'].astype(str)
	playerDF['release_clause_euro']=playerDF['release_clause_euro'].astype(str)
	playerDF['national_jersey_number']=playerDF['national_jersey_number'].astype(str)
	playerDF['player_id']=playerDF['player_id'].astype(str)

	
	analyse(playerDF,'footballplayers')
	

	pickle.dump(playerDF, open('./playerDF.pkl', 'wb'))



if __name__ == '__main__':
	main()