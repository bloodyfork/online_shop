setTimeout(() => {



    var AddToCart = document.getElementsByClassName('cart-update')
    for( let i=0; i<AddToCart.length; i++){
        AddToCart[i].addEventListener('click', function () {

            var  ProductId = this.dataset.product
            var  action = this.dataset.action
            console.log('ProductId:', ProductId, 'action:', action)
            console.log("USER:", user)
        })
    }



}, 1000);

