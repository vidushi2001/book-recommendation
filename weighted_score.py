ratings['ISBN'].nunique()
ratings['ISBN'].nunique
ratings['Book-Rating'].unique()
ratings_new = ratings[ratings['ISBN'].isin(books['ISBN'])]
ratings_new = ratings_new[ratings_new['User-ID'].isin(users['User-ID'])]
sns.countplot(data=ratings_explicit,x='Book-Rating')
ratings = ratings[ratings['ISBN'].isin(books['ISBN'])]
ratings
ratings['ISBN'].nunique()
count = ratings['ISBN'].value_counts()
ratings = ratings[ratings['Book-Rating']!=0]
ratings = ratings[ratings['ISBN'].isin(count[count>=95].index)]
ratings.shape
ratings['ISBN'].nunique()
df = pd.DataFrame(ratings.groupby(['ISBN'])['Book-Rating'].mean())
df.shape
df.head()
df_count = pd.DataFrame(ratings['ISBN'].value_counts())
df_count.shape
df_count.rename(columns={'ISBN':'count'},inplace=True)
df_count.index.name = "ISBN"
df_count.info()
df.rename(columns={'Book-Rating':'rating_avg'},inplace=True)
df
df_count
df_count = df_count.merge(df,on='ISBN')
df_count
df_count['count'].unique()
ratings.drop('User-ID',axis=1,inplace=True)
ratings.info()
ratings = ratings.merge(df_count,on='ISBN')
ratings.info()
R = ratings['rating_avg']
v = ratings['count']
C = ratings['rating_avg'].mean()
m = ratings['count'].quantile(0.70)
ratings['W'] = ((R*v)+(C*m))/(v+m)
ratings
books = books.merge(ratings,on='ISBN')
df_u = pd.DataFrame(ratings['ISBN'].unique())
df_u
books.drop_duplicates(subset='ISBN',keep='first',inplace=True)
books
books = books.sort_values('W',ascending=False)
sns.barplot(x=books['W'].head(10),y=books['Book-Title'].head(10),data = books)
plt.xlim(4,10)
plt.xlabel('Weighted score',weight='bold')
plt.ylabel('Book Name',weight = 'bold')
plt.title('TOP 10 POPULAR BOOKS',weight = 'bold')