import os,sys
DIR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_PATH)
oracle_conn={
    'username' : 'bill',
    'password': 'PUB1_12c',
    'ip':'10.143.100.211',
    'port':'1523',
    'service_name':'oracle12c'
}