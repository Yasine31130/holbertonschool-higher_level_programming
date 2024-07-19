from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)

def read_csv(file_path):
    products = []
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        product = {
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        }
        products.append(product)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error_message = None
    
    if source == 'json':
        try:
            products = read_json('products.json')
        except FileNotFoundError:
            error_message = "JSON file not found."
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except FileNotFoundError:
            error_message = "CSV file not found."
    elif source == 'sql':
        try:
            products = read_sqlite('products.db')
        except sqlite3.Error as e:
            error_message = f"Database error: {e}"
    else:
        error_message = "Wrong source"

    if not error_message and product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if product['id'] == product_id]
            if not products:
                error_message = "Product not found"
        except ValueError:
            error_message = "Invalid id"

    return render_template('product_display.html', products=products, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

