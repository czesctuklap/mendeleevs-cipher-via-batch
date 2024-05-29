import os

# Słownik z elementami Mendelejewa
elements = {
    "H": 1, "HE": 2, "LI": 3, "BE": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "NE": 10,
    "NA": 11, "MG": 12, "AL": 13, "SI": 14, "P": 15, "S": 16, "CL": 17, "AR": 18, "K": 19,
    "CA": 20, "SC": 21, "TI": 22, "V": 23, "CR": 24, "MN": 25, "FE": 26, "CO": 27, "NI": 28,
    "CU": 29, "ZN": 30, "GA": 31, "GE": 32, "AS": 33, "SE": 34, "BR": 35, "KR": 36, "RB": 37,
    "SR": 38, "Y": 39, "ZR": 40, "NB": 41, "MO": 42, "TC": 43, "RU": 44, "RH": 45, "PD": 46,
    "AG": 47, "CD": 48, "IN": 49, "SN": 50, "SB": 51, "TE": 52, "I": 53, "XE": 54, "CS": 55,
    "BA": 56, "LA": 57, "CE": 58, "PR": 59, "ND": 60, "PM": 61, "SM": 62, "EU": 63, "GD": 64,
    "TB": 65, "DY": 66, "HO": 67, "ER": 68, "TM": 69, "YB": 70, "LU": 71, "HF": 72, "TA": 73,
    "W": 74, "RE": 75, "OS": 76, "IR": 77, "PT": 78, "AU": 79, "HG": 80, "TL": 81, "PB": 82,
    "BI": 83, "PO": 84, "AT": 85, "RN": 86, "FR": 87, "RA": 88, "AC": 89, "TH": 90, "PA": 91,
    "U": 92, "NP": 93, "PU": 94, "AM": 95, "CM": 96, "BK": 97, "CF": 98, "ES": 99, "FM": 100,
    "MD": 101, "NO": 102, "LR": 103, "RF": 104, "DB": 105, "SG": 106, "BH": 107, "HS": 108,
    "MT": 109, "DS": 110, "RG": 111, "CN": 112, "NH": 113, "FL": 114, "MC": 115, "LV": 116,
    "TS": 117, "OG": 118
}

# Funkcja szyfrująca tekst zgodnie z szyfrem Mendelejewa
def mendeleev_cipher(input_text):
    sentence = list(input_text.upper())  # Konwersja tekstu na wielkie litery
    ciphered = []
    output = ""

# Główna pętla sprawdzająca
    i = 0
    while i < len(sentence):
        if sentence[i].isalpha():
            pair = "  "
            if i + 1 < len(sentence):
                pair = sentence[i] + sentence[i + 1]

            if pair in elements:
                ciphered.append(str(elements[pair]))

                if i + 2 == len(sentence):
                    break
                else:
                    ciphered.append("*")
                    i += 1
            else:
                if sentence[i] in elements:
                    ciphered.append(str(elements[sentence[i]]))
                    if i + 1 == len(sentence):
                        break
                    else:
                        ciphered.append("*")
                else:
                    raise Exception()
        elif sentence[i] == ' ':
            ciphered.append("*")
        else:
            raise Exception()
        i += 1

    for element in ciphered:
        output += element

    return output

# Funkcja sprawdzająca możliwość zaszyfrowania tekstu
def check(text):
    try:
        output = mendeleev_cipher(text)
        return output
    except Exception as e:
        return "Nie mozna zaszyfrowac podanego tekstu"

if __name__ == "__main__":    
    filenameIN = "input.txt"
    output_folder = r"C:\Users\zuzia\Desktop\wszystko\Python\semestr III\Języki Skryptowe\projekt\backup"
    
    # Utworzenie folderu na kopie zapasowe, jeśli nie istnieje
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        # Odczytanie tekstu z pliku wejściowego
        with open(filenameIN, "r") as file:
            input_text = file.read()
            input_text_lines = input_text.split("\n")

        # Szyfrowanie linii tekstu
        encrypted_text_lines = [check(line) for line in input_text_lines]

        # Zapisanie zaszyfrowanego tekstu do pliku
        output_filename = os.path.join(output_folder, "output.txt")
        with open(output_filename, "w") as file:
            for encrypted_line in encrypted_text_lines:
                file.write(encrypted_line + "\n")

        # Dodatkowe zapisanie zaszyfrowanego tekstu do pliku w oryginalnej lokalizacji
        output_filename_original = "output.txt"
        with open(output_filename_original, "w") as file:
            for encrypted_line in encrypted_text_lines:
                file.write(encrypted_line + "\n")

    except FileNotFoundError:
        print("Nie znaleziono pliku")

    except Exception as e:
        print(e)
