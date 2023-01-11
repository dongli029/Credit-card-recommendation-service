from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@ip/your database'
db = SQLAlchemy(app)

@app.route('/')
def index():
    sql = """
    CREATE TABLE aneka (
    id serial NOT NULL,
    uid character varying(50) NOT NULL,
    PRIMARY KEY (id));

    CREATE TABLE card_table (
    id serial NOT NULL,
    bid character varying(50) NOT NULL,
    card_name character varying(50) NOT NULL,
    PRIMARY KEY (id))
    """
    db.engine.execute(sql)
    return "資料表建立成功！"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)