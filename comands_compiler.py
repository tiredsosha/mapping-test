with open('mouse.txt', 'w') as mousetxt: # open/make file where comands will be write out

    with open('mouse.mmmacro') as comands: # open mouse macros
        comands = comands.readlines()
        for line in comands:
            line = line.split('|')

            if line[4] == ' Left Click Down\n':
                x_start, y_start = line[1], line[2]
            elif line[4] == ' Keypress tab\n':
                mousetxt.writelines('tab\n')
            elif line[4] == ' Left Click Release\n':
                x_end, y_end = line[1], line[2]

                # write click and moves
                if x_start == x_end:
                    mousetxt.writelines(f'click {x_end.strip()} {y_end.strip()}\n')
                elif x_start != x_end:
                    mousetxt.writelines(f'move {x_start.strip()} {y_start.strip()} {x_end.strip()} {y_end.strip()}\n')

print('done\ncommands are in mouse.txt')
