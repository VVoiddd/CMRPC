whitelist = set()

def add_to_whitelist(user_id):
    whitelist.add(user_id)

def remove_from_whitelist(user_id):
    whitelist.discard(user_id)

def is_whitelisted(user_id):
    return user_id in whitelist

def get_whitelist():
    return whitelist
