/* JS Document */

/******************************

[Table of Contents]

1. Vars and Inits
2. Set Preloader
3. Init Navs
4. Init Dropdown Icon 
5. Init About Me Popup
6. Init Intro Carousel
7. Category Items
  7.1 Init Counter Loved
8. Gallery

******************************/

$(document).ready(()=>{
  
  /* 

	1. Vars and Inits

	*/

  let navLink = $(".nav-item .nav-link"),
      aboutMePopup = $(".about-me"),
      aboutMeLink  = $(".nav-link.about-me-link"),
      closeAboutMeBtn = $(".about-me .close-btn"),
      preloader    = $(".preloader");

      
  // About Me
  $(aboutMeLink).on("click",(e)=>{
    e.preventDefault();
    initAboutMePopup();
  });
  $(closeAboutMeBtn).on("click",initAboutMePopup)
  $(aboutMePopup).on("click",function(e){
    if(aboutMePopup.hasClass("open")){
      if(e.target == this){
        initAboutMePopup();
      }
    }
  });

  // Gallery
  let galleryBox = $(".gallery-pp");
  $(galleryBox).on("click",function(e){
    if($(galleryBox).hasClass("open")){
      if(e.target == this){
        $(galleryBox).removeClass("open")
      }
    }
  });


      
      
  function bodyScroll(){
    if($("body").hasClass("stop-scroll")){
      $("body").removeClass("stop-scroll");
    }
    else{
      $("body").addClass("stop-scroll");
    }
  }
  loadWindow();
  Navbar();
  initCarousel();
  InitCounterlove();
  initGallery();

  // **************************

  /* 

	2. Set Preloader

	*/

  function loadWindow(){ 
    bodyScroll()
    let loaderWindow = $(".preloader"),
    loaderImg    = $(".image");

    $(loaderImg).on("animationend webkitAnimationEnd oAnimationEnd MSAnimationEnd",()=>{
        loaderImg.addClass("finish");
    });
    // Stop Body Scroll To View Preloader Without Scrollbar
    $(window).on("load",()=>{
        setTimeout(()=>{
            $("body").removeClass("stop-scroll");
            $(loaderWindow).addClass("hide");
            setTimeout(()=>{
                $(loaderWindow).css("display","none");
            },600)
        },500)
    })
  }

  // **************************

  /* 

	3. Init Navs

	*/

  function Navbar(){

    if($(".nav-item .nav-link").length){

      $(navLink).on("click",function(){

        $(this).parent().addClass("active").siblings().removeClass("active")

      });

      let link = $(navLink).parent().find(".dropdown-toggle"),
          dropdownItem = $(link).parent().find(".dropdown-item");
      
      $(link).on("click",changeIcon)
      $(dropdownItem).on("click",changeIcon);

    }

  }

  // **************************

  /* 

	4. Init Dropdown 

	*/

  function changeIcon(){

    let link = $(navLink).parent().find(".dropdown-toggle");

    if($(link).hasClass("open")){
      
      $(link).removeClass("open")
    }
    else{
      $(link).addClass("open")
    }

  }

  // **************************

  /* 

	4. Init About Me Popup 

	*/

  function initAboutMePopup(){
    bodyScroll()
    if($(aboutMePopup).is(":hidden")){
      $(aboutMePopup).css("display","block");
      setTimeout(()=>{
        aboutMePopup.addClass("open");
      },100)
    }
    else{
      aboutMePopup.removeClass("open");
      setTimeout(()=>{
        $(aboutMePopup).css("display","none");
      },300)
    }
    $(document).on("keydown",(e)=>{
      if(aboutMePopup.hasClass("open")){
        if(e.keyCode === 27){
          if(aboutMePopup.hasClass("open")){
            aboutMePopup.removeClass("open");
            setTimeout(()=>{
              $(aboutMePopup).css("display","none");
            },300)
            bodyScroll();
          }
        }
      }
    })
  }

  /* 

	6. Init Intro Carousel

	*/

  function initCarousel(){

    if($(".intro-carousel-inner").length){

      $('.intro-carousel-inner').owlCarousel({
      rtl:true,
      loop:true,
      nav:false,
      margin:0,
      autoplay:true,
      autoplayTimeout:10000,
      responsiveClass:true,
      responsive:{
          0:{
              items:1,
          },
          600:{
              items:1,
          },
          1000:{
              items:1,
          }
      }
    })
    }
  }

  // **************************

  /* 

	7.1. Init Counter Loved

	*/
  function InitCounterlove(){ 
    const counter = $(".fav");
    let counterNum = $(".fav span"),
        icon       = $(".fav i"),
        rate       = localStorage.getItem("initRate") || 0;
    $(counterNum).text(localStorage.getItem("initRate") || 0);
    $(icon).addClass(localStorage.getItem("initIcon") || "fal")
    $(counter).on("click",()=>{
      localStorage.setItem("initIcon","fas");
      rate++
      if($(counterNum).text() == 0){
        localStorage.setItem("initRate",rate)
        $(counterNum).text(rate);
        $(icon).addClass(localStorage.getItem("initIcon")).removeClass("fal")
      }
      else{
        return false
      }
    })
  }
  // **************************

  /* 

	8. Gallery

	*/

  function initGallery(){

    const galleryItem  = $(".gallery-items .item"),
          galleryBox   = $(".gallery-pp"),
          galleryClose = $(".gallery-pp .close-btn"),
          galleryImg   = $(".gallery-pp img"),
          galleryCount = $(".gallery-pp .counter"),
          nextBtn      = $(".gallery-pp .prev"),
          prevBtn      = $(".gallery-pp .next");
    let   index        = 0;

    for(let i = 0; i < $(galleryItem).length; i++){
      $(galleryItem[i]).on("click",function(){
        index = i
        togglePopup()
        changeItem()
      })
    }

    $(nextBtn).click(next);

    $(prevBtn).click(prev);

    function togglePopup(){
      galleryBox.toggleClass("open");
      $(document).on("keydown",(e)=>{
        if(galleryBox.hasClass("open")){
          if(e.keyCode === 27){
            if(galleryBox.hasClass("open")){
              galleryBox.removeClass("open");
            }
          }
          if(e.keyCode === 37){
            next()
          }
          else if(e.keyCode === 39){
            prev()
          }
        }
      })
    }

    function changeItem(){
      let imgSrc = $(galleryItem[index]).find("img").attr("src");
      $(galleryImg).attr("src",imgSrc);
      $(galleryCount).text((index + 1) + " من " + $(galleryItem).length);
    }

    function next(){
      if(index == $(galleryItem).length - 1){
        index = 0;
      }
      else{
        index++
      }
      changeItem()
    }

    function prev(){
      if(index == 0){
        index = $(galleryItem).length - 1;
      }
      else{
        index--
      }
      changeItem()
    }

    // Close Popup Gallery
    $(galleryClose).on('click',togglePopup);

  }
  // **************************


  /* 

  9. Alert Sended Message

  */

  (function alertMessage(){

    const alertBox = $(".alert-message"),
          closeAlertBtn = $(".alert-message .close-alert");

    $(closeAlertBtn).on("click",()=>{
      alertBox.fadeOut(500)
    })

    $(window).on("load",()=>{
      setTimeout(()=>{
        alertBox.fadeOut(700)
      },3000)
    });

  })();



  // **************************

})