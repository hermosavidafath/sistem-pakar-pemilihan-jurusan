import streamlit as st

# 1. CONFIG Halaman
st.set_page_config(
    page_title="Sistem Pakar Pemilihan Jurusan",
    layout="centered"
)

# 2. STYLING (Custom CSS agar tampilan modern dan profesional)
st.markdown("""
<style>
.stApp {
    background-color: #F8FAFC;
}
.title {
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    color: #1E3A8A;
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    color: #64748B;
    font-size: 16px;
    margin-bottom: 30px;
}
.box-fakta {
    background-color: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);
    border: 1px solid #E2E8F0;
    margin-bottom: 25px;
}
.result-card {
    padding: 20px;
    border-radius: 12px;
    background-color: #EFF6FF;
    border-left: 5px solid #3B82F6;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# 3. HEADER INTERFACE
st.markdown('<p class="title">Sistem Pakar Pemilihan Jurusan</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Membantu Kamu Menentukan Masa Depan Akademik Sesuai Minatmu</p>', unsafe_allow_html=True)

# 4. KNOWLEDGE BASE (Penyimpanan Fakta & Aturan secara Terstruktur)
# Kumpulan Aturan (Rules) yang mencakup minimal 5 fakta dan lebih dari 5 kombinasi aturan terarah
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

# 5. INPUT FAKTA (User Interface untuk mengumpulkan Fakta dari pengguna)
st.subheader("📋 Pilih Karakteristik & Minatmu:")
st.write("Centang semua pernyataan yang paling menggambarkan dirimu sekarang:")

# Menyediakan fakta yang lebih luas dan banyak pilihan (>5 Fakta)
fakta_logika = st.checkbox("Saya suka memecahkan teka-teki logika, analisis, dan matematika.")
fakta_komputer = st.checkbox("Saya tertarik mempelajari software, coding, hardware, atau teknologi digital.")
fakta_desain = st.checkbox("Saya senang menggambar, membuat desain grafis, fotografi, atau editing video.")
fakta_komunikasi = st.checkbox("Saya percaya diri dalam berbicara di depan umum, presentasi, atau negosiasi.")
fakta_bisnis = st.checkbox("Saya tertarik dengan dunia wirausaha, investasi, manajemen, atau strategi pasar.")
fakta_kesehatan = st.checkbox("Saya menyukai pelajaran biologi, anatomi, atau hal-hal medis.")
fakta_sosial = st.checkbox("Saya senang membantu sesama manusia dan peduli dengan isu kemanusiaan.")

st.markdown('</div>', unsafe_allow_html=True)

# 6. INFERENCE ENGINE (Mesin Pelacak forward-chaining yang terpicu saat tombol ditekan)
if st.button("🔍 Lihat Hasil Rekomendasi", type="primary", use_container_width=True):
    
    # Kumpulkan fakta yang aktif ke dalam list aktif
    fakta_aktif = []
    if fakta_logika: fakta_aktif.append("logika")
    if fakta_komputer: fakta_aktif.append("komputer")
    if fakta_desain: fakta_aktif.append("desain")
    if fakta_komunikasi: fakta_aktif.append("komunikasi")
    if fakta_bisnis: fakta_aktif.append("bisnis")
    if fakta_kesehatan: fakta_aktif.append("kesehatan")
    if fakta_sosial: fakta_aktif.append("sosial")

    # Evaluasi aturan berdasarkan fakta aktif
    hasil_rekomendasi = []
    
    for rule in KNOWLEDGE_RULES:
        # Cek apakah semua kondisi dalam rule tersebut terpenuhi oleh fakta_aktif dari user
        if all(cond in fakta_aktif for cond in rule["conditions"]):
            hasil_rekomendasi.append(rule)

    # 7. OUTPUT RENDERER (Menampilkan Hasil Kesimpulan)
    if hasil_rekomendasi:
        st.balloons() # Efek visual animasi balon sukses
        st.success(f"{len(hasil_rekomendasi)} rekomendasi jurusan yang cocok untukmu:")
        
        for item in hasil_rekomendasi:
            st.markdown(f"""
            <div class="result-card">
                <h4 style="margin: 0 0 8px 0; color: #1E3A8A;">{item['jurusan']}</h4>
                <p style="margin: 0; color: #475569; font-size: 14px;"><b>Alasan :</b> {item['alasan']}</p>
            </div>
            """, unsafe_allow_html=True)
            
    else:
        # Jika fakta kurang atau kombinasi tidak menghasilkan kesimpulan tertentu
        if len(fakta_aktif) < 2:
            st.warning("⚠️ Silakan pilih minimal 2 atau lebih kombinasi minatmu untuk mendapatkan rekomendasi yang lebih sesuai.")
        else:
            st.info("💡 Kombinasi peminatanmu sangat unik! Kami menyarankan untuk mengambil kelas General Studies atau berkonsultasi langsung dengan konselor akademik.")

# FOOTER
st.markdown("<br><hr><center style='color: #94A3B8; font-size: 12px;'>Sistem Pakar Pemilihan Jurusan</center>", unsafe_allow_html=True)