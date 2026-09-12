import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv('Amazon Sale Report-selected-columns.csv')

# Apply all fixes
df.drop_duplicates(inplace=True)
df['Date'] = df['Date'].apply(lambda x: x[:-2] + '20' + x[-2:] if len(x) == 8 else x)
df['Date'] = pd.to_datetime(df['Date'])
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype('category')
df.rename(columns={
    'Order ID': 'order_id', 'Date': 'date', 'Status': 'status',
    'Fulfilment': 'fulfilment', 'Sales Channel': 'sales_channel',
    'ship-service-level': 'ship_service_level', 'Category': 'category',
    'Size': 'size', 'Courier Status': 'courier_status'
}, inplace=True)

st.title('Amazon Sales Dashboard')

# Chart 1: Orders by Category
st.subheader('1. Orders by Category')
fig, ax = plt.subplots()
df['category'].value_counts().plot(kind='bar', ax=ax, color='steelblue')
ax.set_xlabel('Category')
ax.set_ylabel('Number of Orders')
st.pyplot(fig)
st.write('**Insight:** T-shirts and Shirts dominate sales — the business should prioritize stock for these categories.')

# Chart 2: Order Status Distribution
st.subheader('2. Order Status Distribution')
fig, ax = plt.subplots()
df['status'].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')
ax.set_ylabel('')
st.pyplot(fig)
st.write('**Insight:** A significant portion of orders are cancelled — investigating cancellation reasons could improve revenue.')

# Chart 3: Fulfilment Method
st.subheader('3. Fulfilment Method')
fig, ax = plt.subplots()
df['fulfilment'].value_counts().plot(kind='bar', ax=ax, color='coral')
ax.set_xlabel('Fulfilment Method')
ax.set_ylabel('Number of Orders')
st.pyplot(fig)
st.write('**Insight:** Amazon fulfilment dominates — merchants rely heavily on Amazon logistics.')

# Chart 4: Orders Over Time
st.subheader('4. Orders Over Time')
fig, ax = plt.subplots()
df.groupby('date')['order_id'].count().plot(kind='line', ax=ax, color='green')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Orders')
st.pyplot(fig)
st.write('**Insight:** Order volume fluctuates over time — identifying peak periods can help with inventory planning.')

# Chart 5: Ship Service Level
st.subheader('5. Ship Service Level')
fig, ax = plt.subplots()
df['ship_service_level'].value_counts().plot(kind='bar', ax=ax, color='purple')
ax.set_xlabel('Service Level')
ax.set_ylabel('Number of Orders')
st.pyplot(fig)
st.write('**Insight:** Most orders use Expedited shipping — customers prefer faster delivery.')