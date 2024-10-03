from .utils import setup_logger

logger = setup_logger(__name__)

RECORDS_KEY = 'Records'


def process_event(event: dict):
    logger.info(f'Processing event: {event}')

    records = event.get(RECORDS_KEY, [])
    for record in records:
        process_record(record)


def process_record(record):
    pass
