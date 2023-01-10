from flask import Flask, jsonify, redirect, render_template
import sqlite3

app = Flask(__name__)

# connect to the sqlite3 db
conn = sqlite3.connect('meter_data.db', check_same_thread=False)
c = conn.cursor()

# create the tables if they don't already exist
# c.execute('''CREATE TABLE IF NOT EXISTS meters
#              (id INTEGER PRIMARY KEY, label TEXT)''')

# c.execute('''CREATE TABLE IF NOT EXISTS meter_data
#              (id INTEGER PRIMARY KEY, meter_id INTEGER, timestamp DATETIME, value INTEGER,
#               FOREIGN KEY (meter_id) REFERENCES meters(id))''')

# # add fake meter data to the db
# c.execute("INSERT INTO meters (label) VALUES ('Meter X')")
# c.execute("INSERT INTO meters (label) VALUES ('Meter Y')")

# c.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (1, '2020-05-01 00:00:00', 10)")
# c.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (1, '2020-05-02 00:00:00', 20)")
# c.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (1, '2020-05-03 00:00:00', 30)")
# c.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (2, '2020-05-01 00:00:00', 40)")
# c.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (2, '2020-05-02 00:00:00', 50)")
# c.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (2, '2020-05-03 00:00:00', 60)")

# conn.commit()

@app.route('/')
def index():
    return redirect("/meters/")

# endpoint to get a list of unique meters
@app.route('/meters/')
def get_meters():
    c.execute('SELECT DISTINCT label FROM meters')
    data = c.fetchall()
    meters = []
    # create a list of objects with the meter id and label
    for meter in data:
        meters.append({'id': data.index(meter)+1, 'label': meter[0]})

    # for meter in data:
    #     meters.append(meter[0])
    print(meters)
    return render_template("home.html", meters = meters)


# endpoint to get the data associated with a particular meter
@app.route('/meters/<int:meter_id>')
def get_meter_data(meter_id):
    c.execute('SELECT * FROM meter_data WHERE meter_id=? ORDER BY timestamp', (meter_id,))
    data = c.fetchall()
    meter_data = []
    for row in data:
        meter_data.append({'timestamp': row[2], 'value': row[3]})
    
    print(data)
    return jsonify(meter_data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)