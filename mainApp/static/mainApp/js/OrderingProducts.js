let filterItems = document.querySelectorAll(".products__control__item")

Array.from(filterItems).forEach(
    (item) => {
        item.addEventListener('click', (e) => {
            e.preventDefault()
            let filter = item.dataset.filter
            let productList = document.querySelector(".products__list")
            var allGoods = document.querySelectorAll(".products__item")
            var allGoodsArray = Array.from(allGoods);
            let sorted = []


            if (filter === 'by-views') {
                sorted = allGoodsArray.sort((a, b) => +a.dataset.views - +b.dataset.views)
                productList.classList.toggle('reverse-order')
                if (productList.className.indexOf('reverse-order') !== -1) {
                    item.innerHTML = "Least popular"
                } else {
                    sorted = sorted.reverse()
                    item.innerHTML = "Most popular"
                }
                sorted.forEach(e => productList.appendChild(e));

            } else if (filter === 'by-date') {
                let sorted = allGoodsArray.sort((a, b) => +a.dataset.created - +b.dataset.created);
                productList.classList.toggle('reverse-order')

                if (productList.className.indexOf('reverse-order') !== -1) {
                    item.innerHTML = "Oldest products"
                } else {
                    item.innerHTML = "Newest popular"
                }

                sorted.reverse().forEach(e => productList.appendChild(e));
            }


        })
    }
)
