from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
"""
# Configure MySQL connection
db = mysql.connector.connect(
    host='database-1.cucrqjiimp6l.us-east-2.rds.amazonaws.com',
    user='admin',
    password='Test!098',
    database='terraform'
)
cursor = db.cursor()"""



@app.route('/', methods=['GET'])
def index():
    return "Hello world! localhost"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)



"""from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Test@123',
    database='terraform'
)
cursor = db.cursor()



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment_text = request.form['comment_text']
        name_text = request.form['name_text']
        tweet = request.form['tweet']
        comment_id = request.form['comment_id']
        

        insert_query = '''
            INSERT INTO terraform.content (Author, content, tweet, timestamp, comment_id) 
            VALUES (%s, %s, %s, CURRENT_TIMESTAMP(), %s)

        '''
        cursor.execute(insert_query, (name_text, comment_text,tweet,comment_id))
        db.commit()

    select_query = '''
        SELECT ID, Author, content, Tweet,timestamp,comment_id from terraform.content
    '''
    cursor.execute(select_query)
    comments = cursor.fetchall()
    return render_template('home.html', comments=comments)


if __name__ == '__main__':
    app.run()"""
