# Import Packages
from pypresence import Presence
import time

client_id = "801321552250535977"  # Your application id here

# button labels and urls
btn_label_1 = "Invite Cartero"
btn_label_2 = "Join Support Server"
btn_url_1 = "https://discord.com/api/oauth2/authorize?client_id=801321552250535977&permissions=8&scope=bot%20applications.commands"
btn_url_2 = "https://discord.com/invite/bNZefkNqVw"

# Rich Presence setup
RPC = Presence(client_id=client_id)
RPC.connect()
RPC.update(
    state='Developing Cartero',  # Rich Presence state
    details='Moderation',  # Rich Presence details
    small_image='small', small_text='Cartero',  # Set small image and its text (Optional)
    large_image='large', large_text='Cartero',  # Set large image and its text (Optional)
    buttons=[
        {"label": btn_label_1, "url": btn_url_1},   # btn 1 (Optional)
        {"label": btn_label_2, "url": btn_url_2}    # btn 2 (Optional)
    ]
)

print("Rich Presence enabled")

while 1:
    time.sleep(15)
