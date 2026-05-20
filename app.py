import streamlit as st

# 1. CONFIG Halaman
st.set_page_config(
    page_title="Sistem Pakar Pemilihan Jurusan",
    layout="centered"
)

# 2. STYLING (Sudah diperbaiki agar support Light & Dark Mode secara otomatis)
st.markdown("""
<style>
/* Menggunakan CSS Variables bawaan Streamlit agar warna teks otomatis menyesuaikan tema */
.title {
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    color: #4F46E5; /* Menggunakan warna Indigo yang aman di dark/light mode */
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    color: #64748B;
    font-size: 16px;
    margin-bottom: 30px;
}
.box-fakta {
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #CBD5E1;
    margin-bottom: 25px;
    background-color: transparent; /* Agar mengikuti background tema Streamlit */
}
.result-card {
    padding: 20px;
    border-radius: 12px;
    background-color: #EFF6FF;
    border-left: 5px solid #3B82F6;
    margin-top: 15px;
}
/* Memastikan teks di dalam result-card tetap terbaca di dark mode */
.result-card h4 {
    color: #1E3A8A !important;
    margin: 0 0 8px 0;
}
.result-card p {
    color: #1E293B !important;
    margin: 0;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# 3. HEADER INTERFACE
st.markdown('<p class="title">Sistem Pakar Pemilihan Jurusan</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Membantu Kamu Menentukan Masa Depan Akademik Sesuai Minatmu</p>', unsafe_allow_html=True)

# 4. KNOWLEDGE BASE (Penyimpanan Fakta & Aturan secara Terstruktur)
KNOWLEDGE_RULES = [
    {
        "conditions": ["logika", "komputer"],
        "jurusan": "💻 Teknik Informatika / Ilmu Komputer",
        "alasan": "Kamu memiliki kombinasi kuat antara kemampuan logika matematika yang tinggi dan tertarik pada teknologi komputer."
    },
    {
        "conditions": ["desain", "komputer"],
        "jurusan": "🎨 Desain Komunikasi Visual (DKV) / Animasi",
        "alasan": "Sangat cocok karena kamu memiliki jiwa kreatifitas visual dan minat memanfaatkan teknologi digital."
    },
    {
        "conditions": ["komunikasi", "bisnis"],
        "jurusan": "📢 Manajemen Bisnis / Pemasaran",
        "alasan": "Kemampuan komunikasi yang baik merupakan aset berharga dalam mengelola organisasi dan strategi bisnis."
    },
    {
        "conditions": ["logika", "bisnis"],
        "jurusan": "📊 Akuntansi / Keuangan",
        "alasan": "Sektor keuangan membutuhkan ketelitian analisis angka dan pemahaman pengelolaan bisnis."
    },
    {
        "conditions": ["kesehatan", "sosial"],
        "jurusan": "🩺 Keperawatan / Kedokteran",
        "alasan": "Ketertarikan pada ilmu biologi/kesehatan dengan jiwa sosial tinggi mengarah pada profesi tenaga medis."
    },
    {
        "conditions": ["komputer", "bisnis"],
        "jurusan": "📈 Sistem Informasi",
        "alasan": "Jurusan ini merupakan jembatan sempurna yang menerapkan teknologi komputer demi efisiensi proses bisnis korporasi."
    },
    {
        "conditions": ["logika", "desain"],
        "jurusan": "📐 Arsitektur / Perencanaan Wilayah",
        "alasan": "Anda mampu menggabungkan perhitungan presisi struktural (logika) dengan estetika bentuk rancangan (desain)."
    }
]

# 5. INPUT FAKTA (Dibungkus container bawaan Streamlit agar teks checkbox aman di dark mode)
with st.container():
    st.subheader("📋 Pilih Karakteristik & Minatmu:")
    st.write("Centang semua pernyataan yang paling menggambarkan dirimu sekarang:")
    
    fakta_logika = st.checkbox("Saya suka memecahkan teka-teki logika, analisis, dan matematika.")
    fakta_komputer = st.checkbox("Saya tertarik mempelajari software, coding, hardware, atau teknologi digital.")
    fakta_desain = st.checkbox("Saya senang menggambar, membuat desain grafis, fotografi, atau editing video.")
    fakta_komunikasi = st.checkbox("Saya percaya diri dalam berbicara di depan umum, presentasi, atau negosiasi.")
    fakta_bisnis = st.checkbox("Saya tertarik dengan dunia wirausaha, investasi, manajemen, atau strategi pasar.")
    fakta_kesehatan = st.checkbox("Saya menyukai pelajaran biologi, anatomi, atau hal-hal medis.")
    fakta_sosial = st.checkbox("Saya senang membantu sesama manusia dan peduli dengan isu kemanusiaan.")

# 6. INFERENCE ENGINE (Mesin Pelacak forward-chaining)
if st.button("🔍 Lihat Hasil Rekomendasi", type="primary", use_container_width=True):
    
    # Kumpulkan fakta yang aktif
    fakta_aktif = []
    if fakta_logika: fakta_aktif.append("logika")
    if fakta_komputer: fakta_aktif.append("komputer")
    if fakta_desain: fakta_aktif.append("desain")
    if fakta_komunikasi: fakta_aktif.append("komunikasi")
    if fakta_bisnis: fakta_aktif.append("bisnis")
    if fakta_kesehatan: fakta_aktif.append("kesehatan")
    if fakta_sosial: fakta_aktif.append("sosial")

    # Evaluasi aturan
    hasil_rekomendasi = []
    for rule in KNOWLEDGE_RULES:
        if all(cond in fakta_aktif for cond in rule["conditions"]):
            hasil_rekomendasi.append(rule)

    # 7. OUTPUT RENDERER
    if hasil_rekomendasi:
        st.balloons() 
        st.success(f"{len(hasil_rekomendasi)} rekomendasi jurusan yang cocok untukmu:")
        
        for item in hasil_rekomendasi:
            st.markdown(f"""
            <div class="result-card">
                <h4>{item['jurusan']}</h4>
                <p><b>Alasan :</b> {item['alasan']}</p>
            </div>
            """, unsafe_allow_html=True)
            
    else:
        if len(fakta_aktif) < 2:
            st.warning("⚠️ Silakan pilih minimal 2 atau lebih kombinasi minatmu untuk mendapatkan rekomendasi.")
        else:
            st.info("💡 Kombinasi peminatanmu sangat unik! Kami menyarankan untuk berkonsultasi langsung dengan konselor akademik.")

# FOOTER
st.markdown("<br><hr><center style='color: #94A3B8; font-size: 12px;'>Sistem Pakar Pemilihan Jurusan</center>", unsafe_allow_html=True)
