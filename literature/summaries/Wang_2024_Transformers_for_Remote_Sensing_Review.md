# Transformers for Remote Sensing: A Systematic Review and Analysis

## 基本信息

- 标题: Transformers for Remote Sensing: A Systematic Review and Analysis
- 作者: Ruikun Wang, Lei Ma, Guangjun He, Brian Johnson, Ziyun Yan, Ming Chang, Ying Liang
- 年份: 2024
- 期刊: Sensors
- DOI/链接: https://doi.org/10.3390/s24113495

## 研究问题

- 研究目标: 系统综述 Transformer 在遥感中的研究进展、应用领域、性能趋势和未来方向。
- 预测的土壤属性: 不直接预测土壤属性。
- 任务类型: 遥感 Transformer 系统综述、方法背景论文。
- 应用场景: LULC 分类、分割、融合、变化检测、目标检测、目标识别、配准等遥感任务。

## 数据集

- 数据集名称: 非单一数据集，综述多个遥感 Transformer 研究。
- 数据来源: 近年 Transformer remote sensing 文献。
- 样本数量: 不适用。
- 光谱范围: 覆盖不同遥感数据类型，需精读确认是否包含 hyperspectral imagery。
- 波段数量: 不适用。
- 标签类型: 取决于被综述任务，如分类标签、分割标签、检测框等。
- 数据划分方式: 不适用。
- 是否公开: 取决于被综述论文和数据集。

## 方法

- 输入数据: 遥感影像、融合数据、变化检测数据、目标检测数据等。
- 光谱预处理: 非土壤光谱论文，未聚焦 soil spectra preprocessing。
- 模型结构: Transformer 及其遥感变体；与 CNN 进行对比分析。
- 损失函数: 不适用，综述论文不统一讨论。
- 训练策略: 不适用，取决于被综述论文。
- 对比方法: Transformer vs CNN，以及不同遥感任务中的 Transformer 应用。
- 评价指标: 分类精度、分割性能、检测性能等，具体取决于任务。

## 创新点

- 创新点 1: 对 2021 年后快速增长的 remote sensing transformer 文献进行系统整理。
- 创新点 2: 将应用划分为 8 个领域，便于理解 Transformer 在遥感中的任务分布。
- 创新点 3: 总结 Transformer 在精度、稳定性、参数量和推理速度上的优势与限制。

## 实验结果

- 主要结果: Transformer 在 LULC classification 和 fusion 中精度较高，在 segmentation 和 object detection 中表现较稳定。
- 最优指标: 综述论文未给出统一最优模型指标。
- 与基线相比的提升: 相比 CNN，Transformer 常有精度优势，但参数量更大、推理速度仍需改进。
- 消融实验: 不适用。
- 外部验证: 不适用。

## 不足

- 数据层面不足: 不是 soil spectroscopy 专门综述，不能直接指导土壤属性预测数据设计。
- 方法层面不足: 偏遥感影像任务，对 1D 光谱序列建模讨论有限。
- 实验设计不足: 综述维度较广，无法替代具体 soil hyperspectral benchmark。
- 泛化能力问题: Transformer 依赖大数据和算力，小样本土壤光谱任务可能不稳定。
- 可解释性问题: Transformer attention 是否等于可解释波段贡献需要谨慎。

## 是否值得复现

- 结论: 不建议直接复现整篇综述，但值得从中提取遥感 Transformer 代表模型。
- 理由: 它是方法背景，不是土壤属性预测实验论文。
- 复现难度: 不适用；若复现其中模型，难度取决于具体论文。
- 数据可获得性: 取决于被选模型和数据集。
- 代码可获得性: 取决于被选模型。
- 预计复现价值: 中等。适合为后续 hyperspectral image soil mapping 提供模型候选。

## 对我的启发

- 对数据处理的启发: 如果做高光谱影像而非点光谱，需要考虑 spectral-spatial 输入和多源融合。
- 对模型设计的启发: Transformer 可用于长程波段依赖、空间上下文、多源数据融合，但需控制参数量。
- 对实验设计的启发: 小样本土壤光谱任务中，应与 CNN/PLSR/RF 做公平比较，避免只追求复杂模型。
- 对后续研究方向的启发: 可作为 `04_Deep_Learning` 的背景文献，后续再找专门的 hyperspectral transformer 和 soil spectra transformer 论文。

## 个人备注

- 需要进一步查证的问题: 是否包含 hyperspectral image transformer；是否有农业/裸土/土壤制图案例。
- 可引用的关键观点: Transformer 在遥感中增长迅速，但参数量和推理速度是重要限制。
- 可能关联的论文: Hyperspectral image classification transformer、spectral-spatial transformer、soil property mapping with deep learning。
- 后续行动: 选读与 hyperspectral、fusion、farmland/agriculture 相关部分，不作为当前土壤综述主线。
