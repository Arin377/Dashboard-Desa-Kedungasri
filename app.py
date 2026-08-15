import streamlit as st
import os
import base64
from streamlit_option_menu import option_menu

# Konfigurasi Halaman (Harus selalu di paling atas)
st.set_page_config(page_title="Desa Kedungasri", page_icon="🏡", layout="wide")

# ==========================================
# FUNGSI GLOBAL (Bisa dipakai di semua menu)
# ==========================================
def get_image_base64(file_path):
    try:
        with open(file_path, "rb") as img_file:
            return f"data:image/jpeg;base64,{base64.b64encode(img_file.read()).decode()}"
    except FileNotFoundError:
        # Jika foto di folder belum ada, tampilkan gambar kosong sementara agar tidak error
        return "https://via.placeholder.com/300x400.png?text=Foto+Kosong"

# ==========================================
# SETUP SESSION STATE UNTUK NAVIGASI
# ==========================================
# Inisialisasi state agar aplikasi ingat menu apa yang sedang dibuka
if "menu_aktif" not in st.session_state:
    st.session_state.menu_aktif = "Gambaran Umum"

# Fungsi callback untuk memindahkan menu dari tombol
def pindah_menu(menu_tujuan):
    st.session_state.menu_aktif = menu_tujuan

# ==========================================
# CSS GLOBAL - DESAIN MODERN & INTERAKTIF (LOGO PALETTE)
# ==========================================
st.markdown("""
    <style>
    /* Gradient Text untuk Judul Utama */
    .hero-title { font-size: 55px !important; font-weight: 900; line-height: 1; margin-bottom: 0px; 
                  background: -webkit-linear-gradient(45deg, #18A924, #24A0ED); 
                  -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    
    .hero-subtitle { font-size: 65px !important; font-weight: 800; line-height: 1; color: #FF5E94; margin-top: -10px; margin-bottom: 20px; }
    
    .tag-lokasi { background-color: #E0F2FE; color: #0288D1; padding: 6px 14px; border-radius: 20px; font-weight: 700; font-size: 13px; display: inline-block; margin-bottom: 15px; border: 1px solid #BAE6FD; }
    
    /* Efek Hover (Melayang) pada semua Kartu/Box */
    .card-outline, .stat-box, .card-info-bottom, div[style*="border:1px solid"] { 
        transition: transform 0.3s ease, box-shadow 0.3s ease !important; 
    }
    .card-outline:hover, .stat-box:hover, .card-info-bottom:hover, div[style*="border:1px solid"]:hover { 
        transform: translateY(-5px); 
        box-shadow: 0 15px 30px -5px rgba(36, 160, 237, 0.15) !important; 
        border-color: #24A0ED !important;
    }
    
    .subtitle-green { color: #18A924; font-weight: 700; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }
    
    /* Styling Dasar Lainnya */
    .section-title-large { font-size: 40px; font-weight: 800; color: #1E293B; margin-bottom: 0; text-transform: uppercase; line-height: 1.1; }
    .section-title-light { font-size: 40px; font-weight: 300; color: #94A3B8; text-transform: uppercase; margin-top: 0px; margin-bottom: 25px; line-height: 1.1; }
    .stat-box { background-color: #FFFFFF; padding: 12px; border-radius: 10px; text-align: center; border: 1px solid #E2E8F0; }
    .stat-title { font-size: 11px; color: #64748B; text-transform: uppercase; font-weight: 700; letter-spacing: 0.5px; }
    .stat-value { font-size: 20px; font-weight: 700; color: #1E293B; }
    .stat-number-large { font-size: 32px; font-weight: 800; color: #1E293B; margin-bottom: -5px; margin-top: 10px; }
    .icon-circle { background-color: #F0FDF4; color: #18A924; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px; font-weight: bold; font-size: 18px; }
    .admin-box { background-color: #FFFFFF; padding: 10px 15px; border-radius: 10px; margin-top: 15px; border: 1px solid #E2E8F0; display: flex; justify-content: space-between; align-items: center; border-left: 4px solid #FFA900; }
    .teks-justify { text-align: justify; line-height: 1.6; color: #475569; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR MENU
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>Desa Kedungasri</h2>", unsafe_allow_html=True)
    st.markdown("---")

    # Menghapus "Galeri Kegiatan"
    daftar_menu = ["Gambaran Umum", "Sejarah", "Potensi Desa", "Risiko Geografis", "Daftar UMKM"]

    # --- TAMBAHKAN KODE PENGECEKAN INI ---
    # Jika menu yang tersimpan di memori tidak ada di daftar_menu yang baru, 
    # kembalikan ke menu awal ("Gambaran Umum") agar tidak error.
    if st.session_state.menu_aktif not in daftar_menu:
        st.session_state.menu_aktif = "Gambaran Umum"
    # -------------------------------------

    # Menyesuaikan index default dengan menu yang sedang aktif di session_state
    idx_default = daftar_menu.index(st.session_state.menu_aktif)

    menu_pilihan = option_menu(
        menu_title=None, 
        options=daftar_menu,
        # Menghapus ikon "images"
        icons=["house", "clock-history", "tree", "exclamation-triangle", "shop"], 
        default_index=idx_default,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#FFA900", "font-size": "18px"}, 
            "nav-link": {
                "font-size": "16px", 
                "text-align": "left", 
                "margin": "0px", 
                "border-radius": "10px",
                "transition": "all 0.3s ease",
                "--hover-color": "#E0F2FE" 
            },
            "nav-link-selected": {
                "background": "linear-gradient(90deg, #18A924, #24A0ED)", 
                "color": "white", 
                "font-weight": "bold",
                "box-shadow": "0 4px 6px rgba(0,0,0,0.1)"
            }, 
        }
    )

    # Jika user mengklik menu dari sidebar, perbarui session state dan refresh
    if menu_pilihan != st.session_state.menu_aktif:
        st.session_state.menu_aktif = menu_pilihan
        st.rerun()

    st.markdown("---")


# ==========================================
# KONDISI PENAMPILAN HALAMAN (Gunakan session_state.menu_aktif)
# ==========================================

# 1. GAMBARAN UMUM
if st.session_state.menu_aktif == "Gambaran Umum":

    col_kiri, col_kanan = st.columns([1.1, 1])

    with col_kiri:
        # Anda bisa mengubah nama Kabupaten/Kecamatan di bawah ini sesuai lokasi asli Kedungasri
        st.markdown('<span class="tag-lokasi">📍 RINGINARUM, KENDAL, JAWA TENGAH</span>', unsafe_allow_html=True)
        
        st.markdown('<p class="hero-title">DESA</p>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">KEDUNGASRI</p>', unsafe_allow_html=True)
        
        # Kata-kata pengantar baru untuk Kedungasri
        st.markdown("""
        <div class="teks-justify">
        Desa Kedungasri merupakan desa yang terletak di bagian selatan Kecamatan Ringinarum, Kabupaten Kendal, pada koordinat 7,0097° LS dan 110,1138° BT. Desa ini dikenal sebagai wilayah agraris dengan mayoritas masyarakat bermata pencaharian di sektor pertanian, terutama budidaya tembakau sebagai salah satu komoditas unggulan. Didukung oleh semangat gotong royong dan kebersamaan masyarakat, Desa Kedungasri terus berkembang dengan tetap menjaga potensi serta identitas desanya.
        </div>
        """, unsafe_allow_html=True)
        
        btn_kol1, btn_kol2 = st.columns([1, 1])
        
        # --- TAMBAHKAN BARIS INI AGAR TOMBOL TURUN KE BAWAH ---
        st.markdown("<br>", unsafe_allow_html=True)
        
        btn_kol1, btn_kol2 = st.columns([1, 1])
        
        # TOMBOL DIPERBARUI DENGAN PANAH KE KANAN
        with btn_kol1:
            st.button("Lihat Sejarah →", use_container_width=True, type="primary", on_click=pindah_menu, args=("Sejarah",))
        with btn_kol2:
            st.button("Potensi Desa", use_container_width=True, on_click=pindah_menu, args=("Potensi Desa",))

    with col_kanan:
        # 1. Gambar Utama 
        st.image("hero_desa.jpeg", use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 2. Grid Statistik Mini (3 Kolom) - Langsung tanpa kartu putih
        stat_col1, stat_col2, stat_col3 = st.columns(3)
        with stat_col1: 
            st.markdown('<div class="stat-box"><p class="stat-title">TOTAL PENDUDUK</p><p class="stat-value">3.200 <span style="font-size:12px; font-weight:normal; color:#64748B;">jiwa</span></p></div>', unsafe_allow_html=True)
        with stat_col2: 
            st.markdown('<div class="stat-box"><p class="stat-title">LUAS WILAYAH</p><p class="stat-value">4,07 <span style="font-size:12px; font-weight:normal; color:#64748B;">km²</span></p></div>', unsafe_allow_html=True)
        with stat_col3: 
            st.markdown('<div class="stat-box"><p class="stat-title">KEPADATAN PENDUDUK</p><p class="stat-value">136,17 <span style="font-size:11px; font-weight:normal; color:#64748B;">/km²</span></p></div>', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)

        # 3. Baris Wilayah Administratif
        st.markdown("""
            <div class="admin-box">
                <span style="color: #475569; font-weight: 600; font-size: 14px;">🏡 Wilayah Administratif</span>
                <span style="color: #1E293B; font-weight: 700; font-size: 14px;">3 RW &nbsp;|&nbsp; 15 RT</span>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    inf1, inf2, inf3 = st.columns(3)
    with inf1: st.markdown('<div class="card-info-bottom"><div class="icon-circle">🏢</div><div><strong style="font-size:16px;">Aktif</strong><br><span style="font-size:12px; color:#64748B;">KANTOR DESA<br>BUKA SENIN-JUMAT</span></div></div>', unsafe_allow_html=True)
    with inf2: st.markdown('<div class="card-info-bottom"><div class="icon-circle">🎓</div><div><strong style="font-size:16px;">5 Unit</strong><br><span style="font-size:12px; color:#64748B;">FASILITAS PENDIDIKAN<br>TK, SD, MI</span></div></div>', unsafe_allow_html=True)
    with inf3: st.markdown('<div class="card-info-bottom"><div class="icon-circle">🏥</div><div><strong style="font-size:16px;">1 Unit</strong><br><span style="font-size:12px; color:#64748B;">FASILITAS KESEHATAN<br>PUSKESMAS PEMBANTU</span></div></div>', unsafe_allow_html=True)

    st.markdown("<br><br><hr style='border-color:#E2E8F0;'><br>", unsafe_allow_html=True)

    st.markdown("""
        <div style="margin-bottom: 20px;">
            <p style="color: #18A924; font-weight: 700; font-size: 16px; letter-spacing: 1px; margin-bottom: 15px; text-transform: uppercase;">
                // GEOGRAFIS 
            </p>
            <p style="font-size: 42px; font-weight: 900; color: #1E293B; margin-bottom: 0px; padding-bottom: 0px; line-height: 1.1;">
                PETA
            </p>
            <p style="font-size: 42px; font-weight: 300; color: #94A3B8; margin-top: 0px; padding-top: 0px; line-height: 1.1;">
                ADMINISTRASI 
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.image("peta_administrasi.jpg", caption="Peta Wilayah Administrasi Desa Kedungasri", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.divider()
    
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <p style="color: #18A924; font-weight: 700; font-size: 16px; letter-spacing: 1px; margin-bottom: 15px; text-transform: uppercase;">
                // DEMOGRAFIS
            </p>
            <p style="font-size: 42px; font-weight: 900; color: #1E293B; margin-bottom: 0px; padding-bottom: 0px; line-height: 1.1;">
                STATISTIK 
            </p>
            <p style="font-size: 42px; font-weight: 300; color: #94A3B8; margin-top: 0px; padding-top: 0px; line-height: 1.1;">
                PENDUDUK DESA 
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    baris1_kol1, baris1_kol2, baris1_kol3 = st.columns(3)
    baris2_kol1, baris2_kol2, baris2_kol3 = st.columns(3)

    def buat_kartu_stat(icon, num, title, desc):
        return f"""
        <div class="card-outline" style="margin-bottom:20px;">
            <div class="icon-circle" style="width:30px; height:30px; font-size:14px;">{icon}</div>
            <p class="stat-number-large">{num}</p>
            <p style="font-size:14px; font-weight:600; color:#475569; margin-bottom:0;">{title}</p>
            <p style="font-size:12px; color:#94A3B8; margin-top:0;">{desc}</p>
        </div>
        """

    with baris1_kol1: st.markdown(buat_kartu_stat("👥", "3.200 jiwa", "Total Penduduk", "Data terverifikasi semester I"), unsafe_allow_html=True)
    with baris1_kol2: st.markdown(buat_kartu_stat("👨", "1.670 jiwa", "Penduduk Laki-laki", "Estimasi dari total populasi"), unsafe_allow_html=True)
    with baris1_kol3: st.markdown(buat_kartu_stat("👩", "1.530 jiwa", "Penduduk Perempuan", "Estimasi dari total populasi"), unsafe_allow_html=True)
    with baris2_kol1: st.markdown(buat_kartu_stat("🌍", "136,17", "Kepadatan Penduduk", "Rasio jiwa per kilometer persegi"), unsafe_allow_html=True)
    with baris2_kol2: st.markdown(buat_kartu_stat("📈", "70,14%", "Usia Produktif", "Penduduk berumur 15-64 tahun"), unsafe_allow_html=True)
    with baris2_kol3: st.markdown(buat_kartu_stat("🎓", "9,10%", "Tingkat Pendidikan", "Warga tamat SLTA / Sederajat"), unsafe_allow_html=True)
    st.markdown("<br><hr style='border-color:#E2E8F0;'><br>", unsafe_allow_html=True)

    st.markdown("""
        <div style="margin-bottom: 20px;">
            <p style="color: #18A924; font-weight: 700; font-size: 16px; letter-spacing: 1px; margin-bottom: 15px; text-transform: uppercase;">
                // APARAT DESA
            </p>
            <p style="font-size: 42px; font-weight: 900; color: #1E293B; margin-bottom: 0px; padding-bottom: 0px; line-height: 1.1;">
                STRUKTUR 
            </p>
            <p style="font-size: 42px; font-weight: 300; color: #94A3B8; margin-top: 0px; padding-top: 0px; line-height: 1.1;">
                PERANGKAT DESA 
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    def get_image_base64(file_path):
            try:
                with open(file_path, "rb") as img_file:
                    return f"data:image/jpeg;base64,{base64.b64encode(img_file.read()).decode()}"
            except FileNotFoundError:
                # Jika foto di folder belum ada, akan menampilkan gambar kosong sementara
                return "https://via.placeholder.com/300x400.png?text=Foto+Kosong"

    # 3. Fungsi cetakan HTML Profil
    def profil_html(url_foto, jabatan, nama):
            return f"""
            <div class="card-outline" style="padding:10px; text-align:center; height: 100%;">
                <img src="{url_foto}" style="width:100%; border-radius:6px; height:200px; object-fit:cover; margin-bottom:12px;">
                <p style="font-size:11px; color:#18A924; font-weight:bold; margin-bottom:0; letter-spacing:0.5px;">{jabatan}</p>
                <p style="font-size:15px; font-weight:800; color:#1E293B; margin-bottom:2px; margin-top:2px;">{nama}</p>
                <p style="font-size:11px; color:#94A3B8; margin-top:0;">Masa Bakti Aktif</p>
            </div>
            """

    # --- BARIS 1 (3 KOLOM) ---
    p1, p2, p3 = st.columns(3)
    with p1: 
            st.markdown(profil_html(get_image_base64("kades.jpeg"), "KEPALA DESA", "Heru Susanto"), unsafe_allow_html=True)
    with p2: 
            st.markdown(profil_html(get_image_base64("sekdes.jpeg"), "SEKRETARIS DESA", "Zakiyatul Fakhiroh"), unsafe_allow_html=True)
    with p3: 
            st.markdown(profil_html(get_image_base64("bendahara.jpeg"), "BENDAHARA DESA", "Askuri"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True) # Jarak antar baris

    # --- BARIS 2 (4 KOLOM) ---
    p4, p5, p6, p7 = st.columns(4)
    with p4: 
            st.markdown(profil_html(get_image_base64("kesejahteraan.jpg"), "KASI KESEJAHTERAAN", "Zaenuri"), unsafe_allow_html=True)
    with p5: 
            st.markdown(profil_html(get_image_base64("kosong.png"), "KASI PEMERINTAHAN", "-"), unsafe_allow_html=True)
    with p6: 
            st.markdown(profil_html(get_image_base64("pelayanan.jpg"), "KASI PELAYANAN", "Solikin"), unsafe_allow_html=True)
    with p7: 
            st.markdown(profil_html(get_image_base64("kaur_tu.jpeg"), "KAUR TU & UMUM", "Teguh Sulistiono"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True) # Jarak antar baris

    # --- BARIS 3 (4 KOLOM) ---
    p8, p9, p10, p11 = st.columns(4)
    with p8: 
            st.markdown(profil_html(get_image_base64("perencanaan.jpeg"), "KAUR PERENCANAAN", "Wahyu Eko Prasetiyo, S.Pd"), unsafe_allow_html=True)
    with p9: 
            st.markdown(profil_html(get_image_base64("kadus1.jpeg"), "KEPALA DUSUN 1", "Ahmad Sobirin"), unsafe_allow_html=True)
    with p10: 
            st.markdown(profil_html(get_image_base64("kadus2.jpg"), "KEPALA DUSUN 2", "Suharto"), unsafe_allow_html=True)
    with p11: 
            st.markdown(profil_html(get_image_base64("kosong.png"), "KEPALA DUSUN 3", "-"), unsafe_allow_html=True)

    st.markdown("<br><br><hr style='border-color:#E2E8F0;'><br>", unsafe_allow_html=True)

    st.markdown("""
        <div style="margin-bottom: 20px;">
            <p style="color: #18A924; font-weight: 700; font-size: 16px; letter-spacing: 1px; margin-bottom: 15px; text-transform: uppercase;">
                // HUBUNGI KAMI
            </p>
            <p style="font-size: 42px; font-weight: 900; color: #1E293B; margin-bottom: 0px; padding-bottom: 0px; line-height: 1.1;">
                LOKASI &
            </p>
            <p style="font-size: 42px; font-weight: 300; color: #94A3B8; margin-top: 0px; padding-top: 0px; line-height: 1.1;">
                KONTAK RESMI
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    kol_peta, kol_form = st.columns([1.2, 1])
    
    with kol_peta:
        # Peta tampil tanpa kotak (sesuai permintaan sebelumnya)
        st.markdown("""
        <iframe src="https://maps.google.com/maps?q=Desa+Kedungasri,+Ringinarum,+Kendal,+Jawa+Tengah&t=&z=14&ie=UTF8&iwloc=&output=embed" 
        width="100%" height="320" style="border:0; border-radius:6px;" allowfullscreen="" loading="lazy"></iframe>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with kol_form:
        st.markdown("<h4 style='margin-top:0; color:#1E293B;'>Alamat Sekretariat</h4>", unsafe_allow_html=True)
        st.write("📍 Balai Desa Kedungasri, Kec. Ringinarum, Kab. Kendal, Jawa Tengah, Kode Pos 51356.")
        st.write("✉️ **Email:** pemdeskedungasri02@gmail.com")
        st.markdown('</div>', unsafe_allow_html=True)

# 2. SEJARAH
elif st.session_state.menu_aktif == "Sejarah":
    st.markdown('<p class="subtitle-green" style="color:#18A924;font-weight:bold;">// HISTORI DESA</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:40px;font-weight:800;color:#1E293B;margin-bottom:30px;">SEJARAH</p><p style="font-size:40px;font-weight:300;color:#94A3B8;margin-top:-40px;">DESA KEDUNGASRI</p>', unsafe_allow_html=True)
    
    # Membagi layout menjadi 2 kolom (Kiri 60% teks, Kanan 40% timeline)
    col_kiri, col_kanan = st.columns([1.5, 1])
    
    with col_kiri:
        # --- BAGIAN TEKS NARASI UTAMA (KIRI) DENGAN FITUR SCROLL ---
        st.markdown("""
<div style="background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; height: 1050px; overflow-y: auto;">

<h4 style="color: #1E293B; font-weight: 800; margin-bottom: 10px; margin-top: 0; font-size: 18px;">1. Asal-usul Desa Kedungasri</h4>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 15px;">
Sejarah Desa Kedungasri menunjukkan bahwa keberadaan wilayah ini telah memiliki akar sejarah yang panjang. Berdasarkan peta topografi Hindia Belanda, nama Kedoeng-sari atau Kedungsari telah tercatat setidaknya sejak abad ke-19. Nama tersebut kemudian tetap muncul dalam sejumlah peta pada awal abad ke-20, sebelum ditemukan bentuk Kedoengasri pada dekade 1920-an. Nama Kedungasri selanjutnya muncul dalam Bataviaasch Nieuwsblad tahun 1923 dalam pemberitaan mengenai banjir di wilayah Kendal. Sejarah lisan masyarakat juga menyebut bahwa nama Kedungasri telah dikenal dan digunakan oleh masyarakat sekitar dekade 1920-an.
</p>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 15px;">
Asal-usul nama Kedungasri dalam ingatan masyarakat berkaitan dengan keberadaan sebuah kedung di salah satu bagian aliran Sungai Blukar. Kedung dipahami sebagai bagian sungai yang berbentuk cekungan dan lebih dalam sehingga airnya relatif tetap tersedia pada musim kemarau. Unsur tersebut kemudian dipercaya berkaitan dengan pemberian nama Kedungasri. Keterangan mengenai asal-usul nama tersebut merupakan bagian dari legenda dan sejarah lisan masyarakat sehingga tidak dapat dijadikan satu-satunya dasar untuk menentukan etimologi nama desa. Namun, cerita tersebut memperlihatkan hubungan yang kuat antara identitas wilayah dengan kondisi lingkungan yang dikenal oleh masyarakat.
</p>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 25px;">
Perkembangan toponim juga dapat ditelusuri melalui perbandingan dengan wilayah di sekitarnya. Nama-nama seperti Ngerjo, Sojomerto, Cabean, Rowobranten, dan Kedunggading telah ditemukan dalam sumber kartografis kolonial dan masih dapat dikenali dalam lanskap wilayah sekarang. Kesamaan nama dan posisi relatif antarlokasi membantu mengidentifikasi bahwa Kedungsari yang tercatat dalam sumber kolonial merupakan bagian dari kawasan yang secara geografis berhubungan dengan wilayah Kedungasri sekarang. Meskipun demikian, belum ditemukan dokumen yang secara pasti menetapkan tahun berdirinya Desa Kedungasri. Data mengenai pemerintahan menunjukkan bahwa struktur kepemimpinan desa telah dapat ditelusuri setidaknya sejak 1927, ketika Sumowijoyo disebut sebagai kepala desa.
</p>

<h4 style="color: #1E293B; font-weight: 800; margin-bottom: 10px; font-size: 18px;">2. Sejarah Pemerintahan, Perubahan Administrasi, dan Infrastruktur</h4>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 15px;">
Perjalanan pemerintahan Desa Kedungasri dapat ditelusuri secara terbatas melalui data kepemimpinan desa. Sumowijoyo tercatat menjabat pada 1927–1937, kemudian data untuk periode 1937–1950 belum berhasil ditemukan. Abdul Karnen tercatat menjabat pada 1950–1966, dilanjutkan oleh Sukaeri (1969–1989), Ahmad Damiri (1989–1999), Abdul Rauf (1999–2000), Ahmad Damiri kembali (2000–2005), Achmad Sholichin (2005–2010), Achmad Supriyanto (2010–2015), dan Heru Susanto (2022–2029). Rangkaian tersebut masih merupakan rekonstruksi berdasarkan sumber yang berhasil dihimpun dan beberapa periodenya masih memerlukan verifikasi melalui arsip pemerintahan.
</p>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 15px;">
Pada masa awal kemerdekaan, terdapat pula ingatan masyarakat mengenai penggunaan nama Kedungsari dan Ndasri serta kemungkinan adanya perbedaan wilayah dan kepemimpinan. Namun, informasi mengenai hubungan atau penyatuan kedua wilayah tersebut belum dapat dikonfirmasi melalui dokumen administratif sezaman. Oleh karena itu, keterangan tersebut ditempatkan sebagai bagian dari sejarah lisan dan belum digunakan untuk menetapkan perubahan administrasi secara pasti.
</p>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 15px;">
Perubahan administratif yang dapat dipastikan terjadi pada masa Reformasi adalah pembentukan Kecamatan Ringinarum pada tahun 2002 melalui pemekaran dari Kecamatan Gemuh. Sebelum pemekaran tersebut, Desa Kedungasri merupakan bagian dari Kecamatan Gemuh. Perubahan ini menempatkan Kedungasri dalam struktur pemerintahan kecamatan yang berbeda dari periode sebelumnya.
</p>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 25px;">
Perkembangan infrastruktur berlangsung secara bertahap sesuai kebutuhan masyarakat. Keterbatasan air bersih menjadi salah satu persoalan penting karena Desa Kedungasri tidak memiliki sumber mata air alami yang besar. Kebutuhan tersebut kemudian diupayakan melalui PAMSIMAS, dengan sumber air yang berkaitan dengan daerah resapan di sekitar Sungai Blukar. Jaringan jalan desa juga mengalami perbaikan secara bertahap, terutama sejak berbagai program pembangunan masyarakat mulai dilaksanakan. Selain itu, jaringan irigasi diperbaiki sekitar 2009 untuk mendukung pengairan pertanian, sedangkan embung dibangun sekitar 2014 sebagai bagian dari upaya penyediaan cadangan air pertanian. Infrastruktur tersebut berfungsi untuk mendukung kebutuhan masyarakat dan kegiatan pertanian, bukan sebagai faktor utama pembentukan pola permukiman desa.
</p>

<h4 style="color: #1E293B; font-weight: 800; margin-bottom: 10px; font-size: 18px;">3. Perkembangan Komoditas Pertanian</h4>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 15px;">
Pertanian merupakan bagian penting dalam sejarah kehidupan masyarakat Desa Kedungasri. Kondisi geografis desa yang berada di kawasan dataran rendah dan berhubungan dengan jaringan Sungai Blukar serta saluran irigasi mendukung berkembangnya kegiatan pertanian. Pada masa awal, masyarakat terutama mengusahakan tanaman pangan seperti padi, singkong, dan tanaman pangan lainnya. Kehidupan pertanian masih menggunakan peralatan sederhana dan banyak mengandalkan tenaga manusia serta hewan.
</p>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 15px;">
Memasuki dekade 1980-an, pertanian Kedungasri mengalami diversifikasi komoditas. Data Kecamatan Gemuh Dalam Angka tahun 1987 mencatat 69,50 hektare lahan tembakau rakyat dan 11,68 hektare lahan tebu di Desa Kedungasri. Keberadaan kedua komoditas tersebut menunjukkan bahwa pertanian desa tidak hanya digunakan untuk memenuhi kebutuhan pangan, tetapi juga telah berkembang menuju komoditas yang memiliki nilai ekonomi dan berhubungan dengan pasar.
</p>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 15px;">
Tebu kemudian mengalami kemunduran. Data tahun 1992 menunjukkan bahwa tebu tidak lagi tercatat sebagai komoditas pertanian Kedungasri. Berdasarkan wawancara dengan masyarakat, sebelumnya hasil tebu masyarakat dikirim ke Pabrik Gula Cepiring, tetapi kemudian kemampuan pabrik dalam menampung hasil panen disebut semakin terbatas. Keterangan tersebut merupakan sejarah lisan dan belum diperkuat arsip pabrik, sehingga tidak dapat digunakan sebagai penyebab yang telah terbukti secara pasti. Sementara itu, tembakau juga mengalami penurunan pada awal dekade 1990-an. Berdasarkan wawancara, perubahan cuaca memengaruhi kualitas tembakau sehingga sebagian hasil panen tidak memenuhi standar pembelian dan pemasaran menjadi semakin sulit.
</p>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 15px;">
Perubahan tersebut kemudian diikuti oleh berkembangnya bawang merah. Data statistik Kecamatan Gemuh pada sekitar 1991–1992 telah menunjukkan bahwa bawang merah telah dibudidayakan di beberapa desa dalam wilayah kecamatan tersebut, meskipun belum menyebut Kedungasri secara khusus. Berdasarkan sejarah lisan, sekitar 1995 petani dari Brebes datang ke Kedungasri dan menyewa lahan untuk menanam bawang merah. Interaksi tersebut kemudian menjadi salah satu sarana masyarakat setempat mengenal teknik budidaya bawang merah. Karena informasi mengenai tahun 1995 hanya berasal dari wawancara, tahun tersebut dipahami sebagai perkiraan berdasarkan ingatan masyarakat.
</p>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 25px;">
Bukti tertulis mengenai perkembangan bawang merah di Kedungasri semakin jelas melalui data BPS tahun 1999, yang mencatat lahan bawang merah seluas 22 hektare dengan produksi mencapai 176,00 ton. Rangkaian data tersebut menunjukkan bahwa pertanian Kedungasri mengalami perubahan dari tebu dan tembakau menuju bawang merah sebagai salah satu komoditas penting pada akhir masa Orde Baru. Perubahan tersebut mencerminkan kemampuan masyarakat menyesuaikan kegiatan pertanian dengan kondisi produksi, pemasaran, serta peluang ekonomi yang tersedia.
</p>

<h4 style="color: #1E293B; font-weight: 800; margin-bottom: 10px; font-size: 18px;">4. Perkembangan Mata Pencaharian dan Kehidupan Masyarakat</h4>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 15px;">
Perubahan pertanian turut memengaruhi kehidupan ekonomi masyarakat. Meskipun pertanian tetap menjadi bagian penting dari kehidupan Desa Kedungasri, sejak akhir masa pembangunan mulai berkembang sumber penghasilan di luar sektor pertanian. Sebagian laki-laki bekerja sebagai buruh proyek di kota-kota besar, terutama secara musiman setelah musim tanam selesai. Sebagian perempuan juga mulai bekerja sebagai pekerja migran di luar negeri. Pada masa Reformasi, berdasarkan keterangan sejumlah warga dan pengurus desa, minat generasi muda untuk bekerja ke luar negeri semakin berkembang, dengan Jepang dan Korea Selatan disebut sebagai beberapa negara tujuan. Informasi tersebut merupakan sejarah lisan dan belum didukung data statistik tingkat desa sehingga lebih tepat dipahami sebagai kecenderungan yang diketahui masyarakat, bukan gambaran seluruh pekerja migran Kedungasri.
</p>
<p style="text-align: justify; color: #475569; font-size: 14px; line-height: 1.7; margin-bottom: 15px;">
Perubahan tersebut menunjukkan bahwa masyarakat Kedungasri tidak meninggalkan pertanian secara langsung, tetapi mengembangkan berbagai strategi untuk memperoleh pendapatan. Pertanian, pekerjaan di luar desa, serta migrasi tenaga kerja kemudian berjalan berdampingan sebagai bagian dari kehidupan ekonomi masyarakat. Di sisi lain, hubungan sosial dan kehidupan masyarakat tetap dipengaruhi oleh lingkungan desa, terutama lahan pertanian dan jaringan pengairan. Saluran irigasi tidak hanya mendukung kegiatan pertanian, tetapi pada beberapa titik juga menjadi bagian dari akses antardusun, seperti jembatan yang menghubungkan Dusun Krajan dan Dusun Tegalsari.
</p>
<div style="background-color: #F8FAFC; border-left: 4px solid #18A924; padding: 15px; border-radius: 4px;">
<p style="text-align: justify; color: #334155; font-size: 13.5px; line-height: 1.6; margin: 0; font-style: italic;">
"Dengan demikian, sejarah Desa Kedungasri memperlihatkan adanya kesinambungan sekaligus perubahan. Identitas Kedungsari yang telah dikenal sejak masa kolonial masih bertahan sebagai nama dusun, sementara Kedungasri berkembang sebagai identitas administratif. Keseluruhan perjalanan tersebut memperlihatkan kemampuan masyarakat dalam mempertahankan identitas lokal sekaligus beradaptasi terhadap perubahan ekonomi, lingkungan, administrasi, dan sosial dari masa ke masa."
</p>
</div>

</div>
        """, unsafe_allow_html=True)

    with col_kanan:
        # --- BAGIAN TIMELINE GARIS WAKTU (KANAN) ---
        st.markdown("""
<div style="border: 1px solid #E2E8F0; border-radius: 12px; overflow: hidden; background-color: #FFFFFF; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; height: 1050px;">
<h3 style="color: #1E293B; font-weight: 800; margin-top: 0; margin-bottom: 25px; font-size:20px;">Garis Waktu (Timeline)</h3>

<!-- Timeline Abad 19 -->
<div style="display: flex; gap: 15px; margin-bottom: 15px; border-bottom: 1px dashed #E2E8F0; padding-bottom: 15px;">
<div style="flex-shrink: 0; width: 85px;">
<span style="background-color: #D1FAE5; color: #065F46; padding: 4px 10px; border-radius: 20px; font-weight: bold; font-size: 12px;">Abad 19</span>
</div>
<div>
<strong style="color: #1E293B; font-size: 14px; display: block; margin-bottom: 3px;">Peta Kolonial</strong>
<p style="color: #475569; font-size: 13px; margin: 0; line-height: 1.5;">Nama Kedoeng-sari / Kedungsari tercatat di peta topografi Hindia Belanda.</p>
</div>
</div>

<!-- Timeline 1923 -->
<div style="display: flex; gap: 15px; margin-bottom: 15px; border-bottom: 1px dashed #E2E8F0; padding-bottom: 15px;">
<div style="flex-shrink: 0; width: 85px;">
<span style="background-color: #D1FAE5; color: #065F46; padding: 4px 10px; border-radius: 20px; font-weight: bold; font-size: 12px;">1920 & 1923</span>
</div>
<div>
<strong style="color: #1E293B; font-size: 14px; display: block; margin-bottom: 3px;">Kedoengasri</strong>
<p style="color: #475569; font-size: 13px; margin: 0; line-height: 1.5;">Nama Kedoengasri muncul pertama kali pada peta Hindia Belanda dan koran Bataviaasch Nieuwsblad.</p>
</div>
</div>

<!-- Timeline 1927 -->
<div style="display: flex; gap: 15px; margin-bottom: 15px; border-bottom: 1px dashed #E2E8F0; padding-bottom: 15px;">
<div style="flex-shrink: 0; width: 85px;">
<span style="background-color: #D1FAE5; color: #065F46; padding: 4px 10px; border-radius: 20px; font-weight: bold; font-size: 12px;">1927</span>
</div>
<div>
<strong style="color: #1E293B; font-size: 14px; display: block; margin-bottom: 3px;">Kepemimpinan Awal</strong>
<p style="color: #475569; font-size: 13px; margin: 0; line-height: 1.5;">Struktur kepemimpinan desa mulai ditelusuri dengan Sumowijoyo sebagai kades.</p>
</div>
</div>

<!-- Timeline 1987 -->
<div style="display: flex; gap: 15px; margin-bottom: 15px; border-bottom: 1px dashed #E2E8F0; padding-bottom: 15px;">
<div style="flex-shrink: 0; width: 85px;">
<span style="background-color: #FEF3C7; color: #92400E; padding: 4px 10px; border-radius: 20px; font-weight: bold; font-size: 12px;">1987</span>
</div>
<div>
<strong style="color: #1E293B; font-size: 14px; display: block; margin-bottom: 3px;">Tebu & Tembakau</strong>
<p style="color: #475569; font-size: 13px; margin: 0; line-height: 1.5;">Diversifikasi pertanian: tercatat 69,5 ha lahan tembakau dan 11,68 ha lahan tebu.</p>
</div>
</div>

<!-- Timeline 1992 -->
<div style="display: flex; gap: 15px; margin-bottom: 15px; border-bottom: 1px dashed #E2E8F0; padding-bottom: 15px;">
<div style="flex-shrink: 0; width: 85px;">
<span style="background-color: #FEE2E2; color: #991B1B; padding: 4px 10px; border-radius: 20px; font-weight: bold; font-size: 12px;">1992</span>
</div>
<div>
<strong style="color: #1E293B; font-size: 14px; display: block; margin-bottom: 3px;">Perubahan Komoditas</strong>
<p style="color: #475569; font-size: 13px; margin: 0; line-height: 1.5;">Tebu tidak lagi tercatat dan tembakau menurun karena faktor cuaca & pasar.</p>
</div>
</div>

<!-- Timeline 1995 -->
<div style="display: flex; gap: 15px; margin-bottom: 15px; border-bottom: 1px dashed #E2E8F0; padding-bottom: 15px;">
<div style="flex-shrink: 0; width: 85px;">
<span style="background-color: #F3E8FF; color: #6B21A8; padding: 4px 10px; border-radius: 20px; font-weight: bold; font-size: 12px;">± 1995</span>
</div>
<div>
<strong style="color: #1E293B; font-size: 14px; display: block; margin-bottom: 3px;">Masuknya Bawang Merah</strong>
<p style="color: #475569; font-size: 13px; margin: 0; line-height: 1.5;">Petani dari Brebes menyewa lahan, mengenalkan teknik budidaya bawang merah ke warga lokal.</p>
</div>
</div>

<!-- Timeline 1999 & Reformasi -->
<div style="display: flex; gap: 15px; margin-bottom: 15px; border-bottom: 1px dashed #E2E8F0; padding-bottom: 15px;">
<div style="flex-shrink: 0; width: 85px;">
<span style="background-color: #E0E7FF; color: #3730A3; padding: 4px 10px; border-radius: 20px; font-weight: bold; font-size: 12px;">1999</span>
</div>
<div>
<strong style="color: #1E293B; font-size: 14px; display: block; margin-bottom: 3px;">Era Reformasi & Perantauan</strong>
<p style="color: #475569; font-size: 13px; margin: 0; line-height: 1.5;">Warga yang menjadi PMI ke timur tengah menjadi penopang perekonomian desa.</p>
</div>
</div>

<!-- Timeline 2002 -->
<div style="display: flex; gap: 15px; margin-bottom: 15px; border-bottom: 1px dashed #E2E8F0; padding-bottom: 15px;">
<div style="flex-shrink: 0; width: 85px;">
<span style="background-color: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 20px; font-weight: bold; font-size: 12px;">2002</span>
</div>
<div>
<strong style="color: #1E293B; font-size: 14px; display: block; margin-bottom: 3px;">Pemekaran Kecamatan</strong>
<p style="color: #475569; font-size: 13px; margin: 0; line-height: 1.5;">Pembentukan Kec. Ringinarum dari pemekaran Kec. Gemuh.</p>
</div>
</div>

</div>
        """, unsafe_allow_html=True)

# 3. POTENSI DESA
elif st.session_state.menu_aktif == "Potensi Desa":
    st.markdown('<p style="color:#18A924;font-weight:bold;">// SUMBER DAYA ALAM & MANUSIA</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:40px;font-weight:800;color:#1E293B;margin-bottom:0;">POTENSI</p><p style="font-size:40px;font-weight:300;color:#94A3B8;margin-top:-10px;">UNGGULAN DESA</p>', unsafe_allow_html=True)
    st.write("Desa Kedungasri menyimpan berbagai potensi luar biasa, mulai dari kekayaan alam, sektor agraris, hingga kekuatan sosial bermasyarakat yang menjadi pilar utama kemajuan desa.")
    st.markdown("<br>", unsafe_allow_html=True)

    # Fungsi pembuat kartu potensi (Gambar Atas, Teks Bawah, Judul Tengah)
    def kartu_potensi(gambar, judul, deskripsi):
        return f"""
<div style="border: 1px solid #E2E8F0; border-radius: 12px; padding: 25px; margin-bottom: 30px; background-color: #fff; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
<img src="{gambar}" style="width: 100%; aspect-ratio: 16/9; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0; margin-bottom: 20px;">
<h3 style="color: #1E293B; margin-top: 0; margin-bottom: 15px; font-weight: 800; text-align: center;">{judul}</h3>
<p style="text-align: justify; color: #475569; font-size: 15px; line-height: 1.6; margin: 0;">{deskripsi}</p>
</div>
        """

    # 1. Potensi Pertanian
    st.markdown(kartu_potensi(
        get_image_base64("pertanian.jpeg"), 
        "🌾 Potensi Sektor Pertanian", 
        "Sektor pertanian merupakan salah satu potensi unggulan Desa Kedungasri sekaligus menjadi penopang utama perekonomian masyarakat. Kegiatan pertanian di desa ini didukung oleh jaringan irigasi yang menjaga ketersediaan air sepanjang musim. Pada lahan sawah beririgasi, petani umumnya menerapkan rotasi tanaman dengan menanam komoditas secara bergantian, seperti bawang merah, jagung, tembakau, maupun tanaman lain sesuai musim, kondisi lahan, dan pertimbangan fluktuasi harga komoditas di lapangan. Selain itu, sebagian petani menerapkan sistem agroforestri, yaitu metode pengelolaan lahan yang mengintegrasikan tanaman berkayu dengan tanaman pertanian secara terencana. Praktik ini dijumpai di beberapa lahan di Dusun Jatigowok melalui kombinasi pohon jati dan tanaman jagung. Beragam praktik budidaya tersebut menunjukkan kemampuan masyarakat dalam mengoptimalkan potensi lahan sekaligus menjaga produktivitas pertanian sehingga sektor pertanian tetap menjadi penggerak utama perekonomian Desa Kedungasri.<br><br><b>Sumber:</b> Agriculture Journal IJOEAR. (2026, July 17). Agroforestry and Intercropping Systems: A Practical and Research-Oriented Guide. Agriculture Journal IJOEAR. https://ijoear.com/blog/agroforestry-and-intercropping-systems-a-practical-and-research-oriented-guide"
    ), unsafe_allow_html=True)

    # 2. Lanskap & Rekreasi
    st.markdown(kartu_potensi(
        get_image_base64("lanskap.jpeg"), 
        "🏞️ Lanskap Pedesaan dan Rekreasi Alam", 
        "Desa Kedungasri memiliki lanskap pedesaan yang didominasi oleh hamparan sawah dan lahan pertanian yang membentang luas. Keindahan panorama tersebut menghadirkan suasana yang asri dan menenangkan, terutama pada pagi dan sore hari, sehingga menjadi daya tarik tersendiri bagi masyarakat maupun pengunjung. Didukung oleh akses jalan yang melintasi area persawahan, kawasan ini memiliki potensi untuk dikembangkan sebagai ruang rekreasi berbasis alam, seperti jalur jogging dan bersepeda. Selain dimanfaatkan sebagai sarana rekreasi, lanskap pedesaan Desa Kedungasri juga berpotensi menjadi lokasi penyelenggaraan berbagai kegiatan berbasis komunitas, seperti fun bike, fun run, jalan sehat, maupun festival desa yang dapat memperkenalkan potensi lokal sekaligus mendorong aktivitas ekonomi masyarakat."
    ), unsafe_allow_html=True)

    # 3. Sosial & Keagamaan
    st.markdown(kartu_potensi(
        get_image_base64("sosial_agama.jpeg"), 
        "🕌 Kehidupan Sosial dan Keagamaan", 
        "Desa Kedungasri memiliki kehidupan sosial dan keagamaan yang kuat, tercermin dari tingginya partisipasi masyarakat dalam berbagai kegiatan keagamaan yang diselenggarakan secara rutin. Kegiatan seperti pengajian, sholawatan, tahlilan, serta peringatan hari-hari besar keagamaan menjadi wadah untuk mempererat hubungan antarwarga sekaligus menjaga nilai-nilai kebersamaan dan gotong royong. Selain itu, Desa Kedungasri juga dikenal sebagai tempat tinggal beberapa tokoh agama yang memiliki pengaruh di masyarakat, salah satunya Gus Ambyar sehingga turut memperkuat peran desa sebagai lingkungan yang aktif dalam kegiatan keagamaan. Modal sosial yang kuat ini menjadi potensi penting dalam mendukung pembangunan desa berbasis partisipasi masyarakat serta menjaga keharmonisan kehidupan bermasyarakat."
    ), unsafe_allow_html=True)

    # ==========================================
    # TAMBAHAN: FUN FACT / FAKTA MENARIK
    # ==========================================
    st.markdown("<br>", unsafe_allow_html=True)
    st.divider() # Garis pembatas
    
    st.markdown('<p style="color:#18A924;font-weight:bold;">// TAHUKAH ANDA?</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:40px;font-weight:800;color:#1E293B;margin-bottom:20px;">FAKTA MENARIK</p><p style="font-size:40px;font-weight:300;color:#94A3B8;margin-top:-30px;">DESA KEDUNGASRI</p>', unsafe_allow_html=True)

    # Membagi Fun Fact menjadi 2 kolom
    f1, f2 = st.columns(2)
    
    with f1:
        st.markdown(f"""
<div class="card-outline" style="border: 1px solid #BAE6FD; border-radius: 8px; background-color: #F0F9FF; height: 100%; overflow: hidden; display: flex; flex-direction: column;">
<img src="{get_image_base64("memanjang.jpeg")}" style="width: 100%; height: 200px; object-fit: cover;">
<div style="padding: 20px;">
<strong style="color: #0284C7; font-size: 18px;">🌊 Pemukiman Memanjang Aliran Sungai</strong>
<p style="text-align: justify; color: #334155; font-size: 14.5px; margin-top: 10px; line-height: 1.6; margin-bottom: 0;">
Salah satu keunikan Desa Kedungasri adalah pola permukimannya yang memanjang mengikuti aliran sungai. Karakteristik geografis ini membentuk tata ruang desa yang berbeda dibandingkan desa dengan permukiman yang mengelompok pada satu pusat kawasan.
</p>
</div>
</div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown(f"""
<div class="card-outline" style="border: 1px solid #BAE6FD; border-radius: 8px; background-color: #F0F9FF; height: 100%; overflow: hidden; display: flex; flex-direction: column;">
<img src="{get_image_base64("jatigowok.jpg")}" style="width: 100%; height: 200px; object-fit: cover;">
<div style="padding: 20px;">
<strong style="color: #0284C7; font-size: 18px;">🌳 Jatigowok, Dusun di Tengah Hutan</strong>
<p style="text-align: justify; color: #334155; font-size: 14.5px; margin-top: 10px; line-height: 1.6; margin-bottom: 0;">
Salah satu keunikan Desa Kedungasri adalah keberadaan Dusun Jatigowok yang terletak di tengah kawasan hutan. Kondisi ini menjadikan Jatigowok memiliki lanskap yang berbeda dibandingkan dusun-dusun lainnya.
</p>
</div>
</div>
        """, unsafe_allow_html=True)

# 4. Risiko Geografis
elif st.session_state.menu_aktif == "Risiko Geografis":
    # Judul Bagian (Menggunakan style rapi yang seragam)
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <p style="color: #18A924; font-weight: 700; font-size: 16px; letter-spacing: 1px; margin-bottom: 15px; text-transform: uppercase;">
                // KESELAMATAN BERSAMA
            </p>
            <p style="font-size: 42px; font-weight: 900; color: #1E293B; margin-bottom: 0px; padding-bottom: 0px; line-height: 1.1;">
                RISIKO
            </p>
            <p style="font-size: 42px; font-weight: 300; color: #94A3B8; margin-top: 0px; padding-top: 0px; line-height: 1.1;">
                GEOGRAFIS 
            </p>
        </div>
    """, unsafe_allow_html=True)

    # MEMBUAT MENU TAB INTERAKTIF
    tab_risiko, tab_k3, tab_psikologi = st.tabs(["🌋 Risiko Bencana", "⛑️ Panduan K3", "💚 Psikologi & After Care"])
    
    # --- TAB 1: RISIKO BENCANA ---
    with tab_risiko:
        st.markdown("""
        <div style="border:1px solid #E2E8F0;border-radius:8px;padding:20px;background-color:#fff; margin-bottom: 20px;">
            <h4 style="color:#1E293B; margin-top:0; font-weight:800;">Risiko Bencana</h4>
            <p class="teks-justify" style="font-size:14px; margin-bottom:0; color:#475569;">
            Bentuk wilayah yang memanjang di Desa Kedungasri menciptakan perbedaan ketinggian yang memicu bencana musiman saling berkaitan. Saat musim hujan, air permukaan dari daerah tangkapan air perbukitan selatan meluncur deras ke Sungai Sungang, lalu meluap menjadi banjir saat menghantam pemukiman landai Dusun Jatigowok, bersamaan dengan ancaman tanah longsor di tebing jalur selatan. Sebaliknya saat kemarau, perbedaan ketinggian ini menguras cadangan air tanah di wilayah atas karena air mengalir turun mengikuti gravitasi ke dataran rendah utara, sehingga memicu krisis air bersih bagi warga hulu.
        </div>
        """, unsafe_allow_html=True)
        
        # Membuat fungsi cetakan kartu HTML agar kode rapi
        def kartu_bencana(gambar, ikon, judul, deskripsi):
            return f"""
            <div class="card-outline" style="border:1px solid #E2E8F0;border-radius:8px;padding:15px;background-color:#fff;height: 100%; display: flex; flex-direction: column;">
                <img src="{gambar}" style="width: 100%; aspect-ratio: 4/3; object-fit: cover; border-radius: 6px; margin-bottom: 15px;">
                <strong style="color:#1E293B; font-size:16px; margin-bottom:8px;">{ikon} {judul}</strong>
                <span style="font-size:13px; color:#475569; text-align:justify; line-height:1.5;">{deskripsi}</span>
            </div>
            """
        
        def get_image_base64(file_path):
            with open(file_path, "rb") as img_file:
                return f"data:image/jpeg;base64,{base64.b64encode(img_file.read()).decode()}"
        
        b1, b2 = st.columns(2)
        b3, b4 = st.columns(2)
        b5, b6 = st.columns(2)  

        with b1:
                    st.markdown(kartu_bencana(
                        get_image_base64("Kering2.jpg"), 
                        "", "Krisis air bersih - Agustus 2023", 
                        "Kondisi kekeringan di Dusun Jatigowok, Desa Kedungasri, Kecamatan Ringinarum sudah menjadi fenomena tahunan yang hampir sering terjadi ketika memasuki musim kemarau. Berdasarkan beberapa kabar berita, pada bulan Agustus 2023 warga Dusun Jatigowok mengalami kesulitan air karena sumur mengering. Warga dusun pun berinisiatif untuk membuat sumur agar bisa mendapatkan air. Namun air yang didapat dari pembuatan sumur nyatanya jauh dari kata layak konsumsi. Ar yang didapatkan dari sumur tersebut pada dasarnya belum dapat dikonsumsi sehingga memerlukan bantuan dari pemerintah terkait untuk mengatasi hal ini."
                        """<br><br><b>Sumber:</b> “2 Minggu Krisis Air Bersih, Warga Jatigowok Kendal Gali Sumur di Sungai (4 September 2023)” https://lingkarjateng.id/2-minggu-krisis-air-bersih-warga-jatigowok-kendal-gali-sumur-di-sungai/"""
                    ), unsafe_allow_html=True)
        
        with b2:
                    st.markdown(kartu_bencana(
                        get_image_base64("Kering1.jpg"), 
                        "", "Kekeringan di Dusun Jatigowok - 19 Juli 2026", 
                        "Kondisi kekeringan yang dialami warga Dusun Jatigowok RT 05 RW 03, Desa Kedungasri, Kabupaten Kendal, bertepatan dengan musim kemarau yang pada tahun ini berpotensi diperkuat oleh pengaruh fenomena El Niño, yang dapat menyebabkan penurunan curah hujan di sebagian wilayah Indonesia, termasuk Jawa Tengah. Berkurangnya curah hujan dalam waktu yang cukup lama mengakibatkan debit air tanah dan sumber air masyarakat menurun sehingga memicu krisis air bersih yang mengganggu kebutuhan rumah tangga dan sanitasi. Menyikapi kondisi tersebut, Pemerintah Kabupaten Kendal telah menetapkan status Siaga Darurat Bencana Kekeringan agar penanganan dapat dilakukan lebih cepat melalui distribusi bantuan air bersih oleh BPBD. Oleh karena itu, percepatan penyaluran bantuan air bersih menjadi langkah penting untuk memenuhi kebutuhan dasar masyarakat hingga kondisi hidrometeorologi kembali membaik."
                        """<br><br><b>Sumber:</b> “Kendal Darurat Kekeringan, Warga Dusun Jatigowok Berharap Bantuan Air Bersih Segera Terealisasi (19 Juli 2026)” https://pekatmedia.com/kendal-darurat-kekeringan-warga-dusun-jatigowok-berharap-bantuan-air-bersih-segera-terealisasi/"""
                    ), unsafe_allow_html=True)
        
        with b3:
            st.markdown(kartu_bencana(
                get_image_base64("Banjir1.jpg"), 
                "", "Banjir Beruntun Awal Januari 2024", 
                "Pada awal Januari 2024, sebanyak 25 desa dari 6 kecamatan di Kabupaten Kendal terendam banjir akibat hujan deras yang mengguyur sejak sore hingga dini hari. Ringinarum tercatat sebagai salah satu kecamatan yang berulang kali terdampak dalam rentang waktu berdekatan pada tahun yang sama."
                "<br><br><b>Sumber:</b> LaporGub! Provinsi Jawa Tengah — https://laporgub.jatengprov.go.id/detail/LGWP04350955.html"
            ), unsafe_allow_html=True)
            
        with b4:
            st.markdown(kartu_bencana(
                get_image_base64("Banjir2.jpg"), 
                "", "Banjir di Kecamatan Ringinarum — 13 Maret 2024", 
                "Hujan dengan intensitas tinggi disertai kiriman air dari hulu menyebabkan sungai meluap dan menggenangi permukiman di enam kecamatan Kabupaten Kendal, salah satunya Kecamatan Ringinarum, pada 13 Maret 2024 sekitar pukul 15.00 WIB. Tercatat lebih dari 10.800 kepala keluarga terdampak di seluruh wilayah terdampak, dengan ketinggian genangan air 10 - 60 cm."
                "<br><br><b>Sumber:</b> Pusat Krisis Kesehatan, Kementerian Kesehatan RI — https://pusatkrisis.kemkes.go.id/Banjir-di-KENDAL-JAWA-TENGAH-13-03-2024-37"
            ), unsafe_allow_html=True)
            
        with b5:
            st.markdown(kartu_bencana(
                get_image_base64("Banjir3.jpg"), 
                "", "Banjir Desember 2024", 
                """Curah hujan tinggi pada 11 - 12 Desember 2024 menyebabkan Sungai Kendal meluap dan berdampak pada lima kecamatan, termasuk Kecamatan Ringinarum, selain Kaliwungu Selatan, Kendal Kota, Pegandon, dan Weleri. Warga setempat menyebut wilayah sepanjang aliran sungai ini sebagai kawasan "langganan banjir" setiap kali hujan deras terjadi di bagian hulu."""
                """<br><br><b>Sumber:</b> detikJateng, "5 Kelurahan di Kendal Kota Terendam Banjir" (12 Desember 2024) — https://www.detik.com/jateng/berita/d-7682944/5-kelurahan-di-kendal-kota-terendam-banjir"""
            ), unsafe_allow_html=True)

        with b6:
            st.markdown(kartu_bencana(
                get_image_base64("Banjir4.jpg"), 
                "", "Bencana Hidrometeorologi (Banjir, Longsor, Puting Beliung) — Desember 2025", 
                "Delapan kecamatan di Kabupaten Kendal, termasuk Ringinarum, dilanda bencana hidrometeorologi berupa banjir, tanah longsor, dan angin puting beliung setelah hujan intensitas tinggi pada 14 Desember 2025. Meski tidak ada korban jiwa, kejadian ini menyebabkan kerusakan rumah warga, akses jalan tertutup material longsor di kecamatan tetangga, dan pohon tumbang di beberapa desa terdampak."
                """<br><br><b>Sumber:</b> Media Indonesia, "8 Kecamatan di Kendal Dilanda Banjir, Longsor, dan Puting Beliung" (15 Desember 2025) — https://mediaindonesia.com/nusantara/840336/8-kecamatan-di-kendal-dilanda-banjir-longsor-dan-puting-beliung"""
            ), unsafe_allow_html=True)

    # --- TAB 2: NARASI K3 ---
    with tab_k3:
        st.markdown("""
<div style="border:1px solid #E2E8F0;border-radius:8px;padding:25px;background-color:#FFFDE7; border-left: 5px solid #FFA900; margin-bottom: 20px;">
<h4 style="color:#F57F17; margin-top:0; font-weight:800;">Keselamatan, Kesehatan, dan Pertolongan Pertama</h4>
<p class="teks-justify" style="font-size:15px; margin-bottom:15px; color:#475569;">
Keselamatan Kerja (K3) wajib diterapkan oleh tim satgas desa dan relawan warga saat melakukan proses evakuasi maupun pembersihan area pasca bencana untuk meminimalisir korban lanjutan. Pertolongan pertama merupakan bantuan awal kepada orang yang sakit atau cedera sampai bantuan tenaga kesehatan tersedia. Tujuannya adalah mencegah kondisi korban bertambah buruk selama menunggu pertolongan profesional.
</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 20px;">
<div class="card-outline" style="background: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #FFE082; border-top: 4px solid #FFA900;">
<strong style="color: #F57F17; font-size:15px;">🎒 Sebelum Bencana</strong><br>
<span style="font-size:13px; color:#475569; font-weight:bold;">Persiapkan Diri dan Keluarga:</span>
<ul style="font-size:13px; color:#475569; padding-left: 15px; margin-top: 8px; margin-bottom: 0;">
<li style="margin-bottom: 4px;">Kenali jalur evakuasi dan lokasi berkumpul yang aman.</li>
<li style="margin-bottom: 4px;">Tentukan cara menghubungi anggota keluarga apabila terpisah.</li>
<li style="margin-bottom: 4px;">Siapkan tas siaga berisi air minum, makanan tahan lama, obat rutin, perlengkapan dasar, dan salinan dokumen penting.</li>
<li>Perhatikan kebutuhan khusus anak-anak, ibu hamil, lanjut usia, penyandang disabilitas, dan anggota keluarga yang sedang sakit.</li>
</ul>
</div>
<div class="card-outline" style="background: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #FFE082; border-top: 4px solid #FFA900;">
<strong style="color: #F57F17; font-size:15px;">🚨 Saat Bencana</strong><br>
<span style="font-size:13px; color:#475569; font-weight:bold;">Utamakan Keselamatan:</span>
<ul style="font-size:13px; color:#475569; padding-left: 15px; margin-top: 8px; margin-bottom: 0;">
<li style="margin-bottom: 4px;">Tetap tenang dan ikuti arahan evakuasi dari pihak berwenang.</li>
<li style="margin-bottom: 4px;">Segera menuju lokasi yang lebih aman.</li>
<li style="margin-bottom: 4px;">Hindari arus banjir, saluran air, genangan dalam, kabel listrik, dan peralatan listrik yang terkena air.</li>
<li style="margin-bottom: 4px;">Apabila terjadi longsor, segera menjauh dari suara gemuruh dan arah datangnya material.</li>
<li style="margin-bottom: 4px;">Apabila terjadi angin kencang, masuklah ke bangunan yang kokoh serta jauhi tiang listrik, papan reklame, dan pohon besar.</li>
<li>Jangan memasuki lokasi berbahaya untuk mengambil barang atau memberikan pertolongan tanpa perlindungan yang memadai.</li>
</ul>
</div>
<div class="card-outline" style="background: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #FFE082; border-top: 4px solid #FFA900;">
<strong style="color: #F57F17; font-size:15px;">🧹 Setelah Bencana</strong><br>
<span style="font-size:13px; color:#475569; font-weight:bold;">Cegah Cedera dan Penyakit:</span>
<ul style="font-size:13px; color:#475569; padding-left: 15px; margin-top: 8px; margin-bottom: 0;">
<li style="margin-bottom: 4px;">Kembali ke rumah hanya setelah lokasi dinyatakan aman oleh pihak berwenang.</li>
<li style="margin-bottom: 4px;">Hindari bangunan yang rusak, instalasi listrik, air yang masih mengalir, dan permukaan jalan yang berpotensi ambles.</li>
<li style="margin-bottom: 4px;">Gunakan sepatu boots, sarung tangan, dan pakaian tertutup saat membersihkan lumpur atau selokan.</li>
<li style="margin-bottom: 4px;">Cuci tangan, kaki, dan bagian tubuh yang terpapar menggunakan sabun dan air bersih.</li>
<li style="margin-bottom: 4px;">Buang makanan yang telah terkena air banjir.</li>
<li style="margin-bottom: 4px;">Gunakan air yang aman untuk minum dan menyiapkan makanan.</li>
<li>Jaga kebersihan jamban dan lindungi sumber air dari pencemaran.</li>
</ul>
</div>
</div>
</div>
<div style="border:1px solid #E2E8F0;border-radius:8px;padding:25px;background-color:#F0FDF4; border-left: 5px solid #22C55E; margin-bottom: 20px;">
<h4 style="color:#166534; margin-top:0; font-weight:800;">Tiga Langkah Tindakan Awal Pertolongan Pertama</h4>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 15px;">
<div class="card-outline" style="background: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #BBF7D0; border-top: 4px solid #22C55E;">
<strong style="color: #166534; font-size:15px;">🛡️ 1. S — Safety</strong><br>
<span style="font-size:13px; color:#475569; font-weight:bold;">Pastikan Keselamatan:</span>
<ul style="font-size:13px; color:#475569; padding-left: 15px; margin-top: 8px; margin-bottom: 8px;">
<li>Perhatikan bahaya di sekitar sebelum mendekati korban, seperti: arus air dan genangan, kabel atau peralatan listrik, material longsoran, pohon tumbang, benda tajam, dan bangunan yang tidak stabil.</li>
<li>Jangan mendekati atau memindahkan korban apabila tindakan tersebut dapat membahayakan penolong, korban, atau masyarakat di sekitar.</li>
</ul>
</div>
<div class="card-outline" style="background: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #BBF7D0; border-top: 4px solid #22C55E;">
<strong style="color: #166534; font-size:15px;">🩺 2. R — Response</strong><br>
<span style="font-size:13px; color:#475569; font-weight:bold;">Periksa Respons dan Pernapasan:</span>
<ul style="font-size:13px; color:#475569; padding-left: 15px; margin-top: 8px; margin-bottom: 8px;">
<li>Panggil korban dengan suara jelas dan tepuk bahunya secara perlahan.</li>
<li>Perhatikan apakah korban memberikan respons.</li>
<li>Periksa apakah korban bernapas secara normal selama paling lama sekitar 10 detik. Napas yang hanya berupa megap-megap tidak dianggap sebagai pernapasan normal.</li>
<li>Periksa adanya perdarahan atau cedera yang terlihat.</li>
<li>Korban yang tidak memberikan respons dan tidak bernapas normal perlu dianggap mengalami keadaan darurat dan segera memperoleh bantuan.</li>
</ul>
</div>
<div class="card-outline" style="background: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #BBF7D0; border-top: 4px solid #22C55E;">
<strong style="color: #166534; font-size:15px;">📞 3. S — Shout for Help</strong><br>
<span style="font-size:13px; color:#475569; font-weight:bold;">Segera Hubungi 119 Apabila Korban:</span>
<ul style="font-size:13px; color:#475569; padding-left: 15px; margin-top: 8px; margin-bottom: 8px;">
<li>Tidak sadar, tidak memberikan respons, atau tidak bernafas secara normal.</li>
<li>Mengalami sesak napas berat, perdarahan yang tidak berhenti, luka dalam, atau cedera berat.</li>
<li>Memerlukan pertolongan yang tidak dapat dilakukan dengan aman oleh warga.</li>
</ul>
<span style="font-size:13px; color:#475569; font-weight:bold;">Sampaikan kepada operator:</span>
<ul style="font-size:13px; color:#475569; padding-left: 15px; margin-top: 8px; margin-bottom: 8px;">
<li>Nama pelapor, lokasi kejadian, jenis kejadian, dan jumlah korban.</li>
<li>Kondisi respons dan pernapasan korban, serta bahaya di lokasi.</li>
</ul>
<p style="font-size:12px; color:#64748B; margin-bottom:0; line-height: 1.4;">*Nomor 119 adalah layanan darurat medis. Kab. Kendal juga memiliki layanan darurat 112 untuk bencana, kecelakaan, dll.</p>
</div>
</div>
</div>
<div style="border:1px solid #FECACA;border-radius:8px;padding:25px;background-color:#FEF2F2; border-left: 5px solid #EF4444;">
<h4 style="color:#B91C1C; margin-top:0; font-weight:800;">⚠️ Hindari Tindakan Berikut</h4>
<ul style="font-size:14px; color:#7F1D1D; padding-left: 20px; margin-top: 10px; margin-bottom: 15px;">
<li style="margin-bottom: 6px;">Jangan memasuki lokasi yang masih berbahaya.</li>
<li style="margin-bottom: 6px;">Jangan memberikan makanan, minuman, atau obat kepada korban yang tidak sadar.</li>
<li style="margin-bottom: 6px;">Jangan memindahkan korban yang diduga mengalami cedera kepala, leher, atau tulang belakang, kecuali terdapat bahaya langsung di lokasi.</li>
<li style="margin-bottom: 6px;">Jangan melakukan nafas bantuan, pemasangan torniket, atau tindakan teknis lainnya apabila belum pernah mendapatkan pelatihan.</li>
<li>Jangan meninggalkan korban sendirian sebelum bantuan datang, kecuali penolong harus berpindah untuk mendapatkan bantuan.</li>
</ul>
<hr style="border-color: #FCA5A5; margin-top: 20px; margin-bottom: 15px;">
<p style="font-size:11px; color:#991B1B; margin-bottom:0; line-height: 1.4;">
<b>Sumber Referensi:</b> BNPB (Buku Saku Tanggap Tangkas Tangguh Menghadapi Bencana, 2020); Kementerian Kesehatan RI (Bantuan Hidup Dasar, 2022 & Akses Darurat Medis 119, 2024); World Health Organization (Humanitarian Emergencies & Community First Aid Response Pocket Guide); Pemerintah Kab. Kendal (Layanan Darurat 112, 2021).
</p>
</div>
        """, unsafe_allow_html=True)

    # --- TAB 3: PSIKOLOGI KEBENCANAAN ---
    with tab_psikologi:
        st.markdown("""
        <div style="border:1px solid #E2E8F0;border-radius:8px;padding:25px;background-color:#FFF0F5; border-left: 5px solid #FF5E94;">
            <h4 style="color:#C2185B; margin-top:0; font-weight:800;">Psikologi Kebencanaan (After Care)</h4>
            <p class="teks-justify" style="font-size:15px; margin-bottom:15px; color:#475569;">
            Pemulihan desa tidak sebatas perbaikan fisik, tetapi juga pemulihan mental warga. Kami menerapkan <i>Psychological First Aid</i> (PFA) atau Pertolongan Pertama Psikologis pasca bencana.
            </p>
            <ol style="color: #475569; font-size: 14px; padding-left: 20px;">
                <li style="margin-bottom: 10px;"><b>Lihat dan Kenali Kondisi:</b> 
                    <ul style="padding-left: 20px; margin-top: 5px;">
                        <li>Pastikan situasi aman.</li>
                        <li>Kenali siapa yang membutuhkan bantuan.</li>
                        <li>Cek kebutuhan dasar (pangan, sandang, papan).</li>
                    </ul>
                </li>
                <li style="margin-bottom: 10px;"><b>Dengarkan dengan Penuh Perhatian:</b> 
                    <ul style="padding-left: 20px; margin-top: 5px;">
                        <li>Dekati dengan tenang.</li>
                        <li>Dengarkan tanpa menghakimi.</li>
                        <li>Jangan memaksa bercerita.</li>
                    </ul>
                </li>
                <li style="margin-bottom: 10px;"><b>Hubungkan dengan Bantuan yang Dibutuhkan:</b> 
                    <ul style="padding-left: 20px; margin-top: 5px;">
                        <li>Hubungkan dengan keluarga.</li>
                        <li>Arahkan ke layanan yang tepat.</li>
                        <li>Berikan informasi yang jelas.</li>
                    </ul>
                </li>
                <li style="margin-bottom: 10px;"><b>Lindungi dari Risiko dan Bahaya:</b> 
                    <ul style="padding-left: 20px; margin-top: 5px;">
                        <li>Pastikan tetap aman.</li>
                        <li>Jaga privasi penyintas.</li>
                        <li>Hindari risiko tambahan.</li>
                    </ul>
                </li>
                <li style="margin-bottom: 10px;"><b>Beri Rasa Nyaman dan Aman:</b> 
                    <ul style="padding-left: 20px; margin-top: 5px;">
                        <li>Penuhi kebutuhan dasar bila memungkinkan.</li>
                        <li>Yakinkan bahwa mereka tidak sendirian.</li>
                    </ul>
                </li>
                <li style="margin-bottom: 10px;"><b>Bangun Harapan:</b> 
                    <ul style="padding-left: 20px; margin-top: 5px;">
                        <li>Berikan semangat realistis.</li>
                        <li>Ajak fokus pada langkah berikutnya.</li>
                        <li>Hindari janji yang berlebihan.</li>
                    </ul>
                </li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

# 5. DAFTAR UMKM
elif st.session_state.menu_aktif == "Daftar UMKM":
    st.markdown('<p style="color:#18A924;font-weight:bold;">// PENGGERAK EKONOMI</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:40px;font-weight:800;color:#1E293B;margin-bottom:0;">PROFIL</p><p style="font-size:40px;font-weight:300;color:#94A3B8;margin-top:-10px;">UMKM LOKAL</p>', unsafe_allow_html=True)
    st.write("Mengenal lebih dekat potensi ekonomi kreatif yang dibangun oleh warga Desa Kedungasri.")
    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # UMKM 1: PIZZA RAJA RASA
    # ==========================================
    st.markdown(f"""
<div style="border:1px solid #E2E8F0; border-radius:12px; padding:25px; background-color:#ffffff; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 30px;">
<div style="display: flex; flex-wrap: wrap; gap: 25px;">
<!-- KIRI: Foto & Info Singkat -->
<div style="flex: 1; min-width: 250px; max-width: 350px;">
<!-- GALERI FOTO RASIO 3:4 DENGAN WATERMARK -->
<div style="display: flex; overflow-x: auto; gap: 10px; scroll-snap-type: x mandatory; padding-bottom: 5px;">
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('pizza1.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Pizza Raja Rasa</div>
</div>
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('pizza2.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Pizza Raja Rasa</div>
</div>
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('pizza3.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Pizza Raja Rasa</div>
</div>
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('pizza4.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Pizza Raja Rasa</div>
</div>
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('pizza5.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Pizza Raja Rasa</div>
</div>
</div>
<p style="font-size: 11px; color: #94A3B8; text-align: center; margin-top: 5px; margin-bottom: 0;"><i>Geser foto ke kiri/kanan ↔️</i></p>

<div style="margin-top: 15px; background-color: #F8FAFC; padding: 15px; border-radius: 8px; border-left: 4px solid #F59E0B;">
<strong style="color: #B45309; font-size:15px;">📋 Ringkasan Usaha</strong><br>
<ul style="font-size: 13px; color: #475569; padding-left: 15px; margin-top: 8px; margin-bottom: 0;">
<li style="margin-bottom: 5px;"><b>Pemilik:</b> Ibu Mualiyah</li>
<li style="margin-bottom: 5px;"><b>Berdiri:</b> Sejak 2-3 tahun lalu</li>
<li style="margin-bottom: 5px;"><b>Sistem:</b> Made by Order</li>
<li style="margin-bottom: 5px;"><b>Batas Order:</b> Pukul 16.00 WIB</li>
<li><b>Omzet:</b> Rp 3 Juta - Rp 5 Juta / bulan</li>
</ul>
</div>
<div style="margin-top: 15px; background-color: #F0FDF4; padding: 15px; border-radius: 8px; border-left: 4px solid #16A34A;">
<strong style="color: #15803D; font-size:15px;">📞 Kontak & Promosi</strong><br>
<p style="font-size: 13px; color: #475569; margin-top: 8px; margin-bottom: 0;">
<b>WhatsApp:</b> 0877-0018-7664<br>
<b>Media Sosial:</b> Grup/Komunitas Facebook
</p>
</div>
</div>
<!-- KANAN: Cerita Lengkap -->
<div style="flex: 2; min-width: 300px;">
<h3 style="margin-top:0; color:#1E293B; font-weight:800; font-size: 24px; margin-bottom: 5px;">🍕 Pizza Raja Rasa</h3>
<hr style="border-color: #E2E8F0; margin-top: 10px; margin-bottom: 15px;">
<h5 style="color:#0F172A; margin-bottom:5px; margin-top:0; font-weight:bold;">Awal Mula Usaha & Manajemen</h5>
<p style="font-size: 14px; color: #475569; text-align: justify; line-height:1.6;">
Berawal dari iseng membuat pizza untuk konsumsi pribadi, Ibu Mualiyah mulai menawarkannya ke tetangga via WhatsApp. Usaha yang dipelajari secara otodidak ini perlahan berkembang menjadi bisnis keluarga. Pembagian tugasnya sangat rapi: <b>Bapak</b> membuat pizza, <b>Ibu</b> mengolah spaghetti, burger, dan kentang, sementara <b>saudara</b> membantu pesanan nasi box. Ibu Mualiyah memegang prinsip bijak; beliau tidak serakah menerima semua pesanan tanpa batas, melainkan tetap mengontrol kapasitas sesuai kemampuan tenaga dan waktu.
</p>
<h5 style="color:#0F172A; margin-bottom:5px; margin-top:15px; font-weight:bold;">Menu & Target Konsumen Unik</h5>
<p style="font-size: 14px; color: #475569; text-align: justify; line-height:1.6;">
Menu yang ditawarkan sangat beragam, mulai dari pizza, kebab, donat, brownis, ayam, hingga kentang goreng (detail harga dan <i>topping</i> tersedia di katalog). Terdapat juga paket <b>Nasi Box Ayam Lalapan seharga Rp 19.000</b> (minimal order 6 paket). Menariknya, sebagian besar pesanan datang dari <b>Pekerja Migran Indonesia di luar negeri</b> yang membelikan makanan untuk keluarga mereka di rumah, membuat pola pesanan menjadi sangat dinamis.
</p>
<h5 style="color:#0F172A; margin-bottom:5px; margin-top:15px; font-weight:bold;">Sistem Produksi, Kendala, & Harapan</h5>
<p style="font-size: 14px; color: #475569; text-align: justify; line-height:1.6;">
Usaha ini dijalankan secara <i>Made by Order</i> sehingga tidak bisa melayani pesanan mendadak. Pengantaran (<i>delivery</i>) menjangkau <b>Pegandon, Patebon, Cepiring, Kangkung, dan Kadilangu</b>, sedangkan pesanan malam hari hanya dibatasi untuk tetangga sekitar. Saat ini, Pizza Raja Rasa menghadapi kendala berupa keterbatasan waktu (sebagai usaha sampingan), cuaca saat <i>delivery</i>, dan minimnya SDM. Ke depannya, Ibu Mualiyah berharap dapat mengembangkan usahanya menjadi lebih besar seiring dengan bertambahnya ilmu bisnis dan modal.
</p>
</div>
</div>
</div>
    """, unsafe_allow_html=True)

    # ==========================================
    # UMKM 2: HADI ALUMINIUM
    # ==========================================
    st.markdown(f"""
<div style="border:1px solid #E2E8F0; border-radius:12px; padding:25px; background-color:#ffffff; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 30px;">
<div style="display: flex; flex-wrap: wrap; gap: 25px;">
<!-- KIRI: Foto & Info Singkat -->
<div style="flex: 1; min-width: 250px; max-width: 350px;">
<!-- GALERI FOTO RASIO 3:4 DENGAN WATERMARK -->
<div style="display: flex; overflow-x: auto; gap: 10px; scroll-snap-type: x mandatory; padding-bottom: 5px;">
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('aluminium1.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Hadi Aluminium</div>
</div>
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('aluminium2.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Hadi Aluminium</div>
</div>
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('aluminium3.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Hadi Aluminium</div>
</div>
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('aluminium4.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Hadi Aluminium</div>
</div>
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('aluminium5.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Hadi Aluminium</div>
</div>
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('aluminium6.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Hadi Aluminium</div>
</div>
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('aluminium7.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Hadi Aluminium</div>
</div>
</div>
<p style="font-size: 11px; color: #94A3B8; text-align: center; margin-top: 5px; margin-bottom: 0;"><i>Geser foto ke kiri/kanan ↔️</i></p>

<div style="margin-top: 15px; background-color: #F8FAFC; padding: 15px; border-radius: 8px; border-left: 4px solid #3B82F6;">
<strong style="color: #1D4ED8; font-size:15px;">📋 Ringkasan Usaha</strong><br>
<ul style="font-size: 13px; color: #475569; padding-left: 15px; margin-top: 8px; margin-bottom: 0;">
<li style="margin-bottom: 5px;"><b>Pemilik:</b> Bapak Nurhadi</li>
<li style="margin-bottom: 5px;"><b>Pengalaman:</b> Sejak 1998 (Berdiri 8 th)</li>
<li style="margin-bottom: 5px;"><b>Sistem:</b> Custom / Made by Order</li>
<li style="margin-bottom: 5px;"><b>Cakupan:</b> Kendal, Weleri, Batang</li>
<li><b>Omzet Kotor:</b> ± Rp 10 Juta / bulan</li>
</ul>
</div>
<div style="margin-top: 15px; background-color: #F0FDF4; padding: 15px; border-radius: 8px; border-left: 4px solid #16A34A;">
<strong style="color: #15803D; font-size:15px;">📞 Kontak & Promosi</strong><br>
<p style="font-size: 13px; color: #475569; margin-top: 8px; margin-bottom: 0;">
<b>WhatsApp:</b> 0831-5453-1711<br>
<b>Media Sosial:</b> Facebook & Mulut ke Mulut
</p>
</div>
</div>
<!-- KANAN: Cerita Lengkap -->
<div style="flex: 2; min-width: 300px;">
<h3 style="margin-top:0; color:#1E293B; font-weight:800; font-size: 24px; margin-bottom: 5px;">🛠️ Hadi Aluminium</h3>
<hr style="border-color: #E2E8F0; margin-top: 10px; margin-bottom: 15px;">
<h5 style="color:#0F172A; margin-bottom:5px; margin-top:0; font-weight:bold;">Sejarah, Pengalaman, & Prinsip Usaha</h5>
<p style="font-size: 14px; color: #475569; text-align: justify; line-height:1.6;">
Bapak Nurhadi memulai perjalanannya sejak tahun 1998 (usia 20 tahun) dengan merantau ke Jakarta untuk bekerja di kantor orang Jepang di kawasan Senayan. Ia juga berpengalaman mengerjakan proyek aluminium di Fakultas Ekonomika dan Bisnis UNDIP. Berbekal ilmu tersebut, beliau mendirikan Hadi Aluminium 8 tahun yang lalu. Beliau memegang prinsip <i>"biar bisa bekerja saja dan tidak ikut orang"</i>—lebih mengutamakan keberlangsungan usaha dan kepuasan pelanggan dibanding mencari untung besar.
</p>
<h5 style="color:#0F172A; margin-bottom:5px; margin-top:15px; font-weight:bold;">Produk, Harga, & Target Pasar (PMI)</h5>
<p style="font-size: 14px; color: #475569; text-align: justify; line-height:1.6;">
Menerima pesanan kustom seperti <b>Kitchen Set</b> (Atas Rp1,5 Jt/m, Bawah Rp3,5 Jt/m), <b>Lemari Pintu 2</b> (Rp2,3 Jt - Rp2,7 Jt), <b>Background TV</b> (Mulai Rp3,5 Jt), <b>Etalase</b> (Rp1,5 Jt/m), dan berbagai cermin hias. Uniknya, sebagian besar pelanggan adalah <b>Pekerja Migran Indonesia (PMI)</b> di luar negeri yang memesan untuk rumah di kampung halaman. Saking percayanya, Bapak Nurhadi jarang meminta <i>Down Payment</i> (DP). Jangkauannya mencakup pasar Kendal, Weleri, hingga Kabupaten Batang (rata-rata 2-3 lokasi per bulan).
</p>
<h5 style="color:#0F172A; margin-bottom:5px; margin-top:15px; font-weight:bold;">Produksi, Kendala, & Visi ke Depan</h5>
<p style="font-size: 14px; color: #475569; text-align: justify; line-height:1.6;">
Bahan baku didatangkan dari toko material besar di Weleri. Waktu pengerjaan bervariasi (lemari/etalase ±3 hari, kitchen set ±2 minggu). Kendala utamanya adalah kelangkaan dan fluktuasi harga bahan baku (terkadang imbas isu global), serta keterbatasan waktu dan daya listrik. Usaha ini tidak dipasarkan lewat e-commerce (seperti Shopee) untuk menghindari persaingan "perang harga" yang tidak sehat. Ke depannya, beliau berharap Hadi Aluminium semakin besar, produknya meluas, dan tampil di pasar yang lebih luas.
</p>
</div>
</div>
</div>
    """, unsafe_allow_html=True)

    # ==========================================
    # UMKM 3: KERIPIK PISANG IBU MA'MUDAH
    # ==========================================
    st.markdown(f"""
<div style="border:1px solid #E2E8F0; border-radius:12px; padding:25px; background-color:#ffffff; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 30px;">
<div style="display: flex; flex-wrap: wrap; gap: 25px;">
<!-- KIRI: Foto & Info Singkat -->
<div style="flex: 1; min-width: 250px; max-width: 350px;">
<!-- GALERI FOTO RASIO 3:4 DENGAN WATERMARK -->
<div style="display: flex; overflow-x: auto; gap: 10px; scroll-snap-type: x mandatory; padding-bottom: 5px;">
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('keripik1.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Keripik Pisang Ibu Ma'mudah</div>
</div>
<div style="position: relative; min-width: 100%; height: 320px; scroll-snap-align: start;">
<img src="{get_image_base64('keripik2.jpg')}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; border: 1px solid #E2E8F0;">
<div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.6); color: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; pointer-events: none; backdrop-filter: blur(2px);">© Keripik Pisang Ibu Ma'mudah</div>
</div>
</div>
<p style="font-size: 11px; color: #94A3B8; text-align: center; margin-top: 5px; margin-bottom: 0;"><i>Geser foto ke kiri/kanan ↔️</i></p>

<div style="margin-top: 15px; background-color: #F8FAFC; padding: 15px; border-radius: 8px; border-left: 4px solid #EAB308;">
<strong style="color: #A16207; font-size:15px;">📋 Ringkasan Usaha</strong><br>
<ul style="font-size: 13px; color: #475569; padding-left: 15px; margin-top: 8px; margin-bottom: 0;">
<li style="margin-bottom: 5px;"><b>Pemilik:</b> Ibu Ma'mudah</li>
<li style="margin-bottom: 5px;"><b>Berdiri:</b> Sejak 15 tahun lalu</li>
<li style="margin-bottom: 5px;"><b>Kapasitas:</b> ± 10 Kg pisang / produksi</li>
<li style="margin-bottom: 5px;"><b>Laba Bersih:</b> ± Rp 50.000 / hari</li>
<li><b>Cakupan:</b> Ringinarum, Kedunggading, Pegandon</li>
</ul>
</div>
<div style="margin-top: 15px; background-color: #F0FDF4; padding: 15px; border-radius: 8px; border-left: 4px solid #16A34A;">
<strong style="color: #15803D; font-size:15px;">📞 Kontak & Pemesanan</strong><br>
<p style="font-size: 13px; color: #475569; margin-top: 8px; margin-bottom: 0;">
<b>WhatsApp:</b> 0878-0291-5868<br>
<b>Lokasi:</b> Datang langsung ke rumah produksi
</p>
</div>
</div>
<!-- KANAN: Cerita Lengkap -->
<div style="flex: 2; min-width: 300px;">
<h3 style="margin-top:0; color:#1E293B; font-weight:800; font-size: 24px; margin-bottom: 5px;">🍌 Keripik Pisang Ibu Ma'mudah</h3>
<hr style="border-color: #E2E8F0; margin-top: 10px; margin-bottom: 15px;">
<h5 style="color:#0F172A; margin-bottom:5px; margin-top:0; font-weight:bold;">Perjalanan 15 Tahun Usaha Mandiri</h5>
<p style="font-size: 14px; color: #475569; text-align: justify; line-height:1.6;">
Usaha keripik pisang ini merupakan bentuk dukungan ekonomi keluarga yang dirintis oleh Ibu Ma'mudah, seorang ibu rumah tangga bersuamikan petani, sejak 15 tahun yang lalu. Belajar ilmu membuat keripik dari kakaknya, Ibu Ma'mudah hingga kini mempertahankan keaslian produknya dengan mengerjakan seluruh proses produksi sendirian (solo)—mulai dari mengupas, mengiris, menggoreng, hingga tahap pengemasan.
</p>
<h5 style="color:#0F172A; margin-bottom:5px; margin-top:15px; font-weight:bold;">Varian Produk, Harga, & Pasar Ekspor Jalur Pekerja Migran</h5>
<p style="font-size: 14px; color: #475569; text-align: justify; line-height:1.6;">
Keripik ini diproduksi menggunakan pisang raja dan pisang nangka (pisang kepok mulai ditinggalkan karena harganya mahal) dengan pilihan rasa asin dan manis. Produk dikemas dalam dua bentuk: irisan memanjang dan bulat biasa. Harga jualnya sangat terjangkau, yaitu <b>Rp 40.000/Kg</b>, atau kemasan 1 ons seharga <b>Rp 4.000 (harga grosir untuk warung)</b> dan Rp 5.000 (harga konsumen langsung). Fakta paling membanggakan adalah keripik ini tak hanya laris menjelang Lebaran, tetapi juga sering dipesan oleh keluarga Pekerja Migran untuk <b>dipaketkan hingga ke luar negeri</b>.
</p>
<h5 style="color:#0F172A; margin-bottom:5px; margin-top:15px; font-weight:bold;">Sistem Penjualan, Kendala, & Kesederhanaan Berbisnis</h5>
<p style="font-size: 14px; color: #475569; text-align: justify; line-height:1.6;">
Dalam satu kali produksi harian, Ibu Ma'mudah menghabiskan sekitar 10 Kg pisang mentah yang diperoleh dari pemasok lokal. Keripik kemudian didistribusikan ke warung-warung di sekitar Kecamatan Ringinarum. Kendala terbesar yang dihadapinya adalah fluktuasi harga pisang, kelangkaan bahan baku di pasaran, serta belum adanya sertifikat halal untuk ekspansi pasar. Meski begitu, Ibu Ma'mudah memiliki pola pikir yang tenang; beliau tidak memusingkan persaingan pasar dan memilih bersyukur menjalankan usahanya mengalir apa adanya.
</p>
</div>
</div>
</div>
    """, unsafe_allow_html=True)

# ==========================================
# FOOTER LEGALITAS (Letakkan di baris paling bawah app.py)
# ==========================================
st.markdown("<br><br><br>", unsafe_allow_html=True)

# Membuat layout kolom agar tombol pop-up berada rapi di tengah
kol_kiri, kol_tengah, kol_kanan = st.columns([0.5, 2, 0.5])

with kol_tengah:
    with st.popover("🛡️ Disusun dengan tetap berpedoman pada UU PDP dan UU KIP"):
        st.markdown("""
<div style="color: #334155; font-size: 13px; text-align: justify; line-height: 2;">

<h3 style="color:#1E293B; margin-top:0; font-weight: 800; text-align: center;">HALAMAN LEGALITAS</h3>

<h4 style="color:#18A924; margin-top: 20px; margin-bottom: 5px;">A. Kebijakan Privasi & Syarat Ketentuan</h4>

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 15px 0 10px 0;">
<span style="font-size: 15px;">UU No 27 Tahun 2022 tentang Perlindungan Data Pribadi (PDP)</span><br>
BAB V<br>
PEMROSESAN DATA PRIBADI<br>
Pasal 16
</div>
(1) Pemrosesan Data Pribadi meliputi:
<div style="padding-left: 20px;">
a. pemerolehan dan pengumpulan;<br>
b. pengolahan dan penganalisisan;<br>
c. penyimpanan;<br>
d. perbaikan dan pembaruan;<br>
e. penampilan, pengumuman, transfer, penyebarluasan, atau pengungkapan; dan/atau<br>
f. penghapusan atau pemusnahan.
</div>
(2) Pemrosesan Data Pribadi sebagaimana dimaksud pada ayat (1) dilakukan sesuai dengan prinsip Pelindungan Data Pribadi meliputi:
<div style="padding-left: 20px;">
a. Pengumpulan Data Pribadi dilakukan secara terbatas dan spesifik, sah secara hukum, dan transparan;<br>
b. pemrosesan Data Pribadi dilakukan sesuai dengan tujuannya;<br>
c. pemrosesan Data Pribadi dilakukan dengan menjamin hak Subjek Data Pribadi;<br>
d. pemrosesan Data Pribadi dilakukan secara akurat, lengkap, tidak menyesatkan, mutakhir, dan dapat dipertanggungjawabkan;<br>
e. pemrosesan Data Pribadi dilakukan dengan melindungi keamanan Data Pribadi dari pengaksesan yang tidak sah, pengungkapan yang tidak sah, pengubahan yang tidak sah, penyalahgunaan, perusakan, dan/atau penghilangan Data Pribadi;<br>
f. pemrosesan Data Pribadi dilakukan dengan memberitahukan tujuan dan aktivitas pemrosesan, serta kegagalan Pelindungan Data Pribadi;<br>
g. Data Pribadi dimusnahkan dan/atau dihapus setelah masa retensi berakhir atau berdasarkan permintaan Subjek Data Pribadi, kecuali ditentukan lain oleh peraturan perundangundangan; dan<br>
h. pemrosesan Data Pribadi dilakukan secara bertanggung jawab dan dapat dibuktikan secara jelas.
</div>
(3) Ketentuan lebih lanjut mengenai pelaksanaan pemrosesan Data Pribadi sebagaimana dimaksud pada ayat (1) diatur dalam Peraturan Pemerintah.

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 15px 0 10px 0;">Pasal 21</div>
(1) Dalam hal pemrosesan Data Pribadi berdasarkan persetujuan sebagaimana dimaksud dalam Pasal 20 ayat (2) huruf a, Pengendali Data Pribadi wajib menyampaikan Informasi mengenai:
<div style="padding-left: 20px;">
a. legalitas dari pemrosesan Data Pribadi;<br>
b. tujuan pemrosesan Data Pribadi;<br>
c. jenis dan relevansi Data Pribadi yang akan diproses;<br>
d. jangka waktu retensi dokumen yang memuat Data Pribadi;<br>
e. rincian mengenai Informasi yang dikumpulkan;<br>
f. jangka waktu pemrosesan Data Pribadi; dan<br>
g. hak Subjek Data Pribadi.
</div>
(2) Dalam hal terdapat perubahan Informasi sebagaimana dimaksud pada ayat (1), Pengendali Data Pribadi wajib memberitahukan kepada Subjek Data Pribadi sebelum terjadi perubahan Informasi.

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 15px 0 10px 0;">Pasal 22</div>
(1) Persetujuan pemrosesan Data Pribadi dilakukan melalui persetujuan tertulis atau terekam.<br>
(2) Persetujuan sebagaimana dimaksud pada ayat (1) dapat disampaikan secara elektronik atau non-elektronik.<br>
(3) Persetujuan sebagaimana dimaksud pada ayat (1) mempunyai kekuatan hukum yang sama.<br>
(4) Dalam hal persetujuan sebagaimana dimaksud pada ayat (1) memuat tujuan lain, permintaan persetujuan harus memenuhi ketentuan:
<div style="padding-left: 20px;">
a. dapat dibedakan secara jelas dengan hal lainnya;<br>
b. dibuat dengan format yang dapat dipahami dan mudah diakses; dan<br>
c. menggunalan bahasa yang sederhana dan jelas.
</div>
(5) Persetujuan yang tidak memenuhi ketentuan sebagaimana dimaksud pada ayat (1) dan ayat (4) dinyatakan batal demi hukum.

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 15px 0 10px 0;">Pasal 27</div>
Pengendali Data Pribadi wajib melakukan pemrosesan Data Pribadi secara terbatas dan spesifik, sah secara hukum, dan transparan.

<hr style="border-color:#E2E8F0; margin: 20px 0;">

<h4 style="color:#18A924; margin-bottom: 5px;">B. Database Potensi Ekonomi, UMKM, dan Profil Sosial Masyarakat</h4>

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 15px 0 10px 0;">
<span style="font-size: 15px;">UU No 14 Tahun 2008 tentang Keterbukaan Informasi Publik (KIP)</span><br>
BAB IV<br>
INFORMASI YANG WAJIB DISEDIAKAN DAN DIUMUMKAN<br>
Bagian Kesatu<br>
Informasi yang Wajib Disediakan dan Diumumkan Secara Berkala<br>
Pasal 9
</div>
(1) Setiap Badan Publik wajib mengumumkan Informasi Publik secara berkala.<br>
(2) Informasi Publik sebagaimana dimaksud pada ayat (1) meliputi:
<div style="padding-left: 20px;">
a. informasi yang berkaitan dengan Badan Publik;<br>
b. informasi mengenai kegiatan dan kinerja Badan Publik terkait;<br>
c. informasi mengenai laporan keuangan; dan/atau informasi lain yang diatur dalam peraturan perundang-undangan.
</div>

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 15px 0 10px 0;">Pasal 17</div>
Setiap Badan Publik wajib membuka akses bagi setiap Pemohon Informasi Publik untuk mendapatkan Informasi Publik, kecuali:
<div style="padding-left: 20px;">
a. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik dapat menghambat proses penegakan hukum, yaitu informasi yang dapat:
<div style="padding-left: 20px;">
1. menghambat proses penyelidikan dan penyidikan suatu tindak pidana;<br>
2. mengungkapkan identitas informan, pelapor, saksi, dan/atau korban yang mengetahui adanya tindak pidana;<br>
3. mengungkapkan data intelijen kriminal dan rencana-rencana yang berhubungan dengan pencegahan dan penanganan segala bentuk kejahatan transnasional;<br>
4. membahayakan keselamatan dan kehidupan penegak hukum dan/atau keluarganya; dan/atau<br>
5. membahayakan keamanan peralatan, sarana, dan/atau prasarana penegak hukum.
</div>
b. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik dapat mengganggu kepentingan perlindungan hak atas kekayaan intelektual dan perlindungan dari persaingan usaha tidak sehat;<br>
c. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik dapat membahayakan pertahanan dan keamanan negara, yaitu:
<div style="padding-left: 20px;">
1. informasi tentang strategi, intelijen, operasi, taktik dan teknik yang berkaitan dengan penyelenggaraan sistem pertahanan dan keamanan negara, meliputi tahap perencanaan, pelaksanaan dan pengakhiran atau evaluasi dalam kaitan dengan ancaman dari dalam dan luar negeri;<br>
2. dokumen yang memuat tentang strategi, intelijen, operasi, teknik dan taktik yang berkaitan dengan penyelenggaraan sistem pertahanan dan keamanan negara yang meliputi tahap perencanaan, pelaksanaan dan pengakhiran atau evaluasi;<br>
3. jumlah, komposisi, disposisi, atau dislokasi kekuatan dan kemampuan dalam penyelenggaraan sistem pertahanan dan keamanan negara serta rencana pengembangannya;<br>
4. gambar dan data tentang situasi dan keadaan pangkalan dan/atau instalasi militer;<br>
5. data perkiraan kemampuan militer dan pertahanan negara lain terbatas pada segala tindakan dan/atau indikasi negara tersebut yang dapat membahayakan kedaulatan Negara Kesatuan Republik Indonesia dan/atau data terkait kerjasama militer dengan negara lain yang disepakati dalam perjanjian tersebut sebagai rahasia atau sangat rahasia;<br>
6. sistem persandian negara; dan/atau<br>
7. sistem intelijen negara.
</div>
d. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik dapat mengungkapkan kekayaan alam Indonesia;<br>
e. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik, dapat merugikan ketahanan ekonomi nasional:
<div style="padding-left: 20px;">
1. rencana awal pembelian dan penjualan mata uang nasional atau asing, saham dan aset vital milik negara;<br>
2. rencana awal perubahan nilai tukar, suku bunga, dan model operasi institusi keuangan;<br>
3. rencana awal perubahan suku bunga bank, pinjaman pemerintah, perubahan pajak, tarif, atau pendapatan negara/daerah lainnya;<br>
4. rencana awal penjualan atau pembelian tanah atau properti;<br>
5. rencana awal investasi asing;<br>
6. proses dan hasil pengawasan perbankan, asuransi, atau lembaga keuangan lainnya; dan/atau<br>
7. hal-hal yang berkaitan dengan proses pencetakan uang.
</div>
f. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik, dapat merugikan kepentingan hubungan luar negeri:
<div style="padding-left: 20px;">
1. posisi, daya tawar dan strategi yang akan dan telah diambil oleh negara dalam hubungannya dengan negosiasi internasional;<br>
2. korespondensi diplomatik antarnegara;<br>
3. sistem komunikasi dan persandian yang dipergunakan dalam menjalankan hubungan internasional; dan/atau<br>
4. perlindungan dan pengamanan infrastruktur strategis Indonesia di luar negeri.
</div>
g. Informasi Publik yang apabila dibuka dapat mengungkapkan isi akta otentik yang bersifat pribadi dan kemauan terakhir ataupun wasiat seseorang;<br>
h. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik dapat mengungkap rahasia pribadi, yaitu:
<div style="padding-left: 20px;">
1. riwayat dan kondisi anggota keluarga;<br>
2. riwayat, kondisi dan perawatan, pengobatan kesehatan fisik, dan psikis seseorang;<br>
3. kondisi keuangan, aset, pendapatan, dan rekening bank seseorang;<br>
4. hasil-hasil evaluasi sehubungan dengan kapabilitas, intelektualitas, dan rekomendasi kemampuan seseorang; dan/atau<br>
5. catatan yang menyangkut pribadi seseorang yang berkaitan dengan kegiatan satuan pendidikan formal dan satuan pendidikan nonformal.
</div>
i. memorandum atau surat-surat antar Badan Publik atau intra Badan Publik, yang menurut sifatnya dirahasiakan kecuali atas putusan Komisi Informasi atau pengadilan;<br>
j. informasi yang tidak boleh diungkapkan berdasarkan Undang-Undang.
</div>

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 25px 0 10px 0;">
<span style="font-size: 15px;">UU No 27 Tahun 2022 tentang Perlindungan Data Pribadi (PDP)</span><br>
ВАВ III<br>
JENIS DATA PRIBADI<br>
Pasal 4
</div>
(1) Data Pribadi terdiri atas:
<div style="padding-left: 20px;">
a. Data Pribadi yang bersifat spesifik; dan<br>
b. Data Pribadi yang bersifat umum.
</div>
(2) Data Pribadi yang bersifat spesifik sebagaimana dimaksud pada ayat (1) huruf a meliputi:
<div style="padding-left: 20px;">
a. data dan informasi kesehatan;<br>
b. data biometrik;<br>
c. data genetika;<br>
d. catatan kejahatan;<br>
e. data anak;<br>
f. data keterangan pribadi; dan/atau<br>
g. data lainnya sesuai dengan ketentuan peraturan perundang-undangan.
</div>
(3) Data Pribadi yang bersifat umum sebagaimana dimaksud pada ayat (1) huruf b meliputi:
<div style="padding-left: 20px;">
a. nama lengkap;<br>
b. jenis kelamin;<br>
c. agama;<br>
d. status perkawinan; dan/atau<br>
e. Data Pribadi yang dikombinasikan<br>
f. mengidentifikasi seseorang
</div>

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 15px 0 10px 0;">Pasal 20</div>
(1) Pengendali Data Pribadi wajib memiliki dasar pemrosesan Data Pribadi.<br>
(2) Dasar pemrosesan Data Pribadi sebagaimana dimaksud pada ayat (1) meliputi:
<div style="padding-left: 20px;">
a. persetujuan yang sah secara eksplisit dari Subjek Data Pribadi untuk 1 (satu) atau beberapa tujuan tertentu yang telah disampaikan oleh Pengendali Data Pribadi kepada Subjek Data Pribadi;<br>
b. pemenuhan kewajiban perjanjian dalam hal Subjek Data Pribadi merupakan salah satu pihak atau untuk memenuhi permintaan Subjek Data Pribadi pada saat akan melakukan pejanjian;<br>
c. pemenuhan kewajiban hukum dari Pengendali Data Pribadi sesuai dengan ketentuan peraturan perundang-undangan;<br>
d. pemenuhan pelindungan kepentingan vital Subjek Data Pribadi;<br>
e. pelaksanaan tugas dalam rangka kepentingan umum, pelayanan publik, atau pelaksanaan kewenangan Pengendali Data Pribadi berdasarkan peraturan perundang-undangan; dan/atau<br>
f. pemenuhan kepentingan yang sah lainnya dengan memperhatikan tujuan, kebutuhan, dan keseimbangan kepentingan Pengendali Data Pribadi dan hak Subjek Data Pribadi.
</div>

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 15px 0 10px 0;">Pasal 35</div>
Pengendali Data Pribadi wajib melindungi dan memastikan keamanan Data Pribadi yang diprosesnya, dengan melakukan:
<div style="padding-left: 20px;">
a. penyusunan dan penerapan langkah teknis operasional untuk melindungi Data Pribadi dari gangguan pemrosesan Data Pribadi yang bertentangan dengan ketentuan peraturan perundang-undangan; dan<br>
b. penentuan tingkat keamanan Data Pribadi dengan memperhatikan sifat dan risiko dari Data Pribadi yang harus dilindungi dalam pemrosesan Data Pribadi.
</div>

<hr style="border-color:#E2E8F0; margin: 20px 0;">

<h4 style="color:#18A924; margin-bottom: 5px;">C. Mitigasi Bencana (Risiko Geografis, Keselamatan, & Kesehatan)</h4>

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 15px 0 10px 0;">
<span style="font-size: 15px;">UU No 14 Tahun 2008 tentang Keterbukaan Informasi Publik (KIP)</span><br>
Bagian Kedua<br>
Informasi yang Wajib Diumumkan secara Serta-merta<br>
Pasal 10
</div>
(1) Badan Publik wajib mengumumkan secara serta merta suatu informasi yang dapat mengancam hajat hidup orang banyak dan ketertiban umum.<br>
(2) Kewajiban menyebarluaskan Informasi Publik sebagaimana dimaksud pada ayat (1) disampaikan dengan cara yang mudah dijangkau oleh Masyarakat dan dalam bahasa yang mudah dipahami.<br>

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 25px 0 10px 0;">
<span style="font-size: 15px;">UU No 27 Tahun 2022 tentang Perlindungan Data Pribadi (PDP)</span><br>
Pasal 17
</div>
(1) Pemasangan alat pemroses atau pengolah data visual di tempat umum dan/atau pada fasilitas pelayanan publik dilakukan dengan ketentuan:
<div style="padding-left: 20px;">
a. untuk tujuan keamanan, pencegahan bencana, dan/atau penyelenggaraan lalu lintas atau pengumpulan, analisis, dan pengaturan informasi lalu lintas;<br>
b. harus menampilkan informasi pada area yang telah dipasang alat pemroses atau pengolah data visual; dan<br>
c. tidak digunakan untuk mengidentifikasi seseorang.
</div>
(2) Ketentuan sebagaimana dimaksud pada ayat (1) huruf b dan huruf c dikecualikan untuk pencegahan tindak pidana dan proses penegakan hukum sesuai dengan ketentuan peraturan perundang-undangan.<br>

<br><strong style="color:#1E293B;">Sistem Informasi Geografis (Peta Administrasi, Tata Guna Lahan, dll):</strong><br>

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 15px 0 10px 0;">
<span style="font-size: 15px;">UU No 14 Tahun 2008 tentang Keterbukaan Informasi Publik (KIP)</span><br>
Bagian Ketiga<br>
Informasi yang Wajib Tersedia Setiap Saat<br>
Pasal 11
</div>
(1) Badan Publik wajib menyediakan Informasi Publik setiap saat yang meliputi:
<div style="padding-left: 20px;">
a. daftar seluruh Informasi Publik yang berada di bawah penguasaannya, tidak termasuk informasi yang dikecualikan;<br>
b. hasil keputusan Badan Publik dan pertimbangannya;<br>
c. seluruh kebijakan yang ada berikut dokumen pendukungnya;<br>
d. rencana kerja proyek termasuk di dalamnya perkiraan pengeluaran tahunan Badan Publik;<br>
e. perjanjian Badan Publik dengan pihak ketiga;<br>
f. informasi dan kebijakan yang disampaikan Pejabat Publik dalam pertemuan yang terbuka untuk umum;<br>
g. prosedur kerja pegawai Badan Publik yang berkaitan dengan pelayanan masyarakat; dan/atau<br>
h. laporan mengenai pelayanan akses Informasi Publik sebagaimana diatur dalam Undang-Undang ini.
</div>
(2) Informasi Publik yang telah dinyatakan terbuka bagi masyarakat berdasarkan mekanisme keberatan dan/atau penyelesaian sengketa sebagaimana dimaksud dalam Pasal 48, Pasal 49, dan Pasal 50 dinyatakan sebagai Informasi Publik yang dapat diakses oleh Pengguna Informasi Publik.<br>
(3) Ketentuan lebih lanjut mengenai tata cara pelaksanaan kewajiban Badan Publik menyediakan Informasi Publik yang dapat diakses oleh Pengguna Informasi Publik sebagaimana dimaksud pada ayat (1) dan ayat (2) diatur dengan Petunjuk Teknis Komisi Informasi.

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 25px 0 10px 0;">
BAB V<br>
INFORMASI YANG DIKECUALIKAN<br>
Pasal 17
</div>
Setiap Badan Publik wajib membuka akses bagi setiap Pemohon Informasi Publik untuk mendapatkan Informasi Publik, kecuali:
<div style="padding-left: 20px;">
a. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik dapat menghambat proses penegakan hukum, yaitu informasi yang dapat:
<div style="padding-left: 20px;">
1. menghambat proses penyelidikan dan penyidikan suatu tindak pidana;<br>
2. mengungkapkan identitas informan, pelapor, saksi, dan/atau korban yang mengetahui adanya tindak pidana;<br>
3. mengungkapkan data intelijen kriminal dan rencana-rencana yang berhubungan dengan pencegahan dan penanganan segala bentuk kejahatan transnasional;<br>
4. membahayakan keselamatan dan kehidupan penegak hukum dan/atau keluarganya; dan/atau<br>
5. membahayakan keamanan peralatan, sarana, dan/atau prasarana penegak hukum.
</div>
b. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik dapat mengganggu kepentingan perlindungan hak atas kekayaan intelektual dan perlindungan dari persaingan usaha tidak sehat;<br>
c. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik dapat membahayakan pertahanan dan keamanan negara, yaitu:
<div style="padding-left: 20px;">
1. informasi tentang strategi, intelijen, operasi, taktik dan teknik yang berkaitan dengan penyelenggaraan sistem pertahanan dan keamanan negara, meliputi tahap perencanaan, pelaksanaan dan pengakhiran atau evaluasi dalam kaitan dengan ancaman dari dalam dan luar negeri;<br>
2. dokumen yang memuat tentang strategi, intelijen, operasi, teknik dan taktik yang berkaitan dengan penyelenggaraan sistem pertahanan dan keamanan negara yang meliputi tahap perencanaan, pelaksanaan dan pengakhiran atau evaluasi;<br>
3. jumlah, komposisi, disposisi, atau dislokasi kekuatan dan kemampuan dalam penyelenggaraan sistem pertahanan dan keamanan negara serta rencana pengembangannya;<br>
4. gambar dan data tentang situasi dan keadaan pangkalan dan/atau instalasi militer;<br>
5. data perkiraan kemampuan militer dan pertahanan negara lain terbatas pada segala Tindakan dan/atau indikasi negara tersebut yang dapat membahayakan kedaulatan Negara Kesatuan Republik Indonesia dan/atau data terkait kerjasama militer dengan negara lain yang disepakati dalam perjanjian tersebut sebagai rahasia atau sangat rahasia;<br>
6. sistem persandian negara; dan/atau<br>
7. sistem intelijen negara.
</div>
d. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik dapat mengungkapkan kekayaan alam Indonesia;<br>
e. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik, dapat merugikan ketahanan ekonomi nasional:
<div style="padding-left: 20px;">
1. rencana awal pembelian dan penjualan mata uang nasional atau asing, saham dan aset vital milik negara;<br>
2. rencana awal perubahan nilai tukar, suku bunga, dan model operasi institusi keuangan;<br>
3. rencana awal perubahan suku bunga bank, pinjaman pemerintah, perubahan pajak, tarif, atau pendapatan negara/daerah lainnya;<br>
4. rencana awal penjualan atau pembelian tanah atau properti;<br>
5. rencana awal investasi asing;<br>
6. proses dan hasil pengawasan perbankan, asuransi, atau lembaga keuangan lainnya; dan/atau<br>
7. hal-hal yang berkaitan dengan proses pencetakan uang.
</div>
f. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik, dapat merugikan kepentingan hubungan luar negeri:
<div style="padding-left: 20px;">
1. posisi, daya tawar dan strategi yang akan dan telah diambil oleh negara dalam hubungannya dengan negosiasi internasional;<br>
2. korespondensi diplomatik antarnegara;<br>
3. sistem komunikasi dan persandian yang dipergunakan dalam menjalankan hubungan internasional; dan/atau<br>
4. perlindungan dan pengamanan infrastruktur strategis Indonesia di luar negeri.
</div>
g. Informasi Publik yang apabila dibuka dapat mengungkapkan isi akta otentik yang bersifat pribadi dan kemauan terakhir ataupun wasiat seseorang;<br>
h. Informasi Publik yang apabila dibuka dan diberikan kepada Pemohon Informasi Publik dapat mengungkap rahasia pribadi, yaitu:
<div style="padding-left: 20px;">
1. riwayat dan kondisi anggota keluarga;<br>
2. riwayat, kondisi dan perawatan, pengobatan kesehatan fisik, dan psikis seseorang;<br>
3. kondisi keuangan, aset, pendapatan, dan rekening bank seseorang;<br>
4. hasil-hasil evaluasi sehubungan dengan kapabilitas, intelektualitas, dan rekomendasi kemampuan seseorang; dan/atau<br>
5. catatan yang menyangkut pribadi seseorang yang berkaitan dengan kegiatan satuan Pendidikan formal dan satuan pendidikan nonformal.
</div>
i. memorandum atau surat-surat antar Badan Publik atau intra Badan Publik, yang menurut sifatnya dirahasiakan kecuali atas putusan Komisi Informasi atau pengadilan;<br>
j. informasi yang tidak boleh diungkapkan berdasarkan Undang-Undang.
</div>

<hr style="border-color:#E2E8F0; margin: 20px 0;">

<h4 style="color:#18A924; margin-bottom: 5px;">D. Narasi Sejarah, Konsep Branding, Statistik, dan Copywriting</h4>

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 15px 0 10px 0;">
<span style="font-size: 15px;">UU No 14 Tahun 2008 tentang Keterbukaan Informasi Publik (KIP)</span><br>
Bagian Keempat<br>
Kewajiban Badan Publik<br>
Pasal 7
</div>
(1) Badan Publik wajib menyediakan, memberikan dan/atau menerbitkan Informasi Publik yang berada di bawah kewenangannya kepada Pemohon Informasi Publik, selain informasi yang dikecualikan sesuai dengan ketentuan.<br>
(2) Badan Publik wajib menyediakan Informasi Publik yang akurat, benar, dan tidak menyesatkan.<br>
(3) Untuk melaksanakan kewajiban sebagaimana dimaksud pada ayat (2), Badan Publik harus membangun dan mengembangkan sistem informasi dan dokumentasi untuk mengelola Informasi Publik secara baik dan efisien sehingga dapat diakses dengan mudah.<br>
(4) Badan Publik wajib membuat pertimbangan secara tertulis setiap kebijakan yang diambil untuk memenuhi hak setiap Orang atas Informasi Publik.<br>
(5) Pertimbangan sebagaimana dimaksud pada ayat (4) antara lain memuat pertimbangan politik, ekonomi, sosial, budaya, dan/atau pertahanan dan keamanan negara.<br>
(6) Dalam rangka memenuhi kewajiban sebagaimana dimaksud pada ayat (1) sampai dengan ayat (4) Badan Publik dapat memanfaatkan sarana dan/atau media elektronik dan nonelektronik.

<div style="text-align: center; color: #1E293B; font-weight: bold; margin: 25px 0 10px 0;">
BAB IV<br>
INFORMASI YANG WAJIB DISEDIAKAN DAN DIUMUMKAN<br>
Bagian Kesatu<br>
Informasi yang Wajib Disediakan dan Diumumkan Secara Berkala<br>
Pasal 9
</div>
(1) Setiap Badan Publik wajib mengumumkan Informasi Publik secara berkala.<br>
(2) Informasi Publik sebagaimana dimaksud pada ayat (1) meliputi:
<div style="padding-left: 20px;">
a. informasi yang berkaitan dengan Badan Publik;<br>
b. informasi mengenai kegiatan dan kinerja Badan Publik terkait;<br>
c. informasi mengenai laporan keuangan; dan/atau<br>
d. informasi lain yang diatur dalam peraturan perundang-undangan.
</div>
(3) Kewajiban memberikan dan menyampaikan Informasi Publik sebagaimana dimaksud pada ayat (2) dilakukan paling singkat 6 (enam) bulan sekali.<br>
(4) Kewajiban menyebarluaskan Informasi Publik sebagaimana dimaksud pada ayat (1), disampaikan dengan cara yang mudah dijangkau oleh Masyarakat dan dalam bahasa yang mudah dipahami.<br>
(5) Cara-cara sebagaimana dimaksud pada ayat (4) ditentukan lebih lanjut oleh Pejabat Pengelola Informasi dan Dokumentasi di Badan Publik terkait.<br>
(6) Ketentuan lebih lanjut mengenai kewajiban Badan Publik memberikan dan menyampaikan Informasi Publik secara berkala sebagaimana dimaksud pada ayat (1), ayat (2), dan ayat (3) diatur dengan Petunjuk Teknis Komisi Informasi.

</div>
        """, unsafe_allow_html=True)