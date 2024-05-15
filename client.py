import requests
import json

class FirestoreClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_user(self, name):
        url = f"{self.base_url}/users"
        data = {'name': name}
        response = requests.post(url, json=data)
        return response.json()

    def get_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.get(url)
        return response.json()

    def update_user(self, user_id, name):
        url = f"{self.base_url}/users/{user_id}"
        data = {'name': name}
        response = requests.put(url, json=data)
        return response.json()

    def delete_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.delete(url)
        return response.json()

    def create_journal(self, user_id, name):
        url = f"{self.base_url}/users/{user_id}/journals"
        data = {'name': name}
        response = requests.post(url, json=data)
        return response.json()

    def get_journal(self, user_id, journal_id):
        url = f"{self.base_url}/users/{user_id}/journals/{journal_id}"
        response = requests.get(url)
        return response.json()

    def update_journal(self, user_id, journal_id, name):
        url = f"{self.base_url}/users/{user_id}/journals/{journal_id}"
        data = {'name': name}
        response = requests.put(url, json=data)
        return response.json()

    def delete_journal(self, user_id, journal_id):
        url = f"{self.base_url}/users/{user_id}/journals/{journal_id}"
        response = requests.delete(url)
        return response.json()

    def create_entry(self, user_id, journal_id, name, content):
        url = f"{self.base_url}/users/{user_id}/journals/{journal_id}/entries"
        data = {'name': name, 'content': content}
        response = requests.post(url, json=data)
        return response.json()

    def get_entry(self, user_id, journal_id, entry_id):
        url = f"{self.base_url}/users/{user_id}/journals/{journal_id}/entries/{entry_id}"
        response = requests.get(url)
        return response.json()

    def update_entry(self, user_id, journal_id, entry_id, name, content):
        url = f"{self.base_url}/users/{user_id}/journals/{journal_id}/entries/{entry_id}"
        data = {'name': name, 'content': content}
        response = requests.put(url, json=data)
        return response.json()

    def delete_entry(self, user_id, journal_id, entry_id):
        url = f"{self.base_url}/users/{user_id}/journals/{journal_id}/entries/{entry_id}"
        response = requests.delete(url)
        return response.json()

# Example usage:
if __name__ == '__main__':
    base_url = 'http://127.0.0.1:5000'  # Adjust the base URL as needed
    client = FirestoreClient(base_url)

    # Create a user
    user = client.create_user("John Doe")
    print("Created User:", user)

    # Get a user
    user_id = user['id']
    user = client.get_user(user_id)
    print("Fetched User:", user)

    # Update a user
    updated_user = client.update_user(user_id, "Jane Doe")
    print("Updated User:", updated_user)

    # Delete a user
    delete_response = client.delete_user(user_id)
    print("Deleted User:", delete_response)

    # Create a journal for the user
    journal = client.create_journal(user_id, "My Journal")
    print("Created Journal:", journal)

    # Get a journal
    journal_id = journal['id']
    journal = client.get_journal(user_id, journal_id)
    print("Fetched Journal:", journal)

    # Update a journal
    updated_journal = client.update_journal(user_id, journal_id, "Updated Journal")
    print("Updated Journal:", updated_journal)

    # Delete a journal
    delete_response = client.delete_journal(user_id, journal_id)
    print("Deleted Journal:", delete_response)

    # Create an entry in the journal
    entry = client.create_entry(user_id, journal_id, "First Entry", "This is the content of the first entry.")
    print("Created Entry:", entry)

    # Get an entry
    entry_id = entry['id']
    entry = client.get_entry(user_id, journal_id, entry_id)
    print("Fetched Entry:", entry)

    # Update an entry
    updated_entry = client.update_entry(user_id, journal_id, entry_id, "Updated Entry", "Updated content.")
    print("Updated Entry:", updated_entry)

    # Delete an entry
    delete_response = client.delete_entry(user_id, journal_id, entry_id)
    print("Deleted Entry:", delete_response)
