#nilai yg fix gk berubah
LOKASI = ["A", "B", "C"]
JENIS = [1, 2, 3, 4]
NAMA_JENIS = {
    1: "Helm/Seatbelt",
    2: "Handphone",
    3: "Kecepatan",
    4: "Plat Nomor",
}


#BAGIAN FUNCTION BANTU
#========================================================================
#Meninjau hanya kasus dari satu lokasi tertentu
def ambil_data_lokasi(data, lokasi):
    hasil = []                        # tumpukan baru (masih kosong)
    for d in data:                    # ambil kasus satu per satu
        if d["lokasi"] == lokasi:     # cek tulisan lokasi di kasus
            hasil.append(d)           # cocok -> taruh ke tumpukan baru
    return hasil                      

#hitung suatu jenis pelanggaran dari semua suatu lokasi
def hitung_per_jenis(data):
    hitungan = {1: 0, 2: 0, 3: 0, 4: 0}   # tumbukan baru (directionary), semua pelanggaran mulai dari 0
    for d in data:                         # ambil kasus satu per satu
        hitungan[d["jenis"]] += 1          # tambah 1 di kolom jenis pelanggaran itu
    return hitungan                       

def hitung_per_jam(data):
    hitungan = {}                    #directionary baru kosong
    for jam in range(24):            # untuk semua {jam} sampe jam = 24
        hitungan[jam] = 0            # bernilai 0 (ini intinya bikin "key" di directionary)
    for d in data:                   # ambil kasus satu per satu
        hitungan[d["jam"]] += 1      # tambah 1 di "key" jam yg didapet
    return hitungan

#menghitung siapa modus dan nilai modusnya dari suatu dictionary
def cari_modus(hitungan):                   # parameter inputnya adalah dictionary hitungan (return dari function2 sebelumnya)
                                            # bisa dipake untuk {key} apapun dari dictionary data 
                                            # return nya adalah nilai modus dan siapa yg punya nilai modus itu
    nilai_modus = max(hitungan.values())        #nyari modus dari value di dictionary yg diinput
    if nilai_modus == 0:                        #kalau data kosong
        return 0, []                            

    key_modus = []                          #list kosong baru
    for key in hitungan:                    # ngambil satu per satu {key} (apapun itu) dari dictionary yg diinput
        if hitungan[key] == nilai_modus:    # cek apakah key itu punya value modus 
            key_modus.append(key)           #masukin ke list siapa yg punya
    return nilai_modus, key_modus

#BAGIAN DATA 
# =================================================================================
#Ini baklan menjadi input untuk "database" yang bakal dipake buat ngitung
def input_data():
    data = []
    jumlah = int(input("Jumlah data pelanggaran yang ingin dimasukkan: "))

    for i in range(jumlah):
        print("\nData ke-" + str(i + 1))
        lokasi = input("Lokasi ETLE (A/B/C): ").upper()
        jenis = int(input("Jenis Pelanggaran (1-4): "))
        tanggal = int(input("Tanggal: "))
        bulan = int(input("Bulan: "))
        tahun = int(input("Tahun: "))
        jam = int(input("Pukul (0-23): "))
        menit = int(input("Menit (0-59): "))

        data.append({
            "lokasi": lokasi,
            "jenis": jenis,
            "tanggal": tanggal,
            "bulan": bulan,
            "tahun": tahun,
            "jam": jam,
            "menit": menit,
        })
    return data

#Ini adalah data contoh (pre-exixting data) untuk demonstrasi
def data_contoh():
    # format: (lokasi, jenis, tanggal, bulan, tahun, jam, menit)
    contoh = [
        ("A", 1, 1, 6, 2026, 7, 15), ("A", 1, 1, 6, 2026, 7, 40),
        ("A", 2, 1, 6, 2026, 8, 5),  ("A", 1, 2, 6, 2026, 7, 55),
        ("A", 3, 2, 6, 2026, 17, 30), ("A", 4, 3, 6, 2026, 12, 0),
        ("B", 2, 1, 6, 2026, 17, 10), ("B", 2, 1, 6, 2026, 17, 45),
        ("B", 2, 2, 6, 2026, 18, 20), ("B", 3, 2, 6, 2026, 17, 50),
        ("B", 4, 3, 6, 2026, 9, 0),
        ("C", 4, 1, 6, 2026, 22, 10), ("C", 4, 2, 6, 2026, 22, 30),
        ("C", 3, 2, 6, 2026, 13, 15), ("C", 1, 3, 6, 2026, 22, 45),
        ("C", 2, 3, 6, 2026, 6, 20),
    ]

    data=[]
    for c in contoh:
        data.append({
            "lokasi": c[0], "jenis": c[1], "tanggal": c[2],
            "bulan": c[3], "tahun": c[4], "jam": c[5], "menit": c[6],
        })
    return data
# =======================================================================


# FUNCTION JENIS PELANGGARAN MODUS
def tampilkan_jenis_tertinggi(data):
    print("\n==============================================")
    print("JENIS PELANGGARAN TERTINGGI")
    print("==============================================")

    # --- Gabungan seluruh lokasi ---
    hitungan = hitung_per_jenis(data)
    value_modus, key_modus = cari_modus(hitungan)

    print("\n[Seluruh Lokasi (A+B+C)]")
    for j in JENIS:
        print("  " + NAMA_JENIS[j], ":", hitungan[j], "kali")
        teks = ", ".join([NAMA_JENIS[j] for j in key_modus])

    # --- Per lokasi ---
    for lokasi in LOKASI:
        data_lokasi = ambil_data_lokasi(data, lokasi)
        hitungan = hitung_per_jenis(data_lokasi)
        value_modus, key_modus = cari_modus(hitungan)

        print("\n[Lokasi " + lokasi + "]")
        if value_modus == 0:
            print("  Belum ada data")
            continue
        for j in JENIS:
            print("  " + NAMA_JENIS[j], ":", hitungan[j], "kali")
            teks = ", ".join([NAMA_JENIS[j] for j in key_modus])

#FUNCTION JAM PELANGGARAN PALING SERING
def tampilkan_jam_tertinggi(data):
    print("\n==============================================")
    print("JAM PELANGGARAN PALING SERING DI SETIAP LOKASI")
    print("==============================================")

    for lokasi in LOKASI:
        data_lokasi = ambil_data_lokasi(data, lokasi)
        hitungan = hitung_per_jam(data_lokasi)
        value_modus, key_modus = cari_modus(hitungan)

        print("\n[Lokasi " + lokasi + "]")
        if value_modus == 0:
            print("  Belum ada data")
            continue
        for jam in range(24):
            if hitungan[jam] > 0:
                print("  %02d:00 - %02d:59 : %d kali" % (jam, jam, hitungan[jam]))
        for jam in key_modus:
            print("=> Paling sering: pukul %02d:00 - %02d:59 (%d kali)"
                  % (jam, jam, value_modus))
# ==========================================


#FUNCTION PERBANDINGAN LOKASI
def tampilkan_perbandingan(data):
    print("\n==============================================")
    print("PERBANDINGAN LOKASI A, B, C")
    print("==============================================")

    # Tabel perbandingan
    print("\nLokasi | Helm/Seatbelt | Handphone | Kecepatan | Plat Nomor | Total")
    print("-------+---------------+-----------+-----------+------------+------")
    hasil = {}  # hitungan per jenis untuk tiap lokasi
    total = {}  # total pelanggaran tiap lokasi
    for lokasi in LOKASI:
        data_lokasi = ambil_data_lokasi(data, lokasi)
        hasil[lokasi] = hitung_per_jenis(data_lokasi)
        total[lokasi] = len(data_lokasi)
        h = hasil[lokasi]
        print("  %s    | %13d | %9d | %9d | %10d | %5d"
              % (lokasi, h[1], h[2], h[3], h[4], total[lokasi]))

    # Lokasi dengan pelanggaran total terbanyak
    value_modus, key_modus = cari_modus(total)
    print("\nLokasi dengan pelanggaran terbanyak:", ", ".join(key_modus),
          "(" + str(value_modus) + " kali)")

    # Per jenis: lokasi mana yang paling banyak
    print("\nLokasi tertinggi untuk tiap jenis pelanggaran:")
    for j in JENIS:
        per_lokasi = {}
        for lokasi in LOKASI:
            per_lokasi[lokasi] = hasil[lokasi][j]
        value_modus, key_modus = cari_modus(per_lokasi)
        if value_modus == 0:
            print("  " + NAMA_JENIS[j], ": belum ada data")
        else:
            print("  " + NAMA_JENIS[j], ":", ", ".join(key_modus),
                  "(" + str(value_modus) + " kali)")

    # Jenis terbanyak di tiap lokasi
    print("\nJenis pelanggaran terbanyak di tiap lokasi:")
    for lokasi in LOKASI:
        value_modus, key_modus = cari_modus(hasil[lokasi])
        if value_modus == 0:
            print("  Lokasi", lokasi, ": belum ada data")
        else:
            teks = ", ".join([NAMA_JENIS[j] for j in key_modus])
            print("  Lokasi", lokasi, ":", teks,
                  "(" + str(value_modus) + " kali)")


# PROGRAM UTAMA
# ==========================================
print("=== ANALISIS MAKRO ETLE ===")

pesan = "Selamat datang! Apa yang ingin dilakukan?\n  1.Muat data contoh\n  2.Input data baru\n"
print(pesan)
opt = int(input("Opsi yang dipilih: "))
if opt == 1 :
    data_pelanggaran = data_contoh()
else: 
    data_pelanggaran= input_data()

tampilkan_jenis_tertinggi(data_pelanggaran)
tampilkan_jam_tertinggi(data_pelanggaran)
tampilkan_perbandingan(data_pelanggaran)
