
// Loading DOM elements
document.addEventListener('DOMContentLoaded', function() {
    load_pictures();

})

// Loading bunch of pictures connected with product
function load_pictures() {
    fetch(`/product_images/${get_slug()}`)
    .then(response => response.json())
     .then(data => {
        console.log(data.images)
        data.images.forEach((item) => add_image(item));
     });
}

// Retrieving slug field from URL link
function get_slug() {
    let link = window.location.href;
    let link_array = link.split('/');

    slug = link_array.slice(-1).join('')

    return slug
}

// Adding image to DOM
function add_image(content) {
    // Creating new div
    const image = document.createElement('div');
    image.className = 'carousel-block'
    console.log(`media/${content.imageproduct__image}`)

    image.innerHTML = `<img src='${img_src()}/media/${content.imageproduct__image}'>`

    document.getElementById('carousel-and-info').append(image)

}

// Generates right way for img src tag
function img_src() {
    const link = window.location.href;
    let res = link.split('/product/')
    let root_path = res[0]

    return root_path
}
