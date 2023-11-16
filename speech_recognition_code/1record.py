import speech_recognition as sr

recognizer = sr.Recognizer()

def record(count):
    
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 4 seconds")
        try:
            recorded_audio = recognizer.listen(source, timeout=4) 
            print("Done recording")
            ###  return recognize_audio(recorded_audio, count)
               
        except sr.exceptions.WaitTimeoutError:
            print("Recording Time out. Please speak while recording")
            ###   re_run_program(count+1)
            
        except sr.exceptions.RequestError:
            print("Failed!!! Please check your internet connection")
            return False
            
        except Exception as ex:
            print(ex)
            return False
        
def recognize_audio(): # parameters later
    pass

def re_run_program(): # parameters later
    pass