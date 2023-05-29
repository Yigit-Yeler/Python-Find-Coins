# Ödevi yapanlar
# Yiğit Yeler 1200505021
# Yasemin Karaloğlu 1200505004


import cv2
import numpy as np


def find_coins(image_path):

    image = cv2.imread(image_path)

    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(grey, 50, 150, apertureSize=3)

    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1,
                               minDist=35, param1=50, param2=30, minRadius=10, maxRadius=50)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        tl = 0
        euro = 0

        markers = np.zeros(grey.shape, dtype=np.int32)

        for (x, y, r) in circles:
            cv2.circle(markers, (x, y), r, (255, 255, 255), -1)

            if r >= 45:
                deger = "1 TL"
                tl += 1
            elif r >= 42 and r < 45:
                deger = "1 Euro"
                euro += 1
            elif r >= 39 and r < 42:
                deger = "20 Cent"
                euro += 0.20
            elif r >= 38 and r < 39:
                deger = "25Kurus"
                tl += 0.25
            elif r >= 35 and r < 38:
                deger = "10 Kurus"
                tl += 0.10
            else:
                deger = "5 Kurus"
                tl += 0.5

            cv2.putText(image, deger, (x - 40, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.watershed(image, markers)
        image[markers == -1] = [0, 255, 0]

        cv2.putText(image, "Toplam TL: {}".format(tl),
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(image, "Toplam Euro: {}".format(euro),
                    (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        if image_path == 'image1.jpg':
            cv2.imwrite("result1.jpg", image)
        elif image_path == 'image2.jpg':
            cv2.imwrite("result2.jpg", image)
        elif image_path == 'image3.jpg':
            cv2.imwrite("result3.jpg", image)

        cv2.imshow("Coin", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']

for image_path in image_paths:
    find_coins(image_path)
