
// Loading DOM elements
document.addEventListener('DOMContentLoaded', function() {
    load_pictures();
    apply_onclick();
})

// Loading bunch of pictures connected with product
function load_pictures() {
    let main_picture = '';

    fetch(`/product_images/${get_slug()}`)
    .then(response => response.json())
     .then(data => {
        let api_array = data.images;
        for (let i = 0; i < api_array.length; i++) {
            if (api_array[i]['imageproduct__default'] === true) {
                main_picture = api_array[i];
                api_array.splice(i, 1);
                break;
            }
        }
        add_image(main_picture, 'carousel-block', 'carousel-and-info', 'div')
        api_array.forEach((item) => add_image(item, 'small-images','images-links-to-other-goods-colors', 'li'));
     });

}

// Retrieving slug field from URL link
function get_slug() {
    let link = window.location.href;
    let link_array = link.split('/');

    slug = link_array.slice(-1).join('');

    return slug
}

// Adding image to DOM
function add_image(content, child_div_class_name, parent_id_name, element_tag) {
    // Creating new div
    const image = document.createElement(element_tag);
    image.className = child_div_class_name;

    image.addEventListener('click', click_image)
    image.innerHTML = `<img src='${img_src()}/media/${content.imageproduct__image}'>`;
    document.getElementById(parent_id_name).append(image);

}

// Generates right way for img src tag
function img_src() {
    const link = window.location.href;
    let res = link.split('/product/');
    let root_path = res[0];

    return root_path
}

// Adds event to image
function click_image() {
    let main_image = document.querySelector('.carousel-block')
    console.log(main_image)

}