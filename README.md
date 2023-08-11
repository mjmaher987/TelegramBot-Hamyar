# TelegramBot-Hamyar
Creating and Developing a telegram bot for SUT Hamyar channel.

## Contributors
- Mohammad Javad Maheronnaghsh
- Mohammad Hossein Shafizadegan

## Bot Features
- Admin Pannel :
    - Observing and tracking feedbacks and suggestions given from users anonymously
    - Add events (e.g. workshops) so that the users will recieve reminders.

- User Pannel :
    - Sending feedbacks and suggestions anonymously
    - Subscribe for events to recieve reminders
    - Subscribe for special topics (articles, video clips, notes, ...) so that the bot will send them that special posts. (Beta version)

## To Do
- [x] Developing Admin pannel
    - [x] Feedbacks: Connecting to the MySQL database and fetch data from coressponding table to show the admins
    - [x] Event remider:
        - [x] Create a table for events to be remindered
        - [x] Creating an interface to store the events properties
- [ ] Developing User pannel
    - [x] About us
    - [x] Redirect to main channel
    - [x] Send Feedbacks :
        - [x] Creating table
        - [x] Instering data to the table
    - [ ] Subscribe for event remider
        - [x] Create a table for subscribers and adding users
        - [x] support removing from reminder list too
        - [ ] Developing a function to send remieder to subscribers
            - [ ] fetching data from DB
            - [ ] unschedule and schedule
            - [ ] when somebody subscribes, schedule all the pre-entered events
            - [ ] when some events added, schedule that event for all pre-subscribed users
- [ ] Find a proper server

