import cv2 as cv


def getFrame(in_path, out_path, frame_num):
    """
    :param in_path: 目标视频的路径
    :param out_path: 提取帧存放的路径
    :param frame_num: 要获取第几帧
    :return:
    """
    cap = cv.VideoCapture(in_path)  # 返回一个capture对象
    cap.set(cv.CAP_PROP_POS_FRAMES, frame_num-1)
    flag, frame = cap.read()  # read方法返回一个布尔值和一个视频帧。若帧读取成功，则返回True
    # print(flag)
    assert flag, '提取失败...'
    cv.imwrite(out_path, frame)


def png2jpg(in_path, out_path):
    jpg_img = cv.imread(in_path)
    cv.imwrite(out_path, jpg_img)


if __name__ == '__main__':
    path = 'video/never_gonna_give_you_up.flv'
    getFrame(path, 'img/never800.jpg', 800)

