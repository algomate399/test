from flask import Flask, render_template
from database import get_expiry  # Replace 'your_module' with the module where get_expiry function is defined

app = Flask(__name__)

@app.route('/')
def index():
    indices = "NIFTY"  # Replace with the indices you want to fetch expiry dates for
    expiry_dates = get_expiry(indices)
    return render_template('index.html', expiry_dates=expiry_dates)

if __name__ == '__main__':
    app.run(debug=True)
