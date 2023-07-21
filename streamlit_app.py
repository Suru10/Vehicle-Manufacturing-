#import libraries
import streamlit as st
import pandas as pd
import warnings
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
# Team 1 -> Kevin, Ebenzer, Top
# Team 2 -> Kairos, Harvey, Bottom
df = pd.read_csv("Car Data.csv")
#INFO:
st.title("Whimsical Watermelons")
st.write("Kevin Morante: Lives in Burnaby Area, age 16")
st.write("Ebenezer Alemayehu: Lives in Bay Area, age 17")
st.write('Kairos Torsina: Lives in Arizona, age 14')
st.write('Harvey Fong: lives in bay area, age 14')
#TITLE:
st.title("Synthetic Car Dataset: Brands, Models, Years, Prices, and Locations")
st.header("Introduction")
st.write(
  "This data set contains essential information regarding car manufacturing in the United States. It illustrates important aspects of the vehicle manufacturing industry such as Car ID, Brand, Model, Year, Color, Mileage, Price, and Location. Our main objective is to evaluate and represent graphically the relation between these aspects in order to reach a logical conclusion and answer our initial questions/hypothesis."
)
# code for inspection:
# head
st.markdown("---")

st.header("Inspection")
st.write("Head")
st.table(df.head())
# tail
st.write("Tail")
st.table(df.tail())
#shape
st.write("Shape")
st.write(df.shape)
#describe
st.write("Basic Statistics")
st.table(df.describe())
#info
# df.info()
#columns
st.write("Columns")
st.write(df.columns)
#Line
st.markdown("---")
# code
print(df.isna().sum())
#no null values
# Clean the data -> Leon
numnull = df.isna().sum()
dropped_columns = ['Car ID']
vehicles_dataframe = df.drop(dropped_columns, axis=1, inplace=False)
vehicles_dataframe.describe()

st.header("Cleaning the data")
st.write("Number of null rows: ")
st.write(numnull)
st.write(
  "The data cleaning process involved finding null values and deleting them in order to organize and represent information more easily; however, no null values were found in this data, so we decided to only delete the Car ID column due to its irrelevance in the investigation we are carrying out."
)
st.write("Post-processing Head")
st.table(vehicles_dataframe.head())
st.write("Post-processing Tail")
st.table(vehicles_dataframe.tail())
st.write("Post-processing Shape")
st.write(vehicles_dataframe.shape)
st.write("Post-processing Columns")
st.write(vehicles_dataframe.columns)
st.write("Post-processing Basic Statistics")
st.table(vehicles_dataframe.describe())
#Line2
st.markdown("---")
# Visualizations!!

# team 1 -> Kevin, Ebenezer -> 4 hypothesis
# team 2 -> Kairos, Harvey -> 3 hypothesis

#BOTTOM PART
st.header(
  "Hypothesis 1: How’s the brand of the car related to the price of the vehicle?"
)
fig1 = px.bar(df, x="Brand", y="Price", color="Year")
fig1.update_layout(title_text="Relation between brand and price",
                   xaxis_title="Brand",
                   yaxis_title="Price")
st.plotly_chart(fig1, use_container_width=True)
st.write(
  "According to the bar graph generated, the brand of the car is strongly related to the price of the vehicle. This is evident in the fact that Toyota is the car brand with the highest prices ($27K aprox each/$300K aprox in total) and both Honda and Ford are the ones with the lowest prices ($22K aprox each/$260K aprox in total). The prices of Chevrolet and Hyundai vehicles are between these two values. "
)
st.markdown("---")
st.header(
  "Hypothesis 2: Is there a relation between models and the year of production?"
)
fig2 = px.scatter(df, x="Model", y="Year", color="Location")
fig2.update_layout(title_text="Relation between model and year of production", xaxis_title="Model",yaxis_title="Year")
st.plotly_chart(fig2, use_container_width=True)
st.write(
  "According to the scatter graph generated, each type of model was produced in a time span of 1-2 years, then stopped, then produced again after 1-3 years. There is no evidence that a car model was produced in a specific year or period of time, but each one was developed at various points without relation or pattern. This illustrates that there is no relation between the model of the car and the year of production. "
)
st.markdown("---")

st.title('Hypothesis 3:Does the brand affect the location of distribution?')
st.subheader('Brand Vs. Location')
fig3 = px.scatter(df, x="Brand", y="Location")
fig3.update_layout(title_text="Relation Between Brand and Location of Distribution",
                    xaxis_title="Brand",
                    yaxis_title='Location')
st.plotly_chart(fig3, use_container_width=True)
st.write(
  'The brand seems to have a weak relation to the locatoin of manufacturing, because each brand is manufactured in only 2 cities.'
)
st.divider()

st.title(
  "Hypothesis 4: What’s the connection between the model of the car and the mileage?"
)
st.subheader("Model Vs location")
fig = px.histogram(df, x="Model", y="Mileage", color="Location")
st.plotly_chart
st.write(
  "The scatter graph generated reflects that the Fusion car model is the one with the highest mileage (50K miles aprox each/150K miles aprox in total) while the Kona, Spark, and Camaro car models are the ones with the lowest mileage (35K miles in total). The other models are between both values. This illustrates a relation between car model and mileage"
)
st.divider()

st.title(
  "Hypothesis 5, Does the year of the car's manufacture date relate to its price?"
)
st.subheader("Year Vs Price")
fig5 = px.bar(df, x="Year", y="Price")
fig5.update_layout(title_text="Relation Between Year and Price",
                    xaxis_title='Year',
                    yaxis_title='Price')
st.plotly_chart(fig5, use_container_width=True)
st.write(
  "According to the bar graph shown, the car pirce seems to increase during the year so this proves the hypothesis to be true, that the year and the price of cars are related"
)
st.divider()

st.title("Hypothesis 6, Does the price relate to the mileage?")
st.subheader("Price VS Mileage")
sns.set_theme()
sns.lineplot(data=df, x='Price', y='Mileage')
st.write(
  "According to the line plot, the cars at the cheapest price seem to have above average mileage. Meanwhile, the pricier cars have below average mileage, and the most expensive cars tend to have a low mileage. Therefore, it seems that there is a loose relationship between price and mileage. However, it doesn't mean that all cheap cars are better than the more expensive ones."
)

st.divider()
st.title('Conclusion')
st.write(
  'There are many types of models and brands of cars, and each of them have certain characteristics. For example, the largely known brand Toyota has the highest price rate compared to any of the other brands listed in the dataset, while Honda and Ford have the lowest. A relation found in the dataset is the relation between models and years of production.  Car models were produced for 1-2 years before the brand stopped producing them. Furthermore, one brand has only 2 manufacturers, making each model unique. Adding on to that, each model has a mileage different from others. But as the prices go higher per year, as proven in hypothesis 5, the less mileage the car usually has.'
)
