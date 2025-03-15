import socket
import threading
from twofa_email import send_2fa_email

nickname = input('Choose a nickname: ')
email = input('Choose your email for Two-Factor code: ')

send_2fa_email(email)

TWO_FACTOR_AUTH = input('Please put in the 5-Digit Two Factor Authentication Code to login: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55356))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            elif message == '2FA_CODE':
                client.send(f'2FA:{TWO_FACTOR_AUTH}'.encode('ascii'))
            else:
                print(message)
        except Exception as e:
            print(f"An error occurred: {e}")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
