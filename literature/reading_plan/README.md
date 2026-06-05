# Literature Reading Plan

本阅读计划面向未来 1 周，目标是在暂停模型开发期间建立土壤高光谱深度学习方向的研究基础。

## 总体目标

- 建立 Soil Spectroscopy 与 Hyperspectral Remote Sensing 的基本概念框架。
- 梳理 Soil Property Prediction 的常见任务、数据集和评价方式。
- 理解深度学习在土壤光谱建模中的主要方法。
- 识别后续最值得复现或借鉴的论文。

## 阅读路线

### Day 1: 领域背景与任务定义

重点理解土壤光谱学的基本问题：

- 土壤高光谱数据是什么。
- 可预测的土壤属性有哪些。
- 实验室光谱、近端光谱、航空/卫星高光谱之间的区别。
- 土壤属性预测为什么适合回归建模。

建议输出：

- `notes/domain_basics.md`
- 土壤属性预测任务列表。

### Day 2: 数据集与预处理

重点整理数据来源和光谱预处理方法：

- 常见公开土壤光谱库。
- 光谱波段、分辨率、样本量、土壤属性标签。
- 去噪、平滑、标准化、一阶导数、二阶导数、连续统去除等预处理。
- 数据划分策略和外部验证问题。

建议输出：

- `notes/datasets.md`
- `notes/preprocessing.md`

### Day 3: 传统机器学习基线

重点理解深度学习之前的常用方法：

- PLSR
- SVR
- Random Forest
- Gradient Boosting
- Gaussian Process Regression
- 特征选择和波段选择方法

建议输出：

- `notes/traditional_ml_baselines.md`
- 一张方法优缺点对比表。

### Day 4: 深度学习方法

重点阅读深度学习在光谱建模中的结构设计：

- 1D CNN
- RNN/LSTM/GRU
- Autoencoder
- Transformer
- Attention
- Multi-task Learning
- Domain Adaptation

建议输出：

- `notes/deep_learning_methods.md`
- 初步筛选可复现模型结构。

### Day 5: 遥感高光谱与空间信息

重点理解从点光谱到高光谱影像的差异：

- 像素级土壤属性预测。
- 光谱-空间联合建模。
- 裸土像元识别。
- 遥感影像中的植被、水分、地形和大气影响。

建议输出：

- `notes/hyperspectral_remote_sensing.md`

### Day 6: 论文精读与复现候选

选择 3-5 篇最相关论文，使用 `summaries/template.md` 完成结构化总结。

重点判断：

- 数据集是否可获得。
- 方法是否清晰。
- 代码是否容易复现。
- 结果是否有可信对照。
- 是否能启发当前项目。

建议输出：

- `summaries/paper_01.md`
- `summaries/paper_02.md`
- `summaries/paper_03.md`

### Day 7: 研究总结与后续路线

整理一周调研结论：

- 方向中最成熟的方法是什么。
- 当前研究的主要难点是什么。
- 哪些论文值得复现。
- 后续模型开发应优先尝试什么。

建议输出：

- `notes/week_1_summary.md`
- 更新 `research_map/research_tree.md`

## 每篇论文阅读顺序

1. 先看标题、摘要、任务和数据集。
2. 再看方法框架图和实验设置。
3. 检查评价指标和对比方法。
4. 最后判断创新点、不足和是否值得复现。

## 优先级判断

优先阅读满足以下条件的论文：

- 直接研究土壤属性预测。
- 使用光谱或高光谱数据。
- 方法包含深度学习。
- 数据集、实验设置和评价指标描述清楚。
- 对当前项目有可迁移价值。
