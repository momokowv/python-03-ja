# SQLとPython＋Chinookデータベース

import sqlite3

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()


# アーティストの数
def number_of_artists(db):
    query = "SELECT COUNT(*) FROM artists"  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchone()[0]
    return results

# アーティストのリスト
def list_of_artists(db):
    query = """
    SELECT name FROM artists
    ORDER BY name
    """  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    artists_list = [row[0] for row in results]
    return artists_list

# 「愛」をテーマにしたアルバムのリスト
def albums_about_love(db):
    query = """
    SELECT title FROM albums
    WHERE title LIKE "%love%"
    ORDER BY title
    """ # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    albums_list = [row[0] for row in results]
    return albums_list

# 指定された再生時間よりも長い楽曲数
def tracks_longer_than(db, duration):
    query = """
    SELECT COUNT(*) FROM tracks
    WHERE milliseconds > 180
    """ # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchone()[0]
    return results

# 最も楽曲数が多いジャンルのリスト
def genres_with_most_tracks(db):
    query = """
    SELECT genres.name, COUNT(tracks.trackid) AS track_count
    FROM tracks
    JOIN genres ON tracks.genreid = genres.genreid
    ORDER BY track_count DESC, genres.name
    """ # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    genre_list = [(row[0], row[1])for row in results]
    return genre_list

print("アーティストの数:",number_of_artists(db))
print("アーティストのリスト:")
print(list_of_artists(db))
print("「愛」をテーマにしたアルバムのリスト:")
print(albums_about_love(db))
duration = 180
print(f"{duration}分より長い楽曲の数:", tracks_longer_than(db, duration))
print("最も楽曲数が多いジャンルのリスト:")
print(genres_with_most_tracks(db))

# スクリプトの最後で必ずデータベース接続を閉じる
conn.close()
