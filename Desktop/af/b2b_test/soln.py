from datetime import datetime, date
import requests
from requests.auth import HTTPBasicAuth
import json
import base64
from cryptography.fernet import Fernet
from decouple import config


#decrypt import credentials
def decrypt_creds(cypher_string):
    f = Fernet(config('encryption_key').encode())
    decrypted_string = f.decrypt(cypher_string.encode()).decode()
    return decrypted_string

# Authentication info for the shortcode 3016005
class Authentication_3016005:
    bussiness_shortcode = "3016005"
    consumer_key = decrypt_creds(config('3016005_consumer_key'))
    consumer_secret = decrypt_creds(config("3016005_consumer_secret"))
    auth_url = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    pass_key = decrypt_creds(config("pass_key"))
    SecurityCredential = decrypt_creds(config("security_credential"))

# Authentication info for the shortcode 4044053
class Authentication_4044053:
    bussiness_shortcode = "4044053"
    consumer_key = decrypt_creds(config("4044053_consumer_key"))
    consumer_secret = decrypt_creds(config("4044053_consumer_secret"))
    auth_url = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    pass_key = decrypt_creds(config("pass_key"))
    SecurityCredential = decrypt_creds(config("security_credential"))



def b2b(api_username, amount, partyA, partyB, commandID, callback_url, account_number):
    # generate the access token
    access_token = json.loads(requests.get(Authentication_3016005.auth_url, auth=HTTPBasicAuth(
        Authentication_3016005.consumer_key, Authentication_3016005.consumer_secret)).text)['access_token']

    api_url = "https://api.safaricom.co.ke/mpesa/b2b/v1/paymentrequest"
    request_header = {
        "Authorization": "Bearer %s" % access_token
    }
    request_body = {
        "Initiator": api_username, #hoseamungai  & apib2c
        "SecurityCredential": "iidsMSunLfKNBvElEU9gaa19H48x4fYS/f/BYM5ZY4DA7lq2aJBDRsChkX6/BNW+/T1MgY3iDF5YlKpO+nxlujqLefDlZbfJumYRQ9hDQe5rTQeVfWf1kfZbP4ReKP03K1cxJfF5EI1hawjvg1Dj3bQFx8+Zqaa0MzXLxfSjV0/PT5eNoZ5XBtXes9jkcpjlQEVrfSe6QqFbq56prtnyG+KN0p8kNcjmZdGngI8q/g3KuyIouc+RLl7CdemP4Mk6SV8UmZ9c3FvNcCqKuD4a0U9SLfRjijjZ/vWBIOmOxhuZjE4D0ttdDQSDO+bj//ogd2Gmo6LB76qxz0tt82PGDQ==",
        # "SecurityCredential": Authentication_3016005.SecurityCredential,
        "CommandID": commandID,
        "Amount": amount,
        "PartyA": str(partyA),
        "SenderIdentifierType": "4",
        "PartyB": str(partyB),
        "RecieverIdentifierType": "4",
        "Remarks": "school fees payment",
        "QueueTimeOutURL": callback_url,
        "ResultURL": callback_url,
        "AccountReference": account_number,
        # "AccountReference": "6604003887", #ecobank gilalo
        "Reason":'test'
    }
    response = requests.post(api_url, json=request_body, headers=request_header)
    return response


def b2c(api_username, amount, partyA, partyB, commandID, callback_url):
    # generate the access token
    access_token = json.loads(requests.get(Authentication_3016005.auth_url, auth=HTTPBasicAuth(
        Authentication_3016005.consumer_key, Authentication_3016005.consumer_secret)).text)['access_token']

    api_url = "https://api.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
    request_header = {
        "Authorization": "Bearer %s" % access_token
    }
    request_body = {    
        "InitiatorName": api_username,    
        "SecurityCredential": "iidsMSunLfKNBvElEU9gaa19H48x4fYS/f/BYM5ZY4DA7lq2aJBDRsChkX6/BNW+/T1MgY3iDF5YlKpO+nxlujqLefDlZbfJumYRQ9hDQe5rTQeVfWf1kfZbP4ReKP03K1cxJfF5EI1hawjvg1Dj3bQFx8+Zqaa0MzXLxfSjV0/PT5eNoZ5XBtXes9jkcpjlQEVrfSe6QqFbq56prtnyG+KN0p8kNcjmZdGngI8q/g3KuyIouc+RLl7CdemP4Mk6SV8UmZ9c3FvNcCqKuD4a0U9SLfRjijjZ/vWBIOmOxhuZjE4D0ttdDQSDO+bj//ogd2Gmo6LB76qxz0tt82PGDQ==", 
        "CommandID": commandID,    
        "Amount": amount,    
        "PartyA": partyA,    
        "PartyB": partyB,    
        "Remarks": "marketday withdraw",    
        "QueueTimeOutURL": callback_url,    
        "ResultURL": callback_url,    
        "Occassion": "marketday.co.ke"
    }
    response = requests.post(api_url, json=request_body, headers=request_header)
    return response



def transaction_status(callback_url):
    # generate the access token
    access_token = json.loads(requests.get(Authentication_3016005.auth_url, auth=HTTPBasicAuth(
        Authentication_3016005.consumer_key, Authentication_3016005.consumer_secret)).text)['access_token']

    api_url = "https://api.safaricom.co.ke/mpesa/transactionstatus/v1/query"
    request_header = {
        "Authorization": "Bearer %s" % access_token
    }
    request_body = {
        "Initiator": "apib2c",
        "SecurityCredential": "iidsMSunLfKNBvElEU9gaa19H48x4fYS/f/BYM5ZY4DA7lq2aJBDRsChkX6/BNW+/T1MgY3iDF5YlKpO+nxlujqLefDlZbfJumYRQ9hDQe5rTQeVfWf1kfZbP4ReKP03K1cxJfF5EI1hawjvg1Dj3bQFx8+Zqaa0MzXLxfSjV0/PT5eNoZ5XBtXes9jkcpjlQEVrfSe6QqFbq56prtnyG+KN0p8kNcjmZdGngI8q/g3KuyIouc+RLl7CdemP4Mk6SV8UmZ9c3FvNcCqKuD4a0U9SLfRjijjZ/vWBIOmOxhuZjE4D0ttdDQSDO+bj//ogd2Gmo6LB76qxz0tt82PGDQ==", 
        "CommandID": "TransactionStatusQuery",
        "TransactionID": "11",
        "OriginatorConversationID":"AG_20220202_2050081bd0b8cd3f143a",
        "PartyA": "3016005",
        "IdentifierType": "1",
        "ResultURL": callback_url,
        "QueueTimeOutURL": callback_url,
        "Remarks": " ",
        "Occasion": " "
    }
    response = requests.post(api_url, json=request_body, headers=request_header)
    return response


def reverse(amount, transaction_id, callback_url):
    # generate the access token
    access_token = json.loads(requests.get(Authentication_4044053.auth_url, auth=HTTPBasicAuth(
        Authentication_4044053.consumer_key, Authentication_4044053.consumer_secret)).text)['access_token']
    
    
    api_url = "https://api.safaricom.co.ke/mpesa/reversal/v1/request"
    request_header = {
        "Authorization": "Bearer %s" % access_token
    }
    request_body = {
        "Initiator": "hoseamungai",
        "SecurityCredential": Authentication_4044053.SecurityCredential,
        "CommandID": "TransactionReversal",
        "TransactionID": transaction_id,
        "Amount": amount,
        "ReceiverParty": "4044053",
        "RecieverIdentifierType": "11",
        "ResultURL": callback_url,
        "QueueTimeOutURL": callback_url,
        "Remarks": "Reversed Airtime purchase",
        "Occasion": "work"
    }

    response = requests.post(
        api_url, json=request_body, headers=request_header)
    return response



# amount = 1
account_number = "0340179556749"
# '4044053', '3016005', '3031673'
# bank_shortcode = 247247


# b2b keywords
# "DisburseFundsToBusiness"              Utility to mmf/working
# "BusinessPayBill"                      mmf/working to utility
# BusinessTransferFromMMFToUtility       self explanatory
# BusinessTransferFromUtilityToMMF       self explanatory

# BusinessToBusinessTransfer             mmf/working to mmf/working


# r1 = b2b('apib2c', 1, '3016005', '3016005', "BusinessTransferFromMMFToUtility", callback_url, account_number="0340179556749")
# print(r1.text)

# r2 = b2b('apib2c', 1, '3016005', '3028247', "BusinessPayBill", callback_url, account_number=str(account_number))
# print(r2.text)

callback_url = "https://webhook.site/136d1264-7a2a-44f8-972f-9bf467fc6b1b"

# r3 = b2c("apib2c", 10, "3016005", "254746372071", "BusinessPayment", callback_url)
# print(r3.text)

# ConversationID = "AG_20220202_2050081bd0b8cd3f143a"
# r4 = transaction_status(callback_url)
# print(r4.text)


# r5 = b2b('apib2c', 1, '3016005', '4044053', "DisburseFundsToBusiness", callback_url, account_number=1234)
# r6 = b2b('hoseamungai', 2, '4044053', '3016005', "BusinessToBusinessTransfer", callback_url, account_number=1234)



# -------------------------------------PAYMENTS ENGINE ENDPOINTS-------------------------------------
# from step 30.. utility to 40 .. mmf
r1 = b2b('apib2c', 1, '3016005', '4044053', 'DisburseFundsToBusiness', callback_url, account_number)
print(r1.text)

# from 40.. mmf to 30 mmf
r2 = b2b('hoseamungai', 1, '4044053', '3016005', 'BusinessToBusinessTransfer', callback_url, account_number)
print(r2.text)


# from 40 .. utility to 30 mmf 
r3 = b2b('hoseamungai', 1, '4044053', '3016005', 'DisburseFundsToBusiness', callback_url, account_number)
print(r3.text)


# from 30 .. mmf to 30 utility
r4 = b2b('apib2c', 5000, '3016005', '3016005', 'BusinessTransferFromMMFToUtility', callback_url, account_number)
print(r4.text)
