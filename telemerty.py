import random
import time
import threading
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

CONNECTION_STRING = "HostName=University-IoT-Cart.azure-devices.net;DeviceId=Pi_Envirnoment;SharedAccessKey=TWnLYcXf/sxYoacZry0akx7knPOa2gSojrkZ7oyBfX0="

TEMPERATURE = 20.0
HUMIDITY = 60
MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity}}}'
INTERVAL = 1

def getReadings():
    temperature = TEMPERATURE + (random.random() * 15)
    humidity = HUMIDITY + (random.random() * 20)
    msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity)
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