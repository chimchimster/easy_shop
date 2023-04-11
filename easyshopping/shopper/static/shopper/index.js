// Start with second product
const counter = 2;

// Quantity of products to load
const quantity = 2;

// When DOM is loaded let's generate sales hits
document.addEventListener('DOMContentLoaded', load);

// Load all products
function load() {
    // Set start and end of products to load it
    const start = counter;
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