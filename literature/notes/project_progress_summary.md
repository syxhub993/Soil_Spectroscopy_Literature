# 当前项目进展总结

日期：2026-06-06

## 项目目标

本项目用于系统整理“土壤高光谱 × 深度学习 × 土壤属性预测”方向的文献调研资料。

当前阶段暂停模型开发，重点转向文献调研、研究地图构建、Zotero 文献管理和可复现论文筛选。

## 已完成的主要工作

### 1. 建立本地文献研究库

已在项目中建立 `literature/` 目录，用于保存本地研究产出：

- `papers/`: 后续用于论文索引。
- `notes/`: 文献分析、研究思考、阶段总结。
- `summaries/`: 单篇论文精读总结。
- `reading_plan/`: 文献阅读路线。
- `research_map/`: 研究地图和方向树。

### 2. 建立 Zotero 文献管理结构

已通过 Zotero API 创建文献库 collection：

```text
Soil_Hyperspectral_DL_Research
  00_Reviews
  01_Soil_Spectral_Libraries
  02_Soil_Properties
  03_Chemometrics_and_ML_Baselines
  04_Deep_Learning
  05_Transfer_Learning_Domain_Adaptation
  06_Self_Supervised_Learning
  07_Multitask_Learning
  08_Explainability_Band_Selection
  09_Digital_Soil_Mapping
  10_Soil_Carbon_MRV
  11_Datasets_and_Benchmarks
  12_Reproducible_Papers
  13_Possible_Research_Gaps
  99_To_Read
```

Zotero 用于管理论文条目、PDF、元数据、标签和引用信息。

本地 GitHub 仓库用于管理阅读总结、研究地图、研究 gap 和后续复现计划。

### 3. 完成 `00_Reviews综述` 文献初步分析

已分析 Zotero 中 `00_Reviews综述` collection 的综述类文献，并形成文档：

```text
literature/notes/zotero_00_reviews_analysis.md
```

主要结论：

- 当前综述文献已覆盖 Vis-NIR 土壤光谱、SOC 遥感估算、传统机器学习基线、田间光谱应用和遥感深度学习趋势。
- 之前缺口集中在 soil spectral libraries、benchmark、reproducibility、domain adaptation、Transformer 和跨数据集泛化。
- 新增的 OSSL 2025、Spectral Transfer Function 2023、Soil Spectral Inference with R、Transformers for Remote Sensing 已补强部分缺口。

### 4. 整理单篇论文 summary

已在 `literature/summaries/` 中建立多篇结构化论文总结，包括：

- Ahmadi 2021: Vis-NIR 土壤属性预测系统综述与 Meta-analysis
- Piccini 2024: 田间 Vis-NIR 土壤光谱综述
- Lima 2025: SOC 遥感与机器学习系统综述
- Odebiri 2021: SOC 遥感中基础模型与深度学习综述
- Angelopoulou 2019: SOC 遥感估算综述
- Chinilin 2023: Vis-NIR SOC Meta-analysis
- Shin 2025: Vis-NIR + ML 土壤属性预测综述
- Safanelli 2025: OSSL 开放土壤光谱库
- Francos 2023: 土壤光谱库 spectral transfer function
- Wadoux 2021: Soil Spectral Inference with R
- Wang 2024: Remote Sensing Transformer 系统综述

### 5. GitHub 仓库已建立并同步

GitHub 仓库：

```text
https://github.com/syxhub993/Soil_Spectroscopy_Literature
```

仓库已用于保存研究文档、Zotero 初始化脚本、论文总结和研究路线。

## 当前研究判断

### 最适合作为第一阶段目标的方向

1. OSSL / LUCAS / KSSL 等 soil spectral libraries 的 benchmark 建模。
2. SOC 作为第一阶段预测属性。
3. PLSR、Cubist、RF、SVR 作为强基线。
4. 在强基线基础上比较 1D CNN、Transformer、domain adaptation。
5. 重点关注跨数据集泛化，而不是只追求随机划分下的高 R2。

### 当前最重要的研究 gap

- 不同 soil spectral libraries 的测量协议不一致。
- 单数据集随机划分容易高估模型能力。
- 深度学习论文常缺少强基线和外部验证。
- 土壤属性预测需要区分直接光谱响应和间接相关属性。
- 可复现 benchmark 和跨库验证仍然不足。

## 下一步优先任务

1. 精读 OSSL 2025，确认数据、代码、属性列表和复现实验协议。
2. 建立 `paper_index.md`，统一记录论文状态、Zotero 目录、标签、是否精读、是否复现。
3. 从综述中提取原始方法论文，补充到 `04_Deep_Learning`、`11_Datasets_and_Benchmarks`、`12_Reproducible_Papers`。
4. 设计第一个可复现实验方向：OSSL 或 LUCAS 上的 SOC 预测基线。
5. 继续补充 domain adaptation、self-supervised learning、multitask learning 和 explainability 相关论文。
