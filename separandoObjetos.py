import cv2

img = cv2.imread('imagemTesteElementos.jpg')
img = cv2.resize(img,(600,500))

imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgCanny = cv2.Canny(imgCinza,30,200)
imgClose = cv2.morphologyEx(imgCanny,cv2.MORPH_CLOSE,(7,7))

contours, hierarchy = cv2.findContours(imgClose,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

numOb = 1
for cnt in contours:
# #    cv2.drawContours(img,cnt,-1,(255,0,0),2)
     x,y,w,h = cv2.boundingRect(cnt)
     objeto = img[y:y+h,x:x+w]
     cv2.imwrite(f'objetos/objeto{numOb}.jpg',objeto)
     cv2.rectangle(img,(x,y),(x+w,h+y),(255,0,0),2)
     numOb += 1


cv2.imshow('Imagem', img)
# cv2.imshow('Imagem Cinza', imgCinza)
# cv2.imshow('Imagem Canny', imgCanny)

cv2.waitKey(0)