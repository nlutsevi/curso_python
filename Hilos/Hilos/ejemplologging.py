import logging

logging.basicConfig(level=logging.DEBUG,
format="%(asctime)s (%(levelname)s): %(message)s (archivo: %(filename)s)",
datefmt="%H:%M:%S", filename="controllogging.txt", filemode="w")

logging.debug("Mensaje de depuración")
logging.info("Mensaje de información")
logging.warning("Mensaje de aviso")
logging.error("Mensaje de error")
logging.critical("Mensaje de error crítico")

milogging = logging.getLogger("prueba")
milogging.info("Mensaje con un logging alternativo")