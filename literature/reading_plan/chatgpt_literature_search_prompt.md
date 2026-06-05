# 发给 ChatGPT 的详细提示词

下面这段提示词用于让 ChatGPT 基于当前项目状态继续帮我找文献、筛文献和规划下一步阅读。

```text
你现在是我的科研文献检索和研究规划助手。

我的项目是：

“土壤高光谱 × 深度学习 × 土壤属性预测”

GitHub 仓库：
https://github.com/syxhub993/Soil_Spectroscopy_Literature

我的 Zotero 文献库结构如下：

根目录：
Soil_Hyperspectral_DL_Research

子目录：
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

我目前已经完成：

1. 建立了本地文献研究库 literature/。
2. 建立了 Zotero collection 结构。
3. 已经整理并分析了 00_Reviews 综述目录中的一批核心文献。
4. 已经生成了多篇 summary，包括：
   - Ahmadi 2021: Vis-NIR soil property prediction systematic review and meta-analysis
   - Piccini 2024: In-field Vis-NIR soil spectroscopy review
   - Lima 2025: SOC remote sensing and machine learning systematic literature review
   - Odebiri 2021: Basic and deep learning models in remote sensing of SOC estimation
   - Angelopoulou 2019: Remote sensing techniques for SOC estimation
   - Chinilin 2023: Vis-NIR spectroscopy for SOC meta-analysis
   - Shin 2025: Vis-NIR spectroscopy combined with ML for soil properties
   - Safanelli 2025: Open Soil Spectral Library (OSSL)
   - Francos 2023: Spectral transfer function for harmonizing soil spectral libraries
   - Wadoux 2021: Soil Spectral Inference with R
   - Wang 2024: Transformers for Remote Sensing

当前初步判断：

- SOC 是第一阶段最适合预测的土壤属性。
- OSSL、LUCAS、KSSL、global soil spectral library 是重点数据方向。
- PLSR、Cubist、RF、SVR 是必须比较的强基线。
- 深度学习不能只和弱基线比较，必须做公平实验。
- 最大研究 gap 是跨数据集、跨仪器、跨测量协议和跨区域的泛化能力。
- Spectral library harmonization、domain adaptation、self-supervised learning、multitask learning、explainability 和 band selection 是后续重点方向。

请你基于这些信息，继续帮我完成以下任务：

任务 1：继续推荐文献

请不要再推荐泛泛的普通综述。请重点推荐以下类别的真实论文：

1. Soil spectral libraries / SSL / OSSL / LUCAS / KSSL / global SSL
2. Soil spectral benchmark / reproducible calibration model
3. Cross-dataset soil spectra prediction
4. Calibration transfer / spectral transfer / instrument harmonization
5. Domain adaptation for soil spectroscopy
6. Transfer learning for soil spectroscopy
7. Self-supervised learning for spectral data or hyperspectral data
8. Multitask learning for soil property prediction
9. Explainable deep learning for soil spectra
10. Band selection / wavelength selection for soil property prediction
11. 1D CNN / Transformer for soil spectra
12. Strong baseline papers using PLSR, Cubist, RF, SVR, GPR

任务 2：按 Zotero collection 分类

每篇论文请告诉我应该放入哪个 Zotero collection，例如：

- 01_Soil_Spectral_Libraries
- 03_Chemometrics_and_ML_Baselines
- 04_Deep_Learning
- 05_Transfer_Learning_Domain_Adaptation
- 06_Self_Supervised_Learning
- 07_Multitask_Learning
- 08_Explainability_Band_Selection
- 11_Datasets_and_Benchmarks
- 12_Reproducible_Papers
- 13_Possible_Research_Gaps

任务 3：给出标签

请使用或扩展以下标签：

classic
review
dataset-paper
method-paper
baseline
deep-learning
cnn
transformer
transfer-learning
domain-adaptation
self-supervised
multitask-learning
explainability
band-selection
soil-organic-carbon
soil-texture
pH
CEC
LUCAS
KSSL
global-ssl
must-read
reproduce
possible-research-gap
2022-2025
sci-potential

任务 4：每篇论文输出以下信息

请按表格或结构化列表输出：

- 标题
- 作者
- 年份
- 期刊/会议
- DOI 或链接
- 推荐 Zotero collection
- 推荐标签
- 研究任务
- 数据集
- 方法
- 主要贡献
- 主要不足
- 是否值得精读
- 是否值得复现
- 对我的项目有什么启发

任务 5：优先级排序

请最后给我一个优先阅读列表：

- 最高优先级 5 篇
- 第二优先级 10 篇
- 暂时只收藏、不急读的论文

任务 6：帮我判断研究路线

请基于推荐文献，判断以下哪个方向最适合我后续发展成 SCI 论文：

1. OSSL/LUCAS/KSSL 上的 SOC 跨数据集预测 benchmark
2. 基于 spectral transfer function 的 soil spectral library harmonization
3. 1D CNN / Transformer 用于 soil spectra prediction
4. Self-supervised pretraining for soil spectra
5. Multitask learning for SOC, texture, pH, CEC
6. Explainable band selection for soil property prediction

请明确说明：

- 哪个方向最稳妥
- 哪个方向创新性最高
- 哪个方向最容易复现
- 哪个方向最有 SCI 潜力
- 我下一步应该先读哪些论文

注意：

请优先推荐真实存在、可查证、有 DOI 或明确链接的论文。
如果你不确定某篇论文是否真实存在，请明确标注“不确定，需要核查”。
不要编造 DOI。
不要只给论文列表，要解释为什么值得读。
```
