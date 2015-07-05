# une2presse

une2presse is an automatic tweeter to push first page of top newspaper in France


Installation on Debian

package to manage python :
> apt-get install python-setuptools

Install selenium package for python
> easy_install selenium

Install Chrome and ChromeDriver
> wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
> sudo sh -c 'echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
> sudo apt-get update
> sudo apt-get install google-chrome-stable
> apt-get install chromedriver

Install Display python package
> easy_install pyvirtualdisplay
> apt-get install xvfb

Manage the path where chrome and chromedriver are installed
ln -s /usr/bin/chromium /usr/bin/google-chrome
ln -s /usr/lib/chromium/chromedriver /usr/local/bin/google-chrome


TODO :
* logger & send error email
* config file
* deploy in user
* store files in an special folder, like : ~BASE~/NewsPaperCover
* install and use sqlite

