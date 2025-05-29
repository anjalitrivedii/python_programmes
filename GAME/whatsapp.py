import pywhatkit as kit
import datetime
def send_whatsapp_message(phone_number,message,hour,minute):
    now = datetime.datetime.now()

    #Ensure the time is in the future
    if (hour < now.hour) or (hour == now.hour and minute <= now.minute):
        print("The specified time is in the past. Please set a future time. ")
        return
    try:
        #Schedule the message
        kit.sendwhatmsg(phone_number,message,hour,minute)
        print("Message scheduled successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

#Example usage (make sure to replace with a valid phone number)
send_whatsapp_message("+918320656936","hello from python!!",10,39)