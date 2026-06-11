# Simultaneous prediction of soil properties from VNIR-SWIR spectra using a localized multi-channel 1-D convolutional neural network

## 基本信息

**题目：**
Simultaneous prediction of soil properties from VNIR-SWIR spectra using a localized multi-channel 1-D convolutional neural network

**作者：**
Nikolaos L. Tsakiridis, Konstantinos D. Keramaris, John B. Theocharis, George C. Zalidis

**期刊：**
Geoderma

**年份：**
2020

**DOI：**
10.1016/j.geoderma.2020.114208

**研究方向：**
土壤光谱学（Soil Spectroscopy）、深度学习（Deep Learning）、卷积神经网络（CNN）、多任务学习（Multi-task Learning）

---

## 研究问题

传统VNIR-SWIR土壤光谱建模主要存在以下问题：

1. 每次仅预测单个土壤属性；
2. 通常仅使用一种光谱预处理结果；
3. 全局模型无法充分利用局部相似样本的信息；
4. PLSR、SVR、Cubist等传统机器学习模型难以充分挖掘复杂非线性关系。

作者希望解决的问题是：

**是否能够利用深度学习框架，同时融合多种光谱预处理信息、多个土壤属性之间的相关性以及局部邻域信息，从而提高土壤属性预测精度？**

---

## 数据集

### 数据来源

LUCAS 2009 Topsoil Database

欧洲公开土壤光谱库。

### 数据规模

总样本数：

```text
约20000个样本
```

矿质土样本：

```text
17937个
```

覆盖：

```text
23个欧盟国家
```

### 光谱范围

```text
400–2500 nm
```

原始波段数：

```text
4200
```

### 预处理

删除：

```text
400–500 nm
```

降采样：

```text
每20个点保留1个
```

最终：

```text
200个波段
```

### 使用的6种输入光谱

1. Absorbance
2. SG0 + SNV
3. SG1
4. SG1 + SNV
5. SG2
6. Continuum Removal (CR)

---

### 预测属性

共10个土壤属性：

```text
Clay
Silt
Sand
pH
CEC
SOC (OC)
CaCO3
Total N
P
K
```

---

## 方法

### 整体框架

作者提出：

```text
Multi-Channel
+
Multi-Output
+
Localized Learning
+
1D CNN
```

---

### 第一部分：多通道输入（Multi-channel CNN）

不同预处理结果作为独立输入通道：

```text
Abs
SG0+SNV
SG1
SG1+SNV
SG2
CR
```

类似RGB图像：

```text
R
G
B
```

但这里变成：

```text
6个光谱通道
```

目标：

利用不同预处理中的互补信息。

---

### 第二部分：多输出预测（Multi-output CNN）

传统方法：

```text
一个模型 → 一个属性
```

作者方法：

```text
一个模型
↓
同时预测10个属性
```

输出层：

```text
10个神经元
```

分别对应：

```text
Clay
Silt
Sand
pH
CEC
SOC
CaCO3
N
P
K
```

利用属性间相关性：

```text
Clay ↔ CEC
SOC ↔ N
Sand ↔ Clay
```

---

### 第三部分：局部学习（Localized Learning）

模型训练完成后：

对于每个测试样本：

```text
寻找最相似光谱邻居
```

距离计算：

```text
oPC-M
(Optimal Principal Component Mahalanobis Distance)
```

最佳邻域数：

```text
k = 40
```

利用邻居历史预测误差：

```text
Error Correction
```

修正CNN预测结果。

思想类似：

```text
Global CNN
+
Local KNN Correction
```

---

### CNN结构

输入：

```text
6 × 200
```

第一卷积层：

```text
32 filters
kernel = 7
```

MaxPooling：

```text
2:1
```

第二卷积层：

```text
64 filters
kernel = 7
```

全连接层：

```text
100
↓
40
↓
10
```

输出：

```text
10个土壤属性
```

---

## 创新点

### 创新1

首次明确利用：

```text
多种光谱预处理结果
```

作为CNN多输入通道。

---

### 创新2

构建：

```text
Multi-Output CNN
```

同时预测10种土壤属性。

充分利用属性相关性。

---

### 创新3

提出：

```text
Localized Error Correction
```

利用光谱邻域进行误差修正。

属于：

```text
Global + Local Hybrid Learning
```

思想。

---

### 创新4

研究CNN可解释性。

分析：

- 卷积核权重
- 特征图激活区域
- 重要波段

而非完全黑箱模型。

---

## 实验结果

### 最优模型

```text
local-m-m
```

即：

```text
Multi-channel
+
Multi-output
+
Local Learning
```

---

### Clay

```text
RMSE = 4.80%
R² = 0.86
```

---

### SOC

```text
RMSE = 10.96 g/kg
R² = 0.86
```

---

### Total N

```text
RMSE = 0.66 g/kg
R² = 0.83
```

---

### pH

```text
RMSE = 0.36
R² = 0.93
```

---

### CaCO3

```text
R² = 0.96
```

---

### 最难预测

#### P

```text
R² = 0.42
```

#### K

```text
R² = 0.65
```

说明：

P和K缺乏明显直接光谱响应。

---

### 与传统方法比较

整体性能：

```text
CNN
>
SBL
>
Cubist
≈
SVR
>
PLSR
```

统计检验表明：

```text
local-m-m
显著优于
PLSR
SVR
Cubist
SBL
```

---

## 不足

### 1

仅在LUCAS数据库验证。

泛化能力仍需进一步测试。

---

### 2

需要计算多种预处理光谱。

增加数据准备工作。

---

### 3

局部学习阶段需要搜索邻居。

预测速度低于普通CNN。

---

### 4

对P和K预测效果有限。

说明部分土壤属性无法仅依靠VNIR-SWIR光谱准确预测。

---

### 5

仍属于实验室光谱条件：

```text
风干
过筛
实验室扫描
```

与实际田间环境存在差异。

---

## 是否值得复现

### 非常值得

原因：

#### 学术价值高

属于：

```text
土壤光谱CNN经典论文
```

引用量较高。

---

#### 方法先进

融合：

```text
Multi-channel
Multi-output
Local Learning
```

多个重要思想。

---

#### 数据公开

```text
LUCAS
公开获取
```

可直接复现。

---

#### 与当前研究接轨

后续很多：

```text
CNN
Transformer
Hybrid Network
```

都延续了类似思路。

---

## 对我的启发

### 1

不要只使用一种光谱预处理。

可以尝试：

```text
Raw
SG1
SNV
CR
```

共同输入模型。

---

### 2

SOC预测可结合：

```text
SOC
TN
Clay
CEC
```

进行多任务学习。

---

### 3

局部学习思想值得借鉴。

可尝试：

```text
CNN
+
KNN校正
```

或者：

```text
CNN
+
Memory Bank
```

结构。

---

### 4

模型解释性很重要。

关注：

```text
1400nm
1900nm
2200nm
```

等关键吸收区是否被网络利用。

---

### 5

对于大规模土壤光谱库：

```text
LUCAS
OSSL
GEO-CRADLE
```

深度学习相比传统PLSR具有明显优势。

---

## 个人备注

这是土壤光谱深度学习发展过程中的代表性工作。

论文核心贡献并不仅仅是使用CNN，而是提出：

```text
Multi-source
+
Multi-task
+
Local Learning
```

统一框架。

其思想对后续Transformer、多模态融合和区域适应模型均有参考价值。

对于SOC预测研究而言：

最值得借鉴的是：

```text
多输入通道
+
多任务输出
+
局部误差修正
```

三部分设计。

如果后续开展LUCAS或OSSL复现工作，本论文应作为优先阅读和实现的基准模型之一。
