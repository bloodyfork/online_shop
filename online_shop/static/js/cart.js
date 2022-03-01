setTimeout(() => {



    var AddToCart = document.getElementsByClassName('cart-update')
    for( let i=0; i<AddToCart.length; i++){
        AddToCart[i].addEventListener('click', function () {

            let  ProductId = this.dataset.product
            let  action = this.dataset.action
            let  MyUrl = this.dataset.url
            let  token = this.dataset.c



            console.log('ProductId:', ProductId, 'action:', action, 'url:', MyUrl);
            console.log('USER:', user)

            if(user === 'AnonymousUser'){
                console.log("not logged in")
            }else {
                UpdateUserOrder(ProductId, action, MyUrl, token)
            }


        })
    }



}, 1000);

function UpdateUserOrder(ProductId, action, MyUrl, token){
    console.log('logged in')

    var url = MyUrl

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify({'ProductId': ProductId ,'action': action, })
    })
}

