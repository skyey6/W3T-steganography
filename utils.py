import cv2 as cv
import os


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
    assert flag, 'can not receive frame...'
    cv.imwrite(out_path, frame)
    cap.release()


def video2Imgs(in_path, out_folder):
    """
    :param in_path: 视频路径
    :param out_folder: 图片存放的文件夹路径
    """
    cap = cv.VideoCapture(in_path)
    assert cap.isOpened(), 'cannot open the video...'

    width = int(cap.get(3))
    height = int(cap.get(4))
    total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))  # 总帧数
    print(total_frames, width, height)

    for i in range(1, total_frames+1):
        flag, frame = cap.read()  # 读取每一张 flag frame
        fileName = f'image_{i}.png'
        if flag:
            cv.imwrite(os.path.join(out_folder, fileName), frame)
    cap.release()


def imgs2Video(in_folder, out_path, fps):
    """
    :param in_folder: 存放图片的文件夹路径（png图片）
    :param out_path: 视频输出路径
    :param fps: 视频帧率
    """
    img_list = os.listdir(in_folder)
    img_list.sort(key=lambda x: int(x.replace("image_", "").split('.')[0]))  # 按照图片名进行排序
    path_list = [os.path.join(in_folder, i) for i in img_list]
    print(path_list)
    img = cv.imread(path_list[0], cv.IMREAD_GRAYSCALE)
    size = (img.shape[1], img.shape[0])
    out = cv.VideoWriter(os.path.join(out_path, "video.mp4"), -1, fps, size)

    for item in path_list:
        if item.endswith('.png'):
            img = cv.imread(item)
            out.write(img)
    out.release()


def png2Jpg(in_path, out_path):
    jpg_img = cv.imread(in_path)
    cv.imwrite(out_path, jpg_img)


if __name__ == '__main__':
    # path = 'video/never_gonna_give_you_up.flv'
    # # getFrame(path, 'img/never800.jpg', 800)
    # inpath = 'video/test.mp4'
    # outpath = 'video/test_invert.mp4'
    # setFrame(inpath, outpath, None)
    # video2Imgs('video/test.mp4', 'temp')
    imgs2Video('temp', 'video', 30)