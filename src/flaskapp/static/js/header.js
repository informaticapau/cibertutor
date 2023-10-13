// MIT License

// Copyright (c) 2023 Daniel Feito Pin

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

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