# TelegramBot-Hamyar
Creating and Developing a telegram bot for SUT Hamyar channel.

## Contributors
- Mohammad Javd Maheronnaghsh
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
- [ ] Developing Admin pannel
    - [ ] Feedbacks: Connecting to the MySQL database and fetch data from coressponding table to show the admins
    - [ ] Event remider:
        - [ ] Create a table for events to be remindered
        - [ ] Creating an interface to store the events properties
- [ ] Developing User pannel
    - [ ] About us
    - [ ] Redirect to main channel
    - [ ] Send Feedbacks :
        - [ ] Creating table
        - [ ] Instering data to the table
    - [ ] Subscribe for event remider
        - [ ] Create a table for subscribers and adding users
        - [ ] Developing a function to send remieder to subscribers