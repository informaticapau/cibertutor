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

$(document).ready(() => {

    let nextEmailId = 1;

    const updateTime = () => {

        const months = [
            'January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December'
        ];

        let date = new Date();

        $('#time').text(
            `${date.getHours().toString().padStart(2, '0')}:`
            + `${date.getMinutes().toString().padStart(2, '0')}`
        );

        $('#details-date .details-value').text(
            `${date.getDate()} `
            + `${months[date.getMonth()]} `
            + `${date.getFullYear()}, `
            + `${date.getHours().toString().padStart(2, '0')}:`
            + `${date.getMinutes().toString().padStart(2, '0')}:`
            + `${date.getSeconds().toString().padStart(2, '0')}`
        );
    }

    const loadEmail = (id) => {
        fetch(`/api/phishing_quiz/${id}`)
            .then(response => response.json())
            .then(dto => {
                updateTime();
                $('#from-name').text(dto['from_name']);
                $('#from-email').text(`< ${dto['from_email']} >`);
                $('#details-from .details-value').text(dto['from_email']);
                $('#details-subject .details-value').text(dto['subject']);
                $('#phi-body').html(dto['content']);
                $('#phi-comment-message').html(dto['comment']);

                switch (dto['phishing_location']) {
                    case 'from_name':
                    case 'from_email':
                        $('#from-text').addClass('solution');
                        $('#details-from').addClass('solution');
                        break;
                    case 'subject':
                        $('#details-subject').addClass('solution');
                        break;
                }

                nextEmailId = dto['next'];
                if (nextEmailId == null) {
                    $('#phi-quiz').trigger('lastQuiz');
                }
            })
            .then(() => {
                $('#phi-quiz').trigger('quizLoaded');
            });
    }

    $('#details-button').click(() => {
        $('#phi-header-details').slideToggle(250);
    });

    $('#phi-quiz').on('loadQuiz', () => {
        loadEmail(nextEmailId);
    });

});