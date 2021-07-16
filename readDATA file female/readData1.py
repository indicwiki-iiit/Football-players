import pandas as pd
import pickle
import sweetviz as sv

def analyse(df,title):
    report = sv.analyze([df,title])
    report.show_html()
    return report

def main():
    footballDF = pd.read_csv('femaleplayers1.csv')
    footballDF.dropna(inplace = True)

    # Generating the Sweetviz report
    sv_analyze = analyse(footballDF,"female players'dataAnalysis")

    # Generating the pickle file for the dataset
    pickle.dump(footballDF,open('female_plyrsDF.pkl','wb'))
if __name__=='__main__':
    main()
