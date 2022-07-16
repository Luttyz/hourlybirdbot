# Hourly Bird bot

This Github repo contains the very simple code used by the @HourlyBird Twitter and Telegram bot, it is somewhat modular as it can be easily edited to send any images that can be accessed through a web API.

This should also be pretty easy code as this is the first thing I have made using Python, so even if you're a beginner this should still be easy to understand.

Check out a running example of this code at <a href="https://twitter.com/HourlyBird">@HourlyBird Twitter account</a>.

# Dependencies

This script relies on the following Python packages :
<a href="https://pypi.org/project/requests/">requests</a>
<a href="https://pypi.org/project/shutils/">shutils</a>
<a href="https://pypi.org/project/telegram-send/">telegram-send</a>
<a href="https://pypi.org/project/numpy/">numpy</a>
<a href="https://pypi.org/project/tweepy/">tweepy</a>.
<br> You can install all of these at once by copy pasting `pip3 install json requests shutils telegram_send numpy tweepy` in your favourite commmand prompt.

# Setup

Setup is pretty easy, this guide assumes you already have your Twitter API keys and/or Telegram bot API keys and already configured <a href="https://pypi.org/project/telegram-send/">telegram_send</a>. If you haven't, grab your Twitter API keys by following <a href="https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api">this guide</a>, or by using <a href="https://t.me/BotFather">the BotFather Telegram bot</a> and <a href="https://pypi.org/project/telegram-send/#installation">setting up telegram-send</a>.

Once you are ready, download the `birdbot.py` script, simply replace the Twitter API keys that are located at lines 47 to 50, and set another image API (located at line 9) if you want something else than birds. And voilà! If you want to run this bot hourly, the easiest way would be to use a `cron` task on a Linux machine, simple type `crontab -e` in your favourite command prompt and copy paste `0 * * * *  python3 /location/of/the/script/birdbot.py`, from now on the script will run every hour.

# Acknowledgements

Thanks to that one friend with who I had the idea a good year ago if not more, and thank you to everyone who has made the Python packages used by this script.
<br> This script is licensed under the <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0 license</a> as this is the only thing I could think of, not knowing any Software-specific licenses.
