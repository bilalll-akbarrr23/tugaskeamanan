def enkripsi(plain_text, shift):
    chiper_text = ""
    
    for char in plain_text:
        # Huruf besar
        if char.isupper():
            chiper_text += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Huruf kecil
        elif char.islower():
            chiper_text += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Karakter lainnya (misalnya spasi atau tanda baca) tetap sama
        else:
            chiper_text += char   
    return chiper_text

def dekripsi(cipher_text, shift):
    plain_text = ""
    
    for char in cipher_text:
        # Huruf Besar
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        
        # Huruf Kecil
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        
        # Karakter lainnya (misalnya spasi atau tanda baca) tetap sama
        else:
            plain_text += char
    return plain_text

def main():
    print("Selamat datang di program Kriptografi Caesar!")
    
    # Masukkan teks asli dan nilai shift
    plain_text = input("Masukkan teks asli (plaintext): ")
    shift = int(input("Masukkan nilai pergeseran (1-25): "))

    # Panggil fungsi enkripsi
    cipher_text = enkripsi(plain_text, shift)
    print("Teks terenkripsi:", cipher_text)

    # Panggil fungsi dekripsi
    decrypted_text = dekripsi(cipher_text, shift)
    print("Teks terdekripsi:", decrypted_text)

# Menjalankan program
if __name__ == "__main__":
    main()