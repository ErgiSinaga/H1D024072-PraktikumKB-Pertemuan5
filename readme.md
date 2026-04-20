Penjelasan alur kode program Sistem Pakar 2

daftar_gejala = {
    "G1": "Nafas abnormal",
    # ... (gejala lainnya)
}
daftar_gejala = {...}: Ini adalah pembuatan variabel bertipe Dictionary (Kamus). Dictionary menyimpan data dalam format pasangan Key: Value. Di sini, Key adalah kode gejala (misal: "G1") dan Value adalah nama gejalanya

daftar_penyakit = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    # ... (penyakit lainnya)
}
daftar_penyakit = {...}: Ini juga Dictionary. Key-nya adalah nama penyakit, sedangkan Value-nya adalah List (ditandai dengan kurung siku [...]) yang berisi sekumpulan kode gejala penyebab penyakit tersebut. Ini merepresentasikan aturan/pola (Rule Base) sistem pakarnya

def tampilkan_gejala():
    # ... (kode print header)
    items = list(daftar_gejala.items())
items = list(daftar_gejala.items()): Mengambil semua isi dictionary daftar_gejala dan mengubahnya menjadi bentuk List of Tuples. Tujuannya agar data bisa diakses menggunakan indeks angka (0, 1, 2, dst) untuk di-looping nantinya

for i in range(0, len(items), 2):
for i in range(0, len(items), 2):: Melakukan perulangan (looping) dari indeks 0 sampai panjang data, dengan langkah (step) 2. Ini logika utama untuk membuat tampilan 2 kolom (mengambil item ke-0 dan ke-1 untuk baris pertama, item ke-2 dan ke-3 untuk baris kedua, dst).
k1, v1 = items[i]
        if i + 1 < len(items):
            k2, v2 = items[i+1]
            print(f"{k1:^4} | {v1:<25} {k2:^4} | {v2}")
        else:
            print(f"{k1:^4} | {v1:<25}")
a. k1, v1 = items[i]: Mengambil Key (kode) dan Value (nama) dari kolom pertama.
b. if i + 1 < len(items):: Mengecek apakah masih ada sisa data untuk ditaruh di kolom kedua.
c. print(f"{k1:^4} | {v1:<25} ..."): Mencetak teks ke layar menggunakan f-string format.
* :^4 artinya teks dibuat rata tengah (center) dengan lebar 4 spasi.
* :<25 artinya rata kiri (left-aligned) dengan lebar 25 spasi.

def diagnosa(gejala_input):
    hasil_diagnosa = []
hasil_diagnosa = []: Membuat list kosong untuk menampung hasil perhitungan kecocokan penyakit.

for penyakit, gejala_penyakit in daftar_penyakit.items():
for penyakit, ... in daftar_penyakit.items():: Melakukan looping ke setiap penyakit dan aturan gejalanya yang ada di basis pengetahuan.

gejala_cocok = set(gejala_input).intersection(set(gejala_penyakit))
* set(...): Mengubah tipe data List menjadi Set (Himpunan).
* .intersection(...): Ini adalah fungsi himpunan untuk mencari Irisan. Baris ini akan mencari gejala apa saja yang sama-sama ada di inputan user dan di aturan penyakit yang sedang dicek

if len(gejala_cocok) > 0:
            persentase = (len(gejala_cocok) / len(gejala_penyakit)) * 100
            hasil_diagnosa.append({
                "penyakit": penyakit,
                "persentase": persentase,
                "gejala_cocok": gejala_cocok
            })
* if len(gejala_cocok) > 0:: Jika ada minimal 1 gejala yang cocok.
* persentase = ...: Rumus menghitung persentase = (Jumlah irisan gejala / Total gejala pada penyakit tersebut) dikali 100.
* hasil_diagnosa.append(...): Memasukkan data penyakit dan persentasenya ke dalam list hasil_diagnosa dalam bentuk Dictionary

hasil_diagnosa.sort(key=lambda x: x["persentase"], reverse=True)
    return hasil_diagnosa
.sort(key=lambda x: x["persentase"], reverse=True): Mengurutkan list hasil_diagnosa berdasarkan nilai "persentase"-nya. reverse=True memastikan urutannya dari yang paling besar ke yang paling kecil (Descending)

input_user = input("Masukkan kode gejala: ").upper().replace(" ", "")
* .upper(): Mengubah huruf kecil menjadi huruf kapital (contoh: "g1" jadi "G1").
* .replace(" ", ""): Menghapus semua spasi yang mungkin diketik oleh pengguna agar formatnya bersih.

gejala_input = input_user.split(",")
* .split(","): Memecah string menjadi List berdasarkan tanda koma. Contoh string "G1,G2" diubah menjadi List ["G1", "G2"]

gejala_valid = [g for g in gejala_input if g in daftar_gejala]
List Comprehension: Ini adalah cara singkat di Python untuk melakukan looping dan filtering. Baris ini membuat list baru yang HANYA berisi kode gejala yang terdaftar di daftar_gejala. Jika pengguna memasukkan "G99", maka akan otomatis dibuang karena tidak ada di kamus.

if not gejala_valid:
        print("\n[!] Tidak ada kode gejala valid yang dimasukkan...")
        return
Mengecek jika hasil filtering tadi kosong (berarti semua inputan user salah/ngawur), program akan berhenti (return)

hasil = diagnosa(gejala_valid)
Memanggil fungsi diagnosa() dengan mengirimkan data gejala yang sudah divalidasi, lalu menyimpan hasilnya di variabel hasil

kemungkinan_utama = hasil[0]
        # ... (kode print hasil utama)
        for i in range(1, min(4, len(hasil))): 
            print(f"- {hasil[i]['penyakit']} (Kecocokan: {hasil[i]['persentase']:.2f}%)")
* hasil[0]: Mengambil elemen pertama dari list (yang memiliki persentase tertinggi karena sudah di-sort sebelumnya).
* range(1, min(4, len(hasil))): Looping untuk menampilkan kemungkinan penyakit lain. Dimulai dari indeks 1 (penyakit ke-2). min(4, len(hasil)) memastikan maksimal hanya 3 penyakit alternatif yang ditampilkan, atau kurang jika sisa penyakitnya sedikit.
* :.2f: Format string untuk membatasi angka desimal persentase menjadi maksimal 2 angka di belakang koma (contoh: 85.55)

if __name__ == "__main__":
    main()
Ini adalah standar penulisan Python. Baris ini mengecek apakah script sedang dijalankan langsung (bukan di-import oleh file python lain). Jika iya, maka program akan langsung menjalankan fungsi main()