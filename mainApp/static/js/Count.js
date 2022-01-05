let price = document.getElementsByClassName("basket__proucts__item__bottom__price")[0];

let increment = document.getElementsByClassName("btn__count__inc")[0];
let decrement = document.getElementsByClassName("btn__count__dec")[0];
let count = document.getElementsByClassName("btn__count__display")[0];


let countValue = count.innerHTML;
const priceValue = price.innerHTML


price.innerHTML = +priceValue * +countValue

increment.onclick = function () {
    countValue++;
    count.innerHTML = countValue;

    price.innerHTML = +countValue * +priceValue;
};

decrement.onclick = function () {
    if (countValue > 0) {
        countValue--;
        count.innerHTML = countValue;

        price.innerHTML = +countValue * +priceValue
    }
}

