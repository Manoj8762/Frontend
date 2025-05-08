async function fetchBooks() {
    let response = await fetch('http://127.0.0.1:5000/books');
    let books = await response.json();
    const bookContainer = document.getElementById("bookContainer");
    bookContainer.innerHTML = "";

    books.forEach(book => {
        let bookCard = document.createElement("div");
        bookCard.classList.add("book-card");
        bookCard.innerHTML = `
            <img class="book-cover" src="${book.book_cover}" alt="Book Cover">
            <h2>${book.title}</h2>
            <p class="author">By ${book.author}</p>
            <p class="price">$${book.price}</p>
            <p class="availability ${book.stock > 0 ? 'available' : 'not-available'}">
                ${book.stock > 0 ? '🟢 In Stock (' + book.stock + ')' : '🔴 Out of Stock'}
            </p>
            <button onclick="buyBook(${book.id})" ${book.stock === 0 ? 'disabled' : ''}>Buy</button>
        `;
        bookContainer.appendChild(bookCard);
    });
}

async function buyBook(bookId) {
    let response = await fetch('http://127.0.0.1:5000/buy', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ book_id: bookId })
    });

    let result = await response.json();
    alert(result.message);
    fetchBooks(); // Refresh book stock
}

fetchBooks();
