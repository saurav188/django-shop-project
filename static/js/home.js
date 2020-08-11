/*$(document).ready(function(){
    i=1
    $('.dot').on('click',function(){ 
        m=$(this).attr("data");   
        $('.dot').removeClass('dark');
        $('.slides').addClass('hide');
        $('#img'+m).removeClass('hide');
        $(this).addClass('dark');
        i=+m
    })
    slidecontainer=$('.slide-container')
    var visibleslide=$('#img1')
    var darkdot=$('#dot1')
    function changeslide(){
        $('.dot').removeClass('dark');
        $('.slides').addClass('hide');
        darkdot.addClass('dark');
        visibleslide.removeClass('hide');
        if(i<=(slidecontainer.length+1)){
            i=i+1
        }else{
            i=1
        }
        visibleslide=$('#img'+i)
        darkdot=$('#dot'+i)

        setTimeout(changeslide,5000);
        
    }
    changeslide();
})*/
var i=1;
const dots=document.querySelectorAll('.dot');
const slides=document.querySelectorAll('.slides');
slides.forEach(function(each){
    if(each.getAttribute('data-no')===1){
        each.classList.add('show');
    }
});
dots.forEach(function(each){
    each.addEventListener('click',function(e){
        dots.forEach(function(each){
            each.classList.remove('dark');
        });
        slides.forEach(function(each){
            each.classList.add('hide');
        });
        m=parseInt(this.getAttribute('data-no'));
        document.querySelector('#img'+m).classList.remove('hide');
        this.classList.add('dark');
        i=m;
    })
})
const slidecontainer=document.querySelectorAll('.slide-container');
var visibleslide=document.querySelector('#img1');
var dark_dot=document.querySelector('#dot1');
function changeslide(){ 
        document.querySelectorAll('.dot').forEach(function(each){
            each.classList.remove('dark');
        });
        document.querySelectorAll('.slides').forEach(function(each){
            each.classList.add('hide');
        });

        dark_dot.classList.add('dark');
        visibleslide.classList.remove('hide');
        if(i<slides.length){
            i+=1
        }else{
            i=1
        }
        visibleslide=document.querySelector('#img'+i)
        dark_dot=document.querySelector('#dot'+i)

        setTimeout(changeslide,5000);
        
}
changeslide();

