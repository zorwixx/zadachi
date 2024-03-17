import logging
logging.basicConfig(level=logging.DEBUG, filename="logs.top", filemode="w", format="we have logging massage:%(asctime)s:%(levelname)s - %(massege)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
try:
    print(10/0)
except Exception:
    logging.exception("Exception")