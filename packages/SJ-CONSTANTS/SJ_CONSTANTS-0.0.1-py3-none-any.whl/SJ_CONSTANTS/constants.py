"""
 MIT License

Copyright (c) 2022 BertVanAcker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class EmbeddedConstants:
    """
    EmbeddedConstants: Class representing the constants used at the embedded link
    """
    
    #--------------------  
    # ----- General -----
    #--------------------
    STEAMJACK_SERIAL_VERSION = "0.0.1"
    STEAMJACK_UDP_VERSION = "0.0.1"
    STEAMJACK_BLE_VERSION = "0.0.1"
    
    #---------------------    
    # ----- commands -----
    #---------------------
    
    LOOP_COMMAND = 0
    DISCOVERY = 1 
    GET_FIRMWARE_VERSION = 2
    SET_PIN_MODE = 3  
    DIGITAL_WRITE = 4  
    ANALOG_WRITE = 5
    RESET = 99
    

    #----------------------   
    # ----- Reporting -----
    #----------------------
    FEATURES = 20
    DEBUG_PRINT = 99
    REPORTING_DISABLE_ALL = 0
    ENABLE_ALL_REPORTS = 1
    STOP_ALL_REPORTS = 2
    MODIFY_REPORTING = 3
    
    

    #--------------------------   
    # ----- MBD PIN MODES -----
    #--------------------------
    MBD_INPUT = 0
    MBD_OUTPUT = 1
    MBD_INPUT_PULLUP = 2
    MBD_ANALOG = 3
    MBD_MODE_NOT_SET = 255
    
    #--------------------- 
    # ----- MBD PINs -----
    #---------------------
    NUMBER_OF_DIGITAL_PINS = 20
    NUMBER_OF_ANALOG_PINS = 20
