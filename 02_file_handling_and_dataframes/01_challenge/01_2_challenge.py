import os
from pathlib import Path

# データディレクトリと新規作成するライブラリディレクトリ
data_directory = '01_challenge/data'
library_directory = 'library'

# ディレクトリが存在しない場合は新規作成
os.makedirs(os.path.join(data_directory, library_directory), exist_ok=True)

# 10個の Chapter_x.txt ファイルを library ディレクトリに移動
for i in range(1, 11):
    chapter_file = f'Chapter_{i}.txt'
    source_path = os.path.join(data_directory, 'text_files', chapter_file)
    dest_path = os.path.join(data_directory, library_directory, chapter_file)
    os.replace(source_path, dest_path)

# library ディレクトリに移動して、ファイルとサイズを一覧表示
library_path = os.path.join(data_directory, library_directory)
files = os.listdir(library_path)

print(f"{len(files)} 個のファイルが library ディレクトリに保存されました:")
for file in files:
    file_path = os.path.join(library_path, file)
    file_size = os.path.getsize(file_path)
    print(f"{file} - サイズ: {file_size} bytes")
