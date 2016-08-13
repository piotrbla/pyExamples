import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-7s %(message)s',
    datefmt='[%d-%m-%Y %H:%M:%S]',
    filename='c:\\Users\\Piotr\\PycharmProjects\\pyExamples\\sorting.txt',
    filemode='w'
)

logging.info("Coś tam")

formatter = logging.Formatter('%(levelname)-7s %(message)s')
creepy_log = logging.FileHandler('sorting.txt')
creepy_log.setFormatter(formatter)
logging.getLogger('').addHandler(creepy_log)
logging.info("Coś tam jeszcze innego")