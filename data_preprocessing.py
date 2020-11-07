import numpy as np
import pandas as pd
books = pd.read_csv('BX-Books.csv',sep=';',error_bad_lines=False,encoding='latin-1')
books.head()
books = books.drop(['Image-URL-S','Image-URL-M','Image-URL-L'],axis=1)
books.head()
books.info()
books.dtypes
books['Year-Of-Publication'].unique()
pd.set_option('max_colwidth',None)
books.head()
books.loc[books['Year-Of-Publication']=='DK Publishing Inc',:]
books.loc[books['ISBN'] == '078946697X','Year-Of-Publication']=2000
books.loc[books['ISBN'] == '078946697X','Book-Author'] = 'Michael Teitelbaum'
books.loc[books['ISBN'] == '078946697X','Book-Title']='DK Readers: Creating the X-Men, How It All Began (Level 4: Proficient Readers)'
books.loc[books['ISBN'] == '078946697X','Publisher']='DK Publishing Inc'
books.loc[books['ISBN'] == '0789466953','Year-Of-Publication'] = 2000
books.loc[books['ISBN'] == '0789466953','Book-Author']='James Buckley'
books.loc[books['ISBN'] == '0789466953','Book-Title']='DK Readers: Creating the X-Men, How Comic Books Come to Life (Level 4: Proficient Readers)'
books.loc[books['ISBN'] == '0789466953','Publisher']='DK Publishing Inc'
books.loc[books['Book-Author']=='Michael Teitelbaum']
books.loc[books['Year-Of-Publication'] == 'Gallimard']
books.loc[books['ISBN']=='2070426769','Year-Of-Publication'] = 2003
books.loc[books['ISBN']=='2070426769','Book-Author'] = 'J.M.G. Le Clézio'
books.loc[books['ISBN']=='2070426769','Book-Title'] = 'Peuple Du Ciel Suivi de les Bergers'
books.loc[books['ISBN']=='2070426769','Publisher'] = 'Gallimard'
books.loc[books['Book-Author'] == 'J.M.G. Le Clézio',:]
books['Year-Of-Publication'] = pd.to_numeric(books['Year-Of-Publication'],errors='coerce')
books['Year-Of-Publication'].dtype
books.loc[(books['Year-Of-Publication']>2020) | (books['Year-Of-Publication'] == 0),'Year-Of-Publication'] = np.NaN
books['Year-Of-Publication'].fillna(round(books['Year-Of-Publication'].mean()),inplace=True)
users = pd.read_csv('BX-Users.csv',sep=';',error_bad_lines=False,encoding='latin-1')
users.head()
books.loc[books['Publisher'].isnull(),:]
books.loc[books['ISBN'] == '193169656X','Publisher'] = 'other'
books.loc[books['ISBN'] == '1931696993','Publisher'] = 'other'
books.loc[books['Book-Author'].isnull(),:]
books.loc[books['ISBN'] == '9627982032','Book-Author']='Anonymous'
users.info()
users.loc[users['Age']>100,'Age'] = np.nan
users['Age'].fillna(round(users['Age'].mean()),inplace=True)
users['User-ID'].nunique()
ratings = pd.read_csv('BX-Book-Ratings.csv',sep=';',error_bad_lines=False,encoding='latin-1')
ratings.head()
ratings.info()
