import winsound

# winsound is a windows only audio library to play sounds
# I did try to use a few other libraries, but I was unsuccessful
# I was going to just grab the ffmpeg library then hook into it, but this was easier.


def reset(nice, mean, name):
    nice = 0
    mean = 0
    main(nice, mean, name)


def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again?(Y/N)").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        else:
            print("\nSorry to see you go!")
            stop = False
            quit()


def win(nice, mean, name):
    print("\nNice job, you won, {}!".format(name))
    winsound.PlaySound('win.wav', winsound.SND_FILENAME)
    again(nice, mean, name)


def lost(nice, mean, name):
    print("\nToo bad, you lost, {}.  Maybe next time.".format(name))
    winsound.PlaySound('lose.wav', winsound.SND_FILENAME)
    again(nice, mean, name)


def score(nice, mean, name):
    if nice > 2:
        win(nice, mean, name)
    if mean > 2:
        lost(nice, mean, name)
    else:
        nice_mean(nice, mean, name)

def show_score(nice, mean, name):
    print("\n{}, your current total: \nNice: {}\nMean: {}".format(name, nice, mean))

def describe_game(name):
    """
    Check to see if this is a new game
    :param name: Player name
    :return: Player name
    """
    if name != "":
        print("\nThank you for playing again, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name?\n").capitalize()
                if name != "":
                    print("\nWelcome, {}".format(name))
                    print("In this game you will be greeted by several different people.\
                     \nYou can choose to be nice or mean.")
                    print("but at the end of the game, your fate will be sealed by your actions")
                    stop = False

    return name


def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("/nA stranger approaches you for a conversation.  Will you be nice or mean?(N/M)").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice += 1
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you menacingly and storms off...")
            mean += 1
            stop = False
    score(nice, mean, name)


def main(nice=0, mean=0, name=""):
    name = describe_game(name)
    nice_mean(nice, mean, name)



if __name__ == '__main__':
    main()

