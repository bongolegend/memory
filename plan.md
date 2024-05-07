# Requirements

1. User needs to create memories, which are voice recordings.
2. Memories need to be parsed and stored semantically.
3. User needs to be able to ask questions, which are used to query the memories.
4. User needs an answer to their questions, which are drawn from the memories.
5. User needs the answer to be audio.

# Concepts

## Memories
- A memory is a piece of audio that is turned to text and stored semantically. It can then be queried semantically.
- A memory does not need to be a certain audio or word length. The length of the memory corresponds to the length of a single audio input start/stop from the user.
- Individual memories should be retrievable word for word. The audio of the memories does not need to be retrieved exactly.


## Questions
- A question is an audio input from the user that needs to be responded to.
- To distinguish between a question and a memory, the user will press a different button.
- The app should respond to the question by referencing the memories.