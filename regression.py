import statsmodels.api as sm
import pandas as pd

df = pd.read_csv('./data/trade_apt_api.csv')

print(df.head())
print(df.info())

y = df['거래금액']
x = df[['건축년도', '전용면적', '층']]

x = sm.add_constant(x)
print(x.shape)
print(x.head())

model = sm.OLS(y, x).fit()

print(model.summary())
print(model.predict([[1, 2010, 80, 10]]))

import joblib
joblib.dump(model, './model/apt_price.pkl')

load_model = joblib.load('./model/apt_price.pkl')
print(load_model.predict([[1, 2010, 80, 10]]))
