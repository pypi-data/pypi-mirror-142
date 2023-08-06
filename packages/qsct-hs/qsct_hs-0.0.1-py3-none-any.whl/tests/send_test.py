from qsct import functions
from qsct.main import QSCT
import unittest
from socket import socket


def Main_sender():
    host = '127.0.0.1'
    port = 5001

    mySocket = socket()
    mySocket.connect((host, port))
    sender = QSCT(True, "Отправитель")
    # message = input(" ? ")
    message = {'status': 'success', 'info': [{'id': 15495, 'car_number': 'В018АР702', 'brutto': 8220, 'tara': 6170, 'cargo': 2050, 'time_in': 'datetime.datetime(2022, 3, 10, 11, 32, 47, 938082, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=300, name=None))', 'time_out': 'datetime.datetime(2022, 3, 10, 11, 41, 54, 296760, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=300, name=None))', 'inside': None, 'alerts': None, 'carrier': 15, 'trash_type': 2155, 'trash_cat': 1210, 'notes': None, 'operator': 8, 'checked': None, 'tara_state': None, 'brutto_state': None, 'wserver_sent': None, 'wserver_get': None, 'dk7_weight': 0, 'wserver_id': None,'auto': 58, 'owner': None, 'full_notes': ''}]}

    sender.send_data_high(mySocket, message)

    # while message != 'q':
    #     mySocket.send(message.encode())
    #     data = mySocket.recv(1024).decode()
    #
    #     print('Received from server: ' + data)
    #     message = input(" ? ")

    mySocket.close()


if __name__ == '__main__':
    Main_sender()
