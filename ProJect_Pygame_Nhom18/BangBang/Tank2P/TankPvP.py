import pygame
from pygame.locals import *
import random
import time
pygame.init()

################################################ SET UP BẢNG TÍNH ĐIỂM SAU TRẬN ĐẤU #########################################################################
def writeScorefile():
    # mô tả về việc tạo ra một tệp
    '''
   Để bắt đầu, nhóm sẽ kiểm tra xem có tệp điểm số nào tồn tại bằng cách thử mở nó. 
   Nếu không thể mở tệp, cho thấy tệp đó không tồn tại, nhóm sẽ tạo một tệp mới. 
   Trong trường hợp này, tệp mới sẽ được tạo ra và được đặt tiêu đề như "Tên Người Chơi, Điểm Số". 
   Nếu tệp điểm số đã tồn tại, quá trình kiểm tra sẽ kết thúc.
    '''
    haveOne = False
    try:                                #Chương trình sẽ mở tệp tin này
        open('ProJect_Pygame_Nhom18/BangBang/Tank2P/BangTinhDiem.txt', 'r')
        haveOne = True
    finally:
        if not haveOne:                 #Nếu không có tệp tin, chương trình sẽ tạo một tệp mới
        
            scores = open('BangTinhDiem.txt', 'w')   
            scores.write('P1,0' + '\n')
            scores.write('P2,0' + '\n')
            scores.close()
            scoredata = {}
        ''' 
        Chương trình sẽ mở tệp 'BangTinhDiem.txt', sau đó ghi hai dòng vào tệp, mỗi dòng chứa số thứ tự và điểm số cách nhau bởi dấu phẩy. 
        Sau khi ghi, tệp sẽ được đóng và một từ điển rỗng có tên là scoredata sẽ được khởi tạo để lưu trữ dữ liệu.
        '''  
############################################## SET UP CHỈ SỐ TANK ####################################################################################################  
def player_classes(option,player):
    '''
    Để thêm thuộc tính vào player.sprite dựa trên loại xe tăng mà người dùng đã chọn (player1 hoặc player2), 
    chương trình sẽ kiểm tra loại xe tăng đó và thêm các thuộc tính tương ứng. 
    Điều này sẽ giúp xác định các đặc điểm cụ thể của từng loại xe tăng và áp dụng chúng vào sprite của người chơi.
    '''
    if option == 0: #tank 1 có tốc độ bắn và di chuyển nhanh hơn, nhưng có lượng máu thấp hơn

        player.cooldown = 30 #Giảm cooldown để bắn nhanh hơn
        player.health = 3  
        player.speed = 5
        player.pics = ver1 # ảnh dùng cho xe tăng loại 1
        player.image = ver1[0] # Ảnh hiển thị đầu tiên cho xe tăng loại 1

    elif option == 1: #tank 2 có tốc độ bắn và di chuyển chậm, nhưng nhiều máu 
        player.cooldown = 45
        player.health = 6
        player.speed = 3
        player.pics = ver2
        player.image = ver2[0]

############### xử lý đầu vào từ bàn phím để di chuyển tank theo các hướng, ngăn tank đi xuyên tường, đi xuyên player khác #######################
def movement(player):
    
    '''
   Di chuyển trong trò chơi phụ thuộc vào phím được bấm, va chạm sẽ làm giảm vị trí của sprite để ngăn di chuyển qua các đối tượng khác.
    '''
    key = pygame.key.get_pressed()
    #tạo ra một cơ chế di chuyển liên tục cho sprite mà không bị gián đoạn khi người chơi giữ phím 
    #đồng thời đề cập đến cách xử lý va chạm để ngăn sprite không di chuyển qua các vật thể khác.


    if key[player.keys[0]]:
        player.rect.left -= player.speed # Di chuyển sprite sang trái theo tốc độ đã định
        player.direction = 'left' # Cập nhật hướng di chuyển của sprite
        player.image = player.pics[3] # Cập nhật hình ảnh của sprite khi người chơi hướng di chuyển sang trái


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
    #Trong trường hợp "player" nằm trong nhóm sprite "players", chúng ta cần kiểm tra xem có va chạm với đối tượng khác trong nhóm hay không bằng cách xem độ dài của danh sách va chạm có lớn hơn 1 không. Nếu độ dài này lớn hơn 1, điều này có nghĩa là đã có va chạm với một "player" khác.
    #Hàm collidelist sẽ trả về -1 nếu không có va chạm nào. Vì vậy, nếu giá trị trả về khác -1, điều đó cho biết "player" đã va chạm vào 1 khối tuong.
    

        if player.direction == 'left':
            player.rect.left += player.speed
        if player.direction == 'right':
            player.rect.left -= player.speed
        if player.direction == 'up':
            player.rect.top += player.speed
        if player.direction == 'down':
            player.rect.top -= player.speed

################################### SET UP HIỂN THỊ MÁU CỦA PLAYER TRONG TRẬN CHIẾN ###############################################################################
def drawPlayerHealth(player):
    #Hàm này cập nhật và in số máu của người chơi khi ở chế độ chiến đấu
    '''
    Sử dụng vòng lặp for dựa trên lượng máu còn lại của người chơi để in trái tim.
   - Vị trí của trái tim thay đổi tùy theo người chơi,
   - Nếu là người chơi 1, trái tim in ở góc dưới bên trái.
   - Nếu là người chơi 2, trái tim in ở góc dưới bên phải.
    '''
    healthimage = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/blood.png')
    
    p1healthpos = [60, 500]                                 #set up vị trí máu của Player1 trong trận chiến
    p1title = my_font4.render('P1', True, (0,0,0))           #tạo tiêu đề "chữ P1" với màu tương ứng
    p2healthpos = [520,500]
    p2title = my_font4.render('P2', True, (0,0,255))        
    
    screen.blit(p1title, (35, 500)) # vị trí chữ P1, tọa độ x là 35 và y là 500 trên màn hình, thường thì đây là góc dưới bên trái.
    screen.blit(p2title, (495, 500)) # Khi giá trị của tọa độ x tăng, đối tượng di chuyển sang bên phải; tọa độ y tăng,di chuyển xuống dưới.

    #duyệt số lượng máu của người chơi và hiển thị nó trên màn hình tương ứng với vị trí của người chơi 1 hoặc người chơi 2
    #đồng thời cập nhật vị trí kế tiếp để hiển thị hình ảnh máu tiếp theo
    for c in range(player.health):
        if player == player1:
            screen.blit(healthimage,p1healthpos)
            p1healthpos[0] += 15
        else:
            screen.blit(healthimage, p2healthpos)
            p2healthpos[0] += 14
    '''
    Khi player là player1, máu được in tại vị trí p1healthpos trên màn hình.
    Việc tăng tọa độ x của p1healthpos lên 15 cho mỗi cục máu đảm bảo không có chồng lấn giữa các biểu tượng máu.
    '''

############################################ SET UP ĐẠN ###############################################################       
def bullet(player):
    #Hàm tạo đạn, thiết lập kích thước, màu sắc, và vị trí của đạn.
    '''
    Hàm sẽ tạo ra đạn khi người chơi bắn, dựa vào người chơi là player 1 hoặc 2. Đạn sẽ được tạo ra và bay ra khỏi tank
    '''
    bullet = pygame.sprite.Sprite()

    bullet.image = pygame.Surface((5,5)) #kích thước viên đạn
    bullet.image.fill((255,0,0)) #màu viên đạn
    bullet.rect = pygame.Rect(bullet.image.get_rect()) #tạo hình (Rect) cho đối tượng bullet dựa trên kích thước của bullet.image, xác định vị trí và kích thước của đối tượng bullet
    bullet.direction = player.direction

    #set up vị trí của viên đạn sao cho khi bắn ra nó nằm ở giữa nòng súng tank
    if bullet.direction == 'up':                                                
        bullet.rect.x, bullet.rect.y = player.rect.x + 12, player.rect.y - 20   
    elif bullet.direction == 'down':
        bullet.rect.x, bullet.rect.y = player.rect.x + 12, player.rect.y + 24
    elif bullet.direction == 'left':
        bullet.rect.x, bullet.rect.y = player.rect.x - 20, player.rect.y + 12
    elif bullet.direction == 'right':
        bullet.rect.x, bullet.rect.y = player.rect.x + 24, player.rect.y + 12

    bulletgroup.add(bullet)

def bullet_update():
    #cập nhật vị trí của đạn
    '''
    viên đạn di chuyển theo hướng tương ứng với thuộc tính direction của nó khi viên đạn được bắn ra.
    '''
    for bullet in bulletgroup:
        if bullet.direction == 'left':
            bullet.rect.x -= 6
        elif bullet.direction == 'right':
            bullet.rect.x += 6
        elif bullet.direction == 'up': #Khi viên đạn di chuyển lên trên, nghĩa là nó đang đi ngược với trục y của màn hình, do đó để viên đạn di chuyển lên trên, giá trị của trục y cần phải giảm
            bullet.rect.y -= 6
        elif bullet.direction == 'down':
            bullet.rect.y += 6

######################################## SET UP MAP #######################################################################
def readMap():
    '''
    chọn một map từ tệp, đọc và phân tích từng dòng của nó, nơi mỗi ô trong tệp được phân cách bởi dấu phẩy.
    Khi đọc mỗi ô, phương pháp này gán hình ảnh cho mỗi ô và có thể tiến hành chỉnh sửa ô nếu cần thiết
    '''
    Map = open(random.choice(maps), 'r')
    
    x = 0 #Biến x và y bắt đầu từ giá trị 0 và được dùng để theo dõi vị trí khi xử lý tệp để thêm sprite.
    y = 0

    '''
    tạo ra một bức tường từ các tiles có kích thước 11x11 pixel, biểu diễn bởi các dấu chấm trong tệp đầu vào.
    '''
    for l in Map:   
        builtup = l.split(',') #tách dòng thành một danh sách các chuỗi
        builtup[-1] = builtup[-1].strip('\n') 
        for D in builtup:
            if D == '.':
                tile = pygame.sprite.Sprite()
                tile.image = tiles
                tile.rect = pygame.Rect(x, y, 11, 11)       
                walls.add(tile)                    
                y += 11                              
            else:
                y += 11
        x += 11                             
        y = 0
           
    Map.close()

################################## SET UP MENU GAME#############################################################################   
def gameMenu(thisStage):
    '''
    cải thiện menu game bằng cách đặt nền nhạc, và hiển thị tiêu đề cùng với hai lựa chọn:
    "Start Game" và "Exit Game". Khi người chơi di chuyển chuột qua các label lựa chọn, chúng sẽ được làm nổi bật với màu sắc và dấu gạch dưới.
    Phản ứng của label được cập nhật trực tiếp trên màn hình.
    Sự kiện chuột được quản lý để xử lý việc bắt đầu game hoặc thoát khỏi game phụ thuộc vào label mà người dùng chọn.
    '''
    global run, selecting, battling, end                                                
    pygame.mixer.music.load(musicList[0])    
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    
    Title = my_font.render('Tank PvP', True, (255, 0, 0)) # set up tiêu đề game màu đỏ

    #Mã tạo hình chữ nhật (text_rect) xung quanh Title, canh giữa theo ngang và ở trên màn hình theo dọc, làm Title nổi bật.
    text_rect = Title.get_rect(center=(screen.get_width() / 2, screen.get_height() / 4)) 
    # in dòng chữ lên màn hình
    screen.blit(Title, text_rect)

    Start_label = my_font2.render('Start Game', True, (212,212,212))
    Exit_label = my_font2.render('Exit Game', True, (212,212,212))
    
    Srect = Rect(210,280,421,339)         #hiệu ứng khi trỏ chuột vào
    Erect = Rect(245,340,380,430)
        
    while thisStage:
            
            x, y = pygame.mouse.get_pos()        #định vị trí của chuột trên màn hình
            Opt = 0                                            
            '''
            Nếu vị trí chuột (x, y) nằm trong phạm vi của hình chữ nhật Srect
            tức là vùng mà label "Start Game" chiếm giữ trên màn hình, chữ "Start Game" sẽ được làm nổi bật
            '''
            if Srect[0] < x <Srect[2] and Srect[1] < y < Srect[3]: 
                my_font2.set_underline(True)
                Start_label = my_font2.render('Start Game', True, (255,255,0)) # nháy màu vàng, phần gạch chân cũng vậy
                screen.blit(Start_label, (185,280))
                pygame.display.flip()

                Opt = 1 #biến Opt được đặt thành 1, label "Start Game" đang được chọn. Khi người chơi nhấp chuột, có thể sẽ có sự kiện diễn ra tùy vào giá trị của Opt.                                                      
                                                                                 
            elif Erect[0] < x < Erect[2] and Erect[1] < y < Erect[3]:           

                my_font2.set_underline(True)
                Exit_label = my_font2.render('Exit Game', True, (255,0,0))
                screen.blit(Exit_label, (185, 340))
                pygame.display.flip()
                
                Opt = 2
                
            my_font2.set_underline(False)
            Start_label = my_font2.render('Start Game', True, (212,212,212)) #set up màu cho label Star Game
            Exit_label = my_font2.render('Exit Game', True, (212,212,212))

            screen.blit(screenPIC, (0,0))
            screen.blit(Title, (90,120))  # căn giữa Tank2P
            screen.blit(Start_label, (180,280))                 #tọa độ chuỗi Start Game
            screen.blit(Exit_label, (180, 340))
            pygame.display.flip()
            
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    pygame.mixer.music.stop() #khi đóng cửa sổ game thì hàm được gọi để stop nhạc nền của game
                    run = False
                    starting = False
                    selecting = False 
                    battling = False           #các biến được trả về false để kết thúc các trạng thái, các biến ở dòng 213
                    end = False                
                    thisStage = False
                    
                elif ev.type == MOUSEBUTTONDOWN: #kích hoạt event khi click chuột
                    if Opt == 1:
                        pygame.mixer.music.stop()
                        starting = False      #nếu chọn Start game thì nhạc sẽ dừng, kiểm soát hiển thị trên màn và chuyển tiếp vào select tank
                        thisStage = False
                    elif Opt == 2:
                        pygame.mixer.music.stop()
                        run = False
                        starting = False
                        selecting = False
                        battling = False #nếu chọn exit game thì nhạc cũng dừng lại và đóng cửa sổ, kết thúc mọi trạng thái
                        end = False
                        thisStage = False

def selectionScreen(thisStage):
    #shows menu, cửa sổ màn hình đầu tiên khi vào gaem
    '''
    Đoạn mã cần kiểm tra biến 'thisStage' trước khi thực thi một số chức năng như cập nhật lớp của "player tank" và gọi hàm readMap()
    để chuẩn bị cho trận chiến.
    '''
    global run, selecting, battling, end                    #biến toàn cục cho phép thay đổi trong phạm vi cục bộ của hàm
                                                            
    pygame.mixer.music.load(musicList[1])    # chỉ số [1] cho biết rằng nó đang tải bản nhạc thứ hai trong danh sách
    pygame.mixer.music.set_volume(0.4)      #mức âm lượng được set up ở mức 40%
    pygame.mixer.music.play(-1)              #phát nhạc mãi mãi
    
    Opt1 = 0
    Opt2 = 0                                   #Opt1 - Opt2 các cài đặt của player1 - player2
    
    instructionP1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/moveP2.png')   #bảng hướng dẫn điều khiển tank
    instructionP2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/moveP1.png')
    
    Title = my_font3.render('Select Tank', True, (9,255,242))
    # Lấy hình chữ nhật bao quanh văn bản
    Title_rect = Title.get_rect()
    # Canh lề giữa cho văn bản
    Title_rect.centerx = screen.get_rect().centerx
    # in văn bản lên màn hình
    screen.blit(Title, Title_rect)

    p1Title = my_font4.render('P1', True, (255,255,0)) #chữ màu vàng nền trong suốt
    p2Title = my_font4.render('P2', True, (255,255,0))
    
    instruction = my_font4.render('Use your left and right controls to switch between tanks.', True, (255,255,0))
    instruction2 = my_font4.render('Press ENTER to start the battle !', True, (255,255,0))

    options = [imageUp_v1,imageUp_v2]                  #tạo danh sách chứa các ảnh của 2 phiên bản tank 
    stats = {0:['3', '6', '3'], 1:['6','3','1']}
    
    DisplaySurf = pygame.Surface((80,80))
    DisplaySurf.fill((255,255,255))                 #tạo ô nền màu trắng 
    DisplaySurf2 = pygame.Surface((80,80))
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
        screen.blit(Title, (170, 70)) # tọa độ dòng chữ Select Tank

        screen.blit(p1Title, (160, 150))
        screen.blit(p2Title, (420, 150))

        screen.blit(p1statsHealth, (45,200)) 
        screen.blit(p1statsSpeed, (45,220))  
        screen.blit(p1statsReload, (45,240)) 

        screen.blit(p2statsHealth, (500,200)) #tọa độ chỉ số máu của player2
        screen.blit(p2statsSpeed, (500,220)) #tọa độ chỉ tốc độ của player2
        screen.blit(p2statsReload, (500,240)) #tọa độ chỉ số tốc độ bắn của player2

        screen.blit(DisplaySurf, (135, 189))  #tọa độ ô trắng
        screen.blit(DisplaySurf2, (390, 189))
        screen.blit(options[Opt1], (160, 220)) # tọa độ hình tank trong ô màu trắng
        screen.blit(options[Opt2], (415, 220))

        screen.blit(instructionP1, (70, 290))
        screen.blit(instructionP2, (330, 290))

        screen.blit(instruction, (70, 500)) #tọa độ của dòng chữ "Use your left and right controls to switch between tanks..."
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

    scores = open('ProJect_Pygame_Nhom18/BangBang/Tank2P/BangTinhDiem.txt', 'r')
    for l in scores:
        dataFields = l.split(',')
        dataFields[-1] = dataFields[-1].strip('\n')
        scoredata[dataFields[0]] = int(dataFields[1])               #read the score cvs file, update scoredata
    scores.close()
    
    winner = max(player1.health,player2.health)     #use remaining health to determine the winner
    
    if winner == player1.health:
            WinnerTitle =  my_font2.render('PLAYER 1 WINS', True, (255,255,0))
            scoredata['1'] +=1                                                      #whoever wins gets 1 point
    else:
            WinnerTitle = my_font2.render('PLAYER 2 WINS', True, (255,255,0))
            scoredata['2'] +=1

    scores = open('ProJect_Pygame_Nhom18/BangBang/Tank2P/BangTinhDiem.txt', 'w')
    scores.write('1,' + str(scoredata['1']) + '\n')         #record the win
    scores.write('2,' + str(scoredata['2']) + '\n')
    scores.close()
            
    Title = my_font3.render('END OF THE MATCH', True, (255,0,0))
    scoreTitle = my_font2.render('Scores', True, (212,212,212))
    instruction = my_font4.render('Press R to reset scores!', True, (255,255,0))
    instruction2 = my_font4.render('Press ENTER to return to game menu.', True, (255,255,0))

    while thisStage:
        p1Scores = my_font2.render('Player 1:  ' +str(scoredata['1']), True, (255,255,255))
        p2Scores = my_font2.render('Player 2:  '+ str(scoredata['2']), True, (255,255,255))
        #set up tọa độ vị trí căn lề cho các text
        screen.blit(screenPIC, (0,0))
        screen.blit(Title, (60,50))
        screen.blit(WinnerTitle, (155,200))
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

    scores = open('ProJect_Pygame_Nhom18/BangBang/Tank2P/BangTinhDiem.txt', 'w')
    scores.write('1,' + str(scoredata['1']) + '\n')
    scores.write('2,' + str(scoredata['2']) + '\n')         #final recording and updating just to be safe
    scores.close()
        
    starting = True
    selecting = True
    
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
clock = pygame.time.Clock()

colours = pygame.color.THECOLORS
my_font = pygame.font.SysFont('Verdana', 100)
my_font2 = pygame.font.SysFont('moolboran', 66)
my_font3 = pygame.font.SysFont('andalus', 72)      #setup Font chữ
my_font4 = pygame.font.SysFont('candara', 20)
my_font5 = pygame.font.SysFont('arial', 16)

size = (605, 540)
screen = pygame.display.set_mode(size)
screenPIC = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/anhnen.png')
pygame.display.set_caption("Tank Moba PvP")              #setup nền
background = pygame.Surface(size)
background = background.convert()
background.fill(colours['grey']) #màu nền của map trong game

explode = pygame.mixer.Sound('ProJect_Pygame_Nhom18/BangBang/Tank2P/bum.ogg')
shoot = pygame.mixer.Sound('ProJect_Pygame_Nhom18/BangBang/Tank2P/music/fireMusic.mp3')          #setup music game
musicList = ['ProJect_Pygame_Nhom18/BangBang/Tank2P/music/endMusic.mp3','ProJect_Pygame_Nhom18/BangBang/Tank2P/music/selectSong.mp3','ProJect_Pygame_Nhom18/BangBang/Tank2P/mbattle.ogg','ProJect_Pygame_Nhom18/BangBang/Tank2P/music/endMusic.mp3']

maps = ['ProJect_Pygame_Nhom18/BangBang/Tank2P/map1.txt', 'ProJect_Pygame_Nhom18/BangBang/Tank2P/map2.txt', 'ProJect_Pygame_Nhom18/BangBang/Tank2P/map3.txt']
tiles = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tuong.png')

explosion = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/vuno.png')
imageUp_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank1 up.png')
imageDown_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank1 down.png')
imageRight_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank1 right.png')     #load ảnh khi tank thay đổi hướng khi di chuyển
imageLeft_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank1 left.png')

imageUp_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank2 up.png')
imageDown_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank2 down.png')
imageRight_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank2 right.png')
imageLeft_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank2 left.png')

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

