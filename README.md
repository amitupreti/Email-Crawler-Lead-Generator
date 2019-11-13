<br />
<p align="center">
  <a href="https://github.com/nOOBIE-nOOBIE/Email-Crawler-Lead-Generator">
  </a>

  <h3 align="center">Email Crawler and Lead generator in python</h3>
<img src="https://snipboard.io/Ba9Ing.jpg"></img>
<p align="center">
    This crawler takes an webaddress as input and then extracts all emails from that website by sequentially visiting every url in that domain.
    <br />
    <a href="https://github.com/nOOBIE-nOOBIE/Email-Crawler-Lead-Generator"></a>
    <br />
    <br />
    <a href="https://github.com/nOOBIE-nOOBIE/Email-Crawler-Lead-Generator#about-the-project"></a>
    ·
    <a href="https://github.com/nOOBIE-nOOBIE/Email-Crawler-Lead-Generator/issues">Email-Crawler-Lead-Generatorrt Bug</a>
    ·
    <a href="https://github.com/nOOBIE-nOOBIE/Email-Crawler-Lead-Generator/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->

## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

![Crawler Demo](https://media.giphy.com/media/VGtDkE48N9WtMnqQiV/giphy.gif)


The Email Crawler makes sure that it only visits the urls in same domain and doesnot save duplicate emails.It also keeps the log of urls visited and dumps them at the end of crawling



### Built With

* [python](https://www.python.org/)
* [requests](https://3.python-requests.org/)
* [urllib](https://docs.python.org/3/library/urllib.parse.html#)
*  [lxml](https://lxml.de/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation
 
1. Clone the Email-Crawler-Lead-Generator
```sh
git clone https://github.com/nOOBIE-nOOBIE/Email-Crawler-Lead-Generator.git
```
2. Install dependencies
```sh
pip install -r requirements.txt
```



<!-- USAGE EXAMPLES -->
## Usage

Simply pass the url as an argument
```sh
python email_crawler.py https://medium.com/
```

  ### Output
  ```sh
  ➜  email_crawler python3 email_crawler.py https://medium.com/
WELCOME TO EMAIL CRAWLER
CRAWL : https://medium.com/
 1 Email found press@medium.com
 2 Email found u002F589e367c28ca47b195ce200d1507d18b@sentry.io
CRAWL : https://medium.com/creators
 3 Email found joshsrose@me.com
 4 Email found yourfriends@medium.com
 5 Email found partnerprogram@medium.com
 6 Email found dominiquemattiwrites@gmail.com
 7 Email found hihumanparts@gmail.com
CRAWL : https://medium.com/@mshannabrooks
CRAWL : https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40mshannabrooks&source=listing-----5f0204823a1e---------------------bookmark_sidebar-
CRAWL : https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40mshannabrooks&source=-----e5d9a7ef4033----6------------------

```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/nOOBIE-nOOBIE/Email-Crawler-Lead-Generator/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Amit Upreti - [@amitupreti](https://www.linkedin.com/in/amitupreti/)

Project Link: [https://github.com/nOOBIE-nOOBIE/Email-Crawler-Lead-Generator](https://github.com/nOOBIE-nOOBIE/Email-Crawler-Lead-Generator)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [python circle](https://www.pythoncircle.com/post/217/python-script-2-crawling-all-emails-from-a-website/)
* [mukesh ojha](https://www.linkedin.com/in/mukesh-ojha-72675697/)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
