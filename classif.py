import cv2
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import numpy as np
import pafy
import youtube_dl

def analyse(url):
        
    vPafy = pafy.new(url)

    play = vPafy.getbest(preftype = "mp4")

    cap = cv2.VideoCapture(play.url)


    sample_rate = 80


    model = tf.keras.models.load_model('model_cnn2.h5')
    key = 0

    while key == 0 :
        ret, frame = cap.read()
        if not ret:
            break

        
        if cap.get(cv2.CAP_PROP_POS_FRAMES) % sample_rate == 0:
            
    
            frame = cv2.resize(frame, (251, 251))

        
            frame = frame / 255.0
            frame = np.expand_dims(frame, axis=0)
        
        

            detections = model.predict(frame, batch_size=1)

            
            for detection in detections:  
                confidence = detection  
                
                if confidence > 0.94:  
                    smoking_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
                    smoking_frame_minute = smoking_frame // 1800
                    smoking_frame_second = (smoking_frame - smoking_frame_minute * 1800) // 30
                    print("Обнаружен кадр с курением на", smoking_frame_minute, ':', smoking_frame_second)
                    return True
                    # key = 1  
                break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break        
    key = 1   
    # Освободите ресурсы
    cap.release()
    cv2.destroyAllWindows()
    return False