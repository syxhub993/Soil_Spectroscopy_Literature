# Zotero 00_Reviews 综述论文分析

分析对象：Zotero collection `00_Reviews综述`

分析日期：2026-06-03

## 总体判断

当前 `00_Reviews综述` 中的论文质量和主题匹配度较高，已经覆盖了土壤高光谱文献调研的三个核心入口：

1. 土壤光谱学与 Vis-NIR 预测土壤属性
2. 遥感与机器学习估算土壤有机碳
3. 深度学习在 SOC 遥感反演中的应用趋势

但目前文献结构存在一个明显偏向：**SOC 和 Vis-NIR 综述较多，深度学习、Transformer、自监督、多任务学习、domain adaptation 的综述仍然不足**。

下一步不建议继续盲目增加综述数量，而是先用这 7 篇论文建立领域框架，再补 3 类缺口文献：

- 土壤光谱库和 benchmark 综述
- 深度学习/Transformer 光谱建模综述
- 跨区域、跨仪器、跨数据集泛化综述

## 论文清单与定位

| 优先级 | 论文 | 年份 | 主题定位 | 建议标签 | 是否精读 | 是否复现相关 |
|---|---|---:|---|---|---|---|
| 高 | In-field soil spectroscopy in Vis-NIR range for fast and reliable soil analysis: A review | 2024 | 田间 Vis-NIR 土壤光谱综述 | review, soil-spectroscopy, Vis-NIR | 是 | 间接相关 |
| 高 | Soil Properties Prediction for Precision Agriculture Using Visible and Near-Infrared Spectroscopy: A Systematic Review and Meta-Analysis | 2021 | Vis-NIR 土壤属性预测系统综述和 meta-analysis | review, baseline, soil-properties | 是 | 重要基线 |
| 高 | Soil Organic Carbon Assessment Using Remote-Sensing Data and Machine Learning: A Systematic Literature Review | 2025 | SOC 遥感与机器学习系统综述 | review, soil-organic-carbon, 2022-2025 | 是 | 可启发 MRV |
| 中高 | Basic and deep learning models in remote sensing of soil organic carbon estimation: A brief review | 2021 | SOC 遥感中传统 NN 到 DL 的路线 | review, deep-learning, soil-organic-carbon | 是 | 方法路线参考 |
| 中 | Vis-NIR Spectroscopy for Soil Organic Carbon Assessment: A Meta-Analysis | 2023 | Vis-NIR 估算 SOC 的 meta-analysis | review, soil-organic-carbon, baseline | 是 | 评价指标参考 |
| 中 | Remote Sensing Techniques for Soil Organic Carbon Estimation: A Review | 2019 | SOC 遥感估算早期综述 | classic, review, soil-organic-carbon | 选读 | 背景参考 |
| 中 | Prediction of Soil Properties Using Vis-NIR Spectroscopy Combined with Machine Learning: A Review | 2025 | Vis-NIR + ML 土壤属性预测综述 | review, method-paper, 2022-2025 | 选读 | 方法和预处理参考 |

## 单篇论文分析

### 1. In-field soil spectroscopy in Vis-NIR range for fast and reliable soil analysis: A review

- 年份：2024
- 期刊：European Journal of Soil Science
- DOI：10.1111/ejss.13481
- 核心主题：田间 Vis-NIR 土壤光谱测量

这篇最适合作为你理解“实验室光谱”和“田间近端光谱”差异的入口。它关注 350-2500 nm 范围内的 in-field soil spectroscopy，讨论传感器、平台、测量距离、测量方法、目标土壤属性和 soil spectral libraries 的交叉校准。

对你的启发：

- 你的模型如果未来只在实验室光谱上训练，实际应用会遇到田间条件差异。
- 田间光谱受水分、粗糙度、光照、仪器和管理方式影响，这些都是 domain shift 来源。
- 后续可以把“实验室到田间的迁移学习/域适应”作为研究 gap。

建议精读重点：

- in-field measurement protocol
- sensor range and sensor type
- soil spectral libraries cross-calibration
- target soil properties
- harmonization and standardization

### 2. Soil Properties Prediction for Precision Agriculture Using Visible and Near-Infrared Spectroscopy: A Systematic Review and Meta-Analysis

- 年份：2021
- 期刊：Agronomy
- DOI：10.3390/agronomy11030433
- 核心主题：Vis-NIR 预测土壤属性的系统综述和 meta-analysis

这篇是当前 collection 里最适合建立“传统土壤光谱建模基线”的综述。它系统整理了 115 篇文章，覆盖土壤属性、仪器、实验室/田间条件、预处理方法、回归方法、样本数量和数据划分。

对你的启发：

- 后续做深度学习模型时，必须和 PLSR、SVR、RF 等强基线比较。
- 不同土壤属性的可预测性不同，SOC 和 nitrogen 通常较好，texture 中 silt/clay 可能更难。
- 评价指标不能只看 R2，还要关注 RMSE、RPD、外部验证和数据划分方式。

建议精读重点：

- 哪些土壤属性预测效果最好
- 哪些预处理最常见
- 哪些传统模型是强基线
- calibration/validation 划分是否合理

### 3. Soil Organic Carbon Assessment Using Remote-Sensing Data and Machine Learning: A Systematic Literature Review

- 年份：2025
- 期刊：Remote Sensing
- DOI：10.3390/rs17050882
- 核心主题：遥感数据和机器学习估算 SOC

这篇是当前最贴近“遥感 + ML/DL + SOC/MRV”的新综述。它使用 PRISMA 系统综述方法，强调 Sentinel-2、植被指数、DEM、机器学习和深度学习在 SOC 估算中的作用。

对你的启发：

- 如果你想把项目向 SCI 或 MRV 方向发展，SOC 是最容易形成明确应用场景的土壤属性。
- Sentinel-2、vegetation indices、DEM 与 SOC 预测关系密切，但这也说明很多遥感 SOC 模型并不只依赖裸土光谱。
- 需要区分“土壤光谱建模”和“遥感协变量建模”，二者数据机制不同。

建议精读重点：

- Sentinel-2 使用频率
- 输入变量类型
- DL 模型表现和限制
- SOC MRV 或区域尺度监测价值

### 4. Basic and deep learning models in remote sensing of soil organic carbon estimation: A brief review

- 年份：2021
- 期刊：International Journal of Applied Earth Observation and Geoinformation
- DOI：10.1016/j.jag.2021.102389
- 核心主题：SOC 遥感估算中的传统神经网络与深度学习

这篇适合用来梳理从传统神经网络到深度学习的研究路线。它不是最全面的系统综述，但对你判断“DL 在 SOC 遥感中的合理性和局限”很有用。

对你的启发：

- 深度学习的价值不只是提高精度，还包括处理大规模遥感数据和非线性关系。
- 主要挑战包括样本量、可解释性、泛化能力和遥感数据复杂性。
- 后续可以专门找这篇引用的 DL-SOC 论文作为复现候选。

建议精读重点：

- 传统 NN 与 DL 的差异
- SOC 遥感中的 DL 应用场景
- 作者总结的主要挑战和 future directions

### 5. Vis-NIR Spectroscopy for Soil Organic Carbon Assessment: A Meta-Analysis

- 年份：2023
- 期刊：Eurasian Soil Science
- DOI：10.1134/S1064229323601841
- 核心主题：Vis-NIR 估算 SOC 的 meta-analysis

这篇适合用来补充 SOC 光谱建模的定量证据。它整理了 1986-2022 年的 134 项研究，比较了不同预处理、实验室/田间光谱和预测指标。

对你的启发：

- SOC 是土壤光谱建模中证据最充分的目标属性之一。
- 光谱预处理不是装饰性步骤，会显著影响模型效果。
- 你后续实验应该系统比较 preprocessing + model 的组合，而不是只换深度模型。

建议精读重点：

- R2、RMSE、RPD 的统计分布
- 预处理方法比较
- laboratory spectroscopy 与 field spectroscopy 的差异

### 6. Remote Sensing Techniques for Soil Organic Carbon Estimation: A Review

- 年份：2019
- 期刊：Remote Sensing
- DOI：10.3390/rs11060676
- 核心主题：SOC 遥感估算综述

这篇是较早的 SOC 遥感综述，可以作为 classic 背景文献。它覆盖 VNIR-SWIR、卫星、航空和无人机平台，并讨论大气、辐射、几何校正、植被覆盖、土壤水分和粗糙度等问题。

对你的启发：

- 遥感 SOC 估算的核心困难不只是模型，而是观测条件和地表干扰。
- 从 UAS 到 satellite，预测精度可能下降。
- 如果你做遥感影像土壤属性预测，裸土像元筛选和环境校正必须进入研究设计。

建议精读重点：

- VNIR-SWIR 与 SOC 的关系
- UAS、airborne、satellite 平台差异
- 遥感 SOC 的误差来源

### 7. Prediction of Soil Properties Using Vis-NIR Spectroscopy Combined with Machine Learning: A Review

- 年份：2025
- 期刊：Sensors
- DOI：10.3390/s25165045
- 核心主题：Vis-NIR + ML 预测土壤属性

这篇覆盖土壤水分、有机碳和养分预测，重点强调 spectral preprocessing 与机器学习模型。它适合作为最新背景综述，但需要重点检查其引用质量和是否足够系统。

对你的启发：

- 土壤养分、pH、CEC 等属性往往不是直接光谱响应，模型可能依赖间接相关。
- 预处理策略需要根据数据特征设计，不能机械套用。
- 实时田间应用是未来方向，但可靠性仍是问题。

建议精读重点：

- spectral preprocessing
- PLSR/SVMR 等机器学习方法
- nutrient prediction 的局限
- real-time field application

## 当前综述集合的覆盖情况

### 已覆盖较好

- Vis-NIR soil spectroscopy
- SOC estimation
- Soil property prediction
- Remote sensing for SOC
- PLSR/SVMR/RF 等传统基线
- 实验室与田间光谱差异
- 预处理和评价指标

### 覆盖不足

- Soil spectral library and benchmark datasets
- LUCAS、KSSL、全球土壤光谱库
- 1D CNN/Transformer 专门综述
- Self-supervised learning for spectral data
- Multitask learning for multiple soil properties
- Domain adaptation / transfer learning
- Explainability and band selection
- Reproducible benchmark papers

## 建议的精读顺序

第一轮先读 4 篇：

1. Ahmadi et al. 2021 - 建立 Vis-NIR 土壤属性预测全局框架
2. Piccini et al. 2024 - 理解田间光谱和实际应用限制
3. Lima et al. 2025 - 理解 SOC 遥感 + ML/DL 最新路线
4. Odebiri et al. 2021 - 梳理 SOC 深度学习路线

第二轮再读 3 篇：

5. Chinilin et al. 2023 - 补充 SOC meta-analysis 和指标依据
6. Angelopoulou et al. 2019 - 补充遥感 SOC 经典背景
7. Shin et al. 2025 - 补充 Vis-NIR + ML + nutrient prediction

## 对当前项目最重要的结论

1. 不能只做深度学习模型，需要先建立强基线。
   - PLSR
   - SVR
   - Random Forest
   - Cubist
   - GPR

2. SOC 是最成熟、最适合作为初始目标的土壤属性。
   - 文献最多
   - 遥感应用清晰
   - MRV 和碳监测方向有应用价值

3. 预处理是核心实验变量。
   - smoothing
   - normalization
   - MSC
   - SNV
   - first derivative
   - second derivative
   - continuum removal

4. 最大研究 gap 在泛化能力。
   - 实验室到田间
   - 近端到遥感
   - 跨仪器
   - 跨区域
   - 跨数据集

5. 深度学习论文必须回答是否真的超过传统基线。
   如果只在随机划分上超过 PLSR/RF，但没有外部验证，研究价值有限。

## 可以发展成论文选题的方向

### 方向 1：跨数据集土壤光谱属性预测

问题：

现有研究大量使用单一数据集随机划分，泛化能力不足。

可做：

- LUCAS 到 KSSL
- laboratory spectroscopy 到 in-field spectroscopy
- 单区域到跨区域

方法：

- 1D CNN
- Transformer
- domain adaptation
- feature alignment
- uncertainty estimation

### 方向 2：多任务土壤属性预测

问题：

SOC、texture、pH、CEC、nitrogen 等属性之间存在相关性，但很多论文仍做单任务预测。

可做：

- multi-output regression
- shared spectral encoder
- task-specific heads
- loss weighting
- 属性相关性分析

### 方向 3：可解释深度学习与关键波段选择

问题：

深度模型精度可能高，但缺乏土壤学解释。

可做：

- attention-based band importance
- gradient-based saliency
- SHAP
- wavelength selection
- 与已知 SOC、水分、clay 吸收特征对照

### 方向 4：SOC 遥感 MRV 不确定性建模

问题：

SOC 监测需要可信的不确定性，而很多模型只报告 R2/RMSE。

可做：

- ensemble learning
- Bayesian neural network
- quantile regression
- spatial external validation
- uncertainty map

## Zotero 归档建议

这些论文可以继续保留在 `00_Reviews综述`，同时建议额外归入：

- SOC 遥感相关：`10_Soil_Carbon_MRV`
- 数据和 benchmark 相关：`11_Datasets_and_Benchmarks`
- 深度学习路线相关：`04_Deep_Learning`
- 可能研究缺口：`13_Possible_Research_Gaps`

建议加标签：

- `review`
- `soil-organic-carbon`
- `baseline`
- `deep-learning`
- `domain-adaptation`
- `sci-potential`
- `must-read`

## 下一步行动

1. 先精读 Ahmadi 2021 和 Piccini 2024。
2. 为每篇精读论文在 `literature/summaries/` 新建总结文件。
3. 从 Lima 2025 和 Odebiri 2021 中抽取深度学习 SOC 相关原始论文。
4. 继续补充 `01_Soil_Spectral_Libraries` 和 `11_Datasets_and_Benchmarks`。
5. 开始建立 `paper_index.md`，把每篇论文的类型、标签、是否精读、是否复现记录下来。
