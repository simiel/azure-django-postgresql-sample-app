const nav = document.querySelector('#nav')
const open = document.querySelector('#open')
const close = document.querySelector('#close')

open.addEventListener('click', ()=>{
  if ( nav.classList.contains('nav-close') ){
    nav.classList.toggle('nav-close')
  }
})


close.addEventListener('click', ()=>{
  if ( nav.classList.contains('nav-close') ){
    
  } else{
    nav.classList.toggle('nav-close')
  }
})