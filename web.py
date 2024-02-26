from flask import Flask, render_template,send_file
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # Import urljoin function

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
    # Replace 'https://example.com' with the URL of the website you want to display
    url = 'http://cx2sa.com/nr/animsat.html'

    try:
        # Make a GET request to the website
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Update URLs for resources to use absolute paths
            for tag in soup.find_all(['link', 'script', 'img'], src=True):
                tag['src'] = urljoin(url, tag['src'])

            for tag in soup.find_all(['link', 'script'], href=True):
                tag['href'] = urljoin(url, tag['href'])

            # Render the template with the updated content
            return render_template('index.html')
        else:
            return f"Error: Unable to fetch content from {url}. Status code: {response.status_code}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/web2')
def index2():
    # Send the 'index.html' file from the same folder
    return send_file('animsat.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
