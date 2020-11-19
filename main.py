import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

df = pd.read_csv('data/heart.csv')

X = df.drop(['target'], axis=1)
y = df['target']

clf = LogisticRegression(random_state=0, max_iter=1000)

rfe = RFE(clf, n_features_to_select=1)
rfe = rfe.fit(X, y)

rf_df = pd.DataFrame(rfe.ranking_, index=X.columns, columns=['Rank']).sort_values(by='Rank', ascending=True)
print(rf_df)
