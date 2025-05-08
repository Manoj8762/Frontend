from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Connection
def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ebook_store"
    )

# Serve Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Serve Cart Page
@app.route('/cart')
def cart_page():
    return render_template('cart.html')

# Fetch all books
@app.route('/books', methods=['GET'])
def get_books():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return jsonify(books)

# Add to Cart (Max 15 books)
@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.json
    user_id = data.get("user_id")
    book_id = data.get("book_id")

    conn = db_connection()
    cursor = conn.cursor()

    # Check if cart has space (Max 15 books)
    cursor.execute("SELECT COUNT(*) FROM cart WHERE user_id = %s", (user_id,))
    cart_count = cursor.fetchone()[0]

    if cart_count >= 15:
        conn.close()
        return jsonify({"message": "Cart is full! Maximum 15 books allowed."}), 400

    cursor.execute("INSERT INTO cart (user_id, book_id) VALUES (%s, %s)", (user_id, book_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Book added to cart successfully!"}), 200

# View Cart
@app.route('/cart/view', methods=['GET'])
def view_cart():
    user_id = request.args.get("user_id")

    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT books.id, books.title, books.author 
        FROM cart 
        JOIN books ON cart.book_id = books.id 
        WHERE cart.user_id = %s
    """, (user_id,))

    cart_books = cursor.fetchall()
    conn.close()
    return jsonify(cart_books)

# Remove Book from Cart
@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.json
    user_id = data.get("user_id")
    book_id = data.get("book_id")

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cart WHERE user_id = %s AND book_id = %s LIMIT 1", (user_id, book_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Book removed from cart successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)



"""
from flask import Flask, request, jsonify
import mysql.connector


app = Flask(__name__)


def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ebook_store"
    )
    
@app.route('/books', methods=['GET'])
def get_books():
    conn = db_connection()  # Establish database connection
    cursor = conn.cursor(dictionary=True)  # Create a cursor for executing SQL queries
    cursor.execute("SELECT * FROM books")  # Fetch all books from the 'books' table
    books = cursor.fetchall()  # Retrieve all query results as a list of dictionaries
    conn.close()  # Close the database connection
    return jsonify(books)  # Convert the list to JSON and return it as a response


@app.route('/buy', methods=['POST'])
def buy_book():
    data = request.json  # Get JSON data from the request
    book_id = data.get("book_id")  # Extract book ID from the request body

    conn = db_connection()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor for executing SQL queries
    
    # Check stock availability
    cursor.execute("SELECT stock FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()  # Fetch the first matching record
    
    if book and book[0] > 0:  # If the book exists and stock is available
        cursor.execute("UPDATE books SET stock = stock - 1 WHERE id = %s", (book_id,))  # Decrement stock by 1
        conn.commit()  # Save the changes
        conn.close()  # Close connection
        return jsonify({"message": "Book purchased successfully!"}), 200  # Return success response
    else:
        conn.close()  # Close connection
        return jsonify({"message": "Book out of stock!"}), 400  # Return failure response
    
@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    user_id = data.get("user_id")
    book_id = data.get("book_id")
    
    conn = db_connection()
    cursor = conn.cursor()
    
    # Check how many books are in the cart
    cursor.execute("SELECT COUNT(*) FROM cart WHERE user_id = %s", (user_id,))
    cart_count = cursor.fetchone()[0]
    
    if cart_count >= 15:
        conn.close()
        return jsonify({"message": "Cart limit reached (15 books max)"}), 400
    
    # Add book to cart
    cursor.execute("INSERT INTO cart (user_id, book_id) VALUES (%s, %s)", (user_id, book_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Book added to cart successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
"""

"""from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to MySQL Database
def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ebook_store"
    )

# Fetch all books
@app.route('/books', methods=['GET'])
def get_books():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return jsonify(books)

# Buy a book (decrement stock)
@app.route('/buy', methods=['POST'])
def buy_book():
    data = request.json
    book_id = data.get("book_id")

    conn = db_connection()
    cursor = conn.cursor()
    
    # Check stock availability
    cursor.execute("SELECT stock FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    
    if book and book[0] > 0:
        cursor.execute("UPDATE books SET stock = stock - 1 WHERE id = %s", (book_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Book purchased successfully!"}), 200
    else:
        conn.close()
        return jsonify({"message": "Book out of stock!"}), 400

if __name__ == '__main__':
    app.run(debug=True)
"""