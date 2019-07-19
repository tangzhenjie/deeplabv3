# DeepLab-v3 Semantic Segmentation in TensorFlow
##动机
本项目参照https://github.com/rishizek/tensorflow-deeplab-v3 的代码，使用tensorflow低阶api重新实现了一下。
本项目的是：由于熟悉tensorflow低阶api而对estimator不是太熟悉。同时又想使用deeplabv3来分割自己的数据集。
所以先保证deeplab实现的正确性。为以后使用打基础。

## 实现结果
我们只跑了一下Resnet50的结果69.87%， 论文上Resnet101结果是77.21%

|       |Method                                | OS  | mIOU       |
|:-----:|:------------------------------------:|:---:|:----------:|
| paper | MG(1,2,4)+ASPP(6,12,18)+Image Pooling|16   | 77.21%     | 
| repo  | MG(1,2,4)+ASPP(6,12,18)+Image Pooling|16   | **69.87%** |

图片结果：
<p align="center">
  <img src="images/Image1.png" width=500 height=250>
</p>
<p align="center">
  <img src="images/Image2.png" width=500 height=250>
</p>

###分析原因
Resnet101可能效果更好，同时原始论文上有一些训练trick,我们没有实现。