let targetForm = document.querySelector('.jss_content');
    targetForm.addEventListener('keyup',function(){
    document.querySelector('.counting_text').innerHTML = targetForm.value.length
})