## 隐写步骤
1. 对秘密图片进行加密
2. 对秘密图片进行henon置乱
3. 对秘密图片进行arnold置乱(抗干扰)
4. 置乱后用LSB写入视频帧蓝色通道中

## 提取步骤
1. 从隐藏了秘密信息的帧中提取出图片
2. 对图片进行逆置乱
3. 用密钥对图片进行解密

## TODO
1. 改进加密算法
2. 增加图像嵌入视频的功能