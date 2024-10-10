from flask import Flask, render_template, request
import psycopg2
app = Flask (__name__)
host = 'localhost'
database = 'ecommerce'
user = 'postgres'
password = 'divcan'
port = '5432'

def get_db_connection():
    conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=port)
    return conn

def get_data(first_name, last_name, email):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
                Insert into survey (first_name, last_name, email) values (%s, %s, %s) 
                ''', (first_name, last_name, email))
    conn.commit()
    cur.close()
    conn.close()
    return "Data inserted successfully"

@app.route('/')
def index():
    return render_template('index.html')  
  
@app.route('/users')
def user_view():
    return render_template('users.html')
@app.route("/submit", methods = ["POST"])
def submit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    get_data(first_name, last_name, email)
    return render_template('users.html')

if __name__ == '__main__':
    app.run(debug=True)

