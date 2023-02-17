$(document).ready(() => {

    let checking = false;

    const addItem = (description, value, status) => {
        let el = $('<li></li>').addClass('pw-info-item');
        el.text(`${description}: ${value}.`)
        switch (status) {
            case 'good':
                el.addClass('pw-check-okay');
                break;
            case 'bad':
                el.addClass('pw-check-wrong');
                break;
            case 'warning':
                el.addClass('pw-check-warning');
                break;
        }
        $('#pw-info').append(el);
    }

    const checkPassword = () => {

        let password;
        let test;

        password = $('#password').val();

        /* Password length */
        if (password.length < 8) {
            addItem('Password length', password.length, 'bad');
        } else if (8 <= password.length && password.length < 12) {
            addItem('Password length', password.length, 'warning');
        } else {
            addItem('Password length', password.length, 'good');
        }

        /* Numbers */
        test = /\d+/.test(password);
        addItem('Includes numbers', test ? 'Yes' : 'No', test ? 'good' : 'bad');
        if (/^\d+$/.test(password)) {
            addItem('Includes more than numbers', 'No', 'bad');
        }

        /* Lowercase letters */
        test = /[a-z]+/.test(password);
        addItem('Includes lowercase letters',
            test ? 'Yes' : 'No', test ? 'good' : 'bad');
        if (/^[a-z]+$/.test(password)) {
            addItem('Includes more than lowercase letters', 'No', 'bad');
        }

        /* Uppercase letters */
        test = /[A-Z]+/.test(password);
        addItem('Includes uppercase letters',
            test ? 'Yes' : 'No', test ? 'good' : 'bad');
        if (/^[A-Z]+$/.test(password)) {
            addItem('Includes more than uppercase letters', 'No', 'bad');
        }

        /* Symbols */
        test = /(_|\W)+/.test(password);
        addItem('Includes symbols', test ? 'Yes' : 'No', test ? 'good' : 'bad');
        if (/^(_|\W)+$/.test(password)) {
            addItem('Includes more than symbols', 'No', 'bad');
        }

    }

    const startChecking = () => {
        if (!checking) {
            checking = true;
            $('#pw-info').slideUp(400, () => {
                $('#pw-info').empty();
                checkPassword();
                $('#pw-info').slideDown(400);
                checking = false;
            });
        }

    }

    $("#password").keydown(e => {
        if (e.which === 13) { // Enter
            startChecking();
        }
    });

    $("#check-button").click(() => startChecking());
});