# Self-supervised and Multi-fidelity Learning for Extended Predictive Soil Spectroscopy

## 基本信息

**题目：**
Self-supervised and Multi-fidelity Learning for Extended Predictive Soil Spectroscopy

**作者：**
Luning Sun et al.

**期刊：**
Geoderma

**年份：**
2026

**DOI：**
10.1016/j.geoderma.2026.117764

**研究方向：**
土壤光谱学（Soil Spectroscopy）、自监督学习（Self-supervised Learning）、多保真学习（Multi-fidelity Learning）、迁移学习（Transfer Learning）、表示学习（Representation Learning）

---

## 研究背景

土壤光谱预测主要依赖两类光谱：

### MIR（Mid-Infrared）

优点：

```text
信息丰富
预测精度高
```

缺点：

```text
设备昂贵
实验室环境
难规模化部署
```

---

### NIR（Near-Infrared）

优点：

```text
便携
成本低
适合现场测量
```

缺点：

```text
预测精度低于MIR
```

---

长期以来存在矛盾：

```text

MIR准确
但昂贵

NIR便宜
但不够准确
```

作者希望：

```text
利用大量MIR数据

帮助NIR预测
```

实现：

```text
MIR精度
+
NIR成本优势
```

---

## 核心思想

论文提出：

```text
Unified Latent Space
统一潜空间
```

假设：

```text
MIR
↓

基础振动信息
```

与

```text
NIR
↓

倍频与组合频信息
```

来源于相同物理机制。

因此：

```text
MIR和NIR

存在共同隐藏表示
```

---

整体框架：

```text
大量MIR
        ↓

自监督预训练

        ↓

学习潜空间

        ↓

NIR映射到该空间

        ↓

预测土壤属性
```

属于：

```text
Self-Supervised Learning

+

Transfer Learning

+

Multi-Fidelity Learning
```

结合。

---

## 数据集

### KSSL MIR数据库

来源：

```text
USDA KSSL
```

规模：

```text
83971个土壤样本

334665次扫描
```

用途：

```text
自监督预训练
```

---

### 配对NIR-MIR数据库

规模：

```text
1976个样本
```

同时拥有：

```text
NIR

MIR
```

用途：

```text
多保真学习
```

---

### 独立测试集

NAPT数据库：

```text
206个样本
```

用途：

```text
独立验证
```

---

## 预测目标

共9个土壤属性：

### 碳相关

```text
TC
总碳

TN
总氮

IC
无机碳

EOC
有机碳
```

---

### 化学性质

```text
pH

CEC
阳离子交换量
```

---

### 质地

```text
Clay

Silt

Sand
```

---

## 数据预处理

### 光谱转换

反射率：

```text
R
```

转换为：

```text
A = log10(1/R)
```

伪吸光度。

---

### SNV标准化

使用：

```text
Standard Normal Variate
```

消除：

```text
散射效应

偏移效应
```

---

### 变量变换

除：

```text
pH

Clay

Silt

Sand
```

外：

```text
log(x+1)
```

变换。

---

### 组成数据处理

对于：

```text
Clay

Silt

Sand
```

使用：

```text
ILR

Isometric Log Ratio
```

变换。

---

## 方法

论文包含三个阶段。

---

## Stage 1

### 自监督学习

使用：

```text
Variational Autoencoder
(VAE)
```

结构：

```text
MIR
 ↓
Encoder
 ↓
Latent Space
 ↓
Decoder
 ↓
MIR
```

目标：

```text
重建原始MIR
```

无需标签。

---

### 潜空间学习

原始光谱：

```text
1700维
```

压缩到：

```text
32维
```

压缩约：

```text
50倍
```

---

### 维度比较

| Latent维度 | Reconstruction Error |
| ---------- | -------------------- |
| 16         | 0.0338               |
| 32         | 0.0226               |
| 64         | 0.0211               |

最终选择：

```text
32维
```

因为性能与复杂度平衡最佳。

---

## Stage 2

### 多保真学习

目标：

```text
NIR
↓

预测MIR表示
```

训练：

```text
NIR Encoder
```

映射：

```text
NIR
 ↓
Latent Space
 ↓
固定MIR Decoder
 ↓
MIR
```

实现：

```text
NIR → MIR
```

转换。

---

### 优势

能够利用：

```text
大规模MIR知识
```

提升：

```text
小规模NIR预测
```

能力。

---

## Stage 3

### 土壤属性预测

使用：

```text
Latent Features
```

预测：

```text
TC
TN
IC
EOC
pH
CEC
Clay
Silt
Sand
```

---

## 对比模型

作者建立：

### MIR模型

```text
MIR-PLSR

MIR-MLP

MIR-SSL-MLP
```

---

### NIR模型

```text
NIR-PLSR

NIR-MLP
```

---

### 多保真模型

```text
NIRtoMIR-MLP

NIRtoMIR-SSL-MLP
```

---

## 创新点

### 创新1

首次系统结合：

```text
自监督学习

+

多保真学习
```

用于土壤光谱。

---

### 创新2

提出：

```text
统一潜空间
```

思想。

---

### 创新3

利用：

```text
MIR预训练
```

帮助：

```text
NIR预测
```

---

### 创新4

将：

```text
表示学习
```

引入土壤光谱领域。

---

## 结果

### MIR模型

平均CCC：

```text
≈0.82
```

---

### MIR + SSL

平均CCC：

```text
≈0.91
```

达到最佳结果。

---

典型结果：

### TC

```text
0.95
↓

0.98
```

---

### Sand

```text
0.68
↓

0.92
```

---

### Silt

```text
0.54
↓

0.89
```

---

说明：

```text
潜空间表示

优于

原始光谱
```

---

## NIR迁移结果

普通NIR：

```text
平均CCC ≈ 0.51
```

---

NIR→MIR迁移：

```text
平均CCC ≈ 0.61
```

提升约：

```text
20%
```

---

其中：

### Silt

```text
0.18

↓

0.55
```

---

### Sand

```text
0.29

↓

0.57
```

接近翻倍。

---

说明：

```text
MIR知识

成功迁移到

NIR模型
```

---

## 潜空间解释性分析

作者分析：

```text
32个Latent Features
```

与MIR波段关系。

发现：

```text
部分特征
对应碳酸盐吸收峰

部分特征
对应有机质吸收峰
```

---

说明：

```text
潜空间

具有物理意义
```

并非完全黑箱。

---

## 可靠性分析

作者发现：

```text
验证集性能

高于

独立测试集
```

原因：

```text
数据分布偏移
```

即：

```text
Distribution Shift
```

问题。

---

因此提出：

```text
未来需加入

不确定性估计
```

机制。

---

## 不足

### 1

仅使用：

```text
VAE
```

未测试：

```text
Transformer

MAE

SimCLR

MoCo
```

---

### 2

NIR→MIR仍有信息损失。

部分波段：

```text
3750–3000 cm⁻¹

2000–1750 cm⁻¹

1250–1100 cm⁻¹
```

误差明显。

---

### 3

尚未形成真正Foundation Model。

仍属于：

```text
Representation Learning
```

阶段。

---

### 4

未进行跨国家验证。

---

## 是否值得复现

### 非常值得

原因：

#### 学术价值

代表：

```text
土壤光谱

下一代建模框架
```

---

#### 与当前趋势一致

```text
Self-Supervised

Transfer Learning

Foundation Model
```

路线。

---

#### 可扩展

未来可替换：

```text
VAE

↓

Transformer
```

---

#### 与OSSL兼容

能够直接利用：

```text
OSSL

KSSL

LUCAS
```

大规模光谱库。

---

## 对我的启发

### 1

未来模型重点：

```text
先学光谱

再学标签
```

而非直接回归。

---

### 2

大规模无标签光谱价值巨大。

---

### 3

MIR可作为：

```text
教师模型
```

指导：

```text
NIR学生模型
```

训练。

---

### 4

可以尝试：

```text
VAE

→

Transformer Encoder
```

升级。

---

### 5

可作为：

```text
Soil Foundation Model
```

的重要前置工作。

---

## 个人备注

Sun et al. (2026) 是目前土壤光谱领域最接近 Foundation Model 思想的工作之一。

其核心贡献不是预测精度，而是提出：

```text
大规模MIR预训练

↓

统一潜空间

↓

跨传感器迁移

↓

土壤属性预测
```

路线。

在知识体系中的位置：

```text
PLSR时代
        ↓

Bogner 2014
(SMOTE)

        ↓

Padarian 2019
(CNN)

        ↓

Piccoli 2023
(Multi-output CNN)

        ↓

Sun 2026
(Self-Supervised + Multi-Fidelity)

        ↓

未来
Soil Foundation Model
```
