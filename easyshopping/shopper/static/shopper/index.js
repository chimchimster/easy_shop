// Start with second product
let counter = 0;

// Quantity of products to load
const quantity = 4;

// Right and left slides variables
const right = 1;
const left = -1;

// When DOM is loaded let's generate sales hits
document.addEventListener('DOMContentLoaded', function() {
    load(0)

    slide('slide-right', right)
    slide('slide-left', left)

});

// Load all products
function load(increment) {
    // Set start and end of products to load it
    const start = counter + increment;
    const end = start + quantity;
    counter = end - 4;

    // Get products and add it to DOM
    fetch(`/sales_hits?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.products.forEach(add_product);
        // Hiding and showing buttons automatically
        length = data.length;
        show_hide_buttons(start, end, length)
    })
}

// Add unique product to DOM
function add_product(contents) {

    // Creating element to store values
    const product = document.createElement('div')

    product.className = 'sales-product'
    product.innerHTML = `<div><p>${contents.productsdescription__p_name}</p><br><img src="media/${contents.productsdescription__p_images}"></div>`

    // Add product to DOM
    document.getElementById('sales-products').append(product);
}

// Links function to specific button
function slide(button_id, destination) {
    document.getElementById(button_id).onclick = function() {
        clear_slider('sales-products')
        load(destination)
    }
}

// Clear slider
function clear_slider(element) {
    el = document.getElementById(element)
    el.style.opacity = 1;
    el.style.display = 'block';
    el.style.transition = `opacity 4000ms`;

    setTimeout(() => {
    el.style.opacity = 0.5;},
     4);
    document.getElementById(element).innerHTML = ''
    setTimeout(() => {
    el.style.opacity = 1;},
     4);
}

// Shows or hides slider buttons
function show_hide_buttons(start, end, length) {
    const left = document.getElementById('slide-left');
    const right = document.getElementById('slide-right');

    if (start === 0) {
        left.style.display = 'none';
    } else {
        left.style.display = 'block'
    }

    if (end === length) {
        right.style.display = 'none';
    } else {
        right.style.display = 'block';
    }
}