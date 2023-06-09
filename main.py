from flask import Flask, render_template, request
from details import endpoint
import mysql.connector
import os
import logging


app = Flask(__name__)
# Create a logger
logger = logging.getLogger(__name__)

# Set the log level (optional)
logger.setLevel(logging.DEBUG)

# Create a file handler
file_handler = logging.FileHandler('app.log')

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter on the handler
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)

# Configure MySQL connection
db = mysql.connector.connect(
    #host = "comeon.cucrqjiimp6l.us-east-2.rds.amazonaws.com",
    host=endpoint[:-5],
    user='admin',
    password='Test!098',
    #database='please'
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS please;")
cursor.execute("CREATE TABLE IF NOT EXISTS `please`.`content` (`ID` INT NOT NULL AUTO_INCREMENT,`Author` VARCHAR(45) NOT NULL,`Content` VARCHAR(45) NOT NULL,`Tweet` INT NOT NULL,`Timestamp` VARCHAR(45) NOT NULL,`Comment_Id` INT NOT NULL,PRIMARY KEY (`ID`));")



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment_text = request.form['comment_text']
        name_text = request.form['name_text']
        tweet = request.form['tweet']
        comment_id = request.form['comment_id']
        

        insert_query = '''
            INSERT INTO please.content (Author, content, tweet, timestamp, comment_id) 
            VALUES (%s, %s, %s, CURRENT_TIMESTAMP(), %s)

        '''
        cursor.execute(insert_query, (name_text, comment_text,tweet,comment_id))
        db.commit()

    select_query = '''
        SELECT ID, Author, content, Tweet,timestamp,comment_id from please.content
    '''
    cursor.execute(select_query)
    comments = cursor.fetchall()
    return render_template('home.html', comments=comments)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
