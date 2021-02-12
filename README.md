![CI](https://github.com/benftwc/lydros-bot/workflows/CI/badge.svg)
# LYDROS
## THE LOGSKEEPER

![Lyros, the Lorekeeper](https://i.imgur.com/VA1mFiX.jpg)

### The Discord Logs handler for World of Warcrafts

Inspired by https://github.com/agubelu/discord-bot-template

## Contributing

1. Clone/Fork that repository
2. `cd` into the repository's folder, then create `.env` file
3. Insert into `.env` :

```
DISCORD_API_BOT_TOKEN=<Your bot API token>
BOT_DEFAULT_PREFIX=<your default bot prefix>
```
4. (recommanded) create and use [Python's virtual env module](https://docs.python.org/3/library/venv.html) 

4.a `python -m venv .venv && source .venv/bin/activate`
5. Install development dependencies : `$ pip install -r dev-requirements.txt`
6. Install Coding dependencies : `$ pip install pre-commit && pre-commit install`
7. Start your bot instance with `python main.py`
8. Open new [pull requests](https://github.com/benftwc/lydros-bot/pulls) 
