import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import seaborn as sns


st.title('My first app')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

tips = sns.load_dataset("tips")

line = sns.scatterplot(data=tips, x="total_bill", y="tip")

#line = sns.scatterplot(data=df, x='first column', y='second column')
st.pyplot(line.figure)

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
df.loc[df['first column'] == option]
