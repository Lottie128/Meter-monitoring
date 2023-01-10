
First, set up the Flask application and create the SQLite database.

import flask
from flask import Flask, request, jsonify
import sqlite3

# Create a Flask app
app = Flask(__name__)

# Connect to the database
conn = sqlite3.connect('meters_db.sqlite')

# Create meters table
cur = conn.cursor()
cur.execute('''CREATE TABLE meters
    (id INTEGER PRIMARY KEY, label TEXT UNIQUE)
''')

# Create meter_data table
cur.execute('''CREATE TABLE meter_data
    (id INTEGER PRIMARY KEY, meter_id INTEGER, timestamp DATETIME, value INTEGER)
''')

# Commit changes and close connection
conn.commit()
conn.close()

# Add fake meter data to the database
def add_meter_data(meter_id, timestamp, value):
    conn = sqlite3.connect('meters_db.sqlite')
    cur = conn.cursor()

    cur.execute('''INSERT INTO meter_data (meter_id, timestamp, value)
                    VALUES (?,?,?)''', (meter_id, timestamp, value))

    conn.commit()
    conn.close()

# Create a list of fake meter data
meter_data = [{'meter_id': 1, 'timestamp': '2019-10-01 00:00:00', 'value': 100},
              {'meter_id': 1, 'timestamp': '2019-10-02 00:00:00', 'value': 101},
              {'meter_id': 1, 'timestamp': '2019-10-03 00:00:00', 'value': 102},
              {'meter_id': 2, 'timestamp': '2019-10-01 00:00:00', 'value': 150},
              {'meter_id': 2, 'timestamp': '2019-10-02 00:00:00', 'value': 151},
              {'meter_id': 2, 'timestamp': '2019-10-03 00:00:00', 'value': 152}]

# Add the fake meter data to the database
for data in meter_data:
    add_meter_data(data['meter_id'], data['timestamp'], data['value'])

# Define the endpoints
@app.route('/meters/', methods=['GET'])
def get_meters():
    # Get a list of the unique meters in the DB
    conn = sqlite3.connect('meters_db.sqlite')
    cur = conn.cursor()

    cur.execute('''SELECT DISTINCT meter_id FROM meter_data''')
    meters = cur.fetchall()

    conn.close()

    # Return the response as JSON
    return jsonify(meters)

@app.route('/meters/<int:meter_id>', methods=['GET'])
def get_meter_data(meter_id):
    # Get the meter data for the specified meter
    conn = sqlite3.connect('meters_db.sqlite')
    cur = conn.cursor()

    cur.execute('''SELECT * FROM meter_data WHERE meter_id = ? ORDER BY timestamp''', (meter_id,))
    data = cur.fetchall()

    conn.close()

    # Return the response as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run()