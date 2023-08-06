    # def get_circle(self, img, fname):
    #     np_img = np.array(transforms.ToPILImage()(img[0]))
    #     cv_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
    #     gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    #     blr = cv2.GaussianBlur(gray, (0, 0), 1)
    #     # circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
    #     #                             param1=150, param2=40, minRadius=400,maxRadius=500)
    #     # circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
    #     #                             param1=150, param2=40, minRadius=500,maxRadius=600)

    #     # if len(circles) != 1:
    #     #     print("ERROR for the number of circles: ", fname)
    #     # else:
    #     #     c = np.array(circles[0][0], np.int32)
    #     #     img_ = cv2.circle(np_img, (c[0], c[1]), c[2], (255, 0, 0), 4)
    #     #     print(img_.shape)
    #     #     plt.scatter(c[0], c[1], c='r')
    #     #     plt.imshow(img_)
    #     #     plt.show()

    #     return cv_img, c[0], c[1], c[2]

    # def exceptions(self, tensor_pred, cx, cy, r, offset1, offset2):
    #     # tensor_pred = np.array(transforms.ToPILImage()(tensor_pred[0].byte()))
    #     idxes = np.where(tensor_pred == 64)
    #     # print(tensor_pred.shape)
    #     for x, y in zip(idxes[0], idxes[1]):
    #         if math.sqrt((cx - x)**2 + (cy - y)**2) > r - offset1//2 and \
    #             math.sqrt((cx - x)**2 + (cy - y)**2) < r + offset1:
    #             tensor_pred[idxes[0], idxes[1]] = 0
            
    #         if math.sqrt((cx - x)**2 + (cy - y)**2) > r + offset2:
    #             tensor_pred[idxes[0], idxes[1]] = 0


    #     # tensor_pred = cv2.circle(tensor_pred, (cx, cy), r - offset1//2, (255, 0, 0), 1)
    #     # tensor_pred = cv2.circle(tensor_pred, (cx, cy), r + offset1, (255, 0, 0), 1)
    #     # plt.imshow(tensor_pred)
    #     # plt.show()

    #     return tensor_pred