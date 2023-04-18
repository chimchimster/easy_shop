// Set slider counter
let slider_counter = 0;

// Set all products counter
let product_counter = 0;

// Quantity of slider products to load
const slider_quantity = 4;

// Quantity of all products to load
const products_quantity = 4;

// Right and left slides variables
const right = 1;
const left = -1;

// When DOM is loaded let's generate sales hits
document.addEventListener('DOMContentLoaded', function() {
    load_slider(0)

    slide('slide-right', right)
    slide('slide-left', left)

    load_products()

});


// If scrolled to bottom, render new products
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load_products();
    }
}

// Load all products
function load_products() {

    // Set start and end of all products to load
    const start = product_counter;
    const end = start + products_quantity;
    product_counter = end + 1;

    // Get all products and add it to DOM
    fetch(`/all_products?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.products.forEach((item) => add_product(item, 'product', 'all-products'));
    })
}


// Load slider's products
function load_slider(increment) {
    // Set start and end of slider products to load it
    const start = slider_counter + increment;
    const end = start + slider_quantity;
    slider_counter = end - 4;

    // Get slider products and add it to DOM
    fetch(`/sales_hits?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.products.forEach((item) => add_product(item, 'sales-product', 'sales-products'));
        // Hiding and showing buttons automatically
        length = data.length;
        show_hide_buttons(start, end, length)
    })
}

// Add unique product to DOM
function add_product(contents, child_div_class_name, parent_div_class_name) {

    // Creating element to store values
    const product = document.createElement('div')

    product.className = child_div_class_name

    product.innerHTML = `<div class="row"><div class="col-md-3"><div class="product"><div class="image"><img src="media/${contents.imageproduct__image}" alt =" "></div><div class="info"><h3><a href="product/${contents.slug}">${contents.productsdescription__product_name}</a></h3><ul class="raiting"><li><ion-icon name="star"></ion-icon></li><li><ion-icon name="star"></ion-icon></li><li><ion-icon name="star"></ion-icon></li><li><ion-icon name="star"></ion-icon></li><li><ion-icon name="star-half"></ion-icon></li></ul><div class="info-price"><span class="price">${contents.product_price}<small>P</small></span><button class="add-to-cart"><ion-icon name="cart-outline"></ion-icon></button></div></div></div></div></div>`

    // Add product to DOM
    document.getElementById(parent_div_class_name).append(product);
}

// Links function to specific button
function slide(button_id, destination) {
    document.getElementById(button_id).onclick = function() {
        clear_slider('sales-products')
        load_slider(destination)
    }
}

// Clear slider
function clear_slider(element) {
    el = document.getElementById(element)
    el.style.opacity = 1;
    el.style.display = 'block';
    el.style.transition = `opacity 4000ms`;

    document.getElementById(element).innerHTML = ''
}

// Shows or hides slider buttons
function show_hide_buttons(start, end, length) {
    const left = document.getElementById('slide-left');
    const right = document.getElementById('slide-right');

    if (start === 0) {
        left.style.display = 'none';
    } else {
        left.style.display = 'block';
        left.style.display = 'inline-block ';
    }

    if (end === length) {
        right.style.display = 'none';
    } else {
        right.style.display = 'block';
        right.style.display = 'inline-block';
    }
}


