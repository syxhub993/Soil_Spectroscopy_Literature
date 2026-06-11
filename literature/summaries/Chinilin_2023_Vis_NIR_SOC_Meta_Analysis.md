# Vis-NIR Spectroscopy for Soil Organic Carbon Assessment: A Meta-Analysis

## 基本信息

* 标题: Vis-NIR Spectroscopy for Soil Organic Carbon Assessment: A Meta-Analysis
* 作者: A. V. Chinilin, G. V. Vindeker, I. Yu. Savin
* 年份: 2023
* 期刊: Eurasian Soil Science
* DOI/链接: [https://doi.org/10.1134/S1064229323601841](https://doi.org/10.1134/S1064229323601841)

## 研究问题

* 研究目标:
  * 系统分析使用 Vis-NIR 光谱评估土壤有机碳（SOC）含量的研究论文。
  * 通过 meta-analysis 比较不同光谱预处理方法、建模方法、实验室光谱与田间原位光谱在 SOC 预测中的表现。
  * 评估 Vis-NIR diffuse reflectance spectroscopy 是否能够作为快速、低成本、环境友好的 SOC 预测方法。
  * 判断当前文献证据是否足以支持 Vis-NIR 在实验室和田间条件下稳定测量 SOC。
* 预测的土壤属性:
  * Soil Organic Carbon, SOC
  * 论文核心只关注 SOC。
  * 背景部分也提到 Vis-NIR 可预测其他土壤属性，如水分、颗粒组成、pH、盐分、矿物组成、铁氧化物等，但 meta-analysis 的目标变量是 SOC。
* 任务类型:
  * Meta-analysis
  * 系统文献分析
  * SOC 光谱预测性能比较
  * 光谱预处理方法比较
  * 多变量建模方法比较
  * 实验室光谱与田间原位光谱比较
* 应用场景:
  * 土壤有机碳快速检测
  * 近地面土壤感知，proximal soil sensing
  * 土壤碳储量监测
  * 农田 SOC 空间制图
  * 实验室 SOC 测定的低成本补充方案
  * 田间原位 SOC 快速评估
  * 面向卫星遥感 SOC 反演的底层光谱校准

## 数据集

* 数据集名称:
  * 非单一实验数据集。
  * 本文构建了关于 Vis-NIR 光谱预测 SOC 的文献指标数据库。
* 数据来源:
  * Science Direct
  * Scopus
  * Google Scholar
  * RSCI
  * 检索关键词：
    * “Vis-NIR spectroscopy AND soil organic carbon”
    * RSCI 中还使用 “soil spectroscopy”
  * 检索对象为 1986–2022 年发表的相关研究论文。
* 样本数量:
  * 纳入 134 篇研究论文。
  * 提取 709 个定量评价指标值。
  * 约 66 篇论文发表于 2018–2022 年，占全部纳入论文约 49%。
  * 测量场景：
    * 约 84% 的研究为实验室光谱
    * 约 16% 的研究为 in situ 或 on-the-go 田间测量
  * PLSR 被约 107 篇论文使用，占约 80%。
* 光谱范围:
  * Vis-NIR diffuse reflectance spectroscopy
  * 通常为 400–2500 nm
  * 文中对比了：
    * Vis-NIR: 400–2500 nm
    * MIR: 2500–25000 nm
  * 作者指出 MIR 对部分土壤性质预测通常更强，但 Vis-NIR 成本更低、设备更便携，更适合田间应用。
* 波段数量:
  * 具体波段数量取决于不同研究和仪器。
  * 本文没有统一统计各研究的波段数量。
  * Vis-NIR 光谱通常为高维连续光谱数据，存在大量相邻且高度共线的波段。
* 标签类型:
  * SOC 实验室标准测定值。
  * 标签为连续数值，因此属于回归任务。
* 数据划分方式:
  * 本文不是单一建模实验，没有统一数据划分。
  * 被纳入文献通常报告 calibration / validation 或 cross-validation 指标。
  * 作者提取 R²cv/val、RMSE、RPD 等模型预测性能指标。
* 是否公开:
  * 本文没有提供统一原始光谱数据集。
  * 图 1 示例光谱来自开放的 ICRAF-ISRIC Soil VNIR Spectral Library。
  * 原始研究数据是否公开取决于各被纳入论文。

## 方法

* 输入数据:
  * Vis-NIR diffuse reflectance spectra。
  * 数据来源包括：
    * 实验室干燥、研磨、筛分土样光谱
    * 田间原位 in situ 光谱
    * on-the-go 土壤光谱
  * SOC 光谱信号会受到矿物组成、铁氧化物、水分、粒径等共同影响。
* 光谱预处理:
  * 比较了多种常见光谱预处理方法：
    * R: raw reflectance
    * A: absorption spectra, A = log(1/R)
    * SG: Savitzky–Golay smoothing
    * FD: first-order derivative
    * MSC: multiplicative scattering correction
    * SNV: standard normal variate
    * WT: wavelet transform
    * CR: continuum removal
    * DT: detrending
    * MA: moving average filtering
    * A*: SG + absorption transformation
    * A**: SNV + absorption transformation
  * 论文图 1 展示了原始反射率、吸收光谱、SG 平滑、一阶导数、SNV 和 detrending 后的曲线形态。
  * 作者强调没有统一的最佳预处理标准，需要针对不同数据迭代测试。
* 模型结构:
  * MLR, Multiple Linear Regression
  * PCR, Principal Component Regression
  * PLSR, Partial Least Squares Regression
  * NN, Neural Networks
  * RF, Random Forest
  * SVM, Support Vector Machine
  * Cubist regression model
  * MBL, Memory-Based Learning
  * PLSR 是最常用方法，约 80% 的纳入论文使用了 PLSR。
* 损失函数:
  * 本文为 meta-analysis，不讨论统一损失函数。
  * 被纳入研究多为回归模型，目标通常是最小化 SOC 预测误差。
* 训练策略:
  * 常见流程：
    * 采集土样或田间光谱
    * 实验室测定 SOC
    * 光谱预处理
    * 多变量建模
    * calibration / validation 或 cross-validation
    * 计算 R²、RMSE、RPD
* 对比方法:
  * 预处理方法比较：
    * R、A、SG、FD、MSC、SNV、WT、CR、DT、MA 及组合预处理
  * 建模方法比较：
    * Cubist、MBL、MLR、NN、PCR、PLSR、RF、SVM
  * 测量环境比较：
    * Laboratory spectroscopy
    * Field / in situ spectroscopy
  * 统计检验：
    * Kruskal–Wallis
    * Mann–Whitney
    * Dunn’s post-hoc pairwise comparison
* 评价指标:
  * R²cv/val
  * RMSE
  * RPD
  * R² 和 RPD 越高越好，RMSE 越低越好。
  * 性能等级：
    * RPD < 1.5 且 R² < 0.5: unsuccessful
    * RPD 1.5–2 且 R² 0.5–0.7: satisfactory
    * RPD 2–2.5 且 R² 0.7–0.9: good
    * RPD > 2.5 且 R² > 0.9: excellent

## 创新点

* 创新点 1:
  * 基于 134 篇论文和 709 个定量指标，对 Vis-NIR 光谱预测 SOC 的整体性能进行 meta-analysis。
* 创新点 2:
  * 系统比较多种光谱预处理方法对 SOC 预测性能的影响，为后续建模实验提供预处理参考。
* 创新点 3:
  * 比较实验室光谱与田间原位光谱的 SOC 预测表现，明确指出田间证据不足，是后续研究空白。

## 实验结果

* 主要结果:
  * Vis-NIR 光谱用于 SOC 预测总体达到“满意到较好”水平。
  * 所有纳入研究整体中位数：
    * R² = 0.67
    * RMSE = 0.48
    * RPD = 1.99
  * 大多数 SOC 预测结果落在 satisfactory 和 good 区间，而不是 excellent 区间。
  * 实验室光谱占绝大多数，约 84%。
  * 田间 in situ 或 on-the-go 研究仅约 16%，说明田间证据不足。
  * PLSR 是最常用方法，约 80% 的研究使用。
  * 实验室光谱总体预测精度优于田间原位光谱。
* 最优指标:
  * 预处理方法：
    * WT 中位 R² 约 0.81。
    * SG + absorption transformation 中位 R² 约 0.78。
    * SG 中位 R² 约 0.77。
    * FD 中位 R² 约 0.74。
    * FD 中位 RMSE 约 0.26。
    * A 中位 RMSE 约 0.34。
    * R 中位 RMSE 约 0.40。
  * 建模方法：
    * NN 中位 R² 约 0.77。
    * MLR 中位 R² 约 0.71。
    * PCR 中位 R² 约 0.70。
    * PLSR 中位 R² 约 0.69。
    * Cubist 中位 RMSE 约 0.29。
    * SVM 中位 RMSE 约 0.33。
    * PLSR 中位 RMSE 约 0.38。
  * 测量环境：
    * 实验室光谱中位 R² 约 0.69。
    * 田间光谱中位 R² 约 0.49。
    * 实验室光谱比田间光谱 R² 高约 20%。
* 与基线相比的提升:
  * 本文没有提出新算法，因此不存在单一基线提升。
  * 不同预处理、不同模型、不同测量环境的中位性能存在显著差异。
* 消融实验:
  * 无传统消融实验。
  * 但通过 meta-analysis 比较了预处理方法、建模方法、测量环境。
* 外部验证:
  * 无新的外部验证实验。
  * 外部性来自 134 篇文献和不同尺度研究的汇总。
  * 作者指出大尺度光谱库可能因土壤类型差异和训练/测试集代表性不足而产生偏差。

## 不足

* 数据层面不足:
  * 田间原位和 on-the-go 光谱研究数量较少。
  * 不同研究之间土壤类型、样本处理、仪器、测量条件和验证方式差异较大。
  * 可能存在发表偏差。
  * 原始光谱数据未统一汇总。
* 方法层面不足:
  * meta-analysis 按文献报告指标比较方法，不能完全控制混杂因素。
  * 不同研究的 R²、RMSE、RPD 可比性有限。
  * 预处理方法效果依赖土壤类型、仪器噪声、SOC 变化范围和测量环境。
* 实验设计不足:
  * 没有在同一数据集下做公平 benchmark。
  * 对 spatial validation、external validation、cross-region validation 讨论不足。
* 泛化能力问题:
  * 区域、国家和全球尺度光谱库中，不同土壤类型和环境条件混合可能导致模型偏差。
  * 局部预测可能需要 spiking 或分层建模。
* 可解释性问题:
  * SOC 光谱响应受到多种因素共同影响。
  * NN 等复杂模型存在 black box 问题。
  * 作者提到 Shapley vector，但没有展开实证分析。

## 是否值得复现

* 结论:
  * 值得部分复现。
  * 不建议完整复现全部 134 篇文献的 meta-analysis。
  * 建议复现核心比较实验：预处理 × 模型 × 验证方式。
* 理由:
  * 提供了 SOC Vis-NIR 光谱预测的重要性能基准。
  * 可作为后续深度学习模型创新的强基线参考。
* 复现难度:
  * 完整复现 meta-analysis：中等偏高。
  * 复现方法比较实验：中等。
* 数据可获得性:
  * 可使用 ICRAF-ISRIC、LUCAS、KSSL、WoSIS 等公开土壤光谱库。
  * 本文没有提供完整机器可读的文献指标数据集。
* 代码可获得性:
  * 未提供完整代码。
  * 可用 R 的 prospectr、ggstatsplot 或 Python 的 scikit-learn、pywavelets 等实现。
* 预计复现价值:
  * 高。
  * 特别适合建立标准 benchmark：
    * raw reflectance
    * SG
    * FD
    * SNV
    * MSC
    * WT
    * PLSR
    * RF
    * SVM
    * Cubist
    * NN / 1D-CNN

## 对我的启发

* 对数据处理的启发:
  * 光谱预处理不是固定流程，不能默认 SG 或 SNV 一定最好。
  * 原始未处理光谱在某些情况下可能优于部分预处理。
  * 田间数据必须重点考虑水分、粗糙度和表面状态影响。
* 对模型设计的启发:
  * PLSR 仍然是 SOC 光谱预测中最重要的强基线。
  * Cubist、SVM、NN 都值得作为对比模型。
  * 如果使用深度学习，应加入可解释性分析。
  * spiking 对跨区域 / 局部泛化很有价值。
* 对实验设计的启发:
  * 应设计完整的预处理 × 模型组合实验。
  * 应同时报告 R²、RMSE、RPD。
  * 应区分实验室光谱、田间光谱和卫星遥感预测。
* 对后续研究方向的启发:
  * Vis-NIR SOC 预测标准化 benchmark。
  * 不同预处理方法对深度学习模型的影响。
  * 实验室光谱到田间光谱迁移学习。
  * SOC 光谱预测中的 spiking 方法。
  * 按土壤类型分层建模。
  * 田间水分影响去除与 EPO 方法。
  * 模型可解释性与关键波段识别。

## 个人备注

* 需要进一步查证的问题:
  * 134 篇论文的完整列表和每个指标值是否可获取。
  * WT 表现较好的原因是否受样本选择影响。
  * Cubist 的低 RMSE 是否受特定数据集或样本分布影响。
  * 实验室光谱与田间光谱差距在控制水分后能否缩小。
* 可引用的关键观点:
  * Vis-NIR 是传统 SOC 实验室分析的快速、低成本、环境友好补充方法。
  * Vis-NIR 对 SOC 预测总体达到满意到较好水平。
  * 预处理方法没有通用最优标准。
  * PLSR 是 SOC Vis-NIR 光谱建模中最常用方法。
  * 实验室光谱预测表现显著优于田间原位光谱。
  * 田间 SOC 光谱数据量仍不足。
* 可能关联的论文:
  * Ahmadi et al., 2021
  * Piccini et al., 2024
  * Angelopoulou et al., 2019
  * Shin et al., 2025
  * Stenberg et al., 2010
  * Soriano-Disla et al., 2014
* 后续行动:
  * 将本文作为 SOC Vis-NIR 光谱预测方向的核心 meta-analysis 加入文献库。
  * 单独整理“Vis-NIR SOC 光谱预处理方法比较”笔记。
  * 对 LUCAS / ISRIC 数据进行预处理 × 模型组合实验。
