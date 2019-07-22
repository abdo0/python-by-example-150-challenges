tv_program = ['GOT', 'Prison Break', 'Supernatural', 'Chernobyl ']
for i in tv_program:
    print(i)
ask_name = str(input('Enter a name of show you want to add to list : '))
ask_position = int(input('Enter position of entered show in  list : '))
tv_program.insert(ask_position, ask_name)
for i in tv_program:
    print(i)
