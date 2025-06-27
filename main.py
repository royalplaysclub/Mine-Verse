from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/deposit')
def deposit():
    return render_template('deposit.html')

@app.route('/withdraw')
def withdraw():
    return render_template('withdraw.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/submit', methods=['POST'])
def submit():
    action = request.form.get('action')
    amount = request.form.get('amount')
    return f"You selected {action} of ${amount}"

# ✅ THIS LINE is needed so Render detects the port
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # 10000 is a default fallback
    app.run(host='0.0.0.0', port=port)
