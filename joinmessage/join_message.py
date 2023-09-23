from database.database import db
from utilitys.embed_builder import embed_builder

def send_join_message(target_member, guild_id):
    # Try to get the join message from the database
    try:
        join_message = db.get_join_message(guild_id)
    except:
        # If there's an error, set the join message to "None"
        join_message = "None"
    
    # Build the welcome message using the join message
    message = embed_builder(
        "Welcome",
        join_message,
    )
    
    # Return the welcome message
    return message