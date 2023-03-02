#@title  { vertical-output: true }
#@title { form-width: "500%", display-mode: "form" }
import os
import sys
import subprocess
from IPython.display import display, HTML, Javascript, clear_output
#from google.colab import files
from discount_check import FetchOptionData
import datetime

from py5paisa import (
    FivePaisaClient,
    InvalidLoginCredentialsException,
    InvalidFutureExpiryDateException,
    InvalidLoginException,
    FetchExpiryException,
    InvalidOptionExpiryDateException,
    FuturesFetchException, 
    SpotFetchException, 
    OptionChainFetchException,
    getEpochTime,
    convertTimeString
    )

sys.tracebackit = 0

EMAIL = "asanjay96@gmail.com"
PASSWORD_5PAISA = "asdf@1243"
DOB_YYYYMMDD = "19960215"

APP_NAME = "5P50882761"
APP_SOURCE = "15267"
USER_ID = "zMy0tlSzFnE"
PASSWORD = "TDfHLJOvfKv"
USER_KEY = "hxeNKd4GUOGvdUr3CDnmxEPvQQbxK7j1"
ENCRYPTION_KEY = "Ap1jaV5ABAGOSerMUd4UAOQWsz03GGK0"

CREDS = {'APP_NAME':APP_NAME, 
         'APP_SOURCE':APP_SOURCE,
         'USER_ID': USER_ID,
         'PASSWORD': PASSWORD,
         'USER_KEY': USER_KEY,
         'ENCRYPTION_KEY': ENCRYPTION_KEY}
display(HTML("<h2 style='color: #00D100'>Credentials Added</h2>"))
print("Credentials Added")

INCLUDE_NIFTY = True #@param { type: 'boolean' }
INCLUDE_BANKNIFTY = True #@param { type: 'boolean' }
INCLUDE_FINNIFTY = False #@param { type: 'boolean' }
#@markdown __________________________________

BNF_NIFTY_FUT_EXPIRY = "2023-03-29" #@param { type: 'date' }
FINNIFTY_FUT_EXPIRY = "2023-03-28" #@param { type: 'date' }
#@markdown __________________________________

BNF_NIFTY_FUT_EXPIRY_ = convertTimeString(BNF_NIFTY_FUT_EXPIRY)
FINNIFTY_FUT_EXPIRY_ = convertTimeString(FINNIFTY_FUT_EXPIRY)

BNF_NIFTY_EXPIRY = "2023-03-02" #@param { type: 'date' }
FINNIFTY_EXPIRY = "2023-03-06" #@param { type: 'date' }

print(11111111111111111)

BNF_NIFTY_EXPIRY_ = getEpochTime(BNF_NIFTY_EXPIRY)
FINNIFTY_EXPIRY_ = getEpochTime(FINNIFTY_EXPIRY)

print(BNF_NIFTY_EXPIRY_)
print(FINNIFTY_EXPIRY_)

STREAM_DATA = True #@param { type: 'boolean' }
print(BNF_NIFTY_EXPIRY_)
print(FINNIFTY_EXPIRY_)
if STREAM_DATA:
  if INCLUDE_NIFTY or INCLUDE_BANKNIFTY or INCLUDE_FINNIFTY:
    try:
      option_chain = FetchOptionData(
        CREDS, EMAIL, 
        PASSWORD_5PAISA, DOB_YYYYMMDD, 
        BNF_NIFTY_EXPIRY_, FINNIFTY_EXPIRY_,
        INCLUDE_NIFTY, INCLUDE_BANKNIFTY, INCLUDE_FINNIFTY,
        BNF_NIFTY_FUT_EXPIRY_, FINNIFTY_FUT_EXPIRY_)
      
      option_chain.stream()

    except (FetchExpiryException, InvalidLoginException, 
            InvalidLoginCredentialsException, InvalidFutureExpiryDateException,
            InvalidOptionExpiryDateException, OptionChainFetchException,
            FuturesFetchException, SpotFetchException, 
            OptionChainFetchException) as e:
      pass
    except KeyboardInterrupt: 
      clear_output(wait=True)
    
      display(HTML("<h2 style='color: #FF4500'>Error : Option Chain fetch interrupted</h2>"))
  else:
    display(HTML(f"<h2 style='color: #FD7F20'>Select atleast one index</h2>"))

