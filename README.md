# Customized chatbox app for SOEN 390
Faizan Ahmad (40100581) \
Team 18

# General info

There is no backend to handle in this version. The messages are handled by [chatengine.io](https://chatengine.io). This will later be linked to the Django backend of our main application, once the current frontend will be integrated with the main application (in progress). The chatengine.io account is handled by Faizan.\
\
\

# Getting Started with the chat app

Note that its important to do `npm install` if this is the first time that you will be running this application. Then just run `npm start`.\
\
Once the project is started, you should see the admin's view of the messages. For now, you can send and receive messages and images (not all formats are supported, may be expanded later on if needed). \
\
*Note that the images may appear to be cropped and there are some minor bugs in the frontend to deal with (like auto refresh of the page when a new message is added, icon placement, etc)*\
\

## Viewing from another user's point of view and adding new users

At the moment, only two users have been setup for testing purposes. You can switch between `admin` (Faizan) and `user1` (Elizabeth) by commenting/uncommenting the `userName` line in the `App.js` file. \
\
*Note that there can only be one user that can access this at a time. Multiple users can also access it without any issues, but it requires you to have a separate copy of this react app to be running alongside it (or on another device).*\

The code for the chat app will be isolated from the rest of the main application. Just like the graphs in Sprint 2, the contents of the chat app can be updated dynamically. This includes both the user creation (handled by the API) and user views (updated dynamically based on who is currently logged in to the main application). More on that later on, during/after the integration with the main application. \
\
As for adding new users, this can be done dynamically with the API (more details on this later on). 

## Linking sent/received messages to the notification system

Chat Engine supports [server Rest API calls](https://chatengine.io/docs/react/v1/event_hooks#on_new_chat) and so by using event hooks in the `App.js` file, we can make an event happen whenever someone sends a new message to the recepient. This event can be a notification for the recepient (to be implemented soon, requires adding new functionality to the current main application backend). 

## Linking sent/received messages to the notification system
