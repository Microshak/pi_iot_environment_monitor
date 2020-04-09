import random
import time
import threading
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
import json

CONNECTION_STRING = "HostName=University-IoT-Cart.azure-devices.net;DeviceId=Pi_Envirnoment;SharedAccessKey=TWnLYcXf/sxYoacZry0akx7knPOa2gSojrkZ7oyBfX0="

TEMPERATURE = 20.0
HUMIDITY = 60
INTERVAL = 1
readings = {'temperature':0,'humidity':0, 'device_type':'pi_environment_monitor'}

def getReadings():
    
    readings['temperature'] = TEMPERATURE + (random.random() * 15)
    readings['humidity'] = HUMIDITY + (random.random() * 20)
    msg_txt_formatted = json.dumps(readings)
    message = Message(msg_txt_formatted)
    return(message)

def iothub_client_telemetry_run():

    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            message = getReadings()

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print( "Message sent" )
            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )


if __name__ == '__main__':
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_run()