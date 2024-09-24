from pypresence import Presence
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

client_id = os.getenv('CLIENT_ID')  # Load client ID for RPC from .env
rpc = Presence(client_id)
rpc.connect()

def update_rich_presence(state, details, large_image, large_text):
    print(f'Updating Rich Presence with URL: {large_image}')  # Debugging line
    try:
        rpc.update(
            state=state,
            details=details,
            large_image=large_image,
            large_text=large_text,
            buttons=[{"label": "Change what this says", "url": "https://discord.gg/yRzaen7e"}]
        )
        print('Rich Presence updated successfully.')
    except Exception as e:
        print(f'Error updating Rich Presence: {e}')
