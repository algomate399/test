from flask import Flask, render_template
from database import NSE_SESSION  # Replace 'your_module' with the module where get_expiry function is defined

app = Flask(__name__)

@app.route('/')
def index():
    indices = "BANKNIFTY"  # Replace with the indices you want to fetch expiry dates for
    nse = NSE_SESSION()
    expiry_dates = nse.GetExpiry(indices)
    print(expiry_dates)
    return render_template('index.html', expiry_dates=expiry_dates)

# if __name__ == '__main__':
#     app.run(debug=True)
