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