import numpy as np
from flask import Flask, render_template, request
import pickle
import json

from markupsafe import Markup
from datetime import datetime
def show_html(page_html):
    file_dat = 'datarec_china.dat'
    max_data = 100

    with open(file_dat, "rb") as file:
        data = pickle.load(file)

    detected = data['detected'][0:max_data]
    accidents = data['accidents'][0:max_data]
    #traffic_jam = data['traffic_jam']

    max_accidents = max(accidents) + 1

    light = data['light']
    moderate = data['moderate']
    heavy = data['heavy']
    traffic_jam = [heavy, moderate, light]

    car = data['car'][0:max_data]
    truck = data['truck'][0:max_data]
    bus = data['bus'][0:max_data]
    motorcycle = data['motorcycle'][0:max_data]
    max_detected = max([max(car), max(truck), max(bus), max(motorcycle)]) + 1

    spd_car = data['spd_car'][0:max_data]
    spd_truck = data['spd_truck'][0:max_data]
    spd_bus = data['spd_bus'][0:max_data]
    spd_motorcycle = data['spd_motorcycle'][0:max_data]
    max_spd = max([max(spd_car), max(spd_truck), max(spd_bus), max(spd_motorcycle)]) + 5


    label_detected = np.arange(1,len(detected)+1)
    label_detected = [str(num) for num in label_detected][0:max_data]

    label_accidents = np.arange(1, len(accidents) + 1)
    label_accidents = [str(num) for num in label_accidents][0:max_data]

    label_traffic_jam = ['Heavy', 'Moderate', 'Light']


    return render_template(page_html, detected=detected, accidents=accidents, traffic_jam=traffic_jam, max_accidents=max_accidents,
                           car=car, truck=truck, bus=bus, motorcycle=motorcycle, max_detected = max_detected,
                           spd_car=spd_car, spd_truck=spd_truck, spd_bus=spd_bus, spd_motorcycle=spd_motorcycle, max_spd = max_spd,
                           label_detected=label_detected, label_accidents=label_accidents, label_traffic_jam=label_traffic_jam)

app = Flask(__name__)

@app.route('/')
def main():
    page_html = 'detected.html'
    return show_html(page_html)

@app.route('/detected')
def detected_web():
    page_html = 'detected.html'
    return show_html(page_html)

@app.route('/accidents')
def accidents_web():
    page_html = 'accidents.html'
    return show_html(page_html)

@app.route('/traffic_jam')
def traffic_jam_web():
    page_html = 'traffic_jam.html'
    return show_html(page_html)

@app.route('/speed')
def speed_web():
    page_html = 'speed.html'
    return show_html(page_html)




if __name__ == '__main__':
    app.run(port=9999)