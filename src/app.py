'''
Copyright (c) 2022, Shubhankar Valimbe
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

'''

import requests

# returns converted currency value as a string
def convert(covertFrom:str, convertTo:str, amount:str):

  if not amount.isnumeric() or int(amount) == 0: # check if input amount is valid.
    return "Please enter a valid value."

  url = f"https://api.apilayer.com/exchangerates_data/convert?to={convertTo}&from={covertFrom}&amount={amount}"

  payload = {}
  headers = {
      "apikey": "aVyVAFn0x3ShLrFGkmSXYHPhppJZZwr6"
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  # status_code = response.status_code
  resDict = response.json() # converts to Python dict

  return str(round(resDict['result'], 2))

# sample response
# {'success': True, 'query': {'from': 'USD', 'to': 'INR', 'amount': 50}, 'info': {'timestamp': 1667932683, 'rate': 87.999774}, 'date': '2022-11-08', 'result': 4399.9887}
