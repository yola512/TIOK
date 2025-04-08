from numpy.ma.core import bitwise_or
import cv2
          import numpy as np

          circle = np.zeros((300,300), dtype='uint8')
          cv2.circle(circle, (150, 150), 100, 255, -1)

          rectangle = np.zeros((250,250), dtype='uint8')
          cv2.rectangle(rectangle, (25, 30), (250, 250), 255, -1)

          cv2.imshow("Rectangle", rectangle)
          cv2.imshow("Circle", circle)

          bitwiseOR = cv2.bitwise_or(rectangle, circle)
          bitwiseAND = cv2.bitwise_and(rectangle, circle)
          bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
          bitwiseNOT = cv2.bitwise_not(rectangle, circle)

          cv2.imshow("OR", bitwiseOR)
          cv2.imshow("NOT", bitwiseNOT)
          cv2.imshow("XOR", bitwiseXOR)
          cv2.imshow("AND", bitwiseAND)

          cv2.waitKey(0)
          cv2.destroyAllWindows()
