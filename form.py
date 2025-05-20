from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)
EXCEL_FILE = 'user_data.xlsx'

# Create Excel file if it doesn't exist
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=["Name", "Email", "Message"])
    df.to_excel(EXCEL_FILE, index=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        df = pd.read_excel(EXCEL_FILE)
        df.loc[len(df.index)] = [name, email, message]
        df.to_excel(EXCEL_FILE, index=False)

        return redirect('/success')

    return render_template('ui.html')  # ✅ Match your file name

@app.route('/success')
def success():
    return 'Data saved successfully!'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

