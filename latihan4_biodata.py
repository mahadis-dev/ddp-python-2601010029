# Menghitung Total Belanja 

subtotal = float(input("Masukkan subtotal belanja (Rp): "))

PPN_PERSEN = 0.11
ppn = subtotal * PPN_PERSEN
total = subtotal + ppn

print(f"Subtotal: Rp {subtotal}")
print(f"PPN (11%): Rp {ppn}")
print(f"Total Belanja: Rp {total}")