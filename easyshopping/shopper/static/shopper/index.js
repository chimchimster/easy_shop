// When DOM is loaded let's generate sales hits
document.addEventListener('DOMContentLoaded', load);


// Load all products
function load() {

    // Get products and add it to DOM
    fetch(`/sales_hits`)
    .then(response => response.json())
    .then(data => {
        data.forEach(add_product);
    })
}


// Add unique product to DOM
function add_product(contents) {

    // Creating element to store values
    const product = document.createElement('div')
    console.log(product)
    product.className = 'sales-product'
    product.innerHTML = `${contents.productsdescription__p_name}`

    x = document.querySelector('#sales-products')
    console.log(x)

    // Add product to DOM
    document.getElementById('sales-products').append(product);
}