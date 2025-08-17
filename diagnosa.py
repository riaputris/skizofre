import streamlit as st
import pandas as pd
import joblib
from st_keyup import st_keyup
import re

def create_symptom_mapping():
    """Membuat mapping kata kunci gejala dengan column database"""
    return {
        # G1_PEMBULIAN
        'pembulian': 'G1_PEMBULIAN',
        'bully': 'G1_PEMBULIAN',
        'dibully': 'G1_PEMBULIAN',
        'bullying': 'G1_PEMBULIAN',
        
        # G3_FRUSTASI_SULIT_KERJA
        'frustasi': 'G3_FRUSTASI_SULIT_KERJA',
        'sulit kerja': 'G3_FRUSTASI_SULIT_KERJA',
        'kesulitan kerja': 'G3_FRUSTASI_SULIT_KERJA',
        'susah kerja': 'G3_FRUSTASI_SULIT_KERJA',
        
        # G4_PERASAAN_KECEWA
        'kecewa': 'G4_PERASAAN_KECEWA',
        'perasaan kecewa': 'G4_PERASAAN_KECEWA',
        'disappointment': 'G4_PERASAAN_KECEWA',
        
        # G11_PERASAAN_KHAWATIR
        'khawatir': 'G11_PERASAAN_KHAWATIR',
        'perasaan khawatir': 'G11_PERASAAN_KHAWATIR',
        'worry': 'G11_PERASAAN_KHAWATIR',
        'gelisah': 'G11_PERASAAN_KHAWATIR',
        
        # G15_KELUYURAN
        'keluyuran': 'G15_KELUYURAN',
        'suka keluyuran': 'G15_KELUYURAN',
        'jalan-jalan terus': 'G15_KELUYURAN',
        'wandering': 'G15_KELUYURAN',
        
        # PERBAIKAN: Sesuaikan nama kolom dengan yang digunakan saat training
        # G16_MERUSAK BARANG_MEMECAH (perhatikan spasi, bukan underscore)
        'merusak barang': 'G16_MERUSAK BARANG_MEMECAH',
        'memecah': 'G16_MERUSAK BARANG_MEMECAH',
        'merusak': 'G16_MERUSAK BARANG_MEMECAH',
        'destructive': 'G16_MERUSAK BARANG_MEMECAH',
        
        # G17_MEMBERONTAK
        'memberontak': 'G17_MEMBERONTAK',
        'rebel': 'G17_MEMBERONTAK',
        'melawan': 'G17_MEMBERONTAK',
        'pemberontak': 'G17_MEMBERONTAK',
        
        # G18_MARAHMARAH
        'marah': 'G18_MARAHMARAH',
        'marah-marah': 'G18_MARAHMARAH',
        'angry': 'G18_MARAHMARAH',
        'emosi': 'G18_MARAHMARAH',
        
        # G19_TIDAK_BERAKTIFITAS
        'tidak beraktivitas': 'G19_TIDAK_BERAKTIFITAS',
        'malas': 'G19_TIDAK_BERAKTIFITAS',
        'pasif': 'G19_TIDAK_BERAKTIFITAS',
        'inactive': 'G19_TIDAK_BERAKTIFITAS',
        
        # G20_SEDIH_MENANGIS
        'sedih': 'G20_SEDIH_MENANGIS',
        'menangis': 'G20_SEDIH_MENANGIS',
        'sad': 'G20_SEDIH_MENANGIS',
        'crying': 'G20_SEDIH_MENANGIS',
        
        # G21_SEDIKIT_BICARA
        'sedikit bicara': 'G21_SEDIKIT_BICARA',
        'pendiam': 'G21_SEDIKIT_BICARA',
        'jarang bicara': 'G21_SEDIKIT_BICARA',
        'silent': 'G21_SEDIKIT_BICARA',
        
        # G23_TERGANGGU
        'terganggu': 'G23_TERGANGGU',
        'disturbed': 'G23_TERGANGGU',
        'terusik': 'G23_TERGANGGU',
        
        # G25_MELAMUN
        'melamun': 'G25_MELAMUN',
        'daydreaming': 'G25_MELAMUN',
        'bengong': 'G25_MELAMUN',
        
        # G26_MEMUKUL_ORANGLAIN
        'memukul orang lain': 'G26_MEMUKUL_ORANGLAIN',
        'memukul': 'G26_MEMUKUL_ORANGLAIN',
        'violence': 'G26_MEMUKUL_ORANGLAIN',
        'kekerasan': 'G26_MEMUKUL_ORANGLAIN',
        
        # G28_MELAKUKAN_TERIAK
        'teriak': 'G28_MELAKUKAN_TERIAK',
        'berteriak': 'G28_MELAKUKAN_TERIAK',
        'shouting': 'G28_MELAKUKAN_TERIAK',
        'scream': 'G28_MELAKUKAN_TERIAK',
        
        # G29 _BICARA
        'bicara': 'G29 _BICARA',
        'talking': 'G29 _BICARA',
        
        # G30_PUTUSASA
        'putus asa': 'G30_PUTUSASA',
        'hopeless': 'G30_PUTUSASA',
        'despair': 'G30_PUTUSASA',
        
        # G31_CEMAS
        'cemas': 'G31_CEMAS',
        'anxiety': 'G31_CEMAS',
        'anxious': 'G31_CEMAS',
        
        # G35_MENGURUNG
        'mengurung diri': 'G35_MENGURUNG',
        'isolasi': 'G35_MENGURUNG',
        'menyendiri': 'G35_MENGURUNG',
        'isolation': 'G35_MENGURUNG',
        
        # PERBAIKAN: G36 _MONDAR-MANDIR (perhatikan tanda hubung)
        'mondar mandir': 'G36 _MONDAR-MANDIR',
        'bolak balik': 'G36 _MONDAR-MANDIR',
        'pacing': 'G36 _MONDAR-MANDIR',
        
        # PERBAIKAN: G37_KEINGINAN KERJA_KULIAH (perhatikan spasi)
        'keinginan kerja': 'G37_KEINGINAN KERJA_KULIAH',
        'keinginan kuliah': 'G37_KEINGINAN KERJA_KULIAH',
        'motivasi kerja': 'G37_KEINGINAN KERJA_KULIAH',
        
        # PERBAIKAN: G38 _MELUKAI DIRISENDIRI (perhatikan spasi)
        'melukai diri sendiri': 'G38 _MELUKAI DIRISENDIRI',
        'self harm': 'G38 _MELUKAI DIRISENDIRI',
        'menyakiti diri': 'G38 _MELUKAI DIRISENDIRI',
        
        # G43_KEINGINAN_BUNUH_DIRI
        'bunuh diri': 'G43_KEINGINAN_BUNUH_DIRI',
        'suicide': 'G43_KEINGINAN_BUNUH_DIRI',
        'ingin mati': 'G43_KEINGINAN_BUNUH_DIRI',
        
        # G44_PERCOBAAN_BUNDIR
        'percobaan bunuh diri': 'G44_PERCOBAAN_BUNDIR',
        'suicide attempt': 'G44_PERCOBAAN_BUNDIR',
        'coba bunuh diri': 'G44_PERCOBAAN_BUNDIR',
        
        # G45_BERBICARA_SENDIRI
        'berbicara sendiri': 'G45_BERBICARA_SENDIRI',
        'talking to self': 'G45_BERBICARA_SENDIRI',
        'monolog': 'G45_BERBICARA_SENDIRI',
        
        # G47_SULIT_MAKAN
        'sulit makan': 'G47_SULIT_MAKAN',
        'susah makan': 'G47_SULIT_MAKAN',
        'eating difficulty': 'G47_SULIT_MAKAN',
        'nafsu makan hilang': 'G47_SULIT_MAKAN',
        
        # G48_TIDAK_BERSOSIALISASI
        'tidak bersosialisasi': 'G48_TIDAK_BERSOSIALISASI',
        'antisocial': 'G48_TIDAK_BERSOSIALISASI',
        'tidak bergaul': 'G48_TIDAK_BERSOSIALISASI',
        
        # G49_KEPIKIRAN_SESUATU
        'kepikiran sesuatu': 'G49_KEPIKIRAN_SESUATU',
        'overthinking': 'G49_KEPIKIRAN_SESUATU',
        'banyak pikiran': 'G49_KEPIKIRAN_SESUATU',
        
        # G50_DIAM_SAAT_PEMERIKSAAN
        'diam saat pemeriksaan': 'G50_DIAM_SAAT_PEMERIKSAAN',
        'silent during examination': 'G50_DIAM_SAAT_PEMERIKSAAN',
        'tidak mau bicara saat diperiksa': 'G50_DIAM_SAAT_PEMERIKSAAN',
        
        # G51_PIKIRAN_KACAU
        'pikiran kacau': 'G51_PIKIRAN_KACAU',
        'confused thinking': 'G51_PIKIRAN_KACAU',
        'pikiran tidak teratur': 'G51_PIKIRAN_KACAU',
        
        # G52_TIDAK_BERSEMANGAT
        'tidak bersemangat': 'G52_TIDAK_BERSEMANGAT',
        'tidak bergairah': 'G52_TIDAK_BERSEMANGAT',
        'demotivated': 'G52_TIDAK_BERSEMANGAT',
        'lesu': 'G52_TIDAK_BERSEMANGAT',
        
        # G53_PERASAAN_BINGUNG
        'bingung': 'G53_PERASAAN_BINGUNG',
        'confused': 'G53_PERASAAN_BINGUNG',
        'perasaan bingung': 'G53_PERASAAN_BINGUNG',
        
        # PERBAIKAN: G55_MENGALAMI_PERMASALAHAN_SEBELUMNYA -> G55_MENGALAMI_PERMASALAHAN_SEBELUMNYA
        'masalah sebelumnya': 'G55_MENGALAMI_PERMASALAHAN_SEBELUMNYA ',
        'riwayat masalah': 'G55_MENGALAMI_PERMASALAHAN_SEBELUMNYA ',
        'previous problems': 'G55_MENGALAMI_PERMASALAHAN_SEBELUMNYA ',
        
        # G56_MENGALAMI_PERSELISIHAN
        'perselisihan': 'G56_MENGALAMI_PERSELISIHAN',
        'konflik': 'G56_MENGALAMI_PERSELISIHAN',
        'pertengkaran': 'G56_MENGALAMI_PERSELISIHAN',
        'conflict': 'G56_MENGALAMI_PERSELISIHAN',
        
        # G57_PERASAANLELAH
        'lelah': 'G57_PERASAANLELAH',
        'tired': 'G57_PERASAANLELAH',
        'fatigue': 'G57_PERASAANLELAH',
        'capek': 'G57_PERASAANLELAH',
        
        # G59_KETAKUTAN
        'takut': 'G59_KETAKUTAN',
        'ketakutan': 'G59_KETAKUTAN',
        'fear': 'G59_KETAKUTAN',
        'afraid': 'G59_KETAKUTAN',
        
        # G62_KELUAR_RUMAH
        'keluar rumah': 'G62_KELUAR_RUMAH',
        'kabur': 'G62_KELUAR_RUMAH',
        'running away': 'G62_KELUAR_RUMAH',
        'meninggalkan rumah': 'G62_KELUAR_RUMAH',
        
        # G63_HALUSINASI_VISUAL
        'halusinasi visual': 'G63_HALUSINASI_VISUAL',
        'melihat sesuatu': 'G63_HALUSINASI_VISUAL',
        'visual hallucination': 'G63_HALUSINASI_VISUAL',
        'penglihatan aneh': 'G63_HALUSINASI_VISUAL',
        
        # G65_HALUSINASI_DIANCAM
        'halusinasi diancam': 'G65_HALUSINASI_DIANCAM',
        'merasa diancam': 'G65_HALUSINASI_DIANCAM',
        'threatened hallucination': 'G65_HALUSINASI_DIANCAM',
        
        # G66_HALUSINASI_AUDITORIK_MENDENGAR_SESUATU
        'halusinasi auditorik': 'G66_HALUSINASI_AUDITORIK_MENDENGAR_SESUATU',
        'mendengar sesuatu': 'G66_HALUSINASI_AUDITORIK_MENDENGAR_SESUATU',
        'mendengar suara': 'G66_HALUSINASI_AUDITORIK_MENDENGAR_SESUATU',
        'auditory hallucination': 'G66_HALUSINASI_AUDITORIK_MENDENGAR_SESUATU',
        
        # G73_KETAKUTAN_DIIKUTI_HALGHAIB
        'diikuti hal gaib': 'G73_KETAKUTAN_DIIKUTI_HALGHAIB',
        'takut hantu': 'G73_KETAKUTAN_DIIKUTI_HALGHAIB',
        'supernatural fear': 'G73_KETAKUTAN_DIIKUTI_HALGHAIB',
        'paranormal': 'G73_KETAKUTAN_DIIKUTI_HALGHAIB',
        
        # G74_WAHAM_REFERENSI_MERASA_DIBICARAKAN
        'merasa dibicarakan': 'G74_WAHAM_REFERENSI_MERASA_DIBICARAKAN',
        'dibicarakan orang': 'G74_WAHAM_REFERENSI_MERASA_DIBICARAKAN',
        'reference delusion': 'G74_WAHAM_REFERENSI_MERASA_DIBICARAKAN',
        'digosipkan': 'G74_WAHAM_REFERENSI_MERASA_DIBICARAKAN',
        
        # G75_WAHAM_BERSALAH
        'waham bersalah': 'G75_WAHAM_BERSALAH',
        'merasa bersalah': 'G75_WAHAM_BERSALAH',
        'guilt delusion': 'G75_WAHAM_BERSALAH',
        'perasaan berdosa': 'G75_WAHAM_BERSALAH',
        
        # G76_WAHAM_PERSEKUTORIK_MERASA_DIJAHATI
        'merasa dijahati': 'G76_WAHAM_PERSEKUTORIK_MERASA_DIJAHATI',
        'persecutory delusion': 'G76_WAHAM_PERSEKUTORIK_MERASA_DIJAHATI',
        'paranoid': 'G76_WAHAM_PERSEKUTORIK_MERASA_DIJAHATI',
        'curiga': 'G76_WAHAM_PERSEKUTORIK_MERASA_DIJAHATI',
        
        # G78_WAHAM_KEBESARAN
        'waham kebesaran': 'G78_WAHAM_KEBESARAN',
        'merasa hebat': 'G78_WAHAM_KEBESARAN',
        'grandiose delusion': 'G78_WAHAM_KEBESARAN',
        'sombong berlebihan': 'G78_WAHAM_KEBESARAN',
        
        # G80_WAHAM_MAGIC_MISTIK
        'waham magic': 'G80_WAHAM_MAGIC_MISTIK',
        'waham mistik': 'G80_WAHAM_MAGIC_MISTIK',
        'magical thinking': 'G80_WAHAM_MAGIC_MISTIK',
        'mistik': 'G80_WAHAM_MAGIC_MISTIK',
        
        # G83_MERASA_SESEORANG_BERKATA_JELEK
        'merasa dihakimi': 'G83_MERASA_SESEORANG_BERKATA_JELEK ',
        'dikritik': 'G83_MERASA_SESEORANG_BERKATA_JELEK ',
        'being judged': 'G83_MERASA_SESEORANG_BERKATA_JELEK ',
        'dikata-katain': 'G83_MERASA_SESEORANG_BERKATA_JELEK ',
        
        # G84_MERASA_ADA_BAYANG-BAYANG
        'merasa ada bayangan': 'G84_MERASA_ADA_BAYANG-BAYANG',
        'melihat bayangan': 'G84_MERASA_ADA_BAYANG-BAYANG',
        'shadow hallucination': 'G84_MERASA_ADA_BAYANG-BAYANG',
        'bayangan aneh': 'G84_MERASA_ADA_BAYANG-BAYANG',
        
        # G87_MENUDUH_SESEORANG_BERBUAT_JAHAT
        'menuduh berbuat jahat': 'G87_MENUDUH_SESEORANG_BERBUAT_JAHAT',
        'accusing others': 'G87_MENUDUH_SESEORANG_BERBUAT_JAHAT',
        'menyalahkan orang': 'G87_MENUDUH_SESEORANG_BERBUAT_JAHAT',
        
        # G88_DELUSI_BADAN_MERASA_DIKENDALIKAN_DARI_LUAR
        'merasa dikendalikan': 'G88_DELUSI_BADAN_MERASA_DIKENDALIKAN_DARI_LUAR',
        'controlled delusion': 'G88_DELUSI_BADAN_MERASA_DIKENDALIKAN_DARI_LUAR',
        'tidak bisa mengontrol diri': 'G88_DELUSI_BADAN_MERASA_DIKENDALIKAN_DARI_LUAR',
        
        # G90_THOUGHT_ECHO
        'thought echo': 'G90_THOUGHT_ECHO',
        'pikiran bergema': 'G90_THOUGHT_ECHO',
        'echo pikiran': 'G90_THOUGHT_ECHO',
        
        # G94_CURIGA_BERLEBIHAN
        'curiga berlebihan': 'G94_CURIGA_BERLEBIHAN',
        'excessive suspicion': 'G94_CURIGA_BERLEBIHAN',
        'paranoid berlebihan': 'G94_CURIGA_BERLEBIHAN',
        'tidak percaya siapa-siapa': 'G94_CURIGA_BERLEBIHAN'
    }

def highlight_detected_symptoms(text, detected_symptoms):
    """Highlight kata-kata yang terdeteksi sebagai gejala"""
    if not detected_symptoms:
        return text
    
    highlighted_text = text
    # Sort by length descending untuk menghindari overlapping highlight
    sorted_symptoms = sorted(detected_symptoms, key=len, reverse=True)
    
    for symptom in sorted_symptoms:
        pattern = re.compile(re.escape(symptom), re.IGNORECASE)
        highlighted_text = pattern.sub(f'**:green[{symptom}]**', highlighted_text)
    
    return highlighted_text

def process_input_text(text, symptom_mapping):
    """Memproses input text dan mendeteksi gejala"""
    text_lower = text.lower()
    detected_symptoms = set()
    detected_columns = set()
    
    # Cek setiap kata kunci dalam mapping
    for keyword, column in symptom_mapping.items():
        if keyword in text_lower:
            detected_symptoms.add(keyword)
            detected_columns.add(column)
    
    return detected_symptoms, detected_columns

def initialize_session_state():
    """Initialize session state variables"""
    if 'detected_columns' not in st.session_state:
        st.session_state.detected_columns = set()
    if 'input_history' not in st.session_state:
        st.session_state.input_history = []

def create_input_dataframe(detected_columns):
    """Membuat dataframe input untuk prediksi"""
    # PERBAIKAN: Nama kolom yang sesuai dengan model training
    all_columns = [
        'G1_PEMBULIAN', 'G3_FRUSTASI_SULIT_KERJA', 'G4_PERASAAN_KECEWA', 'G11_PERASAAN_KHAWATIR',
        'G15_KELUYURAN', 'G16_MERUSAK BARANG_MEMECAH', 'G17_MEMBERONTAK', 'G18_MARAHMARAH',
        'G19_TIDAK_BERAKTIFITAS', 'G20_SEDIH_MENANGIS', 'G21_SEDIKIT_BICARA', 'G23_TERGANGGU',
        'G25_MELAMUN', 'G26_MEMUKUL_ORANGLAIN', 'G28_MELAKUKAN_TERIAK', 'G29 _BICARA', 'G30_PUTUSASA',
        'G31_CEMAS', 'G35_MENGURUNG', 'G36 _MONDAR-MANDIR', 'G37_KEINGINAN KERJA_KULIAH',
        'G38 _MELUKAI DIRISENDIRI', 'G43_KEINGINAN_BUNUH_DIRI', 'G44_PERCOBAAN_BUNDIR',
        'G45_BERBICARA_SENDIRI', 'G47_SULIT_MAKAN',
        'G48_TIDAK_BERSOSIALISASI', 'G49_KEPIKIRAN_SESUATU', 'G50_DIAM_SAAT_PEMERIKSAAN',
        'G51_PIKIRAN_KACAU', 'G52_TIDAK_BERSEMANGAT', 'G53_PERASAAN_BINGUNG',
        'G55_MENGALAMI_PERMASALAHAN_SEBELUMNYA ', 'G56_MENGALAMI_PERSELISIHAN',
        'G57_PERASAANLELAH', 'G59_KETAKUTAN',
        'G62_KELUAR_RUMAH', 'G63_HALUSINASI_VISUAL', 'G65_HALUSINASI_DIANCAM',
        'G66_HALUSINASI_AUDITORIK_MENDENGAR_SESUATU',
        'G73_KETAKUTAN_DIIKUTI_HALGHAIB', 'G74_WAHAM_REFERENSI_MERASA_DIBICARAKAN',
        'G75_WAHAM_BERSALAH', 'G76_WAHAM_PERSEKUTORIK_MERASA_DIJAHATI',
        'G78_WAHAM_KEBESARAN', 'G80_WAHAM_MAGIC_MISTIK', 'G83_MERASA_SESEORANG_BERKATA_JELEK ',
        'G84_MERASA_ADA_BAYANG-BAYANG', 'G87_MENUDUH_SESEORANG_BERBUAT_JAHAT',
        'G88_DELUSI_BADAN_MERASA_DIKENDALIKAN_DARI_LUAR',
        'G90_THOUGHT_ECHO', 'G94_CURIGA_BERLEBIHAN'
    ]
    
    input_data = {}
    for col in all_columns:
        input_data[col] = [1 if col in detected_columns else 0]
    
    return pd.DataFrame(input_data)

# TAMBAHKAN FUNGSI VALIDASI BARU
def validate_symptoms(detected_columns):
    """Validasi apakah ada minimal 1 gejala yang terdeteksi"""
    return len(detected_columns) > 0

def main() :
    #Set page title
    st.set_page_config (page_title ='Diagnosa Skizofrenia')
    # Initialize session state
    initialize_session_state()
    
    # Create symptom mapping
    symptom_mapping = create_symptom_mapping()
    
    # Title
    st.title('Klasifikasi Penyakit Skizofrenia')
    st.write('Selamat Datang di Website kami')
    
    # Input section
    st.title("Input Diagnosa Skizofrenia")
    st.write("Masukkan gejala-gejala yang dialami. Sistem akan secara otomatis mendeteksi dan menandai gejala yang relevan:")
    
    # Live input dengan st_keyup
    user_input = st_keyup(
        "Ketik gejala-gejala yang dialami (contoh: merasa sedih, sering menangis, sulit tidur):",
        value="",
        key="symptom_input",
        debounce=300
    )
    
    # Process input
    if user_input:
        detected_symptoms, new_detected_columns = process_input_text(user_input, symptom_mapping)
        
        # Update session state dengan gejala baru
        st.session_state.detected_columns.update(new_detected_columns)
        
        # Highlight text
        highlighted_text = highlight_detected_symptoms(user_input, detected_symptoms)
        
        # Display highlighted text
        st.subheader("Text dengan Gejala Terdeteksi:")
        st.markdown(highlighted_text)
        
        # Show detected symptoms
        if detected_symptoms:
            st.subheader("Gejala Terdeteksi:")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Kata Kunci Terdeteksi:**")
                for symptom in sorted(detected_symptoms):
                    st.write(f"✅ {symptom}")
            
            with col2:
                st.write("**Kolom Database Terkait:**")
                for column in sorted(new_detected_columns):
                    st.write(f"📊 {column}")
    
    # Show all accumulated symptoms
    if st.session_state.detected_columns:
        st.subheader("Semua Gejala yang Tersimpan dalam Session:")
        
        # Display dalam format yang rapi
        symptoms_df = pd.DataFrame({
            'Kolom Database': sorted(list(st.session_state.detected_columns)),
            'Status': ['✅ Terdeteksi'] * len(st.session_state.detected_columns)
        })
        st.dataframe(symptoms_df, use_container_width=True)
        
        # Button untuk clear session
        if st.button("🗑️ Hapus Semua Gejala", type="secondary"):
            st.session_state.detected_columns = set()
            st.session_state.input_history = []
            st.rerun()
    
    # Prediction section
    st.title("Hasil Klasifikasinya Adalah")
    
    if st.button('🔍 Predict', type="primary", use_container_width=True):
        # TAMBAHKAN VALIDASI DI SINI
        if not validate_symptoms(st.session_state.detected_columns):
            st.error("""
            ❌ **Tidak ada gejala yang terdeteksi!**
            
            Silakan masukkan minimal 1 gejala yang dapat dikenali sistem terlebih dahulu.
            
            **Tips:**
            - Gunakan kata kunci seperti: "sedih", "menangis", "cemas", "takut", dll
            - Ketik gejala dengan bahasa yang lebih spesifik
            - Lihat contoh gejala di bagian bawah halaman
            """)
            return
        
        if st.session_state.detected_columns:
            try:
                # Create input dataframe
                input_df = create_input_dataframe(st.session_state.detected_columns)
                
                # Debug: tampilkan kolom yang terdeteksi
                st.info(f"🔍 Gejala terdeteksi: {len(st.session_state.detected_columns)} gejala")
                
                # Load model dan predict
                model = joblib.load('skizofrenia_akurasi_94.pkl')
                prediction = model.predict(input_df)[0]
                
                # Map predictions to proper display format
                diagnosis_map = {
                    "Undifferentiated": {"code": 3, "desc": "Undifferentiated"},
                    "Paranoid": {"code": 0, "desc": "Paranoid"},
                    "Shizoaffective disorder, depressive type": {"code": 2, "desc": "Shizoaffective disorder, depressive type"},
                    "Severe depressive episode with psychotic symptoms": {"code": 1, "desc": "Severe depressive episode with psychotic symptoms"}
                }
                
                result = diagnosis_map[prediction]
                
                # Display results with styling
                st.subheader("🎯 Hasil Diagnosis")
                
                # Create columns for better layout
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    st.markdown(f"""
                    **Kode Diagnosis:**
                    <div style='background-color:rgba(240, 242, 246, 0.1); padding:20px; border-radius:10px; text-align:center; font-size:24px; font-weight:bold; color:#1f77b4;'>
                    {result['code']}
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    **Jenis Gangguan:**
                    <div style='background-color:rgba(240, 242, 246, 0.1); padding:20px; border-radius:10px;'>
                    🩺 {result['desc']}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Show prediction confidence if available
                try:
                    prediction_proba = model.predict_proba(input_df)[0]
                    classes = list(model.classes_)
                    proba_by_class = dict(zip(classes, prediction_proba))
                    pred_proba = float(proba_by_class.get(prediction, max(prediction_proba)))

                    st.subheader("📊 Tingkat Kepercayaan Prediksi")
                    confidence_percent = pred_proba * 100

                    st.progress(pred_proba)
                    st.write(f"Kepercayaan: {confidence_percent:.1f}%")
                    
                    # Show all probabilities
                    with st.expander("Detail Probabilitas Semua Diagnosis"):
                        classes = list(model.classes_)
                        prob_df = pd.DataFrame({
                            'Diagnosis': classes,
                            'Probabilitas': [float(p) for p in prediction_proba]
                        })
                        prob_df['Probabilitas (%)'] = (prob_df['Probabilitas'] * 100).round(2)
                        prob_df = prob_df.sort_values('Probabilitas', ascending=False, ignore_index=True)
                        st.dataframe(prob_df[['Diagnosis', 'Probabilitas (%)']], use_container_width=True)
                        
                except Exception as e:
                    st.info("Model tidak mendukung probability prediction")
                
                # Show input summary
                st.subheader("📋 Ringkasan Input yang Digunakan")
                
                # Count detected symptoms
                total_symptoms = len(st.session_state.detected_columns)
                st.metric("Total Gejala Terdeteksi", total_symptoms)
                
                # Show detected symptoms in a nice format
                if total_symptoms > 0:
                    symptoms_list = sorted(list(st.session_state.detected_columns))
                    symptoms_text = ", ".join([symptom.replace('G', '').replace('_', ' ').title() for symptom in symptoms_list])
                    
                    st.text_area(
                        "Gejala yang Terdeteksi:",
                        value=symptoms_text,
                        height=100,
                        disabled=True
                    )
                
                # Warning/disclaimer
                st.warning("""
                ⚠️ **Disclaimer:** 
                Hasil diagnosis ini adalah prediksi dari model machine learning dan bukan pengganti diagnosis medis profesional. 
                Untuk diagnosis yang akurat, silakan berkonsultasi dengan dokter atau psikiater.
                """)
                
            except FileNotFoundError:
                st.error("❌ File model 'skizofrenia_akurasi_94.pkl' tidak ditemukan. Pastikan file model tersedia.")
            except Exception as e:
                st.error(f"input_df: {input_df}")
                st.error(f"❌ Terjadi kesalahan saat melakukan prediksi: {str(e)}")
                # Debug info
                st.info("Debug: Periksa nama kolom yang digunakan vs yang diharapkan model")
    
    # Additional features
    st.markdown("---")
    
    # Help section
    with st.expander("ℹ️ Panduan Penggunaan"):
        st.markdown("""
        ### Cara Menggunakan Aplikasi:
        
        1. **Input Gejala**: Ketik gejala-gejala yang dialami di text area di atas
        2. **Live Detection**: Sistem akan secara otomatis mendeteksi dan menandai gejala yang relevan dengan warna hijau
        3. **Akumulasi Gejala**: Semua gejala yang terdeteksi akan tersimpan dalam session
        4. **Prediksi**: Klik tombol "Predict" untuk mendapatkan hasil diagnosis
        5. **Hasil**: Lihat kode diagnosis, jenis gangguan, dan tingkat kepercayaan prediksi
        
        ### Contoh Input:
        - "Saya sering merasa sedih dan menangis"
        - "Kadang saya mendengar suara-suara aneh"
        - "Saya merasa diawasi dan curiga pada orang lain"
        - "Sulit berkonsentrasi dan pikiran kacau"
        
        ### Tips:
        - Gunakan bahasa Indonesia atau Inggris
        - Jelaskan gejala dengan detail
        - Sistem dapat mendeteksi sinonim dan variasi kata
        """)
    
    # Sample symptoms for testing
    with st.expander("🧪 Contoh Gejala untuk Testing"):
        sample_symptoms = [
            "sedih menangis tidak bersemangat",
            "mendengar suara halusinasi auditorik berbicara sendiri",
            "curiga berlebihan merasa diawasi paranoid",
            "marah-marah merusak barang memukul orang lain",
            "melamun tidak bersosialisasi mengurung diri"
        ]
        
        st.write("Klik salah satu contoh untuk mencoba:")
        for i, sample in enumerate(sample_symptoms):
            if st.button(f"Contoh {i+1}: {sample}", key=f"sample_{i}"):
                # Update the input (ini memerlukan JavaScript, jadi kita bisa menampilkan saja)
                st.info(f"Salin text ini ke input: **{sample}**")
    
if __name__ == '__main__':
    main()