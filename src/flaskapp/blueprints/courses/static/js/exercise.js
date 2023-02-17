$(document).ready(() => {
    $('.answer').click(e => {
        $('.answer').removeClass('active checked');
        $(e.currentTarget).addClass('active');
        $('#check_answers').addClass('active');
    });

    $('#check_answers').click(e => {
        if ($(e.currentTarget).hasClass('active')) {
            $('.answer.active').removeClass('active').addClass('checked');
            $(e.currentTarget).removeClass('active');
        }
    });
});