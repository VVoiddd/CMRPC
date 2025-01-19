from pypresence import Presence

# Discord Rich Presence setup
CLIENT_ID = 'Your Client ID'  # Replace with your application's Client ID
rpc = Presence(CLIENT_ID)
rpc.connect()

def update_rich_presence(state, details, large_image, large_text):
    """Updates the Discord Rich Presence with provided details."""
    try:
        rpc.update(
            state=state,
            details=details,
            large_image=large_image,
            large_text=large_text,
            buttons=[{"label": "Join Discord", "url": "https://discord.gg/INVITE"}]
        )
        print(f"Rich Presence updated: {state} | {details} | Hover Text: {large_text}")
    except Exception as e:
        print(f"Error updating Rich Presence: {e}")
