/* Cookies */
$(document).ready(() => {
    if ($.cookie('cookies_accepted') != 'true') {
        let txt = 'This application uses cookies to function properly.'
        let msg = $(`<p>${txt}</p>`)
        msg.addClass('message');

        let button = $('<button>Understood</button>');
        button.click(() => {
            $.cookie('cookies_accepted', 'true', { path: '/' });
            msg.slideUp(400);
        });

        $('#messages').append(msg);
        msg.append($('<br>'));
        msg.append(button);
    }
});

/* Nav bar*/
$(document).ready(() => {

    $('.nav-link').each((index, el) => {
        if ($(el).attr('href') == window.location.pathname
            || $(el).attr('href') == $('#pagination-back a').attr('href')) {
            $(el).parent().remove();
        }
    });

    $('#nav-menu-icon').click(() => {
        $('#nav-menu').slideToggle(250);
    });
});