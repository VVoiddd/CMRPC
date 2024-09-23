# CMRPC

Change My Rich Custom Presence (CMRPC) is a tool that automatically updates your Discord Rich Presence with user avatars and custom messages when someone joins your server and sends a message.

## Features

- Automatically updates Discord Rich Presence with the user's avatar and custom message.
- Kicks users after they send a message and deletes the message.
- Uses Discord's CDN links to display user avatars.
- Includes a customizable button in the Rich Presence.

## Configuration

- `hidden_channel_id`: The ID of the hidden channel where the bot uploads user avatars.
- `owner_id`: The ID of the owner who is not affected by the bot's actions.

## Where the stinky one is
- [notwithering's Version that stinks](https://github.com/notwithering/rpcmsg)

## TODO 

*Will Follow In This Order Below*

<details>
<summary>1.0 Add Commands Loader</summary>

- Load and handle custom commands from a modular command system.
- This will enable easier addition of new commands without changing the core code.

</details>

<details>
<summary>1.1 Add Better Commands</summary>

- Refine and improve existing commands for better functionality and user experience.
- Focus on fixing bugs and adding more flexibility for customizing actions.

</details>

<details>
<summary>1.2 Fix Not Working On Other Windows Versions</summary>

- Patch compatibility issues so that CMRPC works across different versions of Windows.

</details>

<details>
<summary>1.3 Add install.bat And start.bat For Easy Install And Use</summary>

- Provide a simple installation and start process with batch files for easier setup.

</details>

<details>
<summary>1.4 Fix Whitelist Command</summary>

- Correct issues with the whitelist command to ensure it properly exempts certain users from bot actions.

</details>

<details>
<summary>1.5 Add Customizable Join Messages</summary>

- Allow server owners to customize the welcome/join message for new users.
- Support placeholders like `{username}`, `{server_name}`, and `{timestamp}`.

</details>

<details>
<summary>1.6 Add Role-based Exceptions</summary>

- Enable role-based exceptions so users with specific roles won’t be kicked or have their messages deleted.

</details>

<details>
<summary>1.7 Add Webhook Integration</summary>

- Implement webhook support for notifying external platforms (Slack, Discord channels, etc.) when a user joins.

</details>

<details>
<summary>1.8 Add Avatar Customization Options</summary>

- Provide simple avatar effects like grayscale or pixelation for visual customization.

</details>

<details>
<summary>1.9 Add A Cooldown Period</summary>

- Add a cooldown feature to prevent users from rejoining and spamming after they are kicked.

</details>

<details>
<summary>2.0 Add Enhanced Logging</summary>

- Improve logging to track kicked users, message deletions, and other bot actions with detailed timestamps.
- Support exportable logs (e.g., CSV).

</details>

## Working On (Example)

- **Version 1.0: Commands Loader (Example)**
    - Placeholder example: Working on implementing a modular command system.
    - Status: In Progress (Example)



## Completed (Example)

- **Version 1.0: Commands Loader (Example)**
    - **Released on:** DD/MM/YYYY (Example)
    - **Changes:** Placeholder example: Added a modular command loader, allowing custom commands to be added easily.
    - **Bug Fixes:** Placeholder example: Fixed minor issues with how commands were being handled.

- **Version 1.1: Add Better Commands (Example)**
    - **Released on:** DD/MM/YYYY (Example)
    - **Changes:** Placeholder example: Improved command responses, added error handling, and increased customization options.

