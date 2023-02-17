$(document).ready(() => {
    $('.accordion').click(e => {
        $(e.currentTarget).toggleClass('active');
        $(e.currentTarget).next().slideToggle(250);
    });
});