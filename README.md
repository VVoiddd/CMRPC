# CMRPC

Change My Rich Custom Presence (CMRPC) is a Discord bot that automatically updates the user's Discord Rich Presence based on messages in specific channels. It can update the user's avatar, message content, and display customized Rich Presence statuses.

![Placeholder Image](./Placeholder.png)

## Features

- **Rich Presence Update**: Automatically updates the user's Rich Presence with their avatar, name, and custom message whenever they send a message.
- **Whitelisting**: Only users who are on the whitelist (or the owner) can interact with the bot and have their Rich Presence updated. Non-whitelisted users are kicked from the server.
- **Custom Commands**: Includes commands for managing the whitelist and updating Rich Presence manually.
- **Custom Button**: Displays a button in Rich Presence that links to a Discord invite.

## Setup

1. **Clone this repository** or download the script and dependencies.
2. Install required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

3. Replace the following placeholders in the code with your own values:
    - `OWNER_ID`: Your Discord User ID.
    - `HIDDEN_CHANNEL_ID`: The ID of the channel where Rich Presence should be updated.
    - `COMMAND_CHANNELS`: A list of channel IDs where the bot processes commands.
    - `CLIENT_ID`: Your Discord application's Client ID.
    - `TOKEN`: Your bot's token.

## Configuration

### Variables

- `HIDDEN_CHANNEL_ID`: The channel where the bot updates the Rich Presence and interacts with users.
- `COMMAND_CHANNELS`: Channels where the bot accepts commands and processes them.
- `OWNER_ID`: Your Discord User ID. This ID is exempt from the bot’s actions.
- `WHITELIST_FILE`: Path to the whitelist file (`whitelist.json`).

### JSON Structure of Whitelist
The whitelist is stored in a `whitelist.json` file. The format is:

```json
{
    "user_id_1": {
        "username": "user_name_1",
        "uid": user_id_1
    },
    "user_id_2": {
        "username": "user_name_2",
        "uid": user_id_2
    }
}
```

### Rich Presence Setup
The bot updates Discord Rich Presence using the `pypresence` library, which requires a Discord `CLIENT_ID` for your application. It supports dynamic changes to the state, details, and avatar of the Rich Presence.

### Commands

- **`-whitelist <user>`**: Adds a user to the whitelist, allowing them to use the bot's features.
- **`-listwhitelist`**: Lists all users currently in the whitelist.
- **`-removewhitelist <user>`**: Removes a user from the whitelist.
- **`-force <message>`**: Allows the owner to force a custom Rich Presence update.

## How it Works

- **On Bot Startup**: When the bot starts, it will set the default Rich Presence showing a placeholder state and message.
  
- **On User Message**: When a user sends a message in the specified `HIDDEN_CHANNEL_ID`, the bot:
  - Checks if the user is on the whitelist.
  - If the user is **whitelisted** or the **owner**, the bot updates the Rich Presence with the user's avatar and the message content.
  - If the user is **not whitelisted** and not the owner, the bot deletes the message, notifies the user, updates the Rich Presence, and kicks the user from the server.
  
- **Rich Presence**: The bot dynamically updates the user's Rich Presence based on their message content and avatar. A custom button is also added linking to a Discord invite.

## Example Rich Presence

The Rich Presence will show:
- **State**: The content of the user's message.
- **Details**: The username of the user.
- **Large Image**: The user's avatar or a placeholder image if no avatar is available.

### Example Whitelist Data:

```json
{
    "user_id_1": {
        "username": "user_name_1",
        "uid": user_id_1
    },
    "user_id_2": {
        "username": "user_name_2",
        "uid": user_id_2
    }
}
```

## Handling Non-Whitelisted Users

If a non-whitelisted user sends a message in the `HIDDEN_CHANNEL_ID`, the bot will:
- Delete the message.
- Update the Rich Presence with the message content, showing the username.
- Kick the user from the server.
- Send a DM (if possible) with a new invite link to the server.

## Placeholder Image

The placeholder image (`Placeholder.png`) is used when a user does not have a custom avatar. This image will appear in Rich Presence until a valid avatar is set for the user.

![Placeholder Image](./Placeholder.png)

## Example Rich Presence:

When a user with an avatar sends a message, the Rich Presence will update to show their avatar and message content.

## Summary

The CMRPC bot provides an automated and customizable way to manage Discord Rich Presence with user avatars and messages.
