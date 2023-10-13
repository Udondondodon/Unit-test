def calculator(operasi, bilangan_1, bilangan_2):
    if operasi == '1':
        hasil = bilangan_1 + bilangan_2
        return f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}'
    elif operasi == '2':
        hasil = bilangan_1 - bilangan_2
        return f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}'
    elif operasi == '3':
        hasil = bilangan_1 * bilangan_2
        return f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}'
    elif operasi == '4':
        if bilangan_2 == 0:
            return 'Pembagian oleh nol tidak diizinkan'
        hasil = bilangan_1 / bilangan_2
        return f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}'
    else:
        return 'Tidak valid'