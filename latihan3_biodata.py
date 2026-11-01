# Konversi Celcius ke Fahrenheit dan Kelvin

celcius = float(input("Masukkan suhu dalam Celcius: "))

fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15

print(f"Suhu dalam Fahrenheit: {fahrenheit} °F")
print(f"Suhu dalam Kelvin: {kelvin} K")