import logging
import sys

from static_hole import strategy

logging.basicConfig(filename="bot.log", level=logging.DEBUG)
logger = logging.getLogger()


class HoldemBot(object):
    def __init__(self):
        self.round = 0
        self.settings = {}
        self.match = {}
        self.hand = []
        self.win_percent = 0

        self.hole_strategy = strategy.StaticHoleStrategy()


    def output(self, line, action):
        logger.debug("Responding to {} with {}".format(line, action))
        sys.stdout.write(action + "\n")
        sys.stdout.flush()

    def handle_settings(self, line):
        self.settings[line[1]] = line[2]
        logger.debug("Settings: {}".format(self.settings))

    def handle_match(self, line):
        if line[1] == "round":
            # Start of a round, reinitialize
            self.start_match(line)

        self.match[line[1]] = line[2]
        logger.debug("Match: {}".format(self.settings))

    def start_match(self, line):
        self.round = line[2]
        self.hand = []
        self.match = {}
        self.win_percent = 0
        logger.info("===============Starting round {}=================".format(
            self.round))

    def handle_info(self, line):
        logger.debug("Info: {}".format(line))
        if line[1] == "hand":
            self.win_percent = float(
                self.hole_strategy.get_win_percentage(line[2]))
            logger.info("Estimated win percentage: {}".format(
                self.win_percent))

    def handle_action(self, line):
        logger.debug("Action: {}".format(line))
        if self.win_percent > 50:
            self.output(line, "raise 100")
        else:
            self.output(line, "check 0")

    def run(self):
        logger.debug("Starting up!")
        while not sys.stdin.closed:
            try:
                raw_line = sys.stdin.readline()
                if not raw_line:
                    continue
                line = raw_line.split()

                # Basic sanity check
                if len(line) != 3:
                    logger.error("Invalid input: {}".format(raw_line))

                # Dispatch based on action type
                if line[0] == "Action":
                    self.handle_action(line)
                elif line[0] == "Settings":
                    self.handle_settings(line)
                elif line[0] == "Match":
                    self.handle_match(line)
                elif line[0] in ["player1", "player2"]:
                    self.handle_info(line)
                else:
                    logger.info("Unhandled line: {}".format(raw_line))
            except Exception as e:
                logger.exception("Handling line failed")


if __name__ == "__main__":
    bot = HoldemBot()
    bot.run()
