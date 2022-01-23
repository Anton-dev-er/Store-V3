let goods = document.querySelectorAll('.product-btn');

Array.from(goods).forEach(
    function (button) {
        button.addEventListener('click', function (e) {
            let productBtn = e.target.parentElement;
            let goodId = productBtn.dataset.id

            if (goodId === undefined) {
                goodId = ''
            }

            if (productBtn.className === 'product-btn') {
                let increment = productBtn.querySelector(`#product-btn__inc${goodId}`);
                let decrement = productBtn.querySelector(`#product-btn__dec${goodId}`);
                let count = productBtn.querySelector(`#input${goodId}`);
                let countValue = Number(count.value);
                console.log(increment.onclick, decrement.onclick)

                increment.onclick = () => {
                    count.value = countValue + 1;
                }
                decrement.onclick = () => {
                    count.value = countValue > 0 ? countValue - 1 : 0;
                }
            }

        })
    });




