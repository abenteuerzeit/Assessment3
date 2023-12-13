"""function_app.py"""

import logging
import azure.functions as func


app = func.FunctionApp()


@app.event_hub_message_trigger(arg_name="azeventhub",
                               event_hub_name="myeventhub",
                               connection="EventHubConnectionString")
def eventhub_trigger(azeventhub: func.EventHubEvent) -> None:
    """_summary_
    Event hub trigger function that logs the events it receives.

    Args:
        azeventhub (func.EventHubEvent): _description_
    """
    event = azeventhub.get_body().decode('utf-8')
    logging.info('Python EventHub trigger processed an event: %s', event)
