import os


def extract_keyword(keyword, input_file, output_file):
    try:
        os.makedirs('outputs', exist_ok=True)

        with open(f"data/{input_file}", "r") as infile, open(f"outputs/{output_file}", "w") as outfile:
            for line in infile:
                if keyword in line:
                    outfile.write(line)
        print(f"'{keyword}' anahtar kelimesini içeren satırlar 'outputs/{output_file}' dosyasına başarıyla yazıldı.")

    except FileNotFoundError as e:
        print(f"Hata: {e}. Lütfen girdi dosyasının 'data' klasöründe olduğundan emin olun.")

    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")


def read_in_files(keyword):
    results = []
    directory = 'data/'

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, start=1):
                    if keyword.lower() in line.lower():
                        results.append(f"{filename} (Line {line_num}): {line.strip()}")

    with open('keyword.txt', 'w', encoding='utf-8') as output_file:
        for result in results:
            output_file.write(result + '\n')

    print(f"Toplam {len(results)} satır bulundu. Sonuçlar 'keyword.txt' dosyasına kaydedildi.")


extract_keyword("Python", "file1.txt", "file1_output.txt")
read_in_files("python")

