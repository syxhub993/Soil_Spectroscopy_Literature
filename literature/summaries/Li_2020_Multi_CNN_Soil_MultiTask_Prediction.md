# Simultaneous Prediction of Soil Properties Using Multi_CNN Model

## 基本信息

**题目：** Simultaneous Prediction of Soil Properties Using Multi_CNN Model

**作者：** Ruixue Li, Bo Yin, Yanping Cong, Zehua Du

**期刊：** Sensors

**年份：** 2020

**DOI：** 10.3390/s20216271

**研究方向：** 土壤光谱学、深度学习、卷积神经网络、多任务学习

---

## 研究问题

传统土壤光谱预测模型多为单属性建模，效率低，属性间相关性未利用。

Li 2020 提出：

- 双流 CNN（Dual-stream CNN）
- 多任务学习（Multi-task Learning）
- 可同时预测多个土壤属性（OC/TC, TN/N, Clay, AN/Alkaline N）

目标：

> 提升土壤多属性预测精度，同时兼顾小样本和大样本数据集。

:contentReference[oaicite:0]{index=0}

---

## 数据集

### 小数据集

- 地点：青岛 19 个采样点
- 样本数：180
- 波段：225–975 nm
- 属性：TC, TN, AN
- 仪器：DH-2000 光源 + QE-65000 光谱仪

### 大数据集

- 数据集：LUCAS
- 样本数：19036
- 波段：400–2500 nm（4200波段）
- 属性：OC, N, Clay
- 仪器：FOSS XDS NIR 光谱仪

---

## 数据预处理

- Savitzky-Golay 平滑（S-G）
- 多散射校正（MSC）
- 中心化（Centralization）

目的：

- 降低噪声和散射影响
- 标准化幅值
- 提高信号与土壤属性相关性
- 小数据集转换为 1D 序列
- LUCAS 数据集同时生成 2D Spectrogram（64×64）

:contentReference[oaicite:1]{index=1}

---

## 方法

### Multi_CNN 网络结构

- 双输入流：

  1. 光谱序列 → 1D CNN
  2. 光谱图像 → 2D CNN
- 特征融合后 → 多任务输出：

  ```text
  OC/TC
  TN/N
  Clay/AN
  ```
- 使用残差模块（Residual Block） + 批归一化 + Dropout
- 小数据集适合单输入 1D CNN
- 大数据集适合双流 Multi_CNN

图示参考论文 Figure 5

---

## 创新点

1. 双流 CNN 结合 1D 光谱序列与 2D 光谱图。
2. 多任务学习同时预测多个属性。
3. 自适应输入设计，兼容小样本和大样本数据集。
4. 特征融合提高预测精度。
5. 可在不同尺度数据集上自动选择合适输入方式。

---

## 实验结果

### 小数据集

| 属性 | R²P | RMSEP | RPD  |
| ---- | ---- | ----- | ---- |
| TC   | 0.94 | 0.80  | 4.23 |
| TN   | 0.95 | 0.09  | 4.71 |
| AN   | 0.87 | 11.62 | 2.76 |

优于 PLSR、RFR、GBR 等传统方法。 :contentReference[oaicite:2]{index=2}

### LUCAS 数据集

| 属性 | Multi_CNN | CNN_multi | LSTM | PLSR |
| ---- | --------- | --------- | ---- | ---- |
| OC   | 0.95      | 0.69      | 0.94 | 0.54 |
| N    | 0.91      | 0.60      | 0.91 | 0.55 |
| Clay | 0.83      | 0.68      | 0.80 | 0.50 |

结论：

- 多输入 + 多输出网络优于单输入 1D CNN
- 优于现有 CNN 和 LSTM 网络
- 预测精度高，泛化能力强

---

## 不足

1. 小数据集适用性受限，复杂网络可能过拟合。
2. 仅预测三个或四个属性，没有覆盖全部土壤属性。
3. 2D Spectrogram 转换增加计算成本。
4. 论文未涉及遥感或跨区域迁移能力。
5. 模型仍基于实验室光谱。

---

## 是否值得复现

**非常值得**

- 双流 CNN + 多任务结构是土壤光谱深度学习代表方法
- 可直接作为 OSSL/Transformer 多属性预测实验基线
- 数据和方法公开，可复现

---

## 对我的启发

1. 光谱序列与光谱图像结合，特征互补。
2. 多任务学习可利用属性间相关性，提高精度。
3. 小样本与大样本数据集输入选择应自适应。
4. 可为 SOC、TN、Clay、CEC 等属性预测提供参考架构。
5. 方法可扩展到 Transformer / Foundation Model 时代的多属性土壤预测。

---

## 个人备注

- Li 2020 是多任务 CNN 在土壤光谱中的代表作。
- 连接了 Padarian 2019 的多任务思想和 Liu 2018 的迁移学习理念。
- 在 OSSL 或大规模土壤光谱库上做多属性预测时，是重要参考。
- 文件命名建议：

```text
Li_2020_Multi_CNN_Soil_MultiTask_Prediction.md
```
