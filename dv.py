import pandas as pd
import plotly.express as px
cr=pd.read_csv("coviddata.csv")
figure=px.scatter(cr,x="date",y="cases",color="country",title="Covid cases in different countries")
figure.show()