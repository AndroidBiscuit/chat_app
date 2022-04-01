import requests

# Do not touch these
private_key = '4d1ece90-711f-4ba7-8808-ba8c388a4e81'
public_key = ""
project_id = "7b218aae-0285-437f-b1d3-a068537398c4"


# ----------------------------------------------------------------
# SECTION 1 - Manage users
# ----------------------------------------------------------------

# Create a new user
def add_users():
    r = requests.post(
        # Don't touch this.
        'https://api.chatengine.io/users/',

        data={
            # Username - used to identify, set chat admin
            # This is what will appear on top under the the chat name
            "username": "Test-5", 

            # First and last name
            # This will appear in the user lists on the right (in the chat)
            "first_name": "Faizan", 
            "last_name": "Ahmad", 

            # User password
            "secret": "123123"},
        headers={"Private-Key": private_key}
    )

    # Optional - To check if the user was created (successful return is 201)
    print(r.status_code)







# ----------------------------------------------------------------
# SECTION 2 - Manage chats
# ----------------------------------------------------------------


def new_chat():
    # Don't touch this.
    url = "https://api.chatengine.io/chats/"
    
    payload = {
        # People in the chat (usernames), chat title 
        "usernames": ["Faizan", "Yiheng", "Massimo"], 

        # Chat title 
        "title": "Testing chat admin access"}
    headers = {

    # Don't touch this.
    'Project-ID': project_id,

    # Username and password of the chat admin - Can be set to the current doctor
    'User-Name': 'mail_manager',
    'User-Secret': '123123'
    }

    # Send data
    response = requests.request("PUT", url, headers=headers, data=payload)

    # Optional - Only to see if it worked
    print(response.text)



# ----------------------------------------------------------------

#add_users()
#new_chat()

