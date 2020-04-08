import numpy as np
import cv2
import requests
import io
import json
img=cv2.imread("image.png")

height,width,_=img.shape

roi=img[0:height,0:width]

url_api="https://api.ocr.space/parse/image"
_,compressedimage=cv2.imencode(".png",roi,[1,90])
file_bytes=io.BytesIO(compressedimage)
result= requests.post(url_api,files={"image.png":file_bytes},
              data={"apikey":"b62b4d3a9588957"},
              )
result=result.content.decode()
result=json.loads(result)
text=result.get("ParsedResults")[0].get("ParsedText")
print(text)
cv2.imshow("Image",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()