let goods = document.querySelectorAll('.product-btn');

Array.from(goods).forEach(
    function (button) {
        button.addEventListener('click', function (e) {
            let productBtn = e.target.parentElement;
            let goodId = productBtn.dataset.id

            if (goodId === undefined){
                goodId = ''
            }

            if (productBtn.className === 'product-btn') {
                let increment = productBtn.querySelector(`#product-btn__inc${goodId}`);
                let decrement = productBtn.querySelector(`#product-btn__dec${goodId}`);
                let count = productBtn.querySelector(`#input${goodId}`);
                let countValue = Number(count.value);

                increment.onclick = function () {
                    count.value = countValue + 1;
                };


                decrement.onclick = function () {
                    if (countValue > 0) {
                        count.value = countValue - 1;
                    }
                };
            }
        })
    });



