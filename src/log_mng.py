import logging

LOG_FILE_PATH = "logs/"
LOG_FILE_NAME_MAIN = "main.log"
LOGGER_NAME_MAIN = "lgr.main"
CONSOLE_HANDLER_NAME = "hndl.console"


def add_console(logger: logging.Logger) -> None:
    """Добавление к логгеру вывода в консоль"""
    if CONSOLE_HANDLER_NAME in [hdlr.get_name() for hdlr in logger.handlers]:
        # print(f"{CONSOLE_HANDLER_NAME} in {[hdlr.get_name() for hdlr in logger.handlers]}" )
        return
    else:
        # print(f"{CONSOLE_HANDLER_NAME} creation")
        console_handler = logging.StreamHandler()
        console_handler.set_name(CONSOLE_HANDLER_NAME)
        console_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(lineno)d: %(message)s")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        logger.setLevel(logging.DEBUG)


def mainLog() -> logging.Logger:
    """Функция получения логгера"""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s",
        filename=LOG_FILE_PATH + LOG_FILE_NAME_MAIN,  # Запись логов в файл
        filemode="w",
        encoding="UTF-8",  # "cp1251"
    )
    logger = logging.getLogger(LOGGER_NAME_MAIN)
    # add_console(logger)
    return logger
