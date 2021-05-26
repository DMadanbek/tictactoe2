board = list(range(1,10))
player1=input('Кто х?:')
player2=input('Кто 0?')
def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    prosto = False
    while not prosto:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print (" Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                prosto = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print (" Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                nado=(tmp)
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

    file = open('winhistoryfile.txt', 'a+',encoding='utf-8')# я создал файл txt
    winner=check_win(board)


    winhistory = input('хотите сохранить игру?:')

    if winhistory == 'Y':
        file = open('winhistoryfile.txt', 'a+', encoding='utf-8')
        file.write(player1 + '-' + player2 + '|' + winner)
        file.write(',')
    if winhistory=='N':
        print('Ok')
    check_history=input('хотите посмотреть историю?')
    if check_history == 'Y':
        print(file.read(6))

    if check_history=='N':
        print('ладно')




main(board)