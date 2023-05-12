from google.cloud import bigquery
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

query = """
        SELECT 
          museum,
          visitors,
          city_population 
        FROM `GCP_PROJECT_NAME.BQ_DATABASE_NAME..museums`
        """

client = bigquery.Client()
df = client.query(query).to_dataframe()

x_axis = df["visitors"].values.reshape(-1, 1)
y_axis = df["city_population"].values.reshape(-1, 1)

linear_regressor = LinearRegression()
linear_regressor.fit(x_axis, y_axis)
prediction = linear_regressor.predict(x_axis)

f = plt.figure()
plt.scatter(x_axis, y_axis)
plt.plot(x_axis, prediction, color='red')
f.savefig("regression.pdf", bbox_inches='tight')
