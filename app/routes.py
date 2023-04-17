from flask import render_template, request, redirect, session
from app import app
from app.utils import get_lat_long_for_zip_code, calculate_prayer_times_using_asr, save_prayer_times_to_mysql
from datetime import datetime, timedelta
import requests

@app.route('/')
def index():
    return redirect('/zipcode')

@app.route('/zipcode', methods=['GET', 'POST'])
def zipcode():
    if request.method == 'POST':
        session['zip_code'] = request.form['zip_code']
        return redirect('/prayer_times')
    else:
        return render_template('zipcode_form.html')

@app.route('/prayer_times')
def prayer_times():
    zip_code = session.get('zip_code')
    if zip_code is None:
        return redirect('/zipcode')

    lat_long = get_lat_long_for_zip_code(zip_code, app.config['API_KEY'])
    if lat_long is None:
        return render_template('error.html', message='Unable to find latitude and longitude for zip code')

    prayer_times = []
    date = datetime.now().date()
    for i in range(7):
        prayer_times.append((calculate_prayer_times_using_asr(lat_long[0], lat_long[1], date), date.strftime('%m/%d/%Y')))
        date += timedelta(days=1)

    save_prayer_times_to_mysql(zip_code, prayer_times)

    return render_template('prayer_times.html', prayer_times=prayer_times)
