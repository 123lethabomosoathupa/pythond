# 8-9. Messages
print("\n\tExercise 8.9\n")
def show_messages(messages):
    for message in messages:
        print(message)

messages = [
    "Hello there!",
    "Python is awesome.",
    "Keep learning every day."
]

print("Showing all messages:")
show_messages(messages)

# 8-10. Sending Messages
print("\n\tExercise 8.10\n")
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)  # remove from the start
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

sent_messages = []
print("\nSending and moving messages to sent_messages:")
send_messages(messages, sent_messages)

print("\nOriginal messages list after sending:", messages)
print("Sent messages list:", sent_messages)

# 8-11. Archived Messages
print("\n\tExercise 8.11\n")
print("\n--- Archived Messages Example ---")
messages = [
    "Welcome to the team!",
    "Don't forget the meeting.",
    "Have a great day!"
]

sent_messages = []
send_messages(messages[:], sent_messages)  # pass a copy of the list

print("\nOriginal messages list (should be unchanged):", messages)
print("Sent messages list from copy:", sent_messages)
