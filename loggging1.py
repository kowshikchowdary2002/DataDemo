import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    force="a",
                    format='%(name)s  -  %(levelname)s - %(message)s' 
                    )

logging.debug("iam debug!")
logging.info("ima info!")
logging.critical("ima critical!")
logging.error("iam error!")
logging.warning("iam warining!")