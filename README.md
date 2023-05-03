# zte-networks-evaluation
中兴捧月自智网络赛道模拟评估脚本



注意：

1. **该脚本仅适用于第一阶段的模拟评估**；
2. **gt文件夹中的结果并不是正确答案，而是接近正确答案**；
3. **为了完成100个星系的评估，我将数据集拷贝了一份，请将data文件夹中的数据也对应拷贝一份，并确保名称与gt中的名称是一致的**。



## 脚本工作原理

`evaluation.py`将删除`data`文件夹中的`result.txt`（如有），然后运行`main.py`生成`result.txt`，根据官网给出的评估公式计算评估结果。



## 评估脚本使用方法

1. 将`main.py`和`evaluation.py`置于同一目录中
2. 将`gt`文件夹置于`evaluation.py`的上层目录
3. 运行`evaluation.py`脚本

