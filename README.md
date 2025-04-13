# What is this?
This is a recreation of [Skypromp's TypeRacer stats scraper](https://github.com/SkyPromp/TypeRacer-stats-scraper), which you can find in the attached link. My aim at this point is not the immediate and total recreation of his project (evident from the fact that some graphs are missing), so if you would like to fill in any gaps, pull requests are welcome. :-)

Note: some code was also borrowed from his stats scraper as well, and wherever I have borrowed any code I have placed docstrings at the top of said file denoting as much. If you think I have missed any such docstrings, let me know (or make a pull request)!
# How do I use it?
Before you use it, create a folder `img` in the directory first. Then, you can use it as follows:
```shell
python generate.py username
```
where `username` is your TypeRacer **username**, not to be confused with your **display name**. \
Do note that in order to use this, you need to install some packages which can be found in `requirements.txt`. Create a virtual environment, and then download them with:
```shell
pip install -r requirements.txt`
```