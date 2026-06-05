# Soil Properties Prediction for Precision Agriculture Using Visible and Near-Infrared Spectroscopy: A Systematic Review and Meta-Analysis

## 基本信息

* 标题: Soil Properties Prediction for Precision Agriculture Using Visible and Near-Infrared Spectroscopy: A Systematic Review and Meta-Analysis
* 作者: Arman Ahmadi, Mohammad Emami, Andre Daccache, Liuyue He
* 年份: 2021
* 期刊: Agronomy
* DOI/链接: [https://doi.org/10.3390/agronomy11030433](https://doi.org/10.3390/agronomy11030433)

## 研究问题

* 研究目标:
  * 系统评估可见光—近红外光谱（V-NIR, Visible and Near-Infrared Spectroscopy）在精准农业中预测土壤性质的能力。
  * 通过系统综述和Meta分析，总结过去约30年内相关研究的整体预测精度、常用仪器、预处理方法、建模方法和应用条件。
  * 回答核心问题：V-NIR光谱能多准确地预测土壤碳、氮、有机质、水分、盐分和质地？
* 预测的土壤属性:
  * Soil Organic Carbon, SOC
  * Total Carbon, TC
  * Inorganic Carbon, IC
  * Total Nitrogen, TN
  * Soil Organic Matter, SOM
  * Moisture Content, MC
  * Soil Salinity Content, SSC
  * Soil Texture，包括 Sand、Clay、Silt
* 任务类型:
  * 系统综述
  * Meta-analysis
  * 土壤属性回归预测性能评估
  * 光谱建模方法比较
* 应用场景:
  * 精准农业中的土壤快速检测
  * 大范围土壤空间变异监测
  * 替代传统湿化学分析
  * 低成本、快速、非破坏性土壤属性估计
  * 潜在的田间原位检测与移动平台在线检测

## 数据集

* 数据集名称:
  * 非单一数据集。
  * 本文汇总了1990年至2019年间关于V-NIR土壤光谱预测的文献数据。
* 数据来源:
  * ScienceDirect
  * Scopus
  * Web of Science
  * Google Scholar
  * 按照CEBC / CEE系统综述流程筛选文献。
* 样本数量:
  * 初始检索得到1314篇文献。
  * 去重后剩余589篇。
  * 标题筛选排除326篇。
  * 摘要筛选排除148篇。
  * 最终纳入115篇文章进行Meta分析。
  * 单篇研究中的土壤样本数量不固定，最常见范围为50–150个样本。
  * 大多数研究样点数量少于10个地点。
* 光谱范围:
  * 大多数研究使用V-NIR范围，即约400–2500 nm。
  * 少数研究仅使用NIR范围，即约700–2500 nm。
  * 115篇文章中，仅25篇只使用NIR，其余使用VIS + NIR。
* 波段数量:
  * 不同仪器和研究设置不同。
  * 最常见光谱间隔为2 nm，占约34%。
  * 由于400–2500 nm范围内以2 nm间隔采样，通常会产生上百到上千个高维光谱变量。
* 标签类型:
  * 标准实验室测定结果。
  * 包括湿化学分析、标准土壤理化性质测定、质地分析等。
  * 主要标签为连续型土壤属性值，因此属于回归任务。
* 数据划分方式:
  * 约82%的研究将数据划分为 calibration set 和 validation set。
  * 约18%的研究使用 held-out cross-validation。
  * 在已报告的数据划分中，约24.6%的结果使用61%–65%的数据作为校准集。
* 是否公开:
  * 本文使用的是文献统计结果，不提供统一原始光谱数据集。
  * 各纳入研究的数据是否公开取决于原始论文。
  * 本文的补充材料提供了统计表、土壤属性列表、预处理方法比例等汇总信息。

## 方法

* 输入数据:
  * 土壤样品在不同波长下的反射光谱。
  * 光谱类型包括实验室干燥筛分样品的V-NIR反射率、田间原位光谱和移动平台on-the-go光谱。
  * 85%的研究基于实验室条件下干燥、研磨、筛分后的土壤样品。
  * 11%的研究为田间原位测量。
  * 4%的研究使用移动平台在线测量。
* 光谱预处理:
  * Savitzky-Golay smoothing，约24%。
  * First derivative，约21%。
  * Absorbance transformation，即 log(1/reflectance)，约20%。
  * 其他方法包括多种平滑、导数、标准化、变换和组合预处理。
  * 部分研究只采用一种预处理，部分研究比较多种预处理方案或组合方法。
* 模型结构:
  * 本文不是提出新模型，而是统计已有研究中的回归模型。
  * 最常用模型为 Partial Least Squares Regression, PLSR。
  * 其他模型包括：
    * Modified Partial Least Squares Regression, MPLSR
    * Support Vector Machine Regression, SVMR
    * Linear Regression, LR
    * Artificial Neural Network, ANN
    * 其他机器学习回归方法
* 损失函数:
  * 原文为系统综述，不统一讨论各模型训练损失函数。
  * 对多数传统回归模型而言，优化目标通常与最小化预测误差有关，但本文没有将损失函数作为核心比较维度。
  * 因此该项在本文中“不适用 / 未系统报告”。
* 训练策略:
  * 从纳入文献来看，常见策略是基于校准集训练模型，并在验证集上评估。
  * 另一类策略是交叉验证。
  * 作者重点关注校准/验证划分比例、模型类型和评价指标，而非深度学习式训练策略。
* 对比方法:
  * 不同回归方法间比较：
    * PLSR
    * MPLSR
    * SVMR
    * LR
    * ANN
    * Other
  * 不同土壤属性预测性能比较。
  * 实验室测量与田间原位测量比较，主要针对SOC。
  * 不同仪器、光谱范围、样本处理方式和预处理方法的统计比较。
* 评价指标:
  * Coefficient of Determination, R²
  * Ratio of Performance to Deviation, RPD
  * Root Mean Square Error, RMSE
  * R²和RPD越高表示预测越好。
  * RMSE越低表示误差越小。
  * 作者提醒：R²可能受到数据集方差影响，跨研究直接比较时需要谨慎。

## 创新点

* 创新点 1:
  * 使用系统综述方法评估V-NIR土壤光谱预测能力。
  * 相比普通综述，系统综述通过明确检索词、纳入标准、筛选流程和数据提取规则，降低主观筛选偏差。
* 创新点 2:
  * 不局限于单一土壤属性，而是同时分析碳、氮、有机质、水分、盐分和质地等精准农业关键属性。
  * 这使论文能够比较不同土壤属性在V-NIR预测中的难易程度。
* 创新点 3:
  * 使用Meta分析汇总不同研究的R²、RPD和RMSE，并用violin plot展示统计分布。
  * 不仅给出平均性能，还呈现了不同研究结果的分散程度和不确定性。
  * 进一步比较实验室与田间条件下SOC预测性能，为实际应用提供参考。

## 实验结果

* 主要结果:
  * V-NIR光谱总体上能够较好预测多种土壤属性。
  * 预测效果较好的属性包括：
    * Moisture Content
    * Total Nitrogen
    * Total Carbon
    * Inorganic Carbon
    * Soil Organic Carbon
  * 预测相对困难的属性包括：
    * Silt
    * Clay
    * 部分土壤质地指标
  * 土壤质地预测较困难的原因之一是其组成数据特性，即 Sand + Silt + Clay = 100%，而常规模型通常独立预测三者，容易违反总和约束。
  * 实验室测量的SOC预测性能略优于田间原位测量，但差距并不极端；不过田间研究数量较少，证据仍不足。
* 最优指标:
  * 各土壤属性平均R²如下：
    * SOC: 0.75
    * TN: 0.81
    * SOM: 0.73
    * TC: 0.80
    * Clay: 0.70
    * SSC: 0.76
    * Sand: 0.76
    * MC: 0.87
    * IC: 0.79
    * Silt: 0.68
  * 其中Moisture Content平均R²最高，为0.87。
  * Silt平均R²最低，为0.68。
* 与基线相比的提升:
  * 本文不是单一模型论文，因此没有传统意义上的统一基线提升。
  * 论文主要结论是：V-NIR相较传统湿化学方法具备快速、低成本、非破坏性和可重复测量优势。
  * 在模型比较上，PLSR和MPLSR整体表现相近，并在多数情况下略优于SVMR。
  * 对TC和TN预测，MPLSR表现优于PLSR：
    * TC: MPLSR R²约0.82，PLSR R²约0.78
    * TN: MPLSR R²约0.89，PLSR R²约0.79
* 消融实验:
  * 本文为系统综述和Meta分析，没有传统意义上的消融实验。
  * 但文章从多个维度进行了统计对比：
    * 土壤属性类型
    * 回归模型类型
    * 实验室与田间条件
    * 光谱仪器类型
    * 预处理方法
    * 样本制备方式
    * 光谱分辨率
    * 校准/验证划分方式
* 外部验证:
  * 本文没有单独设计外部验证实验。
  * 其“外部性”主要来自跨115篇文章、30个国家研究结果的综合分析。
  * 但由于不同研究间数据质量、样本数量、实验设计和区域差异较大，这种汇总不能完全替代统一标准下的外部验证。

## 不足

* 数据层面不足:
  * 各土壤属性的报告数量严重不均衡。
  * SOC相关报告超过200条，而Silt只有约10条且主要限于R²。
  * 已发表文献可能存在发表偏差，即正结果更容易发表，导致整体性能被高估。
  * 灰色文献和未发表负结果没有纳入。
* 方法层面不足:
  * 不同研究的模型、预处理、样本制备和评价流程并不统一。
  * 本文将不同论文结果汇总比较，但并未对所有研究质量进行加权。
  * 50个样本的研究和数百个样本的研究在统计中可能被近似同等对待。
  * 对深度学习方法讨论不足，主要原因是纳入文献中PLSR仍占主导。
* 实验设计不足:
  * 大多数研究仍基于实验室干燥、研磨、筛分样品。
  * 田间原位和on-the-go研究比例较低。
  * 因此，当前证据更能支持“实验室光谱替代部分传统检测”，而不能充分证明“田间实时稳定应用”。
* 泛化能力问题:
  * 不同地区、土壤类型、仪器、环境条件之间存在明显差异。
  * 单个研究的数据集往往区域性较强。
  * 大多数研究样点少于10个地点，空间泛化能力可能不足。
  * 缺乏统一的大规模跨区域外部验证框架。
* 可解释性问题:
  * 论文主要关注预测性能统计，而不是深入解释光谱波段与具体土壤理化机制之间的因果关系。
  * 对PLSR等模型的可解释性优势没有充分展开。
  * 对深度学习模型的可解释性、波段贡献和物理机制约束讨论较少。

## 是否值得复现

* 结论:
  * 值得部分复现，但不建议完整复现整篇系统综述。
  * 更适合作为领域综述基础和研究选题依据，而不是直接作为模型复现实验对象。
* 理由:
  * 这篇论文的价值在于建立了V-NIR土壤光谱预测的整体证据图谱。
  * 对确定研究空白很有帮助，例如田间原位测量、土壤质地预测、组成数据建模和跨区域泛化。
  * 但由于它不是提出新算法或新数据集的论文，完整复现Meta分析的工程成本较高，科研收益有限。
* 复现难度:
  * 中等到较高。
  * 需要重新检索文献、筛选文献、提取指标、统一统计口径。
  * 难点不在代码，而在文献筛选和数据提取的一致性。
* 数据可获得性:
  * 汇总统计结果和补充材料可获得。
  * 原始光谱数据分散在115篇不同研究中，未形成统一公开数据集。
  * 因此模型级复现难度较高。
* 代码可获得性:
  * 论文未提供统一代码仓库。
  * Meta分析图表可自行复现，但需要先重建数据表。
* 预计复现价值:
  * 对写综述、开题报告和确定研究方向价值较高。
  * 对训练新模型的直接价值有限。
  * 更推荐复现其中某一类任务，例如SOC预测或土壤质地预测，而不是复现整篇Meta分析。

## 对我的启发

* 对数据处理的启发:
  * 土壤光谱建模不能只关注模型，还必须重视样品制备。
  * 干燥、研磨、过筛会显著影响光谱稳定性。
  * 如果目标是田间应用，不能只依赖实验室干样本结果。
  * 对土壤质地任务，应考虑组成数据约束，不能简单地独立预测Sand、Silt、Clay。
* 对模型设计的启发:
  * PLSR仍然是土壤光谱领域强基线，任何新模型都应该至少与PLSR比较。
  * 高光谱输入存在高维和多重共线性问题，模型设计应考虑降维、波段选择或潜变量建模。
  * 对质地预测，可考虑CoDA、log-ratio transformation、多输出约束回归或物理约束神经网络。
  * 对田间数据，可考虑域适应、迁移学习、光照校正和水分干扰校正。
* 对实验设计的启发:
  * 需要清晰区分实验室预测和田间原位预测。
  * 如果做科研创新，应优先设计跨区域、跨仪器、跨土壤类型的验证。
  * 评价指标不能只报告R²，还应同时报告RMSE、RPD、MAE，并提供外部测试集结果。
  * 样本量应尽可能超过50，且覆盖足够土壤异质性。
* 对后续研究方向的启发:
  * 方向1：田间原位V-NIR土壤属性预测。
  * 方向2：基于组成数据约束的土壤质地预测。
  * 方向3：V-NIR与MIR、多源遥感、环境变量融合。
  * 方向4：大规模土壤光谱库上的跨区域泛化研究。
  * 方向5：可解释机器学习揭示关键波段与土壤理化性质之间的关系。

## 个人备注

* 需要进一步查证的问题:
  * 原文补充材料中不同土壤属性的具体记录数量。
  * 不同仪器之间是否存在系统性偏差。
  * V-NIR和MIR在同一数据集上的真实性能差异。
  * 田间原位测量中水分、表面粗糙度和光照变化的校正方法。
  * 土壤质地预测中CoDA方法是否已经成为主流。
* 可引用的关键观点:
  * V-NIR光谱是一种快速、低成本、非破坏性的土壤性质预测方法。
  * 经过30年研究，已有系统证据表明V-NIR可用于预测多种关键土壤属性。
  * SOC、TN、SOM、MC等属性预测较可靠，而Clay、Silt等质地属性预测仍存在较大不确定性。
  * PLSR是土壤V-NIR光谱预测中最常用的回归方法。
  * 田间原位V-NIR应用仍需要更多实验验证。
  * 土壤质地属于组成数据，常规独立回归可能违反Sand + Silt + Clay = 100%的约束。
* 可能关联的论文:
  * Soriano-Disla et al., 2014, The Performance of Visible, Near-, and Mid-Infrared Reflectance Spectroscopy for Prediction of Soil Physical, Chemical, and Biological Properties.
  * Viscarra Rossel et al., 2006, Visible, near infrared, mid infrared or combined diffuse reflectance spectroscopy for simultaneous assessment of various soil properties.
  * Stenberg et al., 2010, Visible and Near Infrared Spectroscopy in Soil Science.
  * Bellon-Maurel and McBratney, 2011, Near-infrared and mid-infrared spectroscopic techniques for assessing carbon stock in soils.
  * Jaconi et al., 2019, Near infrared spectroscopy as an easy and precise method to estimate soil texture.
* 后续行动:
  * 将本文作为土壤光谱综述类基础文献加入阅读库。
  * 单独整理一篇“PLSR为什么适合高光谱土壤预测”的方法笔记。
  * 查找土壤质地预测中使用CoDA / log-ratio transformation的论文。
  * 收集公开土壤光谱数据集，例如 LUCAS、ICRAF/ISRIC、KSSL 等，用于后续模型实验。
  * 在后续实验中将PLSR作为强基线，并重点关注跨区域外部验证。
