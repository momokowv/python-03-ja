import pandas as pd
from sklearn import datasets

###1. データの読み込みと概要
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

iris_df['species'] = iris.target

print("最初の５行を表示：")
print(iris_df.head())

###2. データのクリーニングと検証
print("\n欠損値の確認：")
print(iris_df.isnull().sum())
print("\n各列のデータ型：")
print(iris_df.dtypes)

###3. 基本的な分析と基本統計量
status_df = iris_df.describe().transpose()
status_df.to_csv('iris_statistics.csv')

print("\n基本統計量のData FrameをCSV形式で出力しました。")
print(status_df)

###4. 特徴量エンジニアリング
iris_df['sepal_area'] = iris_df['sepal length (cm)'] * iris_df['sepal width (cm)']
iris_df['petal_area'] = iris_df['petal length (cm)'] * iris_df['petal width (cm)']
new_feature_stats = iris_df[['sepal_area', 'petal_area']].describe()

print("\n追加した新しい特徴量の基本統計量:")
print(new_feature_stats)

###5. データのフィルタリング
filtered_data = iris_df[iris_df['petal length (cm)'] >= 2.0]
print("\n花弁の長さが2.0以上のデータ：")
print(filtered_data.head())

###6. データのエクスポート
iris_df.to_csv('iris_processed.csv', index=False)

print("\n処理したアイリスのデータをCSV形式で出力しました。")









'''
# ここにコードを書いてください

### 1. データの読み込みと概要


# 必要なライブラリをインポートする
import pandas as pd
from sklearn import datasets

# アイリスのデータセットを読み込み、DataFrameに変換する
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# 品種の列を追加し、0～2の番号を記入する (各番号が異なる品種を表す)
iris_df['species'] = iris.target

# 最初の5行を表示する
print("最初の5行を表示:")
print(iris_df.head())


### 2. データのクリーニングと検証


# 欠損値またはnull値の存在を確認する
print("\n欠損値の確認:")
print(iris_df.isnull().sum())

# 各列のデータ型を確認する
print("\n各列のデータ型:")
print(iris_df.dtypes)


### 3. 基本的な分析と基本統計量

# 数値型の各特徴量について、基本統計量を計算する
stats_df = iris_df.describe().transpose()

# DataFrameを新規作成し、計算した統計情報を格納する
stats_df.to_csv('iris_statistics.csv')

print("\n基本統計量のDataFrameをCSV形式で出力しました。")
print(stats_df)


### 4. 特徴量エンジニアリング


# 新しい列 'sepal_area' (ガクの面積) を追加する
iris_df['sepal_area'] = iris_df['sepal length (cm)'] * iris_df['sepal width (cm)']

# 新しい列 'petal_area' (花弁の面積) を追加する
iris_df['petal_area'] = iris_df['petal length (cm)'] * iris_df['petal width (cm)']

# 新しい特徴量の基本統計量を算出する
new_features_stats = iris_df[['sepal_area', 'petal_area']].describe()

print("\n追加した新しい特徴量の基本統計量:")
print(new_features_stats)


### 5. データのフィルタリング

# 花弁の長さが2.0未満のデータをフィルタリングする
filtered_data = iris_df[iris_df['petal length (cm)'] >= 2.0]

print("\n花弁の長さが2.0以上のデータ:")
print(filtered_data.head())


### 6. データのエクスポート

# DataFrameをCSV形式で保存する
iris_df.to_csv('iris_processed.csv', index=False)

print("\n処理したアイリスのデータをCSV形式で出力しました。")

'''