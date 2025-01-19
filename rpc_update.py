from pypresence import Presence

def update_rich_presence(CLIENT_ID):
    """Initializes the RPC Presence with the provided Client ID."""
    rpc = Presence(CLIENT_ID)  # Initialize Presence with the provided CLIENT_ID
    rpc.connect()  # Connect to Discord's RPC service
    return rpc

def update_rpc(rpc, state, details, large_image, large_text, invite_url):
    """Updates the Discord Rich Presence with provided details."""
    try:
        # Update Rich Presence with the provided data
        rpc.update(
            state=state,
            details=details,
            large_image=large_image,
            large_text=large_text,
            buttons=[{"label": "Join Discord", "url": invite_url}]  # Use dynamic invite link
        )
        print(f"Rich Presence updated: {state} | {details} | Hover Text: {large_text}")
    except Exception as e:
        print(f"Error updating Rich Presence: {e}")
