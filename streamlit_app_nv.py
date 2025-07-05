# load libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Load Dataset
filename = ('https://media.githubusercontent.com/media/nvstudent-unt/adta5410-module4/refs/heads/main/data_clean.csv')
data1 = pd.read_csv(filename)
data = data1[['distance_to_airport_km', 'avg_daily_rate', 'loyalty_points', 'customer_tier', 'target_value']]

# Variables

# Numerical Variables
distance = data["distance_to_airport_km"]
roomrate = data["avg_daily_rate"]
points = data["loyalty_points"]

# Categorical Variables
loyalty_tier = data["customer_tier"]


# Target Variable
revenue = data["target_value"]

# Sidebar
# st.sidebar.header("Filter:")

# Sidebar Filters, Numerical
#distance_filter = st.sidebar.slider("Distance to Airport (KM)", distance.min(), distance.max())
#revenue_filter = st.sidebar.slider("Revenue")

# Title and Description 
st.title("Module 4")
st.write(" Interactive Application ")

# Introduction 
st.title("Introduction")
st.write(" The dataset used for this homework, as well as the final project, is the given Hospitality Data. All data cleaning steps were performed during the previous homework assignments, and are included in Appendix A. Only selected numerical and categorical variables are used from the original dataset. The following are the hypotheses:")

# Hypotheses
st.title("Hypotheses")
st.markdown("The variable distance_to_airport_km is negatively correlated to target_value. This implies that the farther the hotel is from the airport, the less revenue is realized. ")
st.markdown("Secondly, avg_daily_rate is positively correlated with target_value. This is thinking that the higher the price of the room, the more revenue it produces.")
st.markdown("And lastly, loyalty_points is positively correlated to target_value. Meaning, clients with high loyalty points produce more revenue since they accrued those points from spending. ")

# Data Exploration 
st.title("Data Exploration")

numeric_dropdown = data.select_dtypes(include=np.number).columns.tolist()
if numeric_dropdown:
    selected_cols = st.multiselect("Select numerical columns", numeric_dropdown, default=numeric_dropdown)

    if selected_cols:
            stats = data[selected_cols].describe().T
            stats["mode"] = data[selected_cols].mode().iloc[0]

            st.dataframe(stats)
    else:
            st.warning("Please select at least one column.")
else:
        st.error("No numerical columns found in the dataset.")

# Histogram
st.markdown("**Distribution Histogram**")
col_to_plot = st.selectbox("Select column for histogram", selected_cols)

fig, ax = plt.subplots()
sns.histplot(data[col_to_plot], kde=True, ax=ax)
st.pyplot(fig)

# Correlation heatmap
st.markdown("**Correlation Heatmap**")
corr = data[selected_cols].corr()

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
st.pyplot(fig2)

# Insights
st.header("Insights")
st.markdown("The first hypothesis does not hold since the relationship is positive; however, it should be noted that it is only positively correlated at 0.0025 which is very weak. In terms of the second hypothesis, the correlation heatmap supports the positive correlation between the room price and the revenue at 0.24 or 24%. Lastly, the third hypothesis is not supported since loyalty is negatively correlated with revenue. This might be the case since points can be used to book rooms, which lessens the revenue.")

# Recommendations
st.header("Recommendations")
st.markdown("The first recommendation is to prioritize room pricing. From the chosen variables, this can highly affect revenue. Further research should be done to optimize pricing strategies in terms of other possibly correlated variables. Secondly, in relation to distance to the airport, the hotels closer to the airport should consider this advantage despite the positive relationship between revenue and distance, since this correlation is very small. Lastly with loyalty points and revenue, hotels can run promotions where customers can buy points which they can use for reservations, which is still a positive revenue on the front end. Properties can also offer other services and amenities, so customers who only use points to book their stays can still be profitable by spending more on other things in the hotel.")
