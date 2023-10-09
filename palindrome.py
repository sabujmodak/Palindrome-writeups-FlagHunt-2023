import socket

# Define the server IP address and port
server_ip = "45.76.177.238"
server_port = 5000

# Create a socket connection to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((server_ip, server_port))

        # Loop to read and process each query
        for i in range(1000):
            # Receive the string query from the server
            if i == 0:
            	data = s.recv(1024).decode()
            # data = input("Enter your value: ")
            # print(data)

            # Extract the string after ":" and remove leading/trailing spaces
            string_parts = data.split(": ")
            if len(string_parts) != 2:
                print("Invalid data format:", data)
                break

            string_to_check = string_parts[1].strip()
            # print("string_to_check: " + string_to_check)

            # Check if the input string is not empty
            if string_to_check:
                # Function to find the minimum number of characters to make a string palindrome
                def min_changes_to_palindrome(s):
                    left = 0
                    right = len(s) - 1
                    changes = 0

                    while left < right:
                        if s[left] != s[right]:
                            changes += 1
                        left += 1
                        right -= 1

                    return changes

                # Calculate the minimum changes needed to make the string palindrome
                min_changes = min_changes_to_palindrome(string_to_check)

                # Print the result instead of sending it back to the server
                s.sendall(f"{min_changes}\n".encode())
                # print(f"{min_changes}")

                # Receive and print the server's response (e.g., "Good^^")
                response = s.recv(1024).decode()
                print(response)
                data = response

                # Check if we've received the flag and exit the loop
                if "CTF_BD" in response:
                    print("Flag received, exiting loop.")
                    break
            else:
                print("Empty string received, exiting loop.")
                break
    except OSError as e:
        print(f"Socket error: {e}")
