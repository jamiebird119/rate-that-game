
function show_rating(id){
    $(`.loader-gif-container`).toggleClass("d-none")
    setTimeout(() => {
        $(`#${id}`).toggleClass("d-none")
        $(`.loader-gif-container`).toggleClass("d-none")
       }, 2000);
    
    
}
    