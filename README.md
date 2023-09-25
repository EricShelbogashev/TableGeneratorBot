# Setup (linux guide)
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
   
# Usage
   Send command `/generate` to get list of shuffled members with time.
   
   Send command `/generate <part of first excluded member's string> <part of second excluded member's string>` to get list without this members.

   > Note: substring cannot contain spaces.
   
   **Example**
   ```
   list: "user1", "user name", "membbr string"
   
   [me]: /generate 
   [bot]: "user1", "user name", "membbr string"
   
   [me]: /generate user
   [bot]: "membbr string"
   
   [me] /generate me
   [bot] "user1"
   
   [me] /generate user1
   [bot] "user name", "membbr string"
   ```

   Add param `offset=` with minutes value to change default 15 minutes delay in table.
   
   **Example**
   ```
   [me]: /generate user1
   [bot]: "u... 16:20", "m... 16:35"
   
   [me]: /generate user1 offset=30
   [bot]: "u... 16:20", "m... 16:50" 
   ```