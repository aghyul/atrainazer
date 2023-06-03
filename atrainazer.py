import requests

def is_phishing(url):
    payload = {
        'url': url,
        'submit': 'Check'
    }

    response = requests.post('https://isitphishing.org/verify.php', data=payload)

    if 'legitimate site' in response.text:
        return False
    elif 'phishing site' in response.text:
        return True
    else:
        return None

def verify_single_site():
    site_url = input("Enter the URL of the site to verify: ")
    result = is_phishing(site_url)

    if result is None:
        print("Unable to determine if the site is a phishing attempt.")
    elif result:
        print("The site is a phishing attempt.")
    else:
        print("The site is legitimate.")

def verify_multiple_sites():
    file_path = input("Enter the path of the file containing the links (e.g., links.txt): ")

    try:
        with open(file_path, 'r') as file:
            links = file.readlines()

        for link in links:
            link = link.strip()
            result = is_phishing(link)
            print(f"{link} - {result}")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def menu():
    print("=== Phishing Verification ===")
    print("=== V 1.0  ===")
    print("1. Verify a single site")
    print("2. Verify multiple sites from a file")
    print("3. Quit")

    choice = input("Choose an option (1, 2, or 3): ")

    if choice == '1':
        verify_single_site()
        menu()
    elif choice == '2':
        verify_multiple_sites()
        menu()
    elif choice == '3':
        print("Thank you for using the program!")
    else:
        print("Invalid option. Please choose again.")
        menu()

# stealing few lines of code doesn't make you programmer but a noobcoder :D 
#im joking just take the code little kid its Gift For your mom :P
menu()
