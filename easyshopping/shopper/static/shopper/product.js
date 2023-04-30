// Define comment counter
let comment_counter = 0

// Define comment quantity
let comment_quantity = 5


// Loading DOM elements
document.addEventListener('DOMContentLoaded', function() {
    load_pictures();
    load_comments();
    apply_onclick();
})

// If scrolled to bottom, render new comments
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load_comments();
    }
}


// Loading bunch of comments connected with product
function load_comments() {
    let start = comment_counter;
    let end = start + comment_quantity;
    comment_counter = end + 1;

    fetch(`/product_comments/${get_slug()}?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        console.log(data.products)
        data.products.forEach((item) => add_item(item, 'unique-comment', 'all-comments', 'div', 'comment'))
    })

}


// Loading bunch of pictures connected with product
function load_pictures() {
    let main_picture = '';

    fetch(`/product_images/${get_slug()}`)
    .then(response => response.json())
     .then(data => {
        let api_array = data.items;
        for (let i = 0; i < api_array.length; i++) {
            if (api_array[i]['imageproduct__default'] === true) {
                main_picture = api_array[i];
                api_array.splice(i, 1);
                break;
            }
        }
        add_item(main_picture.imageproduct__image, 'carousel-block', 'carousel-and-info-image', 'div', 'image')
        api_array.forEach((item) => add_item(item.imageproduct__image,  'small-images','images-links-to-other-goods-colors', 'li', 'image'));
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
function add_item(content, child_div_class_name, parent_id_name, element_tag, type) {
    // Creating new div
    const item = document.createElement(element_tag);
    item.className = child_div_class_name;

    if (type === 'image') {
        item.innerHTML = `<img src='${img_src()}/media/${content}'>`;
    } else {
        item.innerHTML = `<p>${content.comment__content}</p><br><p>${content.comment__author_id__username}</p>`
    }
    document.getElementById(parent_id_name).append(item);
    if (element_tag === 'li') {
        item.addEventListener('click', () => click_image(item.innerHTML, item))
    }

}

// Generates right way for img src tag
function img_src() {
    const link = window.location.href;
    let res = link.split('/product/');
    let root_path = res[0];

    return root_path
}

// Adds event to image
function click_image(image_html, image) {
    let main_image = document.querySelector('.carousel-block');

    image.innerHTML = main_image.innerHTML;
    main_image.innerHTML = image_html;

}