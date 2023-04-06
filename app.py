from flask import Flask
import mysql.connector

# === DB 接続情報

"""

テスト用テーブル

CREATE TABLE ce_table_01 (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    hinmoku VARCHAR(50),
    nedan INT,
    zaiko_num INT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


---------------------------

INSERT INTO ce_table_01
  (hinmoku, nedan, zaiko_num)
VALUES 
  ('hinmoku_01', 100, 30),
  ('hinmoku_02', 200, 20),
  ('hinmoku_03', 300, 10);

"""


def conn_db():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='flask_db_01'
    )

    return conn


# SQL 文
sql = 'SELECT * FROM ce_table_01'

try:
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
except(mysql.connector.errors.ProgrammingError) as e:
    print('エラー')
    print(e)

print('select開始')

for r_val in rows:
    print(r_val[0], r_val[1], r_val[2], r_val[3])
