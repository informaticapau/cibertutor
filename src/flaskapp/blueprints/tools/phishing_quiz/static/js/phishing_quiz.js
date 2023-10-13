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

/* User Data */
$(document).ready(() => {

    const updateUserInfoForm = () => {
        $('#phi-user-name').val($.cookie('phi-user-name'));
        $('#phi-user-email').val($.cookie('phi-user-email'));
        $('#cancel-button').show();
    }

    const showUserInfoForm = () => {
        $('#change-data, #quiz-container').fadeOut(400, () => {
            $('#phi-user-info').fadeIn(400);
        });
    }

    const hideUserInfoForm = (update = false) => {
        $('#phi-user-info').fadeOut(400, () => {
            if (update) {
                updateUserInfoForm();
            }
            $('#start-quiz').addClass('active')
            $('#change-data, #quiz-container').fadeIn(400);
        });
    }

    $('#phi-user-info').off('submit').submit(() => {
        $.cookie('phi-user-name', $('#phi-user-name').val());
        $.cookie('phi-user-email', $('#phi-user-email').val());
        hideUserInfoForm(true);
    });

    $('#cancel-button').click(() => {
        hideUserInfoForm();
    });

    $('#change-data').click(() => {
        $('#start-quiz').removeClass('active');
        showUserInfoForm();
    });

    if ($.cookie('phi-user-name') == null
        || $.cookie('phi-user-email') == null) {
        $('#phi-user-info').show();
        $('#start-quiz').addClass('active').show();
    } else {
        $('#change-data').show();
        updateUserInfoForm();
        $('#start-quiz').addClass('active').show();
        $('#quiz-container').show();
    }

});

/* Quiz */
$(document).ready(() => {

    let gameStarted = false;
    let counter = 0;
    let score = 0;

    const toogleSelection = el => {
        if (!$('#check-phishing, #mark-legit').hasClass('checked')) {
            if ($(el.currentTarget).hasClass('active')) {
                $('.selectionable.active').removeClass('active');
                $('#check-phishing').removeClass('active');
                $('#mark-legit').addClass('active');
            } else {
                $('.selectionable.active').removeClass('active');
                $(el.currentTarget).addClass('active');
                $('#check-phishing').addClass('active');
                $('#mark-legit').removeClass('active');
            }
        }
    }

    const prepareQuiz = () => {
        $('#phi-quiz').fadeOut(500, () => {

            /* Clear selection */
            $('.selectionable.active').removeClass('active');

            /* Restart buttons status */
            $('#phi-buttons').children().each((index, el) => {
                $(el).removeClass('active checked');
            });
            $('#mark-legit').addClass('active');
            $('#phi-buttons').show();

            /* Hide comment and continue buttons */
            $('#phi-comment, #continue-buttons').hide();

            /* Load quiz */
            $('#phi-quiz').trigger('loadQuiz');

            /* Update quiz counter */
            counter++;
        });
    }

    const checkAnswer = () => {
        let active = $('.selectionable.active')
        return active.hasClass('solution') 
        || active.length === 0 && $('.selectionable.solution').length === 0;
    }

    $('#start-quiz').click(() => {
        if ($('#start-quiz').hasClass('active') && !gameStarted) {
            gameStarted = true;
            $('#description').slideUp(400);
            $('#start-quiz').removeClass('active').fadeOut(400, () => {
                prepareQuiz();
            });
        }
    });

    /* Activate selectionables */
    $('#phi-quiz').on('click', '.selectionable', el => {
        toogleSelection(el);
    });
    $('#phi-quiz').on('click', '.selectionable', el => {
        if (el.which === 13 || el.which === 32) { // Enter or Space
            toogleSelection(el);
        }
    });

    $('#check-phishing, #mark-legit').click(e => {
        if ($(e.currentTarget).hasClass('active')) {
            $(e.currentTarget).removeClass('active')
            $('#check-phishing, #mark-legit').addClass('checked');
            $('#phi-buttons').fadeOut(500, () => {
                let correct = checkAnswer();
                $('#phi-comment-status').text(
                    correct ? 'Correct!: ' : 'Wrong!: '
                );
                if (correct) {
                    score++;
                }
                $('#phi-comment').fadeIn(500);
                $('#continue-buttons').fadeIn(500);
            });
        }
    });

    $('#next-button').click(() => {
        prepareQuiz();
    });

    $('#show-score-button').click(() => {
        $('#phi-quiz').fadeOut(500, () => {
            $('#score').text(score);
            $('#questions').text(counter);
            $('#quiz-score').fadeIn(500);
        });
    });

    $('#phi-quiz').on('quizLoaded', () => {
        $('#details-to .details-value').text($.cookie('phi-user-email'));
        $('.username').text($.cookie('phi-user-name'));
        $('#phi-quiz').fadeIn(500);
    });

    $('#phi-quiz').on('lastQuiz', () => {
        $('#next-button').hide();
        $('#show-score-button').show();
    });

});