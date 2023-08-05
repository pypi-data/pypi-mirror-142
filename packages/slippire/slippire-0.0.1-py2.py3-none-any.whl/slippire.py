'''slippire'''
__version__ = "0.0.1"
import slippi

def enumtostr(enum):
    '''convert slp enumerations to the needed text output'''
    enumstr = str(enum)
    slplist = enumstr.split(".")

    # return 1 as it is the content of the list
    return slplist[1]

def getcharacterlist(gamefile):
    '''get characters as list indexed 0,1 from game file'''
    gameplayers = gamefile.start.players
    character1  = enumtostr(gameplayers[0].character)
    character2  = enumtostr(gameplayers[1].character)
    return (character1, character2)

def getstage(gamefile):
    '''get stage from game file'''
    return enumtostr(gamefile.start.stage)

def getwinner(gamefile):
    '''determine winner in a better way'''
    gframes = gamefile.frames

    p1flags = enumtostr(gframes[len(gframes)-1].ports[0].leader.post.flags)

    if "DEAD" in p1flags:
        winner = "p2"
    else:
        winner = "p1"
    
    return winner

def getkillmoves(gamefile):
    '''calculate lists of kill moves and frames by both players'''
    gframes = gamefile.frames
    totframes = len(gframes) - 1

    p1deathframes = []
    p1deathmoves  = []
    p2deathframes = []
    p2deathmoves  = []

    for itr in range(1, totframes):
        if gframes[itr].ports[0].leader.post.stocks != gframes[itr-1].ports[0].leader.post.stocks:
            p1deathframes.append(itr)
            p1deathmoves.append(gframes[itr].ports[1].leader.post.last_attack_landed)

        if gframes[itr].ports[1].leader.post.stocks != gframes[itr-1].ports[1].leader.post.stocks:
            p2deathframes.append(itr)
            p2deathmoves.append(gframes[itr].ports[0].leader.post.last_attack_landed)

        itr += 1
        # end for loop

    p1flags = enumtostr(gframes[totframes].ports[0].leader.post.flags)
    p2flags = enumtostr(gframes[totframes].ports[1].leader.post.flags)

    if "DEAD" in p1flags:
        p1deathframes.append(totframes)
        p1deathmoves.append(gframes[totframes].ports[1].leader.post.last_attack_landed)

    if "DEAD" in p2flags:
        p2deathframes.append(totframes)
        p2deathmoves.append(gframes[totframes].ports[0].leader.post.last_attack_landed)

    # fill lists with empty data for output if they are not full
    while len(p1deathmoves) < 4:
        p1deathmoves.append("")
    
    while len(p2deathmoves) < 4:
        p2deathmoves.append("")

    return (p1deathmoves, p2deathmoves)

def gettags(gamefile):
    '''to return the unique id's of both players'''
    tag1 = gamefile.metadata.players[0].netplay.code
    tag2 = gamefile.metadata.players[1].netplay.code
    return (tag1, tag2)

def numplayers(gamefile):
    '''determine number of players in a slippi replay'''
    gameplayers = gamefile.start.players[2]
    return gameplayers

def slippire():
    '''main func'''
    return