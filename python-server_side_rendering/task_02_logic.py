from flask import Flask, render_template
import json

app = Flask(__name__)

def read(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
      return render_template('about.html')

@app.route('/contact')
def contact():
      return render_template('contact.html')

@app.route('/items')
def items():
      file_name = "items.json"
      items = read(file_name)
      return render_template('items.html', items=items)

if __name__ == '__main__':
       app.run(debug=True, port=5000)