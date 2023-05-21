# Ponisha position finder

Ponisha is a website that allows you to both hire /work as freelancer programmers, designers, etc.
you can set up a skill set and find the desired project according to your skill. this script will extract open positions on Ponisha according to your skill set which is located in config.py and will text the data using Telegram bot.extracted elements are Title of project, Description of project, price budget and link to the project page website, so you can easily click on the link sent to you via bot and get to project page. 

## Installation

to download the script copy this command in your terminal :

```bash
git clone https://github.com/farzinsharif/ponisha-position-finder.git
```
then install the requirements library
```bash
pip install -r requirements.txt
```
## Prerequisites
Python installed (for running the script).

Telegram BOT API-KEY Chat-id
## Usage
Change the skill_list var locate in config.py file according to your skill set And change the time you want the code to run on server.ask bot father on telegram to get a bot , API key , Chat ID , make sure not to share the API key and chat ID with any one
```python
desired_skill = ['وردپرس', 'پایتون', 'ترجمه', 'میکروکنترلر']
```
for better result this project contain telegram bot script. so all you must do is to contact telegram bot father and create bot with unique API key and chat id. after you done that your almost done all you have to do is to add your API key and chat id to config file and find web hosting to run the code 24/7
I would suggest render.com but you can use which service you want.
## Disclaimer
This script is provided as is. I am not responsible for any damage caused by using this script. Use at your own risk.
to prevent any issue for ponisha please do not make many requests.how ever if run the code with the unchanged config it will send request to site once a day.

## Visuals
make sure not to share your 
## Note 
there is part to send you (admin of bot) The data about anyone who texted the BOT.before you share this bot with anyone or give them service with it, make sure to remove the part which send info about chat id and people id as text message.
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Ponisha-position-finder is released under the terms of the MIT license. See [LICENSE](LICENSE.md) for more
information or see https://opensource.org/licenses/MIT.