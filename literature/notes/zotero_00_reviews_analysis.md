# Zotero 00_Reviews 综述论文分析

分析对象：Zotero collection `00_Reviews综述`

分析日期：2026-06-03

## 总体判断

当前 `00_Reviews综述` 中的论文质量和主题匹配度较高，已经覆盖了土壤高光谱文献调研的三个核心入口：

1. 土壤光谱学与 Vis-NIR 预测土壤属性
2. 遥感与机器学习估算土壤有机碳
3. 深度学习在 SOC 遥感反演中的应用趋势

但目前文献结构存在一个明显偏向：**SOC 和 Vis-NIR 综述较多，深度学习、Transformer、自监督、多任务学习、domain adaptation 的综述仍然不足**。

***下一步不建议继续盲目增加综述数量，而是先用这 7 篇论文建立领域框架，再补 3 类缺口文献：***

- ***土壤光谱库和 benchmark 综述***
- ***深度学习/Transformer 光谱建模综述***
- ***跨区域、跨仪器、跨数据集泛化综述***

## 论文清单与定位

| 优先级 | 论文                                                                                                                                     | 年份 | 主题定位                                     | 建议标签                                   | 是否精读 | 是否复现相关     |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------- | ---: | -------------------------------------------- | ------------------------------------------ | -------- | ---------------- |
| 高     | In-field soil spectroscopy in Vis-NIR range for fast and reliable soil analysis: A review                                                | 2024 | 田间 Vis-NIR 土壤光谱综述                    | review, soil-spectroscopy, Vis-NIR         | 是       | 间接相关         |
| 高     | Soil Properties Prediction for Precision Agriculture Using Visible and Near-Infrared Spectroscopy: A Systematic Review and Meta-Analysis | 2021 | Vis-NIR 土壤属性预测系统综述和 meta-analysis | review, baseline, soil-properties          | 是       | 重要基线         |
| 高     | Soil Organic Carbon Assessment Using Remote-Sensing Data and Machine Learning: A Systematic Literature Review                            | 2025 | SOC 遥感与机器学习系统综述                   | review, soil-organic-carbon, 2022-2025     | 是       | 可启发 MRV       |
| 中高   | Basic and deep learning models in remote sensing of soil organic carbon estimation: A brief review                                       | 2021 | SOC 遥感中传统 NN 到 DL 的路线               | review, deep-learning, soil-organic-carbon | 是       | 方法路线参考     |
| 中     | Vis-NIR Spectroscopy for Soil Organic Carbon Assessment: A Meta-Analysis                                                                 | 2023 | Vis-NIR 估算 SOC 的 meta-analysis            | review, soil-organic-carbon, baseline      | 是       | 评价指标参考     |
| 中     | Remote Sensing Techniques for Soil Organic Carbon Estimation: A Review                                                                   | 2019 | SOC 遥感估算早期综述                         | classic, review, soil-organic-carbon       | 选读     | 背景参考         |
| 中     | Prediction of Soil Properties Using Vis-NIR Spectroscopy Combined with Machine Learning: A Review                                        | 2025 | Vis-NIR + ML 土壤属性预测综述                | review, method-paper, 2022-2025            | 选读     | 方法和预处理参考 |

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

---

# 2026-06-05 新增论文补充分析

本次从 Zotero collection `00_Reviews综述` 中识别到 5 个新增正式条目：

1. A Spectral Transfer Function to Harmonize Existing Soil Spectral Libraries Generated by Different Protocols
2. Transformers for Remote Sensing: A Systematic Review and Analysis
3. Soil Spectral Inference with R: Analysing Digital Soil Spectra using the R Programming Environment
4. Open Soil Spectral Library (OSSL): Building reproducible soil calibration models through open development and community engagement
5. Multi-Region Soil Model for Transmission Line Backflashover Analysis

其中第 1、3、4 篇/本非常重要，直接补上了之前分析中指出的 `soil spectral library / benchmark / reproducibility` 缺口；第 2 篇虽然不是土壤专门综述，但可以作为 Transformer 遥感方法背景；第 5 篇与本项目主题不匹配，建议从 `00_Reviews综述` 中移出。

## 新增论文清单与定位

| 优先级     | 论文                                                                                                                               | 年份 | 主题定位                                             | 建议 Zotero 目录                                                                         | 建议标签                                                       | 是否精读  | 是否复现相关 |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---: | ---------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------- | --------- | ------------ |
| 很高       | Open Soil Spectral Library (OSSL): Building reproducible soil calibration models through open development and community engagement | 2025 | 开放土壤光谱库、可复现 calibration benchmark         | 01_Soil_Spectral_Libraries, 11_Datasets_and_Benchmarks, 12_Reproducible_Papers           | dataset-paper, benchmark, reproduce, global-ssl, sci-potential | 是        | 很高         |
| 很高       | A Spectral Transfer Function to Harmonize Existing Soil Spectral Libraries Generated by Different Protocols                        | 2023 | 不同土壤光谱库协议 harmonization / transfer function | 01_Soil_Spectral_Libraries, 05_Transfer_Learning_Domain_Adaptation                       | method-paper, domain-adaptation, LUCAS, band-selection         | 是        | 高           |
| 高         | Soil Spectral Inference with R                                                                                                     | 2021 | 土壤光谱建模工具书、R 实操、数字土壤光谱分析         | 01_Soil_Spectral_Libraries, 03_Chemometrics_and_ML_Baselines, 11_Datasets_and_Benchmarks | classic, baseline, dataset-paper                               | 选读/查阅 | 高           |
| 中高       | Transformers for Remote Sensing: A Systematic Review and Analysis                                                                  | 2024 | 遥感 Transformer 系统综述                            | 04_Deep_Learning                                                                         | transformer, deep-learning, review, 2022-2025                  | 选读      | 中           |
| 不建议保留 | Multi-Region Soil Model for Transmission Line Backflashover Analysis                                                               | 2021 | 输电线路雷击回击闪络中的土壤电气模型                 | 不建议放在本项目综述目录                                                                 | irrelevant                                                     | 否        | 无           |

## 单篇新增论文分析

### 8. Open Soil Spectral Library (OSSL): Building reproducible soil calibration models through open development and community engagement

- 年份：2025
- 期刊：PLOS ONE
- DOI：10.1371/journal.pone.0296545
- 核心主题：开放土壤光谱库、可复现校准模型、社区数据资源

这篇是当前新增论文中最重要的一篇。它直接解决了你当前研究库之前的缺口：公开土壤光谱库、benchmark、可复现 calibration model。论文介绍 OSSL 如何整合多个 soil spectral libraries，并通过开放开发和社区参与推动可复现土壤光谱建模。

从摘要看，论文不仅介绍数据资源，还包含探索性分析、预测建模、10-fold cross-validation with refitting、独立模型评估、不确定性输出和 representation flag。这比普通数据集论文更有价值，因为它同时提供了“数据 + 建模协议 + 可复现资源 + 局限分析”。

对你的启发：

- OSSL 应该作为后续项目最优先关注的数据资源之一。
- 它可以作为你后续深度学习模型的 benchmark 来源。
- 论文指出 MIR 模型通常显著优于 VisNIR/NIR，这提醒你不能简单假设高光谱/Vis-NIR 对所有属性都有效。
- Cubist 在该研究中表现最好，说明传统机器学习仍然是强基线，后续深度学习必须和 Cubist、PLSR、RF 等比较。
- 部分属性如 total sulfur、extractable sodium、electrical conductivity 表现较差，说明“光谱无法稳定预测所有土壤属性”。

建议精读重点：

- OSSL 数据来源和 harmonization 流程
- VisNIR、NIR、MIR 三类光谱的性能差异
- 10-fold cross-validation with refitting 的设置
- independent model evaluation
- Cubist 为什么表现强
- prediction uncertainty 和 representation flag
- 哪些土壤属性适合作为深度学习目标，哪些不适合

建议 Zotero 处理：

- 保留在 `00_Reviews综述` 或作为基础资源论文。
- 同时归入 `01_Soil_Spectral_Libraries`。
- 同时归入 `11_Datasets_and_Benchmarks`。
- 如果后续能拿到数据和复现实验流程，归入 `12_Reproducible_Papers`。

建议标签：

- `dataset-paper`
- `global-ssl`
- `baseline`
- `reproduce`
- `sci-potential`
- `2022-2025`

### 9. A Spectral Transfer Function to Harmonize Existing Soil Spectral Libraries Generated by Different Protocols

- 年份：2023
- 期刊：Applied and Environmental Soil Science
- DOI：10.1155/2023/4155390
- 核心主题：不同土壤光谱库之间的协议 harmonization

这篇非常契合你项目中“跨数据集泛化”和“domain adaptation”的潜在方向。论文关注不同 soil spectral libraries 因测量协议不同而产生的系统差异，并提出 spectral transfer function，将旧 SSL 转换到 ISS spectral condition。

摘要中提到使用 Brazilian Soil Spectral Library 和 LUCAS SSL，通过 random forest spectral-based models 预测 ISS spectral condition，并在 organic carbon 估计中观察到性能提升。这对你的项目很关键，因为它说明跨光谱库建模的核心问题不只是模型架构，而是测量协议、仪器和数据标准不一致。

对你的启发：

- 跨数据集土壤光谱建模必须考虑 protocol shift。
- domain adaptation 不一定一开始就上深度学习，可以先从 spectral transfer function、standardization、calibration transfer 做起。
- LUCAS 与其他 SSL 的融合是一个非常实际的研究场景。
- 这篇可以作为你后续“跨光谱库泛化”的方法基础。

建议精读重点：

- ISS protocol
- Brazilian SSL 与 LUCAS SSL 的差异
- spectral transfer function 的建模方式
- RF 如何用于谱域转换
- harmonization 前后 OC 预测性能变化
- 是否可以替换为 1D CNN/Transformer 做 transfer function

建议 Zotero 处理：

- 同时归入 `01_Soil_Spectral_Libraries`。
- 同时归入 `05_Transfer_Learning_Domain_Adaptation`。
- 同时归入 `13_Possible_Research_Gaps`。

建议标签：

- `method-paper`
- `domain-adaptation`
- `transfer-learning`
- `LUCAS`
- `soil-organic-carbon`
- `possible-research-gap`

### 10. Soil Spectral Inference with R: Analysing Digital Soil Spectra using the R Programming Environment

- 年份：2021
- 类型：Book
- DOI：10.1007/978-3-030-64896-1
- 核心主题：用 R 分析数字土壤光谱

这是一本工具书，不是普通综述论文。它的价值在于为 soil spectral inference 提供完整的实操框架，可能包含光谱预处理、建模、数据处理、评价指标、可视化和数字土壤制图相关内容。

对你的启发：

- 它可以作为“土壤光谱建模标准流程”的参考资料。
- 即使你后续使用 Python 和深度学习，也可以从这本书中学习传统 soil spectral inference 的实验设计。
- 它适合用来建立 baseline workflow，而不是作为单篇精读综述。

建议使用方式：

- 不建议从头到尾精读。
- 建议作为工具书查阅以下章节：
  - spectral preprocessing
  - soil spectral libraries
  - PLSR / Cubist / RF 等传统模型
  - calibration / validation
  - uncertainty
  - digital soil mapping

建议 Zotero 处理：

- 可以保留在 `00_Reviews综述` 作为基础书籍。
- 更建议同时放入 `03_Chemometrics_and_ML_Baselines`。
- 如果书中包含可运行代码或数据，也可以放入 `12_Reproducible_Papers`。

建议标签：

- `classic`
- `baseline`
- `method-paper`
- `reproduce`

### 11. Transformers for Remote Sensing: A Systematic Review and Analysis

- 年份：2024
- 期刊：Sensors
- DOI：10.3390/s24113495
- 核心主题：遥感领域 Transformer 系统综述

这篇不是 soil spectroscopy 专门论文，但对你理解 Transformer 在遥感中的整体发展有帮助。它将遥感 Transformer 应用划分为 LULC classification、segmentation、fusion、change detection、object detection、object recognition、registration 等方向，并讨论了 Transformer 相比 CNN 的精度、参数量和推理速度问题。

对你的启发：

- Transformer 在遥感中表现强，但常常需要更多参数，对样本量和计算资源要求更高。
- 该综述偏遥感影像任务，不直接回答 1D soil spectra 如何建模。
- 对你的项目而言，它更适合作为“方法背景”，不是核心土壤综述。
- 后续如果做高光谱影像土壤属性预测，Transformer 可以用于 spectral-spatial modeling 或多源数据融合。

建议精读重点：

- Transformer 与 CNN 的比较
- fusion 和 segmentation 方向
- farmland/agriculture 场景应用
- 参数量、推理速度和数据规模限制
- 是否有 hyperspectral image transformer 的代表论文

建议 Zotero 处理：

- 可以保留在 `00_Reviews综述`。
- 更建议同时归入 `04_Deep_Learning`。
- 若后续关注高光谱影像，可归入 `09_Digital_Soil_Mapping`。

建议标签：

- `transformer`
- `deep-learning`
- `review`
- `2022-2025`

### 12. Multi-Region Soil Model for Transmission Line Backflashover Analysis

- 年份：2021
- 会议：2021 35th International Conference on Lightning Protection / SIPDA
- DOI：10.1109/ICLPandSIPDA54065.2021.9627471
- 核心主题：输电线路回击闪络分析中的多区域土壤电气模型

这篇不属于你的当前研究方向。虽然标题中有 `soil model`，但它研究的是输电线路雷击回击闪络、塔 surge impedance、全波电磁建模中的土壤区域变化，不涉及 soil spectroscopy、hyperspectral remote sensing、deep learning 或 soil property prediction。

判断：

- 不建议精读。
- 不建议放在 `00_Reviews综述`。
- 不建议占用当前文献库注意力。

建议 Zotero 处理：

- 从 `00_Reviews综述` 中移出。
- 如果你没有其他电力系统方向需求，可以放入一个临时 `Irrelevant` 或直接不归入本项目 collection。

建议标签：

- `irrelevant`

## 新增论文对原有研究地图的影响

这批新增论文显著补强了两个关键空白：

### 1. Soil Spectral Libraries / Benchmark

新增的 OSSL 和 spectral transfer function 论文说明，土壤光谱深度学习项目不能只停留在模型层面。真正决定模型可用性的关键包括：

- 数据库规模
- 光谱范围
- 测量协议
- 仪器差异
- 数据 harmonization
- 跨库验证
- 不确定性输出
- 代表性判断

这意味着你后续研究应把 `dataset and benchmark` 放在和 `model architecture` 同等重要的位置。

### 2. Cross-dataset / Domain Shift

Spectral transfer function 论文直接支持一个可发展方向：

> 基于 soil spectral library harmonization 的跨数据集土壤属性预测。

这个方向比“单纯换一个 Transformer 模型”更有研究价值，因为它处理的是土壤光谱应用中的真实痛点：不同库、不同仪器、不同协议之间无法直接合并。

## 更新后的优先精读顺序

现在建议调整精读顺序如下：

1. **OSSL 2025**
   - 目的：确定可用数据资源、benchmark 和可复现实验方向。
2. **Ahmadi 2021**
   - 目的：建立 Vis-NIR 土壤属性预测完整框架。
3. **Piccini 2024**
   - 目的：理解田间光谱、传感器、测量协议和应用限制。
4. **Spectral Transfer Function 2023**
   - 目的：理解跨光谱库 harmonization 和 protocol shift。
5. **Lima 2025**
   - 目的：理解 SOC 遥感 + ML/DL + MRV 方向。
6. **Odebiri 2021**
   - 目的：梳理 SOC 深度学习遥感路线。
7. **Transformers for Remote Sensing 2024**
   - 目的：作为 Transformer 遥感方法背景，选读。

## 下一步行动建议

### 立刻做

1. 把 `Multi-Region Soil Model for Transmission Line Backflashover Analysis` 从 `00_Reviews综述` 中移出。
2. 把 OSSL 2025 同时放入：
   - `01_Soil_Spectral_Libraries`
   - `11_Datasets_and_Benchmarks`
   - `12_Reproducible_Papers`
3. 把 Spectral Transfer Function 2023 同时放入：
   - `01_Soil_Spectral_Libraries`
   - `05_Transfer_Learning_Domain_Adaptation`
   - `13_Possible_Research_Gaps`
4. 把 Transformers for Remote Sensing 2024 同时放入：
   - `04_Deep_Learning`

### 今天建议精读

优先读 OSSL 2025。原因：

- 它直接决定你后续能不能做复现实验。
- 它提供开放数据和开放资源。
- 它能帮助你判断哪些土壤属性值得作为第一阶段预测目标。
- 它会让你的研究从“找模型”转向“建立可靠 benchmark”。

建议为它新建总结文件：

```text
literature/summaries/2025_safanelli_ossl_open_soil_spectral_library.md
```

精读时重点回答：

- OSSL 包含哪些数据来源？
- 光谱范围有哪些？MIR、VisNIR、NIR 分别如何？
- 预测了哪些土壤属性？
- 哪些属性表现好，哪些表现差？
- 使用了哪些 baseline 模型？
- 是否提供代码、数据和可复现实验流程？
- 对你的深度学习模型设计有什么约束？
