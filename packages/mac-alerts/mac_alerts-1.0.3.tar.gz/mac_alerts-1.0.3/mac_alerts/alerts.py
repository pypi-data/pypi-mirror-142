from os import system 


def play_notication():
	system(f'afplay /System/Library/Sounds/Blow.aiff')


def play_warning():
	system(f'afplay /System/Library/Sounds/Ping.aiff')


def play_success():
	system(f'afplay /System/Library/Sounds/Funk.aiff')


def play_error():
	system(f'afplay /System/Library/Sounds/Sosumi.aiff')


def main():
	print('.: THANK YOU FOR USING MAC-ALERTS :.')


if __name__ == '__main__':
	main()