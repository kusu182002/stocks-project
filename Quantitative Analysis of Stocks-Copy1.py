#!/usr/bin/env python
# coding: utf-8

# 
# # Project Title : Qunatitative Analysis of Stocks
# 
# 

# # Purpose
#   Quantitative analysis can assess the risk associated with investing in a particular stock by analyzing factors such as volatility and historical performance based on factors such as correlation, and expected return.
# 
#   This helps investors understand the potential downside and volatility of a stock.Quantitative analysis can be used to identify market trends and signals for buying or selling stocks. 

# #                               Importing required libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# # Reading data from csv file

# In[2]:


#importing the data using pandas
data=pd.read_csv('D:\\New folder\\stocks.csv',delimiter=',')
#printing the imported data
print(data)



# The dataset contains the following columns for stock market data:
# 
# - Ticker: The stock ticker symbol.
# - Date: The trading date.
# - Open: The opening price of the stock for the day.
# - High: The highest price of the stock during the day.
# - Low: The lowest price of the stock during the day.
# - Close: The closing price of the stock for the day.
# - Adj Close: The adjusted closing price, which accounts for all corporate actions such as dividends, stock splits, etc.
# - Volume: The number of shares traded during the day.

# ### Printing first and last five records of data.

# In[3]:


#getting first five records
print(data.head())
#getting last five records
print(data.tail())


# ### Getting count of unique values.

# In[4]:


data.nunique()


# Above data indicates how many unique values do each column is having.

# # Shape
# 

# In[5]:


data.shape


# (248, 8) indicates our data consisting of 248 rows and 8 columns.

# # Getting information about data

# In[6]:


#getting information of data
print(data.info())


# From above data we can say that some of the columns like Ticker are string data and some like open are float type and volume is int data type.

# # Statistical information of data

# In[7]:


#getting statistical information of data
descriptive_data = data.describe()
print(descriptive_data)


# From above data we are getting statistical information like mean, standard deviation, minimum,maximum values.

# ### Checking for missing values.

# In[8]:


# check for missing values
data.isnull().sum()


# from above data we can say that our data is not having any null values.

# # Processing data and cleaning the data

# In[9]:


#removing duplicates
clean_data=data.drop_duplicates()
print(clean_data)


# # Descriptive Statistics for each stock by grouping

# In[10]:


# Descriptive Statistics for each stock with opening stock price
descriptive_stats = clean_data.groupby('Ticker')['Open'].describe()

print(descriptive_stats)


# # Time Series Analysis

# In[11]:


# Time Series Analysis
clean_data['Date'] = pd.to_datetime(clean_data['Date'])
pivot_data = clean_data.pivot(index='Date', columns='Ticker', values='Open')

# Create a subplot
fig = make_subplots(rows=1, cols=1)

# Add traces for each stock ticker
for column in pivot_data.columns:
    fig.add_trace(
        go.Scatter(x=pivot_data.index, y=pivot_data[column], name=column),
        row=1, col=1
    )

# Update layout
fig.update_layout(
    title_text='Time Series of opening Prices',
    xaxis_title='Date',
    yaxis_title='Opening Price',
    legend_title='Ticker',
    showlegend=True
)

# Show the plot
fig.show()


# - The above plot displays the time series of the opening prices for each stock (AAPL, GOOG, MSFT, NFLX) over the observed period. 

# In[12]:


# Time Series Analysis
clean_data['Date'] = pd.to_datetime(clean_data['Date'])
pivot_data = clean_data.pivot(index='Date', columns='Ticker', values='Close')

# Create a subplot
fig = make_subplots(rows=1, cols=1)

# Add traces for each stock ticker
for column in pivot_data.columns:
    fig.add_trace(
        go.Scatter(x=pivot_data.index, y=pivot_data[column], name=column),
        row=1, col=1
    )

# Update layout
fig.update_layout(
    title_text='Time Series of Closing Prices',
    xaxis_title='Date',
    yaxis_title='Closing Price',
    legend_title='Ticker',
    showlegend=True
)

# Show the plot
fig.show()


# The above plot displays the time series of the closing prices for each stock (AAPL, GOOG, MSFT, NFLX) over the observed period. Here are some key observations:
# 
# - Trend: Each stock shows its unique trend over time. For instance, AAPL and MSFT exhibit a general upward trend in this period.
# - Volatility: There is noticeable volatility in the stock prices. For example, NFLX shows more pronounced fluctuations compared to others.
# - Comparative Performance: When comparing the stocks, MSFT and NFLX generally trade at higher price levels than AAPL and GOOG in this dataset.
#  
#  By observing above two graphs we can say that the opening stock price changes and closing stock price changes over time are almost same.

# # Volatality Analysis

# In[13]:


# Volatility Analysis
volatility = pivot_data.std().sort_values(ascending=False)

fig = px.bar(volatility,
             x=volatility.index,
             y=volatility.values,
             labels={'y': 'Standard Deviation', 'x': 'Ticker'},
             title='Volatility of Closing Prices (Standard Deviation)')

# Show the figure
fig.show()


# The bar chart and the accompanying data show the volatility (measured as standard deviation) of the closing prices for each stock. Here’s how they rank in terms of volatility:
# 
# - NFLX: Highest volatility with a standard deviation of approximately 18.55.
# - MSFT: Next highest, with a standard deviation of around 17.68.
# - AAPL: Lower volatility compared to NFLX and MSFT, with a standard deviation of about 7.36.
# - GOOG: The least volatile in this set, with a standard deviation of approximately 6.28.
#   
#   It indicates that NFLX and MSFT stocks were more prone to price fluctuations during this period compared to AAPL and GOOG.

# # Correlation Analysis
# Next, we’ll perform a Correlation Analysis to understand how the stock prices of these companies are related to each other:

# In[16]:


#getting correlation values
correlation_matrix = pivot_data.corr()
print(correlation_matrix)


# In[19]:


# Correlation Analysis
correlation_matrix = pivot_data.corr()

fig = go.Figure(data=go.Heatmap(
                    z=correlation_matrix,
                    x=correlation_matrix.columns,
                    y=correlation_matrix.columns,
                    colorscale='blues',
                    colorbar=dict(title='Correlation'),
                    ))

# Update layout
fig.update_layout(
    title='Correlation Matrix of Closing Prices',
    xaxis_title='Ticker',
    yaxis_title='Ticker'
)

# Show the figure
fig.show()


# The heatmap above displays the correlation matrix of the closing prices of the four stocks (AAPL, GOOG, MSFT, NFLX). Here’s what the correlation coefficients suggest:
# - Values close to +1 indicate a strong positive correlation, meaning that as one stock’s price increases, the other tends to increase as well.
# - Values close to -1 indicate a strong negative correlation, where one stock’s price increase corresponds to a decrease in the other.
# - Values around 0 indicate a lack of correlation.
# 
# From the heatmap, we can observe that there are varying degrees of positive correlations between the stock prices, with some pairs showing stronger correlations than others. For instance, AAPL and MSFT seem to have a relatively higher positive correlation.
# 
# 

# # Comparative Analysis
# Now, let’s move on to Comparative Analysis. In this step, we’ll compare the performance of different stocks based on their returns over the period. We’ll calculate the percentage change in closing prices from the start to the end of the period for each stock:

# In[17]:


# Calculating the percentage change in closing prices
percentage_change = ((pivot_data.iloc[-1] - pivot_data.iloc[0]) / pivot_data.iloc[0]) * 100
print(percentage_change)
fig = px.bar(percentage_change,
             x=percentage_change.index,
             y=percentage_change.values,
             labels={'y': 'Percentage Change (%)', 'x': 'Ticker'},
             title='Percentage Change in Closing Prices')

# Show the plot
fig.show()


# The bar chart and the accompanying data show the percentage change in the closing prices of the stocks from the start to the end of the observed period:
# 
# - GOOG: The highest positive change of approximately 16.25%.
# - MSFT: Showed a positive change of approximately 15.11%.
# - AAPL: Showed a positive change of approximately 10.17%.
# - NFLX: Showed a positive change of approximately 5.59%

# # Daily Risk Vs. Return Analysis
# To perform a Risk vs. Return Analysis, we will calculate the average daily return and the standard deviation of daily returns for each stock. The standard deviation will serve as a proxy for risk, while the average daily return represents the expected return.
# 
# We will then plot these values to visually assess the risk-return profile of each stock. Stocks with higher average returns and lower risk (standard deviation) are generally more desirable, but investment decisions often depend on the investor’s risk tolerance:

# In[18]:


daily_returns = pivot_data.pct_change()

# Recalculating average daily return and standard deviation (risk)
avg_daily_return = daily_returns.mean()
risk = daily_returns.std()

# Creating a DataFrame for plotting
risk_return_df = pd.DataFrame({'Risk': risk, 'Average Daily Return': avg_daily_return})

fig = go.Figure()

# Add scatter plot points
fig.add_trace(go.Scatter(
    x=risk_return_df['Risk'],
    y=risk_return_df['Average Daily Return'],
    mode='markers+text',
    text=risk_return_df.index,
    textposition="top center",
    marker=dict(size=10)
))

# Update layout
fig.update_layout(
    title='Risk vs. Return Analysis',
    xaxis_title='Risk (Standard Deviation)',
    yaxis_title='Average Daily Return',
    showlegend=False
)

# Show the plot
fig.show()


# ## Conclusion
# So, AAPL shows the lowest risk combined with a low average daily return, suggesting a better stable investment with consistent returns. GOOG has higher volatility than AAPL and, on average, more daily return, but having more risk indicating a riskier and a little rewarding investment during this period.
# 
# MSFT shows more risk with the highest average daily return, suggesting a not more rewarding investment. NFLX exhibits the highest risk and a low average daily return, indicating it was the most volatile and least rewarding investment among these stocks over the analyzed period.

# In[ ]:




