import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

def main() :
    #Set page title
    st.set_page_config (page_title ='Diagnosa Skizofrenia')
    st.sidebar.title('Diagnosa Skizofrenia')

    G11_PERASAAN_KHAWATIR = st.sidebar.selectbox ('Perasaan Khawatir', ['Tidak', 'Ya'])
    if G11_PERASAAN_KHAWATIR =="Ya" :
        G11_PERASAAN_KHAWATIR = 1
    else:
        G11_PERASAAN_KHAWATIR = 0
    G17_MEMBERONTAK =st.sidebar.selectbox ('Memberontak', ['Tidak', 'Ya'])
    if G17_MEMBERONTAK =="Ya" :
        G17_MEMBERONTAK = 1
    else:
        G17_MEMBERONTAK = 0
    G19_TIDAK_BERAKTIFITAS = st.sidebar.selectbox('Tidak Beraktifitas', ['Tidak', 'Ya'])
    if G19_TIDAK_BERAKTIFITAS =="Ya" :
        G19_TIDAK_BERAKTIFITAS = 1
    else:
        G19_TIDAK_BERAKTIFITAS = 0
    
    input_data ={
        'G11_PERASAAN_KHAWATIR' : [G11_PERASAAN_KHAWATIR],
        'G17_MEMBERONTAK' : [G17_MEMBERONTAK],
        'G19_TIDAK_BERAKTIFITAS' : [G19_TIDAK_BERAKTIFITAS]
    }

    #create a dataframe from the input data 
    input_df = pd.DataFrame(input_data)

    #train the model 
    model = pickle.load (open('diagnosa.pkl', 'rb'))

    #make predictions 
    st.title('Prediksi Penyakit Skizofrenia')
    st.write ('Selamat Datang di Website kami')

    #display the predictions 
    st.title ("Hasil Klasifikasinya Adalah")
    if st.button ('Predict') :
        #make predictions 
        prediction = prediction = model.predict(input_df)[0]

        #display the prediction 
        if prediction == "Undifferentiated" :
            prediction = 3
        elif prediction == "Paranoid" :
            prediction = 0
        elif prediction == "Shizoaffective disorder, depressive type" :
            prediction = 2
        elif prediction == "Severe depressive episode with psychotic symptoms" :
            prediction = 1
    
    if __name__ == '__main__':
        main()
        


    
                                           