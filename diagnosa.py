import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

def main() :
    #Set page title
    st.set_page_config (page_title ='Diagnosa Skizofrenia')
    st.sidebar.title('Diagnosa Skizofrenia')

    G1_PEMBULIAN = st.sidebar.selectbox('Pembulian', ['Tidak', 'Ya'])
    G1_PEMBULIAN = 1 if G1_PEMBULIAN == "Ya" else 0

    G3_FRUSTASI_SULIT_KERJA = st.sidebar.selectbox('Frustasi Sulit Kerja', ['Tidak', 'Ya'])
    G3_FRUSTASI_SULIT_KERJA = 1 if G3_FRUSTASI_SULIT_KERJA == "Ya" else 0

    G4_PERASAAN_KECEWA = st.sidebar.selectbox('Perasaan Kecewa', ['Tidak', 'Ya'])
    G4_PERASAAN_KECEWA = 1 if G4_PERASAAN_KECEWA == "Ya" else 0

    G11_PERASAAN_KHAWATIR = st.sidebar.selectbox ('Perasaan Khawatir', ['Tidak', 'Ya'])
    if G11_PERASAAN_KHAWATIR =="Ya" :
        G11_PERASAAN_KHAWATIR = 1
    else:
        G11_PERASAAN_KHAWATIR = 0

    G15_KELUYURAN = st.sidebar.selectbox('Suka Keluyuran', ['Tidak', 'Ya'])
    G15_KELUYURAN = 1 if G15_KELUYURAN == "Ya" else 0

    G16_MERUSAK_BARANG_MEMECAH = st.sidebar.selectbox('Merusak Barang dengan Memecah', ['Tidak', 'Ya'])
    G16_MERUSAK_BARANG_MEMECAH = 1 if G16_MERUSAK_BARANG_MEMECAH == "Ya" else 0

    G17_MEMBERONTAK =st.sidebar.selectbox ('Memberontak', ['Tidak', 'Ya'])
    if G17_MEMBERONTAK =="Ya" :
        G17_MEMBERONTAK = 1
    else:
        G17_MEMBERONTAK = 0

    G18_MARAHMARAH = st.sidebar.selectbox('Marah-marah', ['Tidak', 'Ya'])
    G18_MARAHMARAH = 1 if G18_MARAHMARAH == "Ya" else 0

    G19_TIDAK_BERAKTIFITAS = st.sidebar.selectbox('Tidak Beraktifitas', ['Tidak', 'Ya'])
    if G19_TIDAK_BERAKTIFITAS =="Ya" :
        G19_TIDAK_BERAKTIFITAS = 1
    else:
        G19_TIDAK_BERAKTIFITAS = 0

    G20_SEDIH_MENANGIS = st.sidebar.selectbox('Sedih Menangis', ['Tidak', 'Ya'])
    if G20_SEDIH_MENANGIS == "Ya":
        G20_SEDIH_MENANGIS = 1
    else:
        G20_SEDIH_MENANGIS = 0

    G21_SEDIKIT_BICARA = st.sidebar.selectbox('Sedikit Bicara', ['Tidak', 'Ya'])
    if G21_SEDIKIT_BICARA == "Ya":
        G21_SEDIKIT_BICARA = 1
    else:
        G21_SEDIKIT_BICARA = 0

    G23_TERGANGGU = st.sidebar.selectbox('Terganggu', ['Tidak', 'Ya'])
    if G23_TERGANGGU == "Ya":
        G23_TERGANGGU = 1
    else:
        G23_TERGANGGU = 0

    G25_MELAMUN = st.sidebar.selectbox('Melamun', ['Tidak', 'Ya'])
    G25_MELAMUN = 1 if G25_MELAMUN == "Ya" else 0

    G26_MEMUKUL_ORANGLAIN = st.sidebar.selectbox('Memukul Orang Lain', ['Tidak', 'Ya'])
    G26_MEMUKUL_ORANGLAIN = 1 if G26_MEMUKUL_ORANGLAIN == "Ya" else 0

    G28_MELAKUKAN_TERIAK = st.sidebar.selectbox('Melakukan Teriak', ['Tidak', 'Ya'])
    G28_MELAKUKAN_TERIAK = 1 if G28_MELAKUKAN_TERIAK == "Ya" else 0

    G30_PUTUSASA = st.sidebar.selectbox('Putus Asa', ['Tidak', 'Ya'])
    G30_PUTUSASA = 1 if G30_PUTUSASA == "Ya" else 0

    G31_CEMAS = st.sidebar.selectbox('Cemas', ['Tidak', 'Ya'])
    G31_CEMAS = 1 if G31_CEMAS == "Ya" else 0

    G35_MENGURUNG = st.sidebar.selectbox('Mengurung Diri', ['Tidak', 'Ya'])
    G35_MENGURUNG = 1 if G35_MENGURUNG == "Ya" else 0

    G36_MONDAR_MANDIR = st.sidebar.selectbox('Mondar Mandir', ['Tidak', 'Ya'])
    G36_MONDAR_MANDIR = 1 if G36_MONDAR_MANDIR == "Ya" else 0

    G37_KEINGINAN_KERJA_KULIAH = st.sidebar.selectbox('Keinginan Kerja Kuliah', ['Tidak', 'Ya'])
    G37_KEINGINAN_KERJA_KULIAH = 1 if G37_KEINGINAN_KERJA_KULIAH == "Ya" else 0

    G38_MELUKAI_DIRISENDIRI = st.sidebar.selectbox('Melukai Diri Sendiri', ['Tidak', 'Ya'])
    G38_MELUKAI_DIRISENDIRI = 1 if G38_MELUKAI_DIRISENDIRI == "Ya" else 0

    G43_KEINGINAN_BUNUH_DIRI = st.sidebar.selectbox('Keinginan Bunuh Diri', ['Tidak', 'Ya'])
    G43_KEINGINAN_BUNUH_DIRI = 1 if G43_KEINGINAN_BUNUH_DIRI == "Ya" else 0

    G44_PERCOBAAN_BUNDIR = st.sidebar.selectbox('Percobaan Bunuh Diri', ['Tidak', 'Ya'])
    G44_PERCOBAAN_BUNDIR = 1 if G44_PERCOBAAN_BUNDIR == "Ya" else 0

    G45_BERBICARA_SENDIRI = st.sidebar.selectbox('Berbicara Sendiri', ['Tidak', 'Ya'])
    G45_BERBICARA_SENDIRI = 1 if G45_BERBICARA_SENDIRI == "Ya" else 0

    G46_TERTAWA_SENDIRI = st.sidebar.selectbox('Tertawa Sendiri', ['Tidak', 'Ya'])
    G46_TERTAWA_SENDIRI = 1 if G46_TERTAWA_SENDIRI == "Ya" else 0

    G47_SULIT_MAKAN = st.sidebar.selectbox('Sulit Makan', ['Tidak', 'Ya'])
    G47_SULIT_MAKAN = 1 if G47_SULIT_MAKAN == "Ya" else 0

    G48_TIDAK_BERSOSIALISASI = st.sidebar.selectbox('Tidak Bersosialisasi', ['Tidak', 'Ya'])
    G48_TIDAK_BERSOSIALISASI = 1 if G48_TIDAK_BERSOSIALISASI == "Ya" else 0

    G49_KEPIKIRAN_SESUATU = st.sidebar.selectbox('Kepikiran Sesuatu', ['Tidak', 'Ya'])
    G49_KEPIKIRAN_SESUATU = 1 if G49_KEPIKIRAN_SESUATU == "Ya" else 0

    G50_DIAM_SAAT_PEMERIKSAAN = st.sidebar.selectbox('Diam Saat Pemeriksaan', ['Tidak', 'Ya'])
    G50_DIAM_SAAT_PEMERIKSAAN = 1 if G50_DIAM_SAAT_PEMERIKSAAN == "Ya" else 0

    G51_PIKIRAN_KACAU = st.sidebar.selectbox('Pikiran Kacau', ['Tidak', 'Ya'])
    G51_PIKIRAN_KACAU = 1 if G51_PIKIRAN_KACAU == "Ya" else 0

    G52_TIDAK_BERSEMANGAT = st.sidebar.selectbox('Tidak Bersemangat', ['Tidak', 'Ya'])
    G52_TIDAK_BERSEMANGAT = 1 if G52_TIDAK_BERSEMANGAT == "Ya" else 0

    G53_PERASAAN_BINGUNG = st.sidebar.selectbox('Perasaan Bingung', ['Tidak', 'Ya'])
    G53_PERASAAN_BINGUNG = 1 if G53_PERASAAN_BINGUNG == "Ya" else 0

    G55_MENGALAMI_PERMASALAHAN_SEBELUMNYA = st.sidebar.selectbox('Masalah Sebelumnya', ['Tidak', 'Ya'])
    G55_MENGALAMI_PERMASALAHAN_SEBELUMNYA = 1 if G55_MENGALAMI_PERMASALAHAN_SEBELUMNYA == "Ya" else 0

    G56_MENGALAMI_PERSELISIHAN = st.sidebar.selectbox('Mengalami Perselisihan', ['Tidak', 'Ya'])
    G56_MENGALAMI_PERSELISIHAN = 1 if G56_MENGALAMI_PERSELISIHAN == "Ya" else 0

    G57_PERASAANLELAH = st.sidebar.selectbox('Perasaan Lelah', ['Tidak', 'Ya'])
    G57_PERASAANLELAH = 1 if G57_PERASAANLELAH == "Ya" else 0

    G59_KETAKUTAN = st.sidebar.selectbox('Ketakutan', ['Tidak', 'Ya'])
    G59_KETAKUTAN = 1 if G59_KETAKUTAN == "Ya" else 0

    G61_BICARAKACAU__MELANTUR = st.sidebar.selectbox('Bicara Kacau/Melantur', ['Tidak', 'Ya'])
    G61_BICARAKACAU__MELANTUR = 1 if G61_BICARAKACAU__MELANTUR == "Ya" else 0

    G62_KELUAR_RUMAH = st.sidebar.selectbox('Keluar Rumah', ['Tidak', 'Ya'])
    G62_KELUAR_RUMAH = 1 if G62_KELUAR_RUMAH == "Ya" else 0

    G63_HALUSINASI_VISUAL = st.sidebar.selectbox('Halusinasi Visual', ['Tidak', 'Ya'])
    G63_HALUSINASI_VISUAL = 1 if G63_HALUSINASI_VISUAL == "Ya" else 0

    G65_HALUSINASI_DIANCAM = st.sidebar.selectbox('Halusinasi Diancam', ['Tidak', 'Ya'])
    G65_HALUSINASI_DIANCAM = 1 if G65_HALUSINASI_DIANCAM == "Ya" else 0

    G66_HALUSINASI_AUDITORIK_MENDENGAR_SESUATU = st.sidebar.selectbox('Halusinasi Auditorik/Mendengar Sesuatu', ['Tidak', 'Ya'])
    G66_HALUSINASI_AUDITORIK_MENDENGAR_SESUATU = 1 if G66_HALUSINASI_AUDITORIK_MENDENGAR_SESUATU == "Ya" else 0

    G71_DIAWASI = st.sidebar.selectbox('Diawasi', ['Tidak', 'Ya'])
    G71_DIAWASI = 1 if G71_DIAWASI == "Ya" else 0

    G72_PERASAAN_KESAL = st.sidebar.selectbox('Perasaan Kesal', ['Tidak', 'Ya'])
    G72_PERASAAN_KESAL = 1 if G72_PERASAAN_KESAL == "Ya" else 0

    G73_KETAKUTAN_DIIKUTI_HALGHAIB = st.sidebar.selectbox('Ketakutan Diiikuti Halghaib', ['Tidak', 'Ya'])
    G73_KETAKUTAN_DIIKUTI_HALGHAIB = 1 if G73_KETAKUTAN_DIIKUTI_HALGHAIB == "Ya" else 0

    G74_WAHAM_REFERENSI_MERASA_DIBICARAKAN = st.sidebar.selectbox('Merasa Dibicarakan', ['Tidak', 'Ya'])
    G74_WAHAM_REFERENSI_MERASA_DIBICARAKAN = 1 if G74_WAHAM_REFERENSI_MERASA_DIBICARAKAN == "Ya" else 0

    G75_WAHAM_BERSALAH = st.sidebar.selectbox('Waham Bersalah', ['Tidak', 'Ya'])
    G75_WAHAM_BERSALAH = 1 if G75_WAHAM_BERSALAH == "Ya" else 0

    G76_WAHAM_PERSEKUTORIK_MERASA_DIJAHATI = st.sidebar.selectbox('Merasa Dijahati', ['Tidak', 'Ya'])
    G76_WAHAM_PERSEKUTORIK_MERASA_DIJAHATI = 1 if G76_WAHAM_PERSEKUTORIK_MERASA_DIJAHATI == "Ya" else 0

    G78_WAHAM_KEBESARAN = st.sidebar.selectbox('Waham Besar', ['Tidak', 'Ya'])
    G78_WAHAM_KEBESARAN = 1 if G78_WAHAM_KEBESARAN == "Ya" else 0

    G80_WAHAM_MAGIC_MISTIK = st.sidebar.selectbox('Waham Magic/Mistik', ['Tidak', 'Ya'])
    G80_WAHAM_MAGIC_MISTIK = 1 if G80_WAHAM_MAGIC_MISTIK == "Ya" else 0

    G83_MERASA_SESEORANG_BERKATA_JELEK = st.sidebar.selectbox('Merasa Dihakimi', ['Tidak', 'Ya'])
    G83_MERASA_SESEORANG_BERKATA_JELEK = 1 if G83_MERASA_SESEORANG_BERKATA_JELEK == "Ya" else 0

    G84_MERASA_ADA_BAYANG_BAYANG = st.sidebar.selectbox('Merada Bayangan', ['Tidak', 'Ya'])
    G84_MERASA_ADA_BAYANG_BAYANG = 1 if G84_MERASA_ADA_BAYANG_BAYANG == "Ya" else 0

    G87_MENUDUH_SESEORANG_BERBUAT_JAHAT = st.sidebar.selectbox('Menuduh Berbuat Jahat', ['Tidak', 'Ya'])
    G87_MENUDUH_SESEORANG_BERBUAT_JAHAT = 1 if G87_MENUDUH_SESEORANG_BERBUAT_JAHAT == "Ya" else 0

    G88_DELUSI_BADAN_MERASA_DIKENDALIKAN_DARI_LUAR = st.sidebar.selectbox('Merasa Dikendalikan', ['Tidak', 'Ya'])
    G88_DELUSI_BADAN_MERASA_DIKENDALIKAN_DARI_LUAR = 1 if G88_DELUSI_BADAN_MERASA_DIKENDALIKAN_DARI_LUAR == "Ya" else 0

    G89_THOUGHT_BROADCASTING_MENGAKU_SESEORANG_DAPAT_MEMBACA_PIKIRAN = st.sidebar.selectbox('Merasa Dapat Membaca Pikiran', ['Tidak', 'Ya'])
    G89_THOUGHT_BROADCASTING_MENGAKU_SESEORANG_DAPAT_MEMBACA_PIKIRAN = 1 if G89_THOUGHT_BROADCASTING_MENGAKU_SESEORANG_DAPAT_MEMBACA_PIKIRAN == "Ya" else 0

    G90_THOUGHT_ECHO = st.sidebar.selectbox('Thought Echo', ['Tidak', 'Ya'])
    G90_THOUGHT_ECHO = 1 if G90_THOUGHT_ECHO == "Ya" else 0

    G94_CURIGA_BERLEBIHAN = st.sidebar.selectbox('Curiga Berlebihan', ['Tidak', 'Ya'])
    G94_CURIGA_BERLEBIHAN = 1 if G94_CURIGA_BERLEBIHAN == "Ya" else 0

    input_data = {
        'G1_PEMBULIAN': [G1_PEMBULIAN],
        'G3_FRUSTASI_SULIT_KERJA': [G3_FRUSTASI_SULIT_KERJA],
        'G4_PERASAAN_KECEWA': [G4_PERASAAN_KECEWA],
        'G11_PERASAAN_KHAWATIR': [G11_PERASAAN_KHAWATIR],
        'G15_KELUYURAN': [G15_KELUYURAN],
        'G16_MERUSAK BARANG_MEMECAH': [G16_MERUSAK_BARANG_MEMECAH],
        'G17_MEMBERONTAK': [G17_MEMBERONTAK],
        'G18_MARAHMARAH': [G18_MARAHMARAH],
        'G19_TIDAK_BERAKTIFITAS': [G19_TIDAK_BERAKTIFITAS],
        'G20_SEDIH_MENANGIS': [G20_SEDIH_MENANGIS],
        'G21_SEDIKIT_BICARA': [G21_SEDIKIT_BICARA],
        'G23_TERGANGGU': [G23_TERGANGGU],
        'G25_MELAMUN' : [G25_MELAMUN],
        'G26_MEMUKUL_ORANGLAIN': [G26_MEMUKUL_ORANGLAIN],
        'G28_MELAKUKAN_TERIAK': [G28_MELAKUKAN_TERIAK],
        'G30_PUTUSASA': [G30_PUTUSASA],
        'G31_CEMAS': [G31_CEMAS],
        'G35_MENGURUNG': [G35_MENGURUNG],
        'G36 _MONDAR-MANDIR': [G36_MONDAR_MANDIR],
        'G37_KEINGINAN KERJA_KULIAH': [G37_KEINGINAN_KERJA_KULIAH],
        'G38 _MELUKAI DIRISENDIRI': [G38_MELUKAI_DIRISENDIRI],
        'G43_KEINGINAN_BUNUH_DIRI': [G43_KEINGINAN_BUNUH_DIRI],
        'G44_PERCOBAAN_BUNDIR': [G44_PERCOBAAN_BUNDIR],
        'G45_BERBICARA_SENDIRI': [G45_BERBICARA_SENDIRI],
        'G46_TERTAWA_SENDIRI': [G46_TERTAWA_SENDIRI],
        'G47_SULIT_MAKAN': [G47_SULIT_MAKAN],
        'G48_TIDAK_BERSOSIALISASI': [G48_TIDAK_BERSOSIALISASI],
        'G49_KEPIKIRAN_SESUATU': [G49_KEPIKIRAN_SESUATU],
        'G50_DIAM_SAAT_PEMERIKSAAN': [G50_DIAM_SAAT_PEMERIKSAAN],
        'G51_PIKIRAN_KACAU': [G51_PIKIRAN_KACAU],
        'G52_TIDAK_BERSEMANGAT': [G52_TIDAK_BERSEMANGAT],
        'G53_PERASAAN_BINGUNG': [G53_PERASAAN_BINGUNG],
        'G55_MENGALAMI_PERMASALAHAN_SEBELUMNYA ': [G55_MENGALAMI_PERMASALAHAN_SEBELUMNYA],
        'G56_MENGALAMI_PERSELISIHAN': [G56_MENGALAMI_PERSELISIHAN],
        'G57_PERASAANLELAH': [G57_PERASAANLELAH],
        'G59_KETAKUTAN': [G59_KETAKUTAN],
        'G61_BICARAKACAU__MELANTUR': [G61_BICARAKACAU__MELANTUR],
        'G62_KELUAR_RUMAH': [G62_KELUAR_RUMAH],
        'G63_HALUSINASI_VISUAL': [G63_HALUSINASI_VISUAL],
        'G65_HALUSINASI_DIANCAM': [G65_HALUSINASI_DIANCAM],
        'G66_HALUSINASI_AUDITORIK_MENDENGAR_SESUATU': [G66_HALUSINASI_AUDITORIK_MENDENGAR_SESUATU],
        'G71_DIAWASI': [G71_DIAWASI],
        'G72_PERASAAN_KESAL': [G72_PERASAAN_KESAL],
        'G73_KETAKUTAN_DIIKUTI_HALGHAIB': [G73_KETAKUTAN_DIIKUTI_HALGHAIB],
        'G74_WAHAM_REFERENSI_MERASA_DIBICARAKAN': [G74_WAHAM_REFERENSI_MERASA_DIBICARAKAN],
        'G75_WAHAM_BERSALAH': [G75_WAHAM_BERSALAH],
        'G76_WAHAM_PERSEKUTORIK_MERASA_DIJAHATI': [G76_WAHAM_PERSEKUTORIK_MERASA_DIJAHATI],
        'G78_WAHAM_KEBESARAN': [G78_WAHAM_KEBESARAN],
        'G80_WAHAM_MAGIC_MISTIK': [G80_WAHAM_MAGIC_MISTIK],
        'G83_MERASA_SESEORANG_BERKATA_JELEK ': [G83_MERASA_SESEORANG_BERKATA_JELEK],
        'G84_MERASA_ADA_BAYANG-BAYANG': [G84_MERASA_ADA_BAYANG_BAYANG],
        'G87_MENUDUH_SESEORANG_BERBUAT_JAHAT': [G87_MENUDUH_SESEORANG_BERBUAT_JAHAT],
        'G88_DELUSI_BADAN_MERASA_DIKENDALIKAN_DARI_LUAR': [G88_DELUSI_BADAN_MERASA_DIKENDALIKAN_DARI_LUAR],
        'G89_THOUGHT_BROADCASTING_MENGAKU_SESEORANG_DAPAT_MEMBACA_PIKIRAN': [G89_THOUGHT_BROADCASTING_MENGAKU_SESEORANG_DAPAT_MEMBACA_PIKIRAN],
        'G90_THOUGHT_ECHO': [G90_THOUGHT_ECHO],
        'G94_CURIGA_BERLEBIHAN': [G94_CURIGA_BERLEBIHAN]
    }

    #create a dataframe from the input data 
    input_df = pd.DataFrame(input_data)

    #train the model 
    model = joblib.load('diagnosa_new.pkl')

    #make predictions 
    st.title('Klasifikasi Penyakit Skizofrenia')
    st.write('Selamat Datang di Website kami')

    #display the predictions 
    st.title("Hasil Klasifikasinya Adalah")
    if st.button('Predict'):
        prediction = model.predict(input_df)[0]
        
        # Map predictions to proper display format
        diagnosis_map = {
            "Undifferentiated": {"code": 3, "desc": "Undifferentiated (Skizofrenia Tidak Terkhususkan)"},
            "Paranoid": {"code": 0, "desc": "Paranoid (Skizofrenia Paranoid)"},
            "Shizoaffective disorder, depressive type": {"code": 2, "desc": "Shizoaffective disorder, depressive type (Gangguan Skizoafektif Tipe Depresif)"},
            "Severe depressive episode with psychotic symptoms": {"code": 1, "desc": "Severe depressive episode with psychotic symptoms (Episode Depresi Berat dengan Gejala Psikotik)"}
        }
        
        result = diagnosis_map[prediction]
        
        # Display results with styling
        st.subheader("Hasil Diagnosis")
        
        # Create columns for better layout
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown(f"**Kode Diagnosis:**<br>"
                        f"<div style='background-color:rgba(240, 242, 246, 0.1); padding:20px; border-radius:10px;'>"
                        f"{result['code']}"
                        f"</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"**Jenis Gangguan:**<br>"
                        f"<div style='background-color:rgba(240, 242, 246, 0.1); padding:20px; border-radius:10px;'>"
                        f"🗒️ {result['desc']}"
                        f"</div>", unsafe_allow_html=True)
    
if __name__ == '__main__':
    main()
        


    
                                           
