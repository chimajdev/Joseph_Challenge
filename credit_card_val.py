def checking(num):
    if not num.startswith(('4', '5', '6')):
        return 'Invalid', 'Starting number'
    count = 0
    check_sep = False
    only_num = ''
    for i in range(len(num)-1):
        if not num[i].isdigit():
            if num[i] == '-':
                check_sep = True
                continue
            else:
                return 'Invalid', 'Non-supported caharacter'
        else:
            only_num += num[i]

    for i in range(len(only_num)-1):
        if only_num[i] == only_num[i+1]:
            count += 1
            if count >= 4:
                return 'Invalid', 'Repeat number'
        else:
            count = 1

    if num[-1].isdigit():
        only_num += num[i]

    if len(only_num) != 16:
        return 'Invalid', 'total length ' + str(len(only_num))
    if check_sep and not all([len(i) == 4 for i in num.split('-')]):
        return 'Invalid', '4 separator '
    return ('Valid',)


for i in range(int(input())):
    print(checking(input())[0])
