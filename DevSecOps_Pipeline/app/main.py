from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/search") # Inform Flask to trigger the search function when someone visits the /search URL (e.g., http://localhost:5000/search).
def search():
    # Intentional SQL Injection vulnerability for the DAST to find (Dynamic Analysis).
    user_input = request.args.get('q') # Capture the value of the query parameter q from the URL. If the URL is /search?q=John, then user_input becomes "John"
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor() # Creates a cursor object, which is used to execute SQL commands and fetch results.
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    return {"status": "searched"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)