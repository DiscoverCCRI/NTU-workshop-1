# Reference: https://pypi.org/project/RPi.bme280/

import bme280
import smbus2
from datetime import datetime

port = 1
address = 0x77
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

bme280_data = bme280.sample(bus, address, calibration_params)

id = bme280_data.id
timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
humidity = bme280_data.humidity
pressure = bme280_data.pressure
ambient_temperature = bme280_data.temperature

print("Chip ID: " + str(id))
print("Timestamp: " + str(timestamp))
print("Humidity: %.2f" % humidity + "% rH")
print("Atmospheric Pressure: %.2f hPa" % pressure)
print("Temperature: %.2f °C" % ambient_temperature)
