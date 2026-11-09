BATAS_RAWAT = 5

daftar_pasien = [
    "Pasien A (Demam Berdarah)",
    "Pasien B (Serangan Jantung)",
    "Pasien C (Patah Tulang)",
    "Pasien D (Stroke Akut)",
    "Pasien E (Tipes)",
    "Pasien F (Pasca Operasi Caesar)",
    "Pasien G (Gagal Ginjal Akut)",
    "Pasien H (Diare Dehidrasi)",
    "Pasien I (Asma Akut)",
    "Pasien J (Trauma Kepala Severe)"
]

print("=== EVALUASI PASIEN OPNAME ===")
print(f"Batas Standar Rawat Inap : {BATAS_RAWAT} Hari\n")

for i in range(10):
    nama_pasien = daftar_pasien[i]
    print(f"--- Pasien ke-{i+1}: {nama_pasien} ---")

    lama_rawat = int(input("Masukkan lama rawat inap (hari): "))
    
    status = "Rawat Panjang" if lama_rawat > BATAS_RAWAT else "Rawat Standar"
    
    print(f"Status Pasien ({nama_pasien}): {status}")
    print("-" * 50)