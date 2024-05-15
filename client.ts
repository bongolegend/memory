import FirestoreClient from './FirestoreClient';

const baseURL = 'http://127.0.0.1:5000';  // Adjust the base URL as needed
const client = new FirestoreClient(baseURL);

async function main() {
    try {
        // Create a user
        const userResponse = await client.createUser('John Doe');
        console.log('Created User:', userResponse.data);

        const userId = userResponse.data.id;

        // Get the created user
        const getUserResponse = await client.getUser(userId);
        console.log('Fetched User:', getUserResponse.data);

        // Update the user
        const updateUserResponse = await client.updateUser(userId, 'Jane Doe');
        console.log('Updated User:', updateUserResponse.data);

        // Delete the user
        const deleteUserResponse = await client.deleteUser(userId);
        console.log('Deleted User:', deleteUserResponse.data);

        // Create a journal for the user
        const journalResponse = await client.createJournal(userId, 'My Journal');
        console.log('Created Journal:', journalResponse.data);

        const journalId = journalResponse.data.id;

        // Get the created journal
        const getJournalResponse = await client.getJournal(userId, journalId);
        console.log('Fetched Journal:', getJournalResponse.data);

        // Update the journal
        const updateJournalResponse = await client.updateJournal(userId, journalId, 'Updated Journal');
        console.log('Updated Journal:', updateJournalResponse.data);

        // Delete the journal
        const deleteJournalResponse = await client.deleteJournal(userId, journalId);
        console.log('Deleted Journal:', deleteJournalResponse.data);

        // Create an entry in the journal
        const entryResponse = await client.createEntry(userId, journalId, 'First Entry', 'This is the content of the first entry.');
        console.log('Created Entry:', entryResponse.data);

        const entryId = entryResponse.data.id;

        // Get the created entry
        const getEntryResponse = await client.getEntry(userId, journalId, entryId);
        console.log('Fetched Entry:', getEntryResponse.data);

        // Update the entry
        const updateEntryResponse = await client.updateEntry(userId, journalId, entryId, 'Updated Entry', 'Updated content.');
        console.log('Updated Entry:', updateEntryResponse.data);

        // Delete the entry
        const deleteEntryResponse = await client.deleteEntry(userId, journalId, entryId);
        console.log('Deleted Entry:', deleteEntryResponse.data);

    } catch (error) {
        console.error('Error:', error);
    }
}

main();
