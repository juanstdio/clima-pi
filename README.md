# Overview
This GitHub project provides a Flask web server that serves as a comprehensive dashboard for streaming two prominent TV channels in Argentina, namely C5N and CrónicaTV. Additionally, the dashboard integrates real-time meteorological data sourced from the Servicio Meteorológico Nacional (SMN) and 5 day forecast provided by meteoblue.com offering users a one-stop solution for staying updated on both news and weather conditions in Argentina.

# Features
- Meteorological Data: Graphics from http://cx2sa.com/nr/animsat.html ; they are being updated every 30 minutes. 
- Optimized for 1366x768 HD Monitors
- Web server only consumes 30 MB of RAM!


### REQUIRED:
- Stable Internet connection
- Python 3.11
- install required packages: Beautiful Soup  & flask
```
# pip install bs4 requests flask
```

# How to Use
Clone the repository to your local machine.
Install the required dependencies using the provided requirements.txt file.
Run the Flask web server using the provided script.
```
# python web.py
```
The web server will open both locally (localhost:5000) and to an assigned IP to the primary interfaces (all addresses).
Debug mode is activated!

# Contribution
Many Thanks to CX2SA AMATEUR RADIO SERVICES (CX2SA.COM) for the satellite images!
Thanks to meteoblue.com for the widget
Contributions to enhance the project are welcome! Feel free to fork the repository, make improvements, and submit pull requests. Bug reports, feature requests, and feedback can be submitted through the GitHub issues page.
