import pygame
from pygame.locals import *
import random
import time
pygame.init()


def writeScorefile():
    # mô tả về việc tạo ra một tệp CSV 
    '''
   Trước tiên, bạn sẽ kiểm tra xem đã có tệp tin điểm số nào tồn tại hay chưa. Bạn có thể làm việc đó bằng cách thử mở tệp tin đó ra. 
   Nếu không mở được tệp, tức là tệp đó không tồn tại và bạn cần tạo một tệp mới. 
   Trong trường hợp này, bạn sẽ tạo một tệp CSV mới và thiết lập tiêu đề cho nó, chẳng hạn như "Tên người chơi, Điểm số". 
   Sau khi tiêu đề đã được viết vào tệp, công việc của bạn coi như hoàn thành. 
   Nếu tệp tin điểm số đã tồn tại, kết thúc quy trình kiểm tra.
    '''
    haveOne = False
    try:                                #Chương trình sẽ mở tệp tin này
        open('ProJect_Pygame_Nhom18/BangBang/tank-game-master/BangTinhDiem.txt', 'r')
        haveOne = True
    finally:
        if not haveOne:                 #Nếu không có tệp tin, chương trình sẽ tạo một tệp mới
        
            scores = open('BangTinhDiem.txt', 'w')   
            scores.write('1,0' + '\n')
            scores.write('2,0' + '\n')
            scores.close()
            scoredata = {}
        ''' 
        Chương trình sẽ mở một tệp tin mới có tên là 'BangTinhDiem.txt' ở chế độ viết ('w'). 
        Sau đó, chương trình sẽ ghi vào tệp tin hai dòng, mỗi dòng chứa một số thứ tự và điểm số, cách nhau bởi dấu phẩy. 
        Cuối cùng, chương trình sẽ đóng tệp tin đó và khởi tạo một từ điển rỗng tên là scoredata để lưu trữ dữ liệu.
        '''    
def player_classes(option,player):
    #Chọn xe tăng
    '''
    Tham số: player1 hoặc player2, tuỳ chọn mà họ đã chọn.
    Không trả về giá trị gì, nhưng những thuộc tính player.sprite được thêm vào.
    Kiểm tra loại xe tăng mà người dùng đã chọn và thêm các thuộc tính tương ứng.
    '''
    if option == 0: #Xe tăng 1 có tốc độ bắn nhanh hơn và di chuyển nhanh hơn, nhưng có lượng máu thấp hơn:

        player.cooldown = 10 #Giảm cooldown để bắn nhanh hơn
        player.health = 3  
        player.speed = 5
        player.pics = ver1 # ảnh dùng cho xe tăng loại 1
        player.image = ver1[0] # Ảnh hiển thị đầu tiên cho xe tăng loại 1

    elif option == 1: #tốc độ bắn và di chuyển chậm, nhưng nhiều máu 
        player.cooldown = 25
        player.health = 6
        player.speed = 3
        player.pics = ver2
        player.image = ver2[0]

def movement(player):
    #Hàm này dùng để di chuyển, có thể áp dụng cho cả hai người chơi.
    #Lớp sprites từ pygame làm điều này có thể, tiết kiệm không gian và sức mạnh xử lý.
    '''
    :param player: player1 hoặc player2,
    :return: không trả về gì, nhưng giúp di chuyển các sprite của người chơi quanh bản đồ.
    Di chuyển:
    Tùy thuộc vào các phím được thiết lập cho di chuyển trên sprite của người chơi,nếu
    một trong những phím đó được bấm, giá trị left hoặc top của đối tượng sprite sẽ được tăng lên
    với tốc độ nhất định, dựa vào lớp xe tăng của họ. Hướng di chuyển của người chơi được thiết lập dựa trên phím được bấm,
    và hình ảnh của sprite thay đổi để phù hợp với chuyển động.

    Nhận diện va chạm:
    Nếu sprite va chạm với bất cứ thứ gì trong nhóm sprite "players" hoặc với các khối tường trên bản đồ,
    tùy thuộc vào hướng của sprite lúc đó, vị trí giá trị left hoặc top của nó sẽ được giảm đi bằng
    với giá trị tốc độ, cơ bản là khiến cho chiếc xe tăng đứng yên khi nó va chạm với người chơi khác hoặc tường.
    '''
    key = pygame.key.get_pressed()
    #tạo ra một cơ chế di chuyển liên tục cho sprite mà không bị gián đoạn khi người chơi giữ phím 
    # đồng thời đề cập đến cách xử lý va chạm để ngăn sprite không di chuyển qua các vật thể khác.


    if key[player.keys[0]]:
        player.rect.left -= player.speed # Di chuyển sprite sang trái theo tốc độ đã định
        player.direction = 'left' # Cập nhật hướng di chuyển của sprite
        player.image = player.pics[3] # Cập nhật hình ảnh của sprite để phản ánh hướng di chuyển sang trái


    elif key[player.keys[1]]:
        player.rect.left += player.speed
        player.direction = 'right'
        player.image = player.pics[2]

    elif key[player.keys[2]]:
        player.rect.top -= player.speed
        player.direction = 'up'
        player.image = player.pics[0]

    elif key[player.keys[3]]:
        player.rect.top += player.speed
        player.direction = 'down'
        player.image = player.pics[1]


    if len(pygame.sprite.spritecollide(player,players,False))> 1 or pygame.sprite.spritecollide(player,walls,False):
    #trương hợp "player" - đối tượng người chơi - nằm trong nhóm sprite "players"
    #chúng ta cần kiểm tra xem có va chạm với đối tượng khác trong nhóm hay không bằng cách xem độ dài của danh sách va chạm có lớn hơn 1 không.
    #Điều này có nghĩa là đã có va chạm với một "player" khác.
    #Hàm collidelist sẽ trả về -1 nếu không có va chạm nào, vậy nên, nếu giá trị trả về không phải là -1, điều đó cho biết "player" đã va chạm vào một khối "wall tile".
    

        if player.direction == 'left':
            player.rect.left += player.speed
        if player.direction == 'right':
            player.rect.left -= player.speed
        if player.direction == 'up':
            player.rect.top += player.speed
        if player.direction == 'down':
            player.rect.top -= player.speed

def drawPlayerHealth(player):
    #Hàm này cập nhật và vẽ số máu của người chơi khi ở chế độ chiến đấu
    '''
    Sử dụng một vòng lặp for trong khoảng của lượng máu còn lại của người chơi, mỗi điểm máu sẽ được vẽ một trái tim.
   - Vị trí của các trái tim thay đổi tùy thuộc vào người chơi nào,
   - Nếu là người chơi 1, các trái tim sẽ được vẽ ở góc dưới bên trái của màn hình.
   - Nếu là người chơi 2, các trái tim sẽ được vẽ ở góc dưới bên phải của màn hình.
    '''
    healthimage = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/blood.png')
    
    p1healthpos = [60, 500]                                 #Vị trí ban đầu của trái tim của người chơi 1
    p1title = my_font4.render('P1', True, (255,0,0))
    p2healthpos = [520,500]
    p2title = my_font4.render('P2', True, (0,0,255))        #Vị trí ban đầu của trái tim của người chơi 2
    
    screen.blit(p1title, (35, 500)) # vị trí player1 được đặt lúc vô trận, tọa độ x là 35 và y là 500 trên màn hình, thường thì đây là góc dưới bên trái.
    screen.blit(p2title, (495, 500)) # Khi giá trị của tọa độ x tăng, đối tượng di chuyển sang bên phải; tọa độ y tăng,di chuyển xuống dưới.
    for c in range(player.health):
        if player == player1:
            screen.blit(healthimage,p1healthpos)
            p1healthpos[0] += 15
        else:
            screen.blit(healthimage, p2healthpos)
            p2healthpos[0] += 14
    '''
    - Nếu player là player1, máu được vẽ tại vị trí p1healthpos trên màn hình. 
      Với mỗi lần máu được đặt tọa độ x (vị trí ngang) của p1healthpos tăng lên 15, điều này đảm bảo rằng cục máu tiếp theo 
      sẽ được đặt ngay cạnh nhau mà không chồng lấn lên biểu tượng trước đó.
    
    '''
            
def bullet(player):
    #function that generate a bullet sprite, sets the size, color, and bullet's postion
    '''
    :param player: player 1 or 2
    :return: nothing, but bullet sprite will be generated
    function will be triggered by players pressing their fire key
    if so, a bullet will be created, it's postion is oriented away from the player postion
    at the end, add the bullet to the bulletgroup
    '''
    bullet = pygame.sprite.Sprite()

    bullet.image = pygame.Surface((10,10))
    bullet.image.fill((0,0,0))
    bullet.rect = pygame.Rect(bullet.image.get_rect())
    bullet.direction = player.direction

    if bullet.direction == 'up':                                                #bullets postions should be facing the direction of the player is facing
        bullet.rect.x, bullet.rect.y = player.rect.x + 5, player.rect.y - 15    #there need to be distance between them 
    elif bullet.direction == 'down':
        bullet.rect.x, bullet.rect.y = player.rect.x + 5, player.rect.y + 24
    elif bullet.direction == 'left':
        bullet.rect.x, bullet.rect.y = player.rect.x - 15, player.rect.y + 5
    elif bullet.direction == 'right':
        bullet.rect.x, bullet.rect.y = player.rect.x + 24, player.rect.y + 5

    bulletgroup.add(bullet)

def bullet_update():
    #updates the bullet's postion
    '''
    :param None
    :return None, however the bullets position will be changed
    update the bullets every cycle, change bullet's x,y to animate the movement
    '''
    for bullet in bulletgroup:
        if bullet.direction == 'left':
            bullet.rect.x -= 6
        elif bullet.direction == 'right':
            bullet.rect.x += 6
        elif bullet.direction == 'up':
            bullet.rect.y -= 6
        elif bullet.direction == 'down':
            bullet.rect.y += 6

def readMap():
    #a function that turn CVS files into iterable lists so tiles can be added according to the info
    #stored in the txt files. Each tile is one sprite in the walls group
    '''
    parameters: None
    return: None, however, a group of sprites r generated
    randomly chooses a map to read, break each line in the cvs file, each seperated dot means a tile needs to be
    created. Gives the tile a image and rect, add the tile to the group
    '''
    Map = open(random.choice(maps), 'r')
    
    x = 0
    y = 0
    
    for l in Map:
        builtup = l.split(',')
        builtup[-1] = builtup[-1].strip('\n')
        for D in builtup:
            if D == '.':
                tile = pygame.sprite.Sprite()
                tile.image = tiles
                tile.rect = pygame.Rect(x, y, 11, 11)       
                walls.add(tile)                     #for every line in the file is one coloumn of the map
                y += 11                               #y coords value increases by 11 becaus the tile image size is 11 by 11
            else:
                y += 11
        x += 11                               #add 11 to x to start on the next coloumn
        y = 0
           
    Map.close()
   
def gameMenu(thisStage):
    #shows the game menu, for pseudocode plz see above
    '''
    parameters: thisStage varible, if it is true, function executes, otherwise, function will not be triggered
    return: none
    '''
    global run, selecting, battling, end     #needs to be global because the change to these variable here are local changes
                                             #global update the changes outside of this funciton. This is ok because every varibale here are already globle                                             #variables
    pygame.mixer.music.load(musicList[0])    #variables
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    
    Title = my_font.render('Tank2P', True, (255, 0, 0)) #màu đỏ
    text_rect = Title.get_rect(center=(screen.get_width() / 2, screen.get_height() / 4))  # giả sử bạn muốn chữ ở vị trí y = 100

    # Vẽ dòng chữ lên màn hình
    screen.blit(Title, text_rect)

    Start_label = my_font2.render('Start Game', True, (212,212,212))
    Exit_label = my_font2.render('Exit Game', True, (212,212,212))
    
    Srect = Rect(210,280, 421, 339)         #rects here are used to see if the mouse coords are in them
    Erect = Rect(245, 340, 380, 430)
        
    while thisStage:
            
            x, y = pygame.mouse.get_pos()
            Opt = 0                                              #Opt means options, this variable smooth out the rendering and event tracking
            
            if Srect[0] < x <Srect[2] and Srect[1] < y < Srect[3]:
                my_font2.set_underline(True)
                Start_label = my_font2.render('Start Game', True, (212,212,212))
                
                screen.blit(Start_label, (210,280))
                pygame.display.flip()

                Opt = 1                                                          #if the mouse is over the titles 
                                                                                 #underline the titles,(a cool effect)
            elif Erect[0] < x < Erect[2] and Erect[1] < y < Erect[3]:           

                my_font2.set_underline(True)
                Exit_label = my_font2.render('Exit Game', True, (212,212,212))
        
                screen.blit(Exit_label, (220, 340))
                pygame.display.flip()
                
                Opt = 2
                
            my_font2.set_underline(False)
            Start_label = my_font2.render('Start Game', True, (255,212,212))
            Exit_label = my_font2.render('Exit Game', True, (212,212,212))

            screen.blit(screenPIC, (0,0))
            screen.blit(Title, (175,100))
            screen.blit(Start_label, (200,280))                 #bliting the labels
            screen.blit(Exit_label, (200, 340))
            pygame.display.flip()
            
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    pygame.mixer.music.stop()
                    run = False
                    starting = False
                    selecting = False
                    battling = False
                    end = False
                    thisStage = False
                    
                elif ev.type == MOUSEBUTTONDOWN:
                    if Opt == 1:
                        pygame.mixer.music.stop()
                        starting = False
                        thisStage = False
                    elif Opt == 2:
                        pygame.mixer.music.stop()
                        run = False
                        starting = False
                        selecting = False
                        battling = False
                        end = False
                        thisStage = False

def selectionScreen(thisStage):
    #shows selection menu, pseudocode are show at the begining
    '''
    parameters: thisStage variable, needs to be true to execute the function
    return: none, but updates the player tank class and readMap() to prepare to 1v1 battle
    '''
    global run, selecting, battling, end                      #needs to be global because the change to these variable here are local changes
                                                            #global update the changes outside of this funciton.
    pygame.mixer.music.load(musicList[1])    
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    Opt1 = 0
    Opt2 = 0                                   #Opt1 for player1 options, Opt2 for player 2 options
    
    instructionP1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/instruction2.png')           #pics with player controls, help users learn the controls of their tanks
    instructionP2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/instruction1.png')
    
    Title = my_font3.render('Game Instructions', True, (9,225,242))
    p1Title = my_font4.render('P1', True, (255,255,0)) #chữ màu vàng nền trong suốt
    p2Title = my_font4.render('P2', True, (255,255,0))
    
    instruction = my_font4.render('Use your left and right controls to switch between tanks.', True, (255,255,0))
    instruction2 = my_font4.render('Press ENTER to start the battle !', True, (255,255,0))

    options = [imageUp_v1,imageUp_v2]                  #actual options and their stats, this helps rendering/bliting when user switch the tanks
    stats = {0:['3', '5', '3'], 1:['5','3','1']}
    
    DisplaySurf = pygame.Surface((100,100))
    DisplaySurf.fill((255,255,255))                 #white surface, create contrast between tanks and background, easy for user to see tank differences
    DisplaySurf2 = pygame.Surface((100,100))
    DisplaySurf2.fill((255,255,255))
    
    while thisStage:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.mixer.music.stop()
                run = False
                selecting = False
                battling = False
                end = False
                thisStage = False
            elif ev.type == KEYDOWN:
                if ev.key == K_RETURN:
                    pygame.mixer.music.stop()
                    readMap()
                    player_classes(Opt1, player1)
                    player_classes(Opt2, player2)
                    selecting = False
                    thisStage = False
                elif ev.key == K_a: 
                    if Opt1 == 0:
                        Opt1 = 1                                   #long nest if states are unavoidable, since inputs are meant for 2 users
                    else:
                        Opt1 -= 1
                elif ev.key == K_d:
                    if Opt1 == 1:
                        Opt1 = 0
                    else:
                        Opt1 += 1
                elif ev.key == K_LEFT:
                    if Opt2 == 0:
                        Opt2 = 1
                    else:
                        Opt2 -= 1
                elif ev.key == K_RIGHT:
                    if Opt2 == 1:
                        Opt2 = 0
                    else:
                        Opt2 += 1
                        
        p1statsHealth = my_font5.render('Health: ' + stats[Opt1][0], True, (212,212,212))
        p1statsSpeed = my_font5.render('Speed: ' + stats[Opt1][1],True, (212,212,212))
        p1statsReload = my_font5.render('Reload: ' + stats[Opt1][2], True, (212,212,212))   #these renders needs to be in the loop because as users switch
        p2statsHealth = my_font5.render('Health: ' + stats[Opt2][0], True, (212,212,212))   #between tanks, the stats info needs to update
        p2statsSpeed = my_font5.render('Speed: ' + stats[Opt2][1],True, (212,212,212))
        p2statsReload = my_font5.render('Reload: ' + stats[Opt2][2], True, (212,212,212))
        
        screen.blit(screenPIC, (0,0))
        screen.blit(Title, (70, 70)) # tọa độ dòng chữ Game Insruction

        screen.blit(p1Title, (160, 150))
        screen.blit(p2Title, (420, 150))

        screen.blit(p1statsHealth, (45,200)) #tọa độ chỉ số máu, tốc độ của player1
        screen.blit(p1statsSpeed, (45,220))  #tọa độ chỉ số máu, tốc độ của player1
        screen.blit(p1statsReload, (45,240)) #tọa độ chỉ số máu, tốc độ của player1

        screen.blit(p2statsHealth, (500,200)) #tọa độ chỉ số máu, tốc độ của player2
        screen.blit(p2statsSpeed, (500,220)) #tọa độ chỉ số máu, tốc độ của player2
        screen.blit(p2statsReload, (500,240)) #tọa độ chỉ số máu, tốc độ của player2

        screen.blit(DisplaySurf, (120, 180))
        screen.blit(DisplaySurf2, (380, 180))
        screen.blit(options[Opt1], (158, 238))
        screen.blit(options[Opt2], (418, 238))

        screen.blit(instructionP1, (70, 290))
        screen.blit(instructionP2, (330, 290))

        screen.blit(instruction, (70, 500)) #tọa độ của dòng chữ Use your left and right controls to switch between tanks
        screen.blit(instruction2, (170, 520))
        pygame.display.flip()
    
def battleScreen(thisStage):
    #blits the battle, test out sprite collisions, pseudocode are show at the begining
    '''
    parameters: thisStage, needs to be True to execute the function,
    return: None, animates the game interaction
    '''
    global run, end         #needs to be global because the change to these variable here are local changes
                            #global update the changes outside of this funciton.
    pygame.mixer.music.load(musicList[2])    
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    timer = 0
    timer2 = 0
    
    while thisStage:
        fps = clock.tick(30)        
        timer += 1
        timer2 += 1
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.mixer.music.stop()
                run = False
                battling = False
                thisStage = False
                end = False
                
        movement(player1)               #governs the player movement, as well as collision with each other and walls
        movement(player2) 
        bullet_update()
        key = pygame.key.get_pressed()

        if key[player1.keys[4]]:
            if timer >= player1.cooldown:
                shoot.play()
                bullet(player1)
                timer = 0

        if key[player2.keys[4]]:
            if timer2 >= player2.cooldown:
                shoot.play()
                bullet(player2)
                timer2 = 0
                
        for bullets in bulletgroup:
            if pygame.sprite.collide_rect(bullets,player1):
                bulletgroup.remove(bullets)
                player1.health -= 1
                explode.play()
                screen.blit(explosion, player1.rect)
                pygame.display.flip()
                time.sleep(1)
                player1.rect.center = spawnpoints[random.randint(0,2)]
                
            if pygame.sprite.collide_rect(bullets,player2):
                bulletgroup.remove(bullets)
                player2.health -= 1
                explode.play()
                screen.blit(explosion, player2.rect)
                pygame.display.flip()
                time.sleep(1)
                player2.rect.center = spawnpoints[random.randint(0,2)]
            if pygame.sprite.spritecollide(bullets,walls,False):
                explode.play()
                bulletgroup.remove(bullets)
            if len(pygame.sprite.spritecollide(bullets,bulletgroup, False))>1:
                pygame.sprite.spritecollide(bullets,bulletgroup, True)


        screen.blit(background, (0,0))
        walls.draw(screen)
        players.draw(screen)
        bulletgroup.draw(screen)
        drawPlayerHealth(player1)
        drawPlayerHealth(player2)
        pygame.display.flip()
        pygame.display.update()
        
        if player1.health == 0 or player2.health == 0:
            pygame.mixer.music.stop()
            battling = False
            thisStage = False
            endScreen(end)

            
def endScreen(thisStage):
    #determines the winner, calculate scores, shows the end screen, as well as clean up, pseudocode are show at the begining
    '''
    parameters: thisStage, needs to be true to execute this function
    returns: None
    '''
    global run, starting, selecting

    pygame.mixer.music.load(musicList[3])    
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    bulletgroup.empty()     #delete all remaining bullets 
    walls.empty()               #delete tiles since map will be redrawn

    scores = open('ProJect_Pygame_Nhom18/BangBang/tank-game-master/BangTinhDiem.txt', 'r')
    for l in scores:
        dataFields = l.split(',')
        dataFields[-1] = dataFields[-1].strip('\n')
        scoredata[dataFields[0]] = int(dataFields[1])               #read the score cvs file, update scoredata
    scores.close()
    
    winner = max(player1.health,player2.health)     #use remaining health to determine the winner
    
    if winner == player1.health:
            WinnerTitle =  my_font2.render('PLAYER 1 WINS', True, (212,212,212))
            scoredata['1'] +=1                                                      #whoever wins gets 1 point
    else:
            WinnerTitle = my_font2.render('PLAYER 2 WINS', True, (212,212,212))
            scoredata['2'] +=1

    scores = open('ProJect_Pygame_Nhom18/BangBang/tank-game-master/BangTinhDiem.txt', 'w')
    scores.write('1,' + str(scoredata['1']) + '\n')         #record the win
    scores.write('2,' + str(scoredata['2']) + '\n')
    scores.close()
            
    Title = my_font3.render('GAME OVER', True, (255,0,0))
    scoreTitle = my_font2.render('Scores', True, (212,212,212))
    instruction = my_font4.render('Press r to reset scores!', True, (175,44,33))
    instruction2 = my_font4.render('Press enter to return to game menu.', True, (175,44,33))

    while thisStage:
        p1Scores = my_font2.render('Player 1:  ' +str(scoredata['1']), True, (255,255,255))
        p2Scores = my_font2.render('Player 2:  '+ str(scoredata['2']), True, (255,255,255))

        screen.blit(screenPIC, (0,0))
        screen.blit(Title, (120,50))
        screen.blit(WinnerTitle, (165,200))
        screen.blit(scoreTitle, (245,280))
        screen.blit(p1Scores, (60,340))
        screen.blit(p2Scores, (350,340))
        screen.blit(instruction, (230, 480))
        screen.blit(instruction2, (170,500))
        pygame.display.flip()
        
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.mixer.music.stop()
                run = False
                end = False
                thisStage = False
            elif ev.type == KEYDOWN:
                if ev.key == K_RETURN:
                    pygame.mixer.music.stop()
                    thisStage = False
                elif ev.key == K_r:
                    scoredata['1'] = 0        #reset the scores if one player gets mad and wants to restart all over
                    scoredata['2'] = 0

    scores = open('ProJect_Pygame_Nhom18/BangBang/tank-game-master/BangTinhDiem.txt', 'w')
    scores.write('1,' + str(scoredata['1']) + '\n')
    scores.write('2,' + str(scoredata['2']) + '\n')         #final recording and updating just to be safe
    scores.close()
        
    starting = True
    selecting = True
    
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
clock = pygame.time.Clock()

colours = pygame.color.THECOLORS
my_font = pygame.font.SysFont('impact', 120)
my_font2 = pygame.font.SysFont('moolboran', 66)
my_font3 = pygame.font.SysFont('andalus', 72)      #fonts setup
my_font4 = pygame.font.SysFont('candara', 20)
my_font5 = pygame.font.SysFont('arial', 16)

size = (605, 540)
screen = pygame.display.set_mode(size)
screenPIC = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/anhnen.png')
pygame.display.set_caption("Tank Moba PvP")              #screen setup
background = pygame.Surface(size)
background = background.convert()
background.fill(colours['grey']) #màu nền của map trong game

explode = pygame.mixer.Sound('ProJect_Pygame_Nhom18/BangBang/tank-game-master/explosion.ogg')
shoot = pygame.mixer.Sound('ProJect_Pygame_Nhom18/BangBang/tank-game-master/fire.ogg')          #sound effects and music
musicList = ['ProJect_Pygame_Nhom18/BangBang/tank-game-master/menuSong.ogg','ProJect_Pygame_Nhom18/BangBang/tank-game-master/selectSong.ogg','ProJect_Pygame_Nhom18/BangBang/tank-game-master/battleSong.ogg','BangBang/tank-game-master/endSong.ogg']

maps = ['ProJect_Pygame_Nhom18/BangBang/tank-game-master/map1.txt', 'ProJect_Pygame_Nhom18/BangBang/tank-game-master/map2.txt', 'ProJect_Pygame_Nhom18/BangBang/tank-game-master/map3.txt']
tiles = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/tile.png')

explosion = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/vuno.png')
imageUp_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/ver1 up.png')
imageDown_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/ver1 down.png')
imageRight_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/ver1 right.png')     #load images for the tanks
imageLeft_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/ver1 left.png')

imageUp_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/ver2 up.png')
imageDown_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/ver2 down.png')
imageRight_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/ver2 right.png')
imageLeft_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/tank-game-master/ver2 left.png')

ver1 = [imageUp_v1,imageDown_v1,imageRight_v1,imageLeft_v1]
ver2 = [imageUp_v2,imageDown_v2,imageRight_v2,imageLeft_v2]
spawnpoints = [(30,30),(40,390),(560,130),(560,390)]                

#pygame.sprite is very useful for organizing and storing info
players = pygame.sprite.Group()

player1 = pygame.sprite.Sprite()
player1.rect = pygame.Rect((20, 20),(24,24))                        #rect is used for collision detection
player1.direction = 'up'                                            #starting position is up
player1.keys = (K_a, K_d, K_w, K_s,K_4)                             #stores the keys needed to use

player2 = pygame.sprite.Sprite()
player2.rect = pygame.Rect((560, 390), (24,24))
player2.direction = 'up'
player2.keys = (K_LEFT, K_RIGHT, K_UP, K_DOWN,K_l)

players.add(player1)
players.add(player2)

bulletgroup = pygame.sprite.Group()
walls = pygame.sprite.Group()                       #create the group for bullets and tiles

            
run = True
starting = True                     #control variables for functions and loops
selecting = True
battling = True
end = True


writeScorefile()
scoredata = {}

while run:
    fps = clock.tick(30)

    gameMenu(starting)
    selectionScreen(selecting)
    battleScreen(battling)
    
   

pygame.display.quit()
quit()

