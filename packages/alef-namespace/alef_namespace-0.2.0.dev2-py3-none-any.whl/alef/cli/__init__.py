from alef.logging import getLogger, initLogging

logging = getLogger("alef")


def main():
    initLogging()
    logging.info("hello")
