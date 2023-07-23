import hashlib

# def calculate_hash(sender, recipient, subject, message, nonce, difficulty):
#     attempts = 0
#     data = sender + recipient + subject + message + str(nonce)

#     while True:
#         attempts += 1
#         hash_value = hashlib.sha256(data.encode()).hexdigest()

#         if hash_value[:difficulty] == "f" * difficulty:
#             return hash_value, attempts

#         nonce += 1
#         data = sender + recipient + subject + message + str(nonce)

# # Example usage:
# sender_email = input("Enter sender's email address: ")
# recipient_email = input("Enter recipient's email address: ")
# subject = input("Enter email subject: ")
# message = input("Enter message body: ")
# nonce = int(input("Enter nonce: "))

# difficulty_level_1 = 2
# difficulty_level_2 = 4

# hash_value_1, attempts_1 = calculate_hash(sender_email, recipient_email, subject, message, nonce, difficulty_level_1)
# hash_value_2, attempts_2 = calculate_hash(sender_email, recipient_email, subject, message, nonce, difficulty_level_2)

# print("Difficulty Level 1:")
# print("Hash value:", hash_value_1)
# print("Attempts:", attempts_1)

# print("\nDifficulty Level 2:")
# print("Hash value:", hash_value_2)
# print("Attempts:", attempts_2)