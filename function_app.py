import azure.functions as func
import mysql.connector as conn
import logging
import json
import os

app = func.FunctionApp()

@app.service_bus_queue_trigger(arg_name="azservicebus", queue_name="iot-devices-queue", connection="AZURE_SERVICEBUS_CONNECTION_STRING") 
def servicebus_queue_trigger(azservicebus: func.ServiceBusMessage):
    # getting data
    message = azservicebus.get_body().decode('utf-8')  # str
    message_obj = json.loads(message)  # dict

    # creating obj
    device = message_obj["deviceId"]
    measurement = list(message_obj["telemetry"].values())[0]  # 1st dict val
    unit = message_obj["enrichments"]["Unit"]
    time = message_obj["messageProperties"]["iothub-creation-time-utc"]
    location = f"{message_obj['enrichments']['Location latitude']},{message_obj['enrichments']['Location longitude']}"
    new_message = {
        "Device": device,
        "Measurement": measurement,
        "Unit": unit,
        "Time": time,
        "Location": location
    }

    # printing info
    logging.info(f"MESSAGE: {new_message}")

    # to mysql
    db_host = os.environ["AZ_DB_HOST"]
    db_user = os.environ["AZ_DB_USER"]
    db_pass = os.environ["AZ_DB_PASSWORD"]
    db_name = os.environ["AZ_DB_NAME"]

    db = conn.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
    insert_str = f"INSERT INTO device(name, measurement, unit, time, location) VALUES('{device}', '{measurement}', '{unit}', '{time}', '{location}');"
    cursor = db.cursor()
    cursor.execute(insert_str)  # running query
    db.commit()  # saving changes
    cursor.close()
    db.close()
