# Prediction of Soil Properties Using Vis-NIR Spectroscopy Combined with Machine Learning: A Review

## 基本信息

* 标题: Prediction of Soil Properties Using Vis-NIR Spectroscopy Combined with Machine Learning: A Review
* 作者: Su Kyeong Shin, Seung Jun Lee, Jin Hee Park
* 年份: 2025
* 期刊: Sensors
* DOI/链接: [https://doi.org/10.3390/s25165045](https://doi.org/10.3390/s25165045)

## 研究问题

* 研究目标:
  * 综述 Vis-NIR 光谱结合机器学习预测土壤性质的研究进展。
  * 重点关注土壤水分、有机碳、无机碳和养分，特别是 N、P、K。
  * 系统说明光谱预处理、波长选择、机器学习算法和田间应用之间的关系。
  * 探讨 Vis-NIR 光谱在实时、原位、精准施肥和土壤养分管理中的应用潜力。
  * 强调建立面向不同数据特征的预处理策略和机器学习模型的重要性。
* 预测的土壤属性:
  * Soil water content
  * Soil organic carbon, SOC
  * Soil inorganic carbon, SIC
  * Soil organic matter, SOM
  * Total nitrogen, TN
  * Total phosphorus, TP
  * Total potassium, TK
  * Available nitrogen, AN
  * Available phosphorus, AP
  * Available potassium, AK
  * pH
  * CEC
  * Texture
  * 重点是土壤养分和与肥力相关的土壤性质。
* 任务类型:
  * Review paper
  * Vis-NIR spectroscopy + machine learning 方法综述
  * 土壤属性回归预测
  * 光谱预处理方法综述
  * 波长选择方法综述
  * 田间实时应用综述
* 应用场景:
  * 精准农业
  * 土壤养分实时监测
  * 变量施肥
  * 土壤水分监测
  * SOC / SIC 快速检测
  * 田间 on-site / on-line 测量
  * 可持续农业和土壤肥力管理

## 数据集

* 数据集名称:
  * 非单一实验数据集。
  * 本文基于 2015–2025 年的文献构建综述资料。
* 数据来源:
  * Web of Science
  * Scopus
  * Google Scholar
  * 检索式：
    * (“soil” OR “soil property” OR “soil nutrient”)
    * AND (“NIR” OR “near infrared” OR “Vis-NIR” OR “visible and near infrared”)
    * AND (“machine learning” OR “deep learning” OR “artificial intelligence”)
* 样本数量:
  * 去重后保留 681 篇文章进行筛选。
  * 根据纳入和排除标准，最终识别 409 篇相关研究。
  * 2015–2025 年发表数量整体上升，2023 年达到峰值，约 70 篇。
  * 文中汇总的具体实验研究样本量各不相同。
* 光谱范围:
  * Vis-NIR 通常为 400–2500 nm。
  * NIR 区域约 800–2500 nm。
  * 文章也提到 MIR 区域为 2500–25000 nm。
  * 土壤水分关键吸收峰包括 1400、1900、2200 nm。
  * 有机质 / SOC 相关波长包括 1100、1600、1700、1800、2000、2200–2400 nm 等。
  * 表 2 总结了理论吸收波长范围。
* 波段数量:
  * 不同仪器和数据源不同。
  * 本文重点讨论波长选择：
    * theory-based wavelength selection
    * data-based wavelength selection
  * 常见数据驱动方法：
    * PCA
    * SPA
    * SA
    * CARS
    * GA
    * IRF
    * IRIV
    * PSO
    * ACO
* 标签类型:
  * 土壤水分、SOC、SIC、SOM、TN、TP、TK、AN、AP、AK 等实测值。
  * 连续型变量，主要为回归预测。
  * 部分研究也涉及分类任务，但本文重点是定量预测。
* 数据划分方式:
  * 本文为综述，没有统一数据划分。
  * 被综述研究常见：
    * calibration / validation
    * cross-validation
    * field validation
    * laboratory-to-field transfer
    * spiking with field samples
  * 作者强调实验室模型应用到田间需要额外验证。
* 是否公开:
  * 本文不提供统一数据集。
  * 各被综述研究数据是否公开取决于原始论文。
  * Sentinel / UAV / GF-1 / ASD / LabSpec 等数据源在不同研究中使用。

## 方法

* 输入数据:
  * Vis-NIR 光谱。
  * 光谱来源包括：
    * ASD FieldSpec
    * ASD LabSpec
    * Labspec5100
    * FT-NIR probe
    * fiber-type vis-NIR spectrophotometer
    * portable ground-object spectrometer
    * NIRs-XDS
    * UAV imagery
    * GF-1 satellite data
    * tractor-mounted on-line NIR detector
  * 输入变量还包括波长选择后的特征波段、植被 / 遥感辅助数据等。
* 光谱预处理:
  * 作者将预处理分为四类：
    * denoising
    * scattering correction
    * baseline correction
    * scaling
  * Denoising:
    * Moving Average, MA
    * Savitzky–Golay, SG
    * Wavelet Transform, WT
    * Empirical Mode Decomposition, EMD
  * Scattering correction:
    * Standard Normal Variate, SNV
    * Multiplicative Scatter Correction, MSC
    * Logarithmic Transformation, Log T
  * Baseline correction:
    * first-order derivative, 1D
    * second-order derivative, 2D
    * fractional-order derivative, FOD
    * continuum removal, CR
  * Scaling:
    * autoscaling, AS
    * mean centering, MC
    * max–min scaling, MMS
    * Pareto scaling, PS
  * 文章强调错误或过度预处理可能删除有用光谱峰，必须基于数据特征选择策略。
* 模型结构:
  * PLSR
  * SVMR / SVM
  * RF
  * GBRT
  * XGBoost
  * ELM
  * Cubist
  * ANN
  * BPNN
  * CNN
  * 1-CNN
  * 2-CNN
  * LSTM
  * DBN
  * ensemble models
  * multi-gate mixture-of-experts network
  * encoder–decoder CNN
  * dual-stream convolutional models
  * memory-based learning
* 损失函数:
  * 本文不系统讨论损失函数。
  * 模型多为回归任务，通常以最小化预测误差为目标。
  * 深度学习模型可能使用 MSE / RMSE 类损失，但文章重点不是训练损失。
* 训练策略:
  * 典型流程：
    * 土壤采样
    * 光谱采集
    * 土壤属性实验室测定
    * 光谱预处理
    * 波长选择
    * 机器学习建模
    * 性能评估
    * 田间应用 / 变量施肥
  * 田间应用策略：
    * laboratory model → field validation
    * sensor calibration transfer
    * transfer learning
    * spiking with field samples
    * soil spectral library transfer
    * IoT / UAV / autonomous platform integration
* 对比方法:
  * 预处理方法比较：
    * SG、SNV、MSC、1D、2D、CR、Log T、EPO 等
  * 波长选择方法比较：
    * PCA、SPA、SA、CARS、GA、IRF、IRIV、PSO、ACO
  * 模型比较：
    * PLSR、SVMR、RF、GBRT、ELM、Cubist、ANN、CNN 等
  * 应用场景比较：
    * laboratory
    * field
    * online / on-the-go
    * UAV
    * remote sensing-assisted
* 评价指标:
  * R²
  * RMSE
  * RPD
  * RPIQ
  * Bias
  * RPD 判据：
    * < 1.5: very poor / unsuccessful
    * 1.5–1.8: acceptable
    * 1.8–2: good
    * > 2: excellent
      >

## 创新点

* 创新点 1:
  * 与传统只关注模型或光谱技术的综述不同，本文将 Vis-NIR 光谱、预处理、波长选择、机器学习和田间应用串成完整框架。
* 创新点 2:
  * 系统梳理了四类光谱预处理方法，并强调预处理策略必须根据数据特征定制，而不是机械套用。
* 创新点 3:
  * 强调 Vis-NIR + ML 在实时土壤养分管理、变量施肥和精准农业中的应用潜力，尤其关注 N、P、K 等养分而不仅是 SOC。

## 实验结果

* 主要结果:
  * 2015–2025 年 Vis-NIR + ML 预测土壤性质研究数量持续增长，2023 年达到峰值。
  * SOC 通常比 N、P、K 等养分更容易预测，因为 C 相关吸收特征更强。
  * Available N 和 K 等属性由于光谱响应弱或间接，预测难度较高。
  * 适当的预处理和波长选择能显著提升模型性能。
  * SVMR、RF、GBRT、CNN 等非线性模型在多个研究中优于 PLSR。
  * 但 PLSR 仍因计算简单、可解释性强，适合快速或现场应用。
  * 田间应用仍受传感器校准、环境变化、土壤水分、温度、表面粗糙度和模型可迁移性限制。
* 最优指标:
  * Soil water content:
    * laboratory PLSR 可达到 R² 0.74–0.84。
    * laboratory + field 中，实验室 R² 可达 0.98，田间 R² 约 0.75。
  * SOC / SIC:
    * RF-SVM + 1D 预测 SOC: R² = 0.91, RMSE = 0.27%, RPD = 2.41。
    * IRF-1-CNN 预测 SIC: R² = 0.90, RMSE = 0.15, RPIQ = 4.20。
    * SG + MSC + 1D + PLSR 预测 SOM: R² = 0.98, RPD = 8.56。
    * SVM 预测 SOC: R² = 0.87–0.93, RPD = 2.5–2.8。
    * RF-SG-1D 预测 SOC: R² = 0.94。
  * Nutrients:
    * GBRT-EPO 预测 TN、TP、TK:
      * TN RPD = 2.63
      * TP RPD = 3.92
      * TK RPD = 2.38
    * 1-CNN 预测 oxalate-extractable P:
      * R² = 0.88, RPIQ = 2.49
    * PLSR 结合合适预处理预测 TN:
      * R² = 0.98, RPD = 6.67
    * SVM 预测 TN:
      * R² = 0.89–0.91, RPD = 2.4
* 与基线相比的提升:
  * SVMR 在部分 TN / SOC 任务中明显优于 PLSR。
  * 1-CNN 在部分 P / SIC 任务中优于 PLSR、RF、DBN、LSTM 等。
  * GBRT-EPO 在 TN、TP、TK 上取得较高 RPD。
  * Spiking 少量田间样本可以显著改善实验室模型在田间的表现：
    * 直接应用实验室模型 R² 约 0.42
    * spiking 后 R² 提高到约 0.75
* 消融实验:
  * 本文不是实验论文，没有统一消融。
  * 但汇总了许多研究中不同预处理、波长选择和模型组合的比较。
  * 文章强调组合预处理有时提升性能，有时低于无预处理模型，因此不能盲目叠加。
* 外部验证:
  * 本文没有开展新外部验证。
  * 汇总了 field validation、online validation 和 transfer learning 研究。
  * 实验室模型迁移到田间仍是关键挑战。

## 不足

* 数据层面不足:
  * 本文纳入研究较多，但没有像系统综述 / meta-analysis 那样重新计算统一指标。
  * 不同研究对象差异大，包括水分、SOC、SIC、TN、TP、TK、AP、AK 等，直接比较困难。
  * 田间真实应用研究仍明显少于实验室研究。
  * 土壤养分尤其 P、K 的直接光谱响应弱，标签与光谱关系可能间接。
* 方法层面不足:
  * 文章更多是叙述性综述，不是严格 quantitative meta-analysis。
  * 对不同模型性能的统计整合不足。
  * 对 deep learning 的讨论较新但仍偏总结，缺少统一 benchmark。
  * 预处理方法很多，但没有给出可操作的自动选择流程。
* 实验设计不足:
  * 大多数被综述研究仍以实验室条件为主。
  * 田间环境变量如水分、温度、粗糙度、光照和传感器漂移影响较大。
  * 实验室模型在田间应用前需要 spiking、transfer learning 或重新校准。
  * 多传感器、多区域、多年份验证仍不足。
* 泛化能力问题:
  * 模型跨土壤类型、地理区域和传感器的泛化能力仍然有限。
  * 预处理方法和模型组合可能只对特定数据集有效。
  * 田间部署需要 domain adaptation、calibration transfer 和 robust data fusion。
* 可解释性问题:
  * CNN、ensemble、mixture-of-experts 等复杂模型性能较强，但透明度不足。
  * PLSR 和 Cubist 相对更易解释，适合现场快速决策。
  * 养分预测中很多关系是间接相关，需要防止模型学习伪相关。

## 是否值得复现

* 结论:
  * 值得复现其中的代表性流程。
  * 不建议复现整篇综述。
  * 特别值得做预处理 × 波长选择 × 模型 × 田间验证的标准化 benchmark。
* 理由:
  * 本文覆盖 2015–2025 年最新进展，对当前 Vis-NIR + ML 土壤属性预测非常有参考价值。
  * 对做精准农业、NPK 检测、SOC 光谱建模和田间传感器应用都很有启发。
  * 可直接指导实验流程设计。
* 复现难度:
  * 复现综述：中等。
  * 复现标准 benchmark：中等到较高。
  * 难点在：
    * 获取土壤养分实测数据
    * 实现多种预处理组合
    * 控制模型公平比较
    * 设计田间验证
* 数据可获得性:
  * 部分数据来自公开光谱库或可采集仪器。
  * NPK 养分标签通常不如 SOC 光谱库公开。
  * 田间在线传感器数据更难获取。
* 代码可获得性:
  * 本文未提供统一代码。
  * 可用 Python / R 实现：
    * scikit-learn
    * PyTorch
    * TensorFlow
    * prospectr
    * scipy.signal
    * pywavelets
* 预计复现价值:
  * 很高。
  * 尤其适合：
    * soil nutrient Vis-NIR benchmark
    * SG/SNV/MSC/FD/CR/LogT 预处理比较
    * CARS/SPA/GA 波长选择比较
    * PLSR/SVMR/RF/GBRT/XGBoost/CNN 比较
    * lab-to-field transfer / spiking

## 对我的启发

* 对数据处理的启发:
  * 预处理应按 denoising、scatter correction、baseline correction、scaling 分类设计。
  * 不能盲目叠加预处理，否则可能删除关键峰或放大噪声。
  * 波长选择很重要，尤其对 N、P、K 等弱光谱响应属性。
  * 水分既是预测对象，也是干扰源。
* 对模型设计的启发:
  * PLSR 是必须比较的基线。
  * SVMR、GBRT、RF、XGBoost、Cubist 是强传统 ML 基线。
  * CNN / 1-CNN 对高维光谱有潜力，但需要足够数据和解释性分析。
  * 对田间应用，模型复杂度、计算成本和可解释性与精度同样重要。
* 对实验设计的启发:
  * 应同时测试实验室和田间数据。
  * 应加入 calibration transfer、spiking 或 transfer learning。
  * 应报告 R²、RMSE、RPD、RPIQ。
  * 应区分 total nutrients 与 available nutrients。
  * 应关注实时传感器、UAV、IoT 和变量施肥场景。
* 对后续研究方向的启发:
  * 方向1：Vis-NIR + ML 的 NPK 预测 benchmark。
  * 方向2：预处理自动选择策略。
  * 方向3：田间水分和温度鲁棒模型。
  * 方向4：Lab-to-field transfer learning。
  * 方向5：小样本 NPK 预测。
  * 方向6：Vis-NIR + UAV / IoT 实时土壤监测。
  * 方向7：多属性联合预测模型。

## 个人备注

* 需要进一步查证的问题:
  * 409 篇研究的完整列表是否公开。
  * 不同预处理组合在同一数据集上的真实差异。
  * N、P、K 的预测是直接光谱响应还是间接相关。
  * CNN 在 spatial / field validation 下是否仍然优于 PLSR / SVMR。
  * spiking 所需最少田间样本数量。
  * Vis-NIR 与 XRF、EC、遥感融合是否能稳定提升 NPK 预测。
* 可引用的关键观点:
  * Vis-NIR 光谱可快速、非破坏性地估计多种土壤属性。
  * 预处理策略必须数据特异化，错误预处理可能降低模型性能。
  * 机器学习可处理光谱与土壤属性之间的非线性关系。
  * SOC 通常比 N、P、K 更容易预测。
  * 田间应用需要解决传感器校准、环境变化和模型迁移问题。
  * Spiking、transfer learning、IoT 和 UAV 是未来重要方向。
* 可能关联的论文:
  * Chinilin et al., 2023
  * Angelopoulou et al., 2019
  * Ahmadi et al., 2021
  * Piccini et al., 2024
  * Lima et al., 2025
  * Barra et al., 2021
  * Dotto et al., 2018
  * Mouazen and Kuang, on-line Vis-NIR phosphorus mapping
  * Tsakiridis et al., 2020
  * Zhong et al., 2021
* 后续行动:
  * 将本文作为 Vis-NIR + ML 土壤性质预测方法综述加入文献库。
  * 整理“光谱预处理四分类”方法笔记。
  * 设计预处理 × 波长选择 × 模型的 benchmark。
  * 查找 NPK 公开数据集和田间在线光谱数据。
  * 后续实验重点关注 lab-to-field、multi-property prediction 和模型解释性。
