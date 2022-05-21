import logging

def configurate_logging():
    logging.basicConfig(format="%(asctime)s: %(message)s",
                        level=logging.INFO, 
                        datefmt="%H:%M:%S")
    logging.info('Logging configurado.')