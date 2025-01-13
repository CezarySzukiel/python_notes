import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)-8s %(name)-10s: %(message)s')

log = logging.getLogger(__name__)

log.debug('Debug message')
log.info('Info message')
log.warning('Warning message')
log.error('Error message')
log.critical('Critical message')


def add(x, y):
    log.info(f"Adding %d + %d", x, y)
    if not isinstance(x, int) or not isinstance(y, int):
        log.error("Both arguments must be integers")
        raise TypeError("Both arguments must be integers")


add(2,3)
add(2, 4)

try:
    add(2, "ala")
except TypeError as e:
    "??"