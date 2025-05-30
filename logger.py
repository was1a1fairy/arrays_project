def log_action(message):
    file = open('data.txt', 'a')
    file.write(message)
    file.write('\n')