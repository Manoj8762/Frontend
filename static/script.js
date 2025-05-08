document.addEventListener("DOMContentLoaded", function () {
    if (window.location.pathname === "/") {
        fetchBooks();
    } else if (window.location.pathname === "/cart") {
        fetchCart();
    }
});

function fetchBooks() {
    fetch("/books")
        .then(response => response.json())
        .then(data => {
            let bookList = document.getElementById("book-list");
            bookList.innerHTML = "";
            data.forEach(book => {
                bookList.innerHTML += `
                    <div class="book">
                        <h3>${book.title}</h3>
                        <p>Author: ${book.author}</p>
                        <button onclick="addToCart(${book.id})">Add to Cart</button>
                    </div>
                `;
            });
        });
}

function fetchCart() {
    fetch("/cart/view?user_id=1")
        .then(response => response.json())
        .then(data => {
            let cartList = document.getElementById("cart-list");
            cartList.innerHTML = "";
            data.forEach(book => {
                cartList.innerHTML += `
                    <div class="book">
                        <h3>${book.title}</h3>
                        <p>Author: ${book.author}</p>
                        <button onclick="removeFromCart(${book.id})">Remove</button>
                    </div>
                `;
            });
        });
}

function addToCart(bookId) {
    fetch("/cart/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: 1, book_id: bookId })
    }).then(() => alert("Book added to cart!"));
}

function removeFromCart(bookId) {
    fetch("/cart/remove", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: 1, book_id: bookId })
    }).then(() => {
        alert("Book removed from cart!");
        fetchCart();
    });
}
