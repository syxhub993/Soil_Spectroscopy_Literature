# Open Soil Spectral Library (OSSL): Building Reproducible Soil Calibration Models Through Open Development and Community Engagement

## 基本信息

* 标题：
  * Open Soil Spectral Library (OSSL): Building Reproducible Soil Calibration Models Through Open Development and Community Engagement
* 作者：
  * Safanelli et al.
* 年份：
  * 2025
* 期刊：
  * PLOS ONE
* DOI：
  * 10.1371/journal.pone.0322391
* Github：
  * OSSL官方仓库（论文提供）
* 数据地址：
  * Open Soil Spectral Library (OSSL)

---

## 研究问题

### 研究目标

* 构建全球开放土壤光谱数据库（OSSL）。
* 统一不同国家、实验室和仪器采集的土壤光谱数据。
* 建立可复现的土壤属性预测模型框架。
* 提供开放数据、开放代码和开放模型。
* 提高土壤光谱模型的跨区域泛化能力。

### 预测土壤属性

主要包括：

* Soil Organic Carbon (SOC)
* Total Carbon (TC)
* Total Nitrogen (TN)
* Clay
* Sand
* Silt
* pH
* CEC
* Bulk Density
* Exchangeable Cations
* Electrical Conductivity (EC)

### 任务类型

* 土壤属性回归预测
* 光谱建模
* 全球土壤光谱库构建
* 不确定性估计
* OOD（Out-of-Distribution）检测

### 应用场景

* 精准农业
* 数字土壤制图
* 土壤监测
* 全球土壤调查
* 土壤碳核算
* 光谱大模型训练

---

## 数据集

### 数据集名称

* Open Soil Spectral Library（OSSL）

---

### 数据来源

整合多个公开光谱库：

* KSSL（美国）
* LUCAS（欧洲）
* AfSIS（非洲）
* ICRAF-ISRIC
* CAF
* Serbia Soil Library
* Garrett Soil Library
* 以及其他公开数据库

---

### 样本数量

| 光谱类型       | 样本数  |
| -------------- | ------- |
| VisNIR         | >60,000 |
| MIR            | >80,000 |
| NeoSpectra NIR | 2,106   |

总样本量：

```text
130,000+
```

---

### 光谱范围

#### VisNIR

```text
350–2500 nm
```

#### MIR

```text
600–4000 cm⁻¹
```

#### NeoSpectra

```text
1350–2550 nm
```

---

### 波段数量

统一重采样：

#### VisNIR

```text
2 nm interval
```

#### MIR

```text
2 cm⁻¹ interval
```

---

### 标签类型

实验室测定属性：

* SOC
* TN
* Clay
* pH
* CEC
* EC
* 等

属于：

```text
监督回归任务
```

---

### 数据划分方式

采用：

```text
Training
Validation
Independent Test
```

并使用：

```text
Cross Validation
```

进行模型选择。

---

### 是否公开

```text
是
```

特点：

* 数据公开
* 模型公开
* 代码公开
* 可复现

---

## 方法

### 输入数据

输入：

```text
土壤反射光谱
```

包括：

* VisNIR
* MIR
* NeoSpectra

---

### 光谱预处理

主要采用：

#### SNV

```text
Standard Normal Variate
```

作用：

* 消除散射效应
* 降低粒径影响
* 降低仪器差异

---

### 光谱标准化

统一：

* 波段范围
* 波长间隔
* 光谱格式

实现跨数据库融合。

---

### 特征工程

#### PCA

保留：

```text
120 PCs
```

解释：

```text
≈99%
光谱信息
```

---

### 模型结构

比较：

* Elastic Net
* Gradient Boosting
* Cubist

最终选择：

```text
Cubist
```

---

### Cubist特点

属于：

```text
Decision Tree
+
Linear Regression
```

优点：

* 适合高维光谱
* 泛化稳定
* 训练效率高

---

### 损失函数

Cubist内部规则回归。

论文未重点讨论损失函数。

---

### 训练策略

```text
SNV
↓
PCA
↓
120 PCs
↓
Cubist
↓
Prediction
```

---

### 对比方法

* Elastic Net
* Gradient Boosting
* Cubist

---

### 评价指标

* R²
* RMSE
* CCC
* RPIQ

---

## 创新点

### 创新点1

构建全球开放土壤光谱库

解决：

```text
数据孤岛问题
```

价值：

```text
形成土壤光谱领域基础设施
```

---

### 创新点2

引入样本代表性检测

方法：

```text
Q-statistic
```

作用：

```text
识别训练集外样本
```

属于：

```text
OOD Detection
```

---

### 创新点3

引入Conformal Prediction

输出：

```text
预测值
+
置信区间
```

作用：

```text
量化预测不确定性
```

---

## 实验结果

### 不同光谱比较

| 光谱       | 表现 |
| ---------- | ---- |
| MIR        | 最优 |
| VisNIR     | 次优 |
| NeoSpectra | 最弱 |

结论：

```text
MIR > VisNIR > NIR
```

---

### 不同属性表现

#### 表现优秀

* SOC
* pH
* Clay
* TC

---

#### SOC

```text
CCC ≈ 0.95
```

---

#### pH

```text
CCC ≈ 0.84
```

---

#### Clay

```text
CCC ≈ 0.74
```

---

### 表现较差

* Sulfur
* Sodium
* EC

原因：

```text
与光谱吸收关系较弱
```

---

## 模型可靠性分析

### 不确定性评估

采用：

```text
Conformal Prediction
```

输出：

```text
Prediction Interval
```

例如：

```text
SOC = 2.3%
±0.4%
```

---

### 样本代表性检测

采用：

```text
Q-statistic
```

判断：

```text
是否超出训练集分布
```

---

### OOD检测

实现方式：

```text
PCA Reconstruction Error
```

如果：

Q > UCL

则：

```text
Prediction Unreliable
```

---

## 作者讨论

### 最重要发现

1. 全球统一光谱库显著提升模型泛化能力。
2. MIR是最优光谱源。
3. 不确定性评估对于实际应用非常重要。

---

### 当前局限

#### 数据层面

* 全球数据仍不均衡
* 某些地区样本不足

#### 模型层面

* 仍以传统机器学习为主
* 深度学习探索不足

#### 应用层面

* 现场实时预测仍需验证

---

### 未来方向

#### 数据

* 更大规模全球光谱库

#### 模型

* Deep Learning
* Transfer Learning
* Multitask Learning

#### 应用

* 遥感融合
* 全球数字土壤制图
* 土壤光谱基础模型

---

## 对我的启发

### 数据处理

* 数据规模比复杂模型更重要。
* 多来源数据统一标准极其关键。

---

### 光谱预处理

* SNV仍然是强基线。
* 预处理对跨区域泛化影响巨大。

---

### 建模流程

推荐基线：

```text
SNV
↓
PCA
↓
Cubist
```

---

### 可改进部分

#### 模型

* Transformer
* Spectral Foundation Model
* GNN

---

#### 特征工程

* AutoEncoder
* Contrastive Learning
* Self-Supervised Learning

---

#### 不确定性

* Deep Ensemble
* Bayesian Neural Network

---

### 可作为对比实验

Baseline：

* PLSR
* Cubist
* RF
* XGBoost

---

## 可复现内容

### 数据

公开：

```text
是
```

---

### 代码

公开：

```text
是
```

---

### 可复现难度

```text
⭐⭐☆☆☆
```

原因：

* 数据完整
* 流程清晰
* 代码开放

---

## 我的评价

### 学术价值

⭐⭐⭐⭐⭐

原因：

建立全球土壤光谱基础设施。

---

### 创新性

⭐⭐⭐☆☆

原因：

创新主要在数据平台而非算法。

---

### 工程价值

⭐⭐⭐⭐⭐

原因：

极强的可复用性和社区价值。

---

### 对课题帮助

⭐⭐⭐⭐⭐

原因：

为未来高光谱土壤预测研究提供统一基线和数据来源。

---

## 核心Takeaways

1. 数据规模决定土壤光谱模型上限。
2. OSSL是当前最重要的开放土壤光谱库之一。
3. MIR仍然是预测性能最强的光谱源。
4. Q-statistic提供了有效的OOD检测方案。
5. 不确定性估计将成为未来土壤光谱研究标配。
6. SNV + PCA + Cubist是极强的传统基线。
7. OSSL有望成为土壤光谱领域的“ImageNet”。
