// Start with second product
const counter = 0;

// Quantity of products to load
const quantity = 2;

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

    // Get products and add it to DOM
    fetch(`/sales_hits?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.products.forEach(add_product);
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
        load(destination)
        clear_slider('sales-products')
    }
}

// Clear slider
function clear_slider(element) {
    el = document.getElementById(element)
    el.style.opacity = 0;
    el.style.display = 'block';
    el.style.transition = `opacity 15ms`;

     setTimeout(() => {
    el.style.opacity = 1;},
     10);
    document.getElementById(element).innerHTML = ''
}
