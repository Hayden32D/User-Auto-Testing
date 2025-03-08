import time

def print_hello_world():
    alphabet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()<>?[]{}/?|'
    target = "hi"
    result = ""

    for char in target:
        for letter in alphabet:
            print(result + letter, end='\r', flush=True)  # Print the current iteration
            time.sleep(0.05)  # Adding a small delay to visualize the search
            if letter == char:
                result += letter
                print(result)  # Print the partial result after finding the correct letter
                break

    print(result)  # Finally, print the complete "Hello world!"

# Uncomment the line below to run the function
print_hello_world()