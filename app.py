from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for expenses
expenses = []

@app.route('/')
def home():
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    # Get data from the form
    date = request.form['date']
    amount = request.form['amount']
    description = request.form['description']
    
    # Add to expenses list
    expenses.append({'date': date, 'amount': amount, 'description': description})
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
