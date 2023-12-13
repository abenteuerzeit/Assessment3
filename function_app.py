"""function_app.py"""

import logging
import azure.functions as func


app = func.FunctionApp()


@app.event_hub_message_trigger(arg_name="azeventhub",
                               event_hub_name="myeventhub",
                               connection="EventHubConnectionString")
def eventhub_trigger(azeventhub: func.EventHubEvent) -> None:
    """
    Event hub trigger function that logs the events it receives.

    Args:
        azeventhub (func.EventHubEvent): Event Hub Event

    Raises:
        Exception: Raises any exception that occurs within the try block
    """
    try:
        event = azeventhub.get_body().decode('utf-8')
        logging.info('Python EventHub trigger processed an event: %s',
                     event)
    except UnicodeDecodeError as err:
        logging.error('Decode Error: Could not decode event data. Error: %s',
                      err)
        raise
    except Exception as err:
        logging.error('Unexpected Error: %s',
                      err)
        raise
