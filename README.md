[![Requirements Status](https://requires.io/github/astrogewgaw/tcal/requirements.svg?branch=release)](https://requires.io/github/astrogewgaw/tcal/requirements/?branch=release)

# tcal

<div style="text-align: center">
<img src='https://github.com/astrogewgaw/tcal/blob/release/src/tcal/data/img/icon.png' width='500px' height='500px' alt="tcal logo">
</div>

<div style="text-align: justify">

__tcal__ a.k.a. **T**he **C**omprehensive **A**strochemists' **L**ist is an attempt to compile and distribute a comprehensive, maintained and updated list of astrochemists across the globe. It came about through discussions I had with some members of the astrochemical community on Twitter. Most such lists either:

* had not be maintained, or
* included only a handful of astrochemists.

This led me to start compiling **tcal**. The aim of this list is to:

* help parts of the community contact one another, and
* open doors for undergraduates like me, who can contact actual, living astrochemists through this list.

As of July 2020, it has more than **300** names, updated and maintained with the help of **20** editors from the astrochemical community!

## What's New?

The *latest* release, **v1.1**, is out! It includes several minor fixes and patches to the code, including:

* A **new** icon!
* The static database is now packaged along with the code, so you can use **tcal** right out of the box!
* *Fixed* a bug that didn't allow data files to be installed. This essentially rendered the GUI unusable.
* *Changed* several urls, since I changed the domain to my personal website.

## Installation

The easiest method is to use pip install, which pulls the latest release from the python package index and installs all required dependencies:

```bash
pip install tcal-astro
```

The alternative is to clone the repository, especially if you want the absolute latest version:

```bash
git clone https://github.com/astrogewgaw/tcal
```

And then in the base directory of `tcal` run

```bash
python setup.py install
```

I am working on preparing _executables_ for Linux, Mac and Windows systems. Watch this space!

The installer adds a link to an app in your python environment using [console_scripts entry points](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html): `tcal`. This is the GUI where you can see the list, search it, update it, and save it in CSV or Excel formats. I have kept the GUI as intuitive as possible, so if you run into any problems, let me know!

<div style="text-align: center">
<img src='https://github.com/astrogewgaw/tcal/blob/release/src/tcal/data/img/screenshot.png' alt="A screenshot showing the main GUI of `tcal`.">
</div>

## **tcal** on the Web

**tcal** is also available on the Web right here: [astrocommunique.netlify.app/tcal/list](https://astrocommunique.netlify.app/tcal/list). I chose to host this on my *personal* website, which makes it easier to maintain.

It's official! [**David E. Woon**](http://www.astrochymist.org/woon/), maintainer of the [**Astrochymist**](http://astrochymist.org/), has given his blessings to the project :grin: ! You can check out the updated version of his Who's Who in Astrochemistry, where he cites **tcal**, [here](http://astrochymist.org/astrochymist_whom.html).

## Help **tcal**!

You can help maintain and update **tcal**! Just fill the form here: [astrocommunique.netlify.app/tcal/help](https://astrocommunique.netlify.app/tcal/help) and I will add you as an editor. The list of editors will be moderated by me, in case the trolls find us! If I don't get back to you, you can send me a reminder through my website!

</div>
