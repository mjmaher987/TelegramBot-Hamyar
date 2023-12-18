# TelegramBot-Hamyar
<img src="https://github.com/mjmaher987/TelegramBot-Hamyar/assets/77095635/4565899d-3d07-48a5-ad48-a1b0df2ea83e)" width="200" />

<img src="https://github.com/mjmaher987/TelegramBot-Hamyar/assets/77095635/a334bd19-2add-4a7c-b603-a23618daa377)" width="200" />


Creating and Developing a telegram bot for SUT Hamyar channel.

## Bot Access
You can access the bot and use it from Telegram at: @sut_hamyar_bot

Help use improve the bot with your welcomming feedbacks. You can leave an issue or create a pull request to join our community.

## Contributors
- Mohammad Javad Maheronnaghsh
- Mohammad Hossein Shafizadegan

## Guide
### Useful Links
We got help from these links ([link1](https://www.youtube.com/watch?v=fReAwuHUiiE) and [link2](https://www.youtube.com/watch?v=LL9XbWEXELc]))
Here are the commands to develop the code on DigitalOcean.
- Check for existing sessions
  ```
  tmux list-sessions
  ```
- Terminate if it is undesired
  ```
  tmux kill-session -t bot-session
  ```
- Start from beginning
  ```
  tmux new-session -s bot-session
  source venv/bin/activate
  python3 bot.py
  ```  
- Go out of the virtual environment
  ```
  deactivate
  ```
- Go out of the Session environment
  ```
  Ctrl-b, then press d
  ```
## Bot Features
- Admin Pannel :
    - Observing and tracking feedbacks and suggestions given from users anonymously
    - Add events (e.g. workshops) so that the users will recieve reminders.

- User Pannel :
    - Sending feedbacks and suggestions anonymously
    - Subscribe for events to recieve reminders
    - Subscribe for special topics (articles, video clips, notes, ...) so that the bot will send them that special posts. (Beta version)

## Server
Firstly it was located on Pythonanywhere, but due to some issues and limitations, we moved onto DigitalOcean.

## To Do
- [x] Developing Admin pannel
    - [x] Feedbacks: Connecting to the MySQL database and fetch data from coressponding table to show the admins
    - [x] Event remider:
        - [x] Create a table for events to be remindered
        - [x] Creating an interface to store the events properties
- [x] Developing User pannel
    - [x] About us
    - [x] Redirect to main channel
    - [x] Send Feedbacks :
        - [x] Creating table
        - [x] Instering data to the table
    - [x] Subscribe for event remider
        - [x] Create a table for subscribers and adding users
        - [x] support removing from reminder list too
        - [ ] Developing a function to send remieder to subscribers
            - [x] fetching data from DB
            - [x] unschedule when unsubscribe
            - [x] when somebody subscribes, schedule all the pre-entered events
            - [x] when some events added, schedule that event for all pre-subscribed users
            - [x] unschedule when remove/cancel event
- [ ] Find a proper server
- [ ] Create Application
- [ ] Guidelines - for users : HELP
- [ ] Privacy (When using admin panel)
- [ ] Add Choose Language
- [ ] Clean Code

