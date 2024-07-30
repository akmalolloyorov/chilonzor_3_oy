import logging


class FunctionExecutionContext(Exception):
    def __init__(self, massage, *args):
        super().__init__(massage, *args)
        self.massage = massage

    def __str__(self):
        return self.massage


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(name)s - %(levelname)s - %(massage)s',
                    datefmt="%Y-%m-%d %I:%M:%",
                    filename='app.log')

logger = logging.getLogger(__name__)


def log_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            # logging.info(f'Called function: {func.__name__}')
            result = func(*args, **kwargs)
            # logging.info(f'Result of function: {func.__name__} - {result}')
            massage = f"function:{func.__name__},args={args},kwargs={kwargs}, result = {result}"
            logger.info(massage)
            return result
        except Exception as e:
            massage = f'An error occurred while executing function: {func.__name__} - {e}'
            logging.exception(massage)
            raise FunctionExecutionContext(massage=massage)

    return wrapper()


@log_decorator
def multiply(a, b):
    return a * b


if __name__ == '__main__':
    multiply(a=1, b=2)
