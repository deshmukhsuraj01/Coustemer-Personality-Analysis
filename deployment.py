import streamlit as st
import pandas as pd
from pickle import load

def create_page():
    st.title('Customer segmentation')
    st.write('Cluster')
    Age = st.sidebar.slider('Choose your age', min_value=19, max_value=75)
    Education = st.sidebar.radio('Education', [0,1,2,3,4])
    st.sidebar.write('0 : 2n Cycle, 1 : Basic, 2 : Graduation, 3 : Master, 4 : PhD')
    Rship_status = st.sidebar.radio('Relationship Status', [0, 1])
    st.sidebar.write('0 : Single, 1 : Taken')
    Children = st.sidebar.radio('Children', [0,1,2,3])
    Income = st.sidebar.slider('Income', min_value=1730, max_value=162397)
    Spent = st.sidebar.slider('Spent', min_value=5, max_value=2525)
    MntWines = st.sidebar.slider('Wines', min_value=0, max_value=1493, step=1)
    MntFruits = st.sidebar.slider('Fruits', min_value=0, max_value=199, step=1)
    MntMeatProducts = st.sidebar.slider('Meat Products', min_value=0, max_value=1725, step=1)
    MntFishProducts = st.sidebar.slider('Fish Products', min_value=0, max_value=259, step=1)
    MntSweetProducts = st.sidebar.slider('Sweet Products', min_value=0, max_value=262, step=1)
    MntGoldProds = st.sidebar.slider('MntGoldProds', min_value=0, max_value=321, step=1)
    NumDealsPurchases = st.sidebar.slider('NumDealsPurchases', min_value=0, max_value=15, step=1)
    NumWebPurchases = st.sidebar.slider('NumWebPurchases', min_value=0, max_value=27, step=1)
    NumCatalogPurchases = st.sidebar.slider('NumCatalogPurchases', min_value=0, max_value=28, step=1)
    NumStorePurchases = st.sidebar.slider('NumStorePurchases', min_value=0, max_value=13, step=1)
    NumWebVisitsMonth = st.sidebar.slider('NumWebVisitsMonth', min_value=0, max_value=20, step=1)
    AcceptedCmp1 = st.sidebar.radio('AcceptedCmp1', [0, 1])
    AcceptedCmp2 = st.sidebar.radio('AcceptedCmp2', [0, 1])
    AcceptedCmp3 = st.sidebar.radio('AcceptedCmp3', [0, 1])
    AcceptedCmp4 = st.sidebar.radio('AcceptedCmp4', [0, 1])
    AcceptedCmp5 = st.sidebar.radio('AcceptedCmp5', [0, 1])
    

    df = {'Education': Education,'Income': Income,'MntWines': MntWines,'MntFruits': MntFruits, 'MntMeatProducts': MntMeatProducts,
          'MntFishProducts': MntFishProducts,'MntSweetProducts': MntSweetProducts, 'MntGoldProds': MntGoldProds, 'NumDealsPurchases': NumDealsPurchases, 'NumWebPurchases': NumWebPurchases, 'NumCatalogPurchases': NumCatalogPurchases, 'NumStorePurchases': NumStorePurchases, 'NumWebVisitsMonth': NumWebVisitsMonth, 'AcceptedCmp3': AcceptedCmp3, 'AcceptedCmp4': AcceptedCmp4, 'AcceptedCmp5': AcceptedCmp5, 'AcceptedCmp1': AcceptedCmp1, 'AcceptedCmp2': AcceptedCmp2, 'Age': Age, 'Rship_status': Rship_status, 'Spent': Spent, 'Children': Children}
    

    df = pd.DataFrame(df, index=[0])
    return df

features = create_page()

# Load the model outside the button click event
loaded_model = load(open('segmentation.pkl', 'rb'))

if st.sidebar.button('Submit'):
    st.write(features)
    # Use the loaded model to predict
    cluster_label = loaded_model.predict(features)
    st.write(f'Belongs to cluster {cluster_label[0]}')
    st.write(cluster_label)
