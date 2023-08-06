import coloredlogs, logging

logger = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG', logger=logger) # Explicar niveles de LOG, pros y contras

logger.info("Programa python de ejemplo")

def add_one(number):
    return number + 1

# Explicar TDD y cobertura
# def add_two(number):
#     return number + 2