daftar_gejala = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Airliur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Beratbadan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bolamata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh dimulut",
    "G29": "Benjolan dileher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam"
}

daftar_penyakit = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nafasoring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"]
}

def tampilkan_gejala():
    print("\n" + "="*50)
    print("DAFTAR GEJALA PENYAKIT THT")
    print("="*50)
    items = list(daftar_gejala.items())
    for i in range(0, len(items), 2):
        k1, v1 = items[i]
        if i + 1 < len(items):
            k2, v2 = items[i+1]
            print(f"{k1:^4} | {v1:<25} {k2:^4} | {v2}")
        else:
            print(f"{k1:^4} | {v1:<25}")
    print("="*50)

def diagnosa(gejala_input):
    hasil_diagnosa = []
    
    for penyakit, gejala_penyakit in daftar_penyakit.items():
        gejala_cocok = set(gejala_input).intersection(set(gejala_penyakit))
        if len(gejala_cocok) > 0:
            persentase = (len(gejala_cocok) / len(gejala_penyakit)) * 100
            hasil_diagnosa.append({
                "penyakit": penyakit,
                "persentase": persentase,
                "gejala_cocok": gejala_cocok
            })
    
    hasil_diagnosa.sort(key=lambda x: x["persentase"], reverse=True)
    return hasil_diagnosa

def main():
    print("\nSelamat Datang di Sistem Pakar Diagnosa Penyakit THT")
    tampilkan_gejala()
    
    print("\nSilakan masukkan kode gejala yang anda alami.")
    print("Gunakan koma untuk memisahkan kode jika lebih dari satu (Contoh: G5,G12,G37)")
    input_user = input("Masukkan kode gejala: ").upper().replace(" ", "")
    gejala_input = input_user.split(",")
    gejala_valid = [g for g in gejala_input if g in daftar_gejala]
    
    if not gejala_valid:
        print("\n[!] Tidak ada kode gejala valid yang dimasukkan. Silakan coba lagi.")
        return

    print("\n" + "-"*50)
    print("Gejala yang anda rasakan:")
    for g in gejala_valid:
        print(f"- {g}: {daftar_gejala[g]}")
    print("-"*50)
    
    hasil = diagnosa(gejala_valid)
    
    print("\nHASIL DIAGNOSA:")
    if hasil:
        kemungkinan_utama = hasil[0]
        if kemungkinan_utama["persentase"] == 100.0:
            print(f"=> Anda didiagnosa menderita: ** {kemungkinan_utama['penyakit']} **")
            print(f"   Kecocokan Gejala: 100%")
        else:
            print("=> Kemungkinan terbesar penyakit yang diderita:")
            print(f"   {kemungkinan_utama['penyakit']} (Kecocokan: {kemungkinan_utama['persentase']:.2f}%)")
            
        print("\nKemungkinan penyakit lainnya:")
        for i in range(1, min(4, len(hasil))): # Menampilkan max 3 kemungkinan lain
            print(f"- {hasil[i]['penyakit']} (Kecocokan: {hasil[i]['persentase']:.2f}%)")
    else:
        print("Penyakit tidak terdeteksi dari gejala yang dimasukkan.")

if __name__ == "__main__":
    main()