# Cibertutor

<div align="center">

***A Cybersecurity Awareness Web Application for Non-Technical Users.***

[![Python](https://img.shields.io/badge/Python_3.10-black?logo=python&logoColor=white&labelColor=grey&color=%233776AB)](<https://www.python.org/> "Python")
[![HTML5](https://img.shields.io/badge/HTML_5-white?logo=html5&logoColor=white&labelColor=grey&color=%23E34F26)](#)
[![CSS3](https://img.shields.io/badge/CSS_3-white?logo=css3&logoColor=white&labelColor=grey&color=%231572B6)](#)
[![JavaScript](https://img.shields.io/badge/JavaScript-white?logo=javascript&logoColor=white&label=%20&labelColor=grey&color=%23F7DF1E)](#)
[![SQLite](https://img.shields.io/badge/SQLite-white?logo=sqlite&logoColor=white&label=%20&labelColor=grey&color=%23003B57)](<https://www.sqlite.org/> "SQLite")
[![Flask](https://img.shields.io/badge/Flask-white?logo=flask&logoColor=white&labelColor=grey&color=%233CACBC)](<https://flask.palletsprojects.com/> "Flask")
[![jQuery](https://img.shields.io/badge/jQuery-white?logo=jquery&logoColor=white&label=%20&labelColor=grey&color=%230769AD)](<https://jquery.com/> "jQuery")
[![Docker](https://img.shields.io/badge/Docker-white?logo=docker&logoColor=white&labelColor=grey&color=%232496ED)](<https://www.docker.com/> "Docker")

[![License: MIT](<https://img.shields.io/github/license/informaticapau/cibertutor>)](LICENSE "License")
[![GitHub issues](https://img.shields.io/github/issues/informaticapau/cibertutor)](<https://github.com/informaticapau/cibertutor> "Issues")
[![GitHub stars](https://img.shields.io/github/stars/informaticapau/cibertutor)](<https://github.com/informaticapau/cibertutor/stargazers> "Stars")

</div>

## Table of Contents

- [Cibertutor](#cibertutor)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
    - [Key Features](#key-features)
  - [Usage](#usage)
  - [Install](#install)
    - [Docker](#docker)
    - [Python Virtualenv](#python-virtualenv)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## About

In an increasingly digital world, the need for comprehensive cybersecurity awareness has never been greater. As the internet continues to shape our daily lives, the risks associated with cyber threats loom larger than ever before. In response to this growing concern, we present "Cibertutor," a cutting-edge application designed to foster cybersecurity consciousness among individuals and organizations.

### Key Features

- **Educational Insights**: Cibertutor offers a dedicated section providing users with in-depth information on cybersecurity risks, offering invaluable insights into the evolving landscape of cyber threats. Users can access relevant resources and best practices for safeguarding their digital lives.
- **Interactive Learning**: The application goes beyond conventional cybersecurity tutorials by offering immersive, interactive scenarios and utilities. Through these engaging features, users can gain practical experience in dealing with simulated cyber threats, empowering them to make informed decisions and mitigate risks effectively.
- **Cross-Platform Compatibility**: Cibertutor is meticulously crafted to ensure compatibility across various platforms and devices. Whether you're accessing it on a desktop computer, tablet, or smartphone, the application delivers a seamless and consistent user experience.

## Usage

This application is avaliable at <https://cibertutor.informaticapau.com/>.

## Install

If you want to deploy the application yourself, you can either do it using Docker, or you can run it directly on a Python virtual environment.

### Docker

There is a Docker Hub image you can pull and run directly:

```bash
docker run -d -p "8000:8000" --name cibertutor \
   informaticapau/cibertutor:latest
```

By default, the application listens on port 8000 but of course this can be changed to whichever port you like.

If you want to build the image yourself, a [Dockerfile](Dockerfile) is provided as well. You can do that by pulling the repository and starting the build process:

```bash
git clone https://github.com/informaticapau/cibertutor
cd cibertutor
docker build -t cibertutor .
```

And then run it using the previous command.

### Python Virtualenv

If you want to run the application inside your own host, you can follow these steps:

1. Clone the respository.
2. [ Optional ] Create an virtual environment.
   - Create a directory `.venv` inside the `src/` directory.
3. Install the dependencies from `src/Pipfile`.
   - `pipenv install` can be used to install them inside the virtual environment.
4. Create a `.env` file with the following content:
   - `PHISHING_QUIZ_EMAILS="path/to/file/phishing_quiz/emails.yml"`
   - `MODULES_DATA_FOLDER="path/to/modules/directory"`
5. Run the app to check that it works with `flask run`.
6. Use a production WSGI server like [`gunicorn`](<https://github.com/benoitc/gunicorn> "Gunicorn").

## Contributing

Contributions are welcome! If you have improvements, bug fixes, or new modules to add, feel free to submit a pull request.

## License

The content of this repository is licensed under the [MIT License](LICENSE).

Dependencies and their licenses are specified inside the [NOTICE](NOTICE) file.

## Contact

Feel free to get in touch with me!

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-%23181717?style=for-the-badge&logo=github&logoColor=%23181717&color=white)](<https://github.com/danielfeitopin>)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-white?style=for-the-badge&logo=linkedin&logoColor=white&color=%230A66C2)](<https://www.linkedin.com/in/danielfeitopin/>)

</div>
