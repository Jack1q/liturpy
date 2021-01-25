from flask import Flask, render_template, jsonify
from liturpy import LiturgicalCalendar

app = Flask(__name__, template_folder='templates')



@app.route('/home')
def main():
    return render_template('page.html')

@app.route('/')
def landing_page():
    return main()

# @app.route('/')
# def main():
#     return jsonify(LiturgicalCalendar().get_main_calendar())

@app.route('/calendar')
def calendar_page():
    return render_template('calendar.html')

@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/<int:year>')
def get_year_calendar(year):
    return jsonify(LiturgicalCalendar(year).get_main_calendar())

@app.route('/<int:year>/<string:month>')
def get_month_calendar(year, month):
    return jsonify(LiturgicalCalendar(year).get_main_calendar()[month])

if __name__ == '__main__':
    app.run(debug=True)