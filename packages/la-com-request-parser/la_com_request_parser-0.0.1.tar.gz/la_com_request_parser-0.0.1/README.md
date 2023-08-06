# LabAutomation Communication Request Manager

In the context of a physics lab automation project, this package aims to simplify communication with different devices. 
Communication is based on 0mq and json-based messages. This package is meant to be used in combination with a 0mq-based device server.

## Sending a request
The only relevant function to use is ReqParser.request():
Parameters:
/t device: to be addressed device name as string (defined in Device Server)
/t action: requested action as string ("connect", "disconnect", "test", arbitrary)
/t payload: values to be passed for arbitrary action 
        
Returns:
/t status: True (successful) or False (communication request failed)
/t info: string of more detailed information 

