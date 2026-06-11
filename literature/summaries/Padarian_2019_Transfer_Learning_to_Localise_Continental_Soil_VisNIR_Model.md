# Transfer learning to localise a continental soil vis-NIR calibration model

## 基本信息

**题目：**
Transfer learning to localise a continental soil vis-NIR calibration model

**作者：**
J. Padarian, B. Minasny, A.B. McBratney

**期刊：**
Geoderma

**年份：**
2019

**DOI：**
10.1016/j.geoderma.2019.01.009

**研究方向：**
土壤光谱学（Soil Spectroscopy）、迁移学习（Transfer Learning）、领域适应（Domain Adaptation）、深度学习（Deep Learning）

---

## 研究问题

随着LUCAS、RaCA等大型土壤光谱库的发展，研究者越来越倾向于使用大规模光谱库建立统一模型。

但存在一个核心问题：

```text
全球模型
↓
本地应用
```

往往效果下降。

原因在于：

```text
全球模型
学习的是普适规律

本地模型
学习的是区域特征
```

两者之间存在：

```text
Domain Shift
（领域偏移）
```

传统方法主要有：

### Spiking

```text
Global Dataset
+
Local Samples
↓
重新建模
```

### Sub-setting

```text
Global Dataset
↓
选相似样本
↓
Local Model
```

二者均存在局限。

作者希望验证：

**是否能够利用迁移学习（Transfer Learning）将大陆尺度模型有效迁移到国家尺度，从而兼顾全球知识和本地特征。**

---

## 数据集

### 数据来源

LUCAS Soil Database

欧洲最大公开土壤光谱库。

---

### 数据规模

```text
约20000个土壤样本
```

覆盖：

```text
21个欧洲国家
```

包括：

```text
France
Spain
Germany
Sweden
Poland
Finland
Italy
United Kingdom
...
```

---

### 光谱范围

```text
400–2500 nm
```

分辨率：

```text
0.5 nm
```

总波段数：

```text
4200
```

---

### 预测属性

共4个土壤属性：

#### OC

```text
Organic Carbon
有机碳
```

#### CEC

```text
Cation Exchange Capacity
阳离子交换量
```

#### Clay

```text
粘粒含量
```

#### pH

```text
土壤酸碱度
```

---

## 方法

### 整体思想

作者提出：

```text
Global Model
↓
Transfer Learning
↓
Local Model
```

实现：

```text
知识迁移
Knowledge Transfer
```

---

### 光谱转换

作者没有直接使用原始光谱。

而是将：

```text
4200维光谱
```

转换为：

```text
Spectrogram
```

即：

```text
短时傅里叶变换(STFT)
```

生成二维图像。

---

转换后尺寸：

```text
51 × 83
```

输入CNN。

---

### CNN结构

采用多任务CNN。

输入：

```text
Spectrogram
```

---

共享层：

```text
Conv 3×3 64

MaxPool

Conv 3×3 128

Conv 3×3 256

MaxPool

Conv 3×3 512
```

---

属性分支：

```text
OC

CEC

Clay

pH
```

分别建立独立预测头。

---

输出：

```text
同时预测4个属性
```

---

### 三种模型

#### 1 Local Model

仅使用本国数据。

例如：

```text
法国模型
仅使用法国样本
```

---

#### 2 Global Model

使用：

```text
欧洲数据
-
目标国家数据
```

训练。

例如：

```text
法国测试

训练集=
欧洲
-
法国
```

---

#### 3 Transfer Model

步骤：

##### Step 1

训练Global Model

```text
Europe
↓
CNN
```

---

##### Step 2

截取前6层

```text
Conv1

Pool1

Conv2

Conv3

Pool2

Conv4
```

---

##### Step 3

冻结这些层

```text
权重不更新
```

---

##### Step 4

利用本地数据训练后续层

```text
Fine-Tuning
```

实现：

```text
Global Knowledge
+
Local Adaptation
```

---

## 创新点

### 创新1

首次系统将：

```text
Transfer Learning
```

引入土壤光谱建模。

---

### 创新2

提出：

```text
Global
↓
Transfer
↓
Local
```

完整迁移框架。

---

### 创新3

验证：

```text
大陆级模型
↓
国家级应用
```

可行性。

---

### 创新4

证明：

```text
Transfer Model
```

优于：

```text
Global Model

和

Local Model
```

---

### 创新5

提出：

```text
知识共享
Knowledge Sharing
```

思想。

大型光谱库不仅服务全球建模。

也可增强局部模型。

---

## 实验结果

### 实验设计

```text
21个国家
×
4个属性
```

共：

```text
84种实验组合
```

---

### 总体结果

Transfer Model：

```text
76 / 84
```

情况下效果最好。

比例：

```text
90.5%
```

---

### OC

平均RMSE下降：

```text
10.5%
```

---

### CEC

平均RMSE下降：

```text
11.8%
```

---

### Clay

平均RMSE下降：

```text
12.0%
```

---

### pH

平均RMSE下降：

```text
11.5%
```

---

### 国家级结果

作者发现：

```text
18个国家
```

至少有一个属性显著改善。

---

其中：

```text
4个国家
```

四项属性全部显著改善。

---

### Transfer优势

对于：

```text
法国
德国
西班牙
波兰
捷克
立陶宛
```

等国家。

Transfer模型明显优于：

```text
Global

和

Local
```

模型。

---

## 不足

### 1

仅研究：

```text
OC
CEC
Clay
pH
```

未研究：

```text
SOC
TN
CaCO3
K
P
```

等属性。

---

### 2

研究尺度为：

```text
大陆
→
国家
```

未进一步验证：

```text
国家
→
区域

区域
→
田块
```

迁移能力。

---

### 3

采用固定超参数。

未针对各国家单独优化。

---

### 4

使用CNN。

未比较：

```text
Transformer
Attention
Graph Network
```

等新模型。

---

### 5

仍基于实验室光谱。

未涉及：

```text
无人机高光谱

机载高光谱

卫星高光谱
```

应用。

---

## 是否值得复现

### 非常值得

原因：

#### 理论价值高

属于：

```text
土壤光谱迁移学习经典论文
```

---

#### 思想先进

提出：

```text
Global Knowledge
+
Local Adaptation
```

框架。

---

#### 数据公开

使用：

```text
LUCAS
```

可获取。

---

#### 与当前研究高度相关

直接关联：

```text
OSSL

Foundation Model

Transformer

Domain Adaptation
```

等方向。

---

## 对我的启发

### 1

大型光谱库价值不仅在于建模。

更在于：

```text
知识迁移
```

---

### 2

未来可采用：

```text
OSSL
↓
Pre-training
↓
Local Fine-Tuning
```

模式。

---

### 3

对于SOC预测：

```text
湖南
新疆
东北
```

应考虑区域适应。

而非直接使用统一模型。

---

### 4

Transformer同样适合：

```text
Transfer Learning
```

框架。

---

### 5

未来可探索：

```text
Global Spectral Foundation Model
```

构建。

---

## 个人备注

这篇论文是土壤光谱迁移学习领域的重要里程碑。

相比Liu（2018）证明迁移学习可行，

Padarian（2019）进一步在：

```text
21个国家
84组实验
```

上系统验证了迁移学习的有效性。

论文核心贡献不是CNN，而是证明：

```text
Global Model
+
Transfer Learning
```

能够稳定优于：

```text
Global Model

或

Local Model
```

其思想与今天的：

```text
Pre-training
+
Fine-Tuning
+
Foundation Model
```

路线高度一致。

对于未来基于OSSL构建土壤光谱大模型具有重要参考价值。
