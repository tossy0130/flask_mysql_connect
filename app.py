from flask import Flask, render_template, request, url_for, redirect
import mysql.connector
import os

app = Flask(__name__)

# === DB 接続情報

"""

テスト用 DB & テーブル

CREATE DATABASE sample_db;
USE sample_db;

CREATE TABLE users (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(50) NOT NULL,
email_address VARCHAR(100) NOT NULL,
PRIMARY KEY (id)
);

use sample_db;
insert into users (name, email_address) values
('John Smith', 'john@example.com'),
('Jane Doe', 'jane@example.com'),
('Bob Johnson', 'bob@example.com'),
('Alice Lee', 'alice@example.com'),
('Mike Davis', 'mike@example.com');

"""


def conn_db():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        port='33306',
        # db='flask_db_01'
        db='sample_db'
    )

    return conn


@app.route('/select', methods=['GET'])
# ========= Mysql SELECT
def select():

    # SQL 文
    sql = 'SELECT * FROM users'

    try:
        conn = conn_db()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
    except(mysql.connector.errors.ProgrammingError) as e:
        print('エラー')
        print(e)

    return render_template('select.html', rows=rows)


@app.route('/', methods=['GET', 'POST'])
# ========= Mysql インサート処理
def up():
    if request.method == 'POST':
        # === form の値取得
        name = request.form['name']
        email_address = request.form['email_address']

        # === Mysql Insert 処理
        conn = conn_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email_address) VALUES (%s, %s)", (name, email_address))

        conn.commit()

        cursor.close()
        return redirect(url_for('select'))
    return render_template('up.html')


if __name__ == '__main__':
    app.run(debug=True)
