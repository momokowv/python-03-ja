import os
import re

# ファイルが含まれるディレクトリ
directory = '01_challenge/data/text_files'

# 書籍名を格納するリスト
book_names = []

# ディレクトリ内のファイルを走査
for filename in os.listdir(directory):
    if filename.startswith("Chapter_") and filename.endswith(".txt"):
        continue  # Chapter_x.txt ファイルはスキップする
    with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
        # 書籍名をファイル名から抽出し、リストに追加
        book_name = re.sub(r'\.txt$', '', filename)  # 拡張子を取り除く
        book_names.append(book_name)

# 書籍名を1つのテキストファイルに保存する
output_filename = 'books.txt'
with open(output_filename, 'w', encoding='utf-8') as output_file:
    for name in book_names:
        output_file.write(name + '\n')

print(f"書籍名が {len(book_names)} 件、ファイル '{output_filename}' に保存されました。")
