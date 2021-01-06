
function show_rating(id){
    $(`.loader-gif-container`).toggleClass("d-none")
    setTimeout(() => {
    //    $(`#${id}`).toggleClass("d-none")
        $(`.loader-gif-container`).toggleClass("d-none")
       }, 1500);
     setTimeout(() => {
       $(`#${id}`).find(".rating").toggleClass("hide-rating show-rating")}, 1750);
    
}
    