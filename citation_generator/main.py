import pandas as pd



if __name__ == '__main__':

    '''
        This script is meant to work with csv files produed by google scholar
    '''

    FNAME='./citations.csv'

    db = pd.read_csv(FNAME, sep=',', header=0)
    db = db.sort_values(by=['Year', 'Authors', 'Title'], ascending=False)
    
    for i, row in db.iterrows():
        
        pubn = "''" if pd.isnull(row['Publication']) else row['Publication']
        pubr = "''" if pd.isnull(row['Publisher'])   else row['Publisher']
        year = row['Year']
    
        APA = f"{row['Authors']}. ({year}). {row['Title']}. {pubn}. {pubr}"

        tp  = "TODO"
        if 'journal' in APA.lower() or 'transaction' in APA.lower()  or 'nature' in APA.lower() or 'letters' in APA.lower():
            tp = "Journal" 
        elif 'conference' in APA.lower() or 'symposium' in APA.lower():
            tp = "Conference"


        print(f"|{APA}|{year}|{tp}|[url]()|[ArXiv]()|")


