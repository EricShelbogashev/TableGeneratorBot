# Usage (linux guide)
1. Set environment `BOT_TOKEN`
    ```bash
    export BOT_TOKEN=6318692078:aae1rdwzuglssqhouk1ouuiebqylrxahmu
    ```
2. Create `members.txt` in the same directory with `main.py` and fill it
    ```
    Name0 Surname0
    Name1 Surname1
    ...
    SomeName SomeSurname
    ...
    Name_n SurnameN
    ```
3. Install [requirements](https://github.com/python-telegram-bot/python-telegram-bot)
   ```bash
   pip install python-telegram-bot --upgrade
   ```
4. Run
   ```bush
   python3 main.py
   ```
   or
   ```bush
   python main.py
   ```