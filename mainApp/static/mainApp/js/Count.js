let productsQty = document.querySelectorAll('.product-btn__qty');


Array.from(productsQty).forEach(
    function (button) {
        button.addEventListener('click', function (e) {
            let productQty = e.target;
            let goodId = productQty.dataset.id
            let count = document.querySelector(`#input${goodId}`);
            let countValue = Number(count.value);

            if (productQty.id === `product-btn__inc${goodId}`) {
                count.value = countValue + 1;
            } else if (productQty.id === `product-btn__dec${goodId}`) {
                count.value = countValue > 0 ? countValue - 1 : 0;
            }
        })
    });




