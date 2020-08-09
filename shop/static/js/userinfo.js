//price and quantity and totals
var cart_item=document.querySelectorAll('.cart-item');
cart_item=Array.from(cart_item);
var pending_item=Array.from(document.querySelectorAll('.pending-item'));
var delivered_item=Array.from(document.querySelectorAll('.delivered-item'));
var i=1;
var tot_price=0;
var tot_qtn=0;
var stop=false;
function quantitychk(){
    if(cart_item.length>0){
        i=1;
        tot_price=0;
        tot_qtn=0;
        for(i=0;i<cart_item.length;i++){
            var qtn_item=cart_item[i].children[3].children[1].value;
            tot_qtn+=(+qtn_item);
            var price=cart_item[i].children[2].textContent;
            cart_item[i].children[4].textContent=price*qtn_item;
            full_price=cart_item[i].children[4].textContent;
            tot_price+=(+full_price);
        };
        document.querySelector('.cart-total').children[3].textContent='Total item:'+tot_qtn;
        document.querySelector('.cart-total').children[4].textContent='Total price:'+tot_price;
    }
    if(pending_item.length>0){
        i=1;
        tot_price=0;
        tot_qtn=0;
        for(i=0;i<pending_item.length;i++){
            var qtn_item=pending_item[i].children[3].textContent;
            tot_qtn+=(+qtn_item);
            var price=pending_item[i].children[2].textContent;
            pending_item[i].children[4].textContent=price*qtn_item;
            full_price=pending_item[i].children[4].textContent;
            tot_price+=(+full_price);
        };
        document.querySelector('.pending-total').children[3].textContent='Total item:'+tot_qtn;
        document.querySelector('.pending-total').children[4].textContent='Total price:'+tot_price;
    }
    if(delivered_item.length>0){
        i=1;
        tot_price=0;
        tot_qtn=0;
        for(i=0;i<delivered_item.length;i++){
            var qtn_item=delivered_item[i].children[3].textContent;
            tot_qtn+=(+qtn_item);
            var price=delivered_item[i].children[2].textContent;
            delivered_item[i].children[4].textContent=price*qtn_item;
            full_price=delivered_item[i].children[4].textContent;
            tot_price+=(+full_price);
        };
        document.querySelector('.delivered-total').children[3].textContent='Total item:'+tot_qtn;
        document.querySelector('.delivered-total').children[4].textContent='Total price:'+tot_price;
    }
    if(stop==true){
        return;
    };
    setTimeout(quantitychk,2000);
};
quantitychk();

//item serial no
var serial_no=document.querySelectorAll('.cart-serial-no');
var pend_serial_no=document.querySelectorAll('.pending-serial-no');
var delivered_serial_no=document.querySelectorAll('.delivered-serial-no');
for(i=0;i<serial_no.length;i++){
    serial_no[i].innerHTML=(i+1);
};
for(i=0;i<pend_serial_no.length;i++){
    pend_serial_no[i].innerHTML=(i+1);
};
for(i=0;i<delivered_serial_no.length;i++){
    delivered_serial_no[i].innerHTML=(i+1);
};

//delete btn
var delete_btn=document.querySelectorAll('.delete-button');
var dont_delete_btn=document.querySelectorAll('.dont-delete')

delete_btn.forEach(function(each){
    each.addEventListener('click',function(event){   
        event.target.parentNode.children[1].classList.remove('hidden');
        event.target.parentNode.children[6].classList.remove('hidden');
        event.target.parentNode.children[1].classList.add('show-animation');
        event.target.parentNode.children[6].classList.add('show-animation');
        setTimeout(function(){
            event.target.parentNode.children[1].classList.rremove('show-animation');
            event.target.parentNode.children[6].classList.remove('show-animation');
        },400)
        event.target.classList.add('hidden');
    })
})
dont_delete_btn.forEach(function(each){
    each.addEventListener('click',function(event){   
        event.target.classList.add('hidden');
        event.target.parentNode.children[6].classList.add('hidden');
        event.target.parentNode.children[0].classList.remove('hidden');
    })
})