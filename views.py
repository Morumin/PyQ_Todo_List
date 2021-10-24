import sqlite3

from flask import Flask, render_template
app = Flask(__name__)

sqlite_path = 'db/todo.db'


def get_db_connection():
    connection = sqlite3.connect(sqlite_path)
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def index():
   connection = get_db_connection()
   cursor = connection.cursor()
   res = cursor.execute('SELECT * FROM todo')  
   return render_template('index.html', todo_list=res.fetchall())

    # return render_template('index.html', title='flask test') #変更

if __name__ == '__main__':
    app.run(debug=True)