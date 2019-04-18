'''
Updated on April 14, 2019

@author: Jaydeep Shah
@author: Venkat Prasad Krishnamurthy
'''


from mat import mat

def on_connect_sub(clientSub, userdata, flags, rc):
    RC = connack_string(rc)
    print("Connected with result code "+ RC)
    clientSub.subscribe("matsensor", 1)
    print("MatSensor")
    clientSub.subscribe("useractivity", 1)
    print("UserActivity")

def connack_string(rc):
    switcher = {
    0: "0: Connection Successful",
    1: "1: Connection refused - incorrect protocol version", 
    2: "2: Connection refused - invalid clientSub identifier",
    3: "3: Connection refused - server unavailable",
    4: "4: Connection refused - bad username or password",
    5: "5: Connection refused - not authorised"   
    }
    return switcher.get(rc, "Invalid response code")

def on_message(client, userdata, msg):
    sdd = msg.payload.decode()
    print(msg.topic+" "+ sdd)
    
    if (msg.topic == "matsensor"):
        print("It was matsensor")
        if (sdd == "on"):
            MAT1 = mat()
            MAT1.start()
        else:
            print("You published the data")    
        
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

'''
This function is called after publish call is executed.
'''        
def on_publish(client, userdata, mid):
    print("Published message successfully.")

'''
This function is called after subscribe call is executed.
'''    
def on_subscribe(client, userdata, mid, granted_qos):
    print (client + " " + userdata+ " "  + mid+ " "  + granted_qos)

'''
This function is called after unsubscribe call is executed.
'''    
def on_unsubscribe(client, userdata, mid):
    print("Topic is unsubscribed")
    print(client + ": " + userdata +" " + mid)
