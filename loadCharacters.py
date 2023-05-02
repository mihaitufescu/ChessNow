spritesPath = [ r"C:\Users\Simona\PycharmProjects\chessNow\resources\Sprites\cal_a.png", r"C:\Users\Simona\PycharmProjects\chessNow\resources\Sprites\cal_n.png", r"C:\Users\Simona\PycharmProjects\chessNow\resources\Sprites\nebun_a.png", r"C:\Users\Simona\PycharmProjects\chessNow\resources\Sprites\nebun_n.png",r"C:\Users\Simona\PycharmProjects\chessNow\resources\Sprites\rege_a.png",r"C:\Users\Simona\PycharmProjects\chessNow\resources\Sprites\rege_n.png",r"C:\Users\Simona\PycharmProjects\chessNow\resources\Sprites\regina_a.png",r"C:\Users\Simona\PycharmProjects\chessNow\resources\Sprites\regina_n.png",r"C:\Users\Simona\PycharmProjects\chessNow\resources\Sprites\tura_a.png",r"C:\Users\Simona\PycharmProjects\chessNow\resources\Sprites\tura_n.png",r"C:\Users\Simona\PycharmProjects\chessNow\resources\Sprites\pion_a.png",r"C:\Users\Simona\PycharmProjects\chessNow\resources\Sprites\pion_n.png"]



def loadPiece(i):
    l = []
    if i==0:
        l = [37.8 * (2 * 1 + 1) + 5 * (2 * 1 + 1), 43, 37.8 * (2 * 6 + 1) + 5 * (2 * 6 + 1), 43]
    elif i==1:
        l = [37.8 * (2 * 1 + 1) + 5 * (2 * 1 + 1), 37.8* (2*7+1) + 5 *(2*7+1), 37.8 * (2 * 6 + 1) + 5 * (2 * 6 + 1), 37.8* (2*7+1) + 5 *(2*7+1)]
    elif i==2:
        l = [37.8 * (2 * 2 + 1) + 5 * (2 * 2 + 1), 43, 37.8 * (2 * 5 + 1) + 5 * (2 * 5 + 1), 43]
    elif i==3:
        l = [37.8 * (2 * 2 + 1) + 5 * (2 * 2 + 1), 37.8* (2*7+1) + 5 *(2*7+1), 37.8 * (2 * 5 + 1) + 5 * (2 * 5 + 1), 37.8* (2*7+1) + 5 *(2*7+1)]
    elif i==4:
        l = [37.8 * (2 * 3 + 1) + 5 * (2 * 3 + 1), 43]
    elif i==5:
        l = [37.8 * (2 * 3 + 1) + 5 * (2 * 3 + 1), 37.8 * (2 * 7 + 1) + 5 * (2 * 7 + 1)]
    elif i==6:
        l = [37.8 * (2 * 4 + 1) + 5 * (2 * 4 + 1), 43]
    elif i==7:
        l = [37.8 * (2 * 4 + 1) + 5 * (2 * 4 + 1), 37.8 * (2 * 7 + 1) + 5 * (2 * 7 + 1)]
    elif i==8:
        l = [37.8 * (2 * 0 + 1) + 5 * (2 * 0 + 1), 43, 37.8 * (2 * 7 + 1) + 5 * (2 * 7 + 1), 43]
    elif i==9:
        l = [37.8 * (2 * 0 + 1) + 5 * (2 * 0 + 1), 37.8 * (2 * 7 + 1) + 5 * (2 * 7 + 1), 37.8 * (2 * 7 + 1) + 5 * (2 * 7 + 1), 37.8 * (2 * 7 + 1) + 5 * (2 * 7 + 1)]
    elif i==10:
        l = [37.8* (2 * 0+ 1) + 5 * (2 *0 +1), 37.8* (2 * 1 + 1) + 5 * (2 * 1 +1)]
    else:
        l = [37.8* (2 * 0+ 1) + 5 * (2 *0 +1), 37.8* (2 * 6 + 1) + 5 * (2 * 6 +1)]
    return l

def loadFiles(i=0):
    return str(spritesPath[i])
