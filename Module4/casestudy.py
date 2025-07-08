from flask import Flask, request, jsonify
app = Flask(__name__)

books = []

def find_book(book_id):
    return next((book for book in books if book['id'] == book_id), None)


@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    books.append({
        'id': data['id'],
        'book_name': data['book_name'],
        'author': data['author'],
        'publisher': data['publisher']
    })
    return jsonify({'message': 'Book added successfully'}), 201


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = find_book(book_id)
    if book:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = find_book(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    book['book_name'] = data.get('book_name', book['book_name'])
    book['author'] = data.get('author', book['author'])
    book['publisher'] = data.get('publisher', book['publisher'])

    return jsonify({'message': 'Book updated successfully'})


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_book(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    books.remove(book)
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)