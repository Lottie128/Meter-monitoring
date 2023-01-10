# Meter Monitoring App

This is a basic Flask application that connects to a local SQLite database and displays fake meter data in json format. The app has two endpoints:

- /meters/: displays a list of the unique meters in the DB. Each one is a clickable link that points to the meter's json page that displays all of its associated data.
- /meters/<meter_id>: displays a list sorted by timestamp of all the datapoint entries from the meter_data in json format for the specific meter_id passed into the URL as a parameter.

## Getting Started
1. Clone the repository by running `git clone https://github.com/lottie128/Meter-monitoring.git`
2. Install the required packages by running `pip install -r requirements.txt`
3. Run the application by running `python app.py`
4. Visit `http://localhost:5000/meters/` to see the list of the unique meters in the DB
5. Click on the meter link you want to see the datapoint entries of.
6. You can also access the data from the different endpoints with the use of a client like postman or in the browser by visiting `http://localhost:5000/meters/<meter_id>`

## Notes
- This app uses SQLite as the database, so the data is stored in a local file. If you want to use a different type of database, you would need to update the connection string in the app.py file.
- The data is hardcoded in the app.py file, but you can change the way the data is inserted in the database, for example by taking input from the user or reading a csv file.
- The templates are rendered using Jinja2, so the HTML and CSS files should be located in the templates folder in the main directory.
- The commented code is to generated the database tables and the mock meter lables and the mock meter data for clear demonstration of the meter monitoring data linked to its respective .json data.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Lottie128/Meter-monitoring/blob/4dc740672bebdd20a9863899aa441aaeeffe5349/LICENSE) file for details.

