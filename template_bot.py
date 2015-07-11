import sys


class HoldemBot(object):
    def run(self):
        while not sys.stdin.closed:
            line = sys.stdin.readline()
            if not line:
                continue
            line = line.split()
            # A move is requested
            if len(line) == 3 and line[0] == "Action":
                sys.stdout.write("check 0\n")
                sys.stdout.flush()
            # Game settings, round information and opponent moves are also
            # given
            else:
                # Store it or something
                pass


if __name__ == '__main__':
    bot = HoldemBot()
    bot.run()
