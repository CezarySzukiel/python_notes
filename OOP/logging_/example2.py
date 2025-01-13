import logging

console_handler = logging.StreamHandler() # handler służy do obsługo logów, z tym że streamy są najbezpieczniejsze
formatter = logging.Formatter('%(asctime)s - %(levelname)-8s %(name)-10s: %(message)s')
console_handler.setFormatter(formatter)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(console_handler)

log.debug('Debug message')
log.info('Info message')
log.warning('Warning message')
log.error('Error message')
log.critical('Critical message')
