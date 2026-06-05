
# In-field soil spectroscopy in Vis–NIR range for fast and reliable soil analysis: A review

## 基本信息

* 标题: In-field soil spectroscopy in Vis–NIR range for fast and reliable soil analysis: A review
* 作者: Chiara Piccini, Konrad Metzger, Guillaume Debaene, Bo Stenberg, Sophia Götzinger, Lubos Borůvka, Taru Sandén, Luca Bragazza, Frank Liebisch
* 年份: 2024
* 期刊: European Journal of Soil Science
* DOI/链接: [https://doi.org/10.1111/ejss.13481](https://doi.org/10.1111/ejss.13481)

## 研究问题

* 研究目标:
  * 系统梳理田间原位 Vis–NIR 土壤光谱技术的发展现状。
  * 分析当前田间土壤光谱测量中使用的传感器、平台、测量距离、采样方式、目标土壤属性和数据处理流程。
  * 识别限制田间 Vis–NIR 光谱可靠性与稳健性的关键瓶颈。
  * 探讨如何将实验室土壤光谱库（Soil Spectral Libraries, SSLs）与田间光谱测量结合。
  * 为未来田间快速土壤分析和农业实际应用提出标准化与方法学建议。
* 预测的土壤属性:
  * Soil Organic Carbon, SOC
  * Soil Organic Matter, SOM
  * Total Carbon, TC
  * Total Nitrogen, TN
  * Soil texture，包括 clay、silt、sand
  * pH
  * Cation Exchange Capacity, CEC
  * Electrical Conductivity, EC
  * Carbonates
  * Bulk density
  * Hydraulic properties
  * Nutrients
  * Heavy metals / contaminants
  * Soil classes
  * Soil respiration
  * Microbial biomass
  * Root density
* 任务类型:
  * 综述研究
  * 田间土壤光谱技术调研
  * Proximal soil sensing 方法总结
  * 传感器与测量平台比较
  * 田间光谱与实验室光谱迁移问题分析
* 应用场景:
  * 精准农业中的快速土壤检测
  * 农田土壤空间变异监测
  * 田间原位土壤属性预测
  * 农业管理分区
  * 变量施肥与变量投入决策支持
  * 土壤制图与土壤监测
  * 遥感地面校准 / ground truthing
  * 实验室土壤检测的低成本替代或补充

## 数据集

* 数据集名称:
  * 非单一实验数据集。
  * 本文构建了一个田间 Vis–NIR 土壤光谱研究文献数据库。
* 数据来源:
  * Scopus
  * ScienceDirect
  * Web of Science
  * 文献检索时间：2022年1月至3月，并在2023年5月、6月、7月更新。
  * 检索关键词包括：
    * Soil proximal sensing
    * in situ
    * NIR
    * Soil spectroscopy
    * Soil
    * Vis–NIR
    * field
    * lab
    * sample preparation
    * subsampling
* 样本数量:
  * 初始纳入103篇参考文献。
  * 其中5篇为综述。
  * 13篇仅涉及干燥和筛分实验室样品。
  * 去除仅实验室分析相关文献后，最终用于综述分析的文献数量为90篇。
  * 这些研究覆盖2006年至2023年。
  * 研究来自23个国家和1个大陆区域，其中中国、德国和美国文献数量较多。
* 光谱范围:
  * 本文重点关注 Vis–NIR 范围。
  * Full range: 350–2500 nm
  * Visible: 350–750 nm
  * NIR: 750–1100 nm
  * SWIR: 1100–2500 nm
  * 少量研究涉及 MIR。
  * 大多数研究使用 full-range Vis–NIR 光谱仪。
* 波段数量:
  * 不同仪器差异较大。
  * 高光谱设备的光谱分辨率通常为3–16 nm。
  * 部分研究将光谱重采样到1 nm或2 nm。
  * 对于350–2500 nm full-range 光谱仪，重采样后可产生超过2000个光谱数据点。
  * 多光谱设备波段数可能从3个RGB波段到约40个波段不等。
* 标签类型:
  * 土壤实验室参考测量值。
  * 田间采样对应的土壤理化性质。
  * 标签多为连续型土壤属性，例如SOC、SOM、TN、pH、CEC、clay含量等。
  * 部分研究涉及土壤类别或土壤分类标签。
* 数据划分方式:
  * 本文为综述，不统一规定数据划分方式。
  * 被综述研究中常见方式包括：
    * Calibration / validation split
    * Cross-validation
    * Leave-one-out cross-validation
    * Five-fold cross-validation
    * Repeated double cross-validation
    * 不同来源数据集构建校准集和验证集
  * 一些研究使用 Kennard–Stone 算法或 fuzzy c-means 等方法划分数据集。
* 是否公开:
  * 本文综述数据库以补充材料形式提供。
  * 原始田间光谱数据是否公开取决于各被综述论文。
  * 文章强调未来需要更大规模、更标准化、跨仪器和跨管理系统的土壤光谱数据库。

## 方法

* 输入数据:
  * 田间条件下采集的 Vis–NIR 土壤光谱。
  * 光谱来源包括：
    * 土壤表面原位扫描
    * 手持式光谱仪测量
    * 接触式探头测量
    * 拖拉机搭载 on-the-go 光谱测量
    * 土壤剖面或土芯扫描
    * 田间取样后现场或实验室测量
  * 光谱数据可能来自不同测量距离：
    * 0 cm 接触式测量
    * 0–10 cm
    * 10–200 cm
    * 200 cm以上
    * 多距离设置
* 光谱预处理:
  * 常见预处理方法包括：
    * Savitzky–Golay smoothing
    * Baseline correction
    * Continuum removal
    * Standard Normal Variate, SNV
    * Multiplicative Scatter Correction, MSC
    * First derivative
    * Second derivative
    * External Parameter Orthogonalization, EPO
    * Direct Standardization, DS
  * 预处理目的包括：
    * 降噪
    * 平滑光谱
    * 消除散射效应
    * 减少土壤水分影响
    * 缓解表面粗糙度和测量几何差异
  * 作者指出，目前尚缺少明确规则来指导如何选择最合适的预处理组合。
* 模型结构:
  * 本文不是提出新模型，而是总结已有研究中的常见建模方法。
  * 常见模型包括：
    * Partial Least Squares Regression, PLSR
    * Random Forest, RF
    * Support Vector Machine, SVM
    * Cubist / M5Rules
    * Neural Network
    * 多种机器学习回归模型
  * PLSR仍然是田间土壤光谱预测中的重要基线模型。
* 损失函数:
  * 本文为综述，不统一讨论损失函数。
  * 传统回归模型通常以最小化预测误差为目标。
  * 神经网络类模型的具体损失函数取决于原始研究，但本文未系统总结。
* 训练策略:
  * 被综述研究常见策略包括：
    * 先建立土壤光谱库，再拟合校准模型。
    * 通过校准集训练模型，通过验证集或交叉验证评估模型。
    * 使用实验室光谱库模型预测田间光谱。
    * 使用 field spectra 对已有 SSL 进行 spiking。
    * 使用 EPO 等方法校正田间湿土光谱，使其更接近干土实验室光谱。
  * 作者认为，田间光谱与实验室光谱之间的连接是未来研究重点。
* 对比方法:
  * 传感器对比：
    * full-range spectrometer
    * reduced-range spectrometer
    * MEMS-based low-cost spectrometer
    * contact probe
    * bare fibre sensor
    * active light source
    * passive light source
  * 平台对比：
    * handheld
    * backpack
    * tractor-mounted
    * benchtop
    * airborne
  * 测量方式对比：
    * in-field
    * lab
    * field vs lab comparison
    * on-the-go
    * surface scanning
    * core/profile scanning
  * 数据处理对比：
    * PLSR、RF、SVM、Cubist、Neural Network 等模型
    * 多种光谱预处理组合
    * 水分校正与非校正方法
* 评价指标:
  * 本文没有统一重新计算所有指标。
  * 被综述研究中常见评价指标包括：
    * R²
    * RMSE
    * RPD
    * Bias
    * Prediction accuracy
    * Repeatability
    * Robustness
  * 作者特别区分 reliability 与 robustness：
    * Reliability 指在一致条件下重复产生稳定结果的能力。
    * Robustness 指在更广泛环境条件下仍能稳定工作的能力。

## 创新点

* 创新点 1:
  * 聚焦“田间原位”土壤光谱，而不是传统实验室干燥筛分样品光谱。
  * 这使论文直接面向精准农业和实际农田应用，而不是仅讨论实验室预测性能。
* 创新点 2:
  * 从传感器、平台、测量距离、样品状态、目标土壤属性、管理系统和数据处理方法等多个维度系统整理田间土壤光谱研究。
  * 文章不仅关注模型性能，还关注测量过程和实际部署条件。
* 创新点 3:
  * 明确指出实验室土壤光谱库与田间光谱之间存在显著差异，并将 Lab-to-Field linkage 作为核心研究空白。
  * 强调未来需要标准化的田间测量协议，以提升结果可比性、可靠性和实际应用能力。

## 实验结果

* 主要结果:
  * 田间 Vis–NIR 土壤光谱具有很大潜力，可以用于快速预测多个土壤属性。
  * 被研究最多的土壤属性是 SOC/SOM，共31篇研究重点关注。
  * 其他常见属性包括 soil texture、total nitrogen、pH、CEC、carbonates、hydraulic properties、bulk density、EC 等。
  * 研究中最常用的光谱范围为 full-range Vis–NIR，即350–2500 nm。
  * 最常用的仪器品牌是 ASD，共62次被提及，其中 ASD FieldSpec 被提及46次。
  * 接触式探头是最常见的传感器类型之一，因为它可以减少环境光影响并提供稳定光照。
  * 手持式、背包式和拖拉机搭载平台是主要田间测量平台。
  * 田间光谱的主要干扰因素包括土壤水分、表面粗糙度、植被残留、土壤结构、石块和小尺度异质性。
  * 实验室模型通常更稳健，但田间测量更适合高密度空间采样和实际农业应用。
* 最优指标:
  * 本文为综述，没有给出统一最优模型指标。
  * 文章强调不同研究由于仪器、测量方式、土壤类型和验证方式不同，结果难以直接比较。
  * 总体结论是：某些属性如SOC、clay、sand、CEC等可在Vis–NIR下实现较好预测，但田间条件下可靠性和稳健性仍依赖于测量协议、校准数据和水分校正方法。
* 与基线相比的提升:
  * 本文没有提出新模型，因此不存在单一模型相较基线的提升。
  * 相对于传统实验室化学分析，田间光谱的优势是速度快、成本低、非破坏性、可高密度采样。
  * 相对于实验室光谱，田间光谱的优势是更接近实际农业应用，但预测精度通常受环境因素影响更大。
  * 作者认为应明确评估 speed/cost 与 reduced accuracy 之间的权衡，尤其是面向低成本便携设备时。
* 消融实验:
  * 本文没有传统意义上的消融实验。
  * 但综述中对以下因素进行了分类比较：
    * 传感器类型
    * 光谱范围
    * 载体平台
    * 传感器到样本距离
    * 田间测量方式
    * 目标土壤属性
    * 土壤管理方式
    * 实验室与田间光谱连接方法
    * 数据预处理方法
    * 建模方法
* 外部验证:
  * 本文没有进行新的外部验证实验。
  * 综述覆盖来自23个国家的研究，具有较广泛的文献外部性。
  * 但作者指出，由于缺乏统一标准，不同研究之间的外部可比性仍然有限。
  * 未来需要跨区域、跨仪器、跨土壤管理系统的统一数据库和验证框架。

## 不足

* 数据层面不足:
  * 不同研究提供的信息不完整，部分论文缺少土壤管理、作物系统或背景信息。
  * 不同土壤属性研究数量不均衡，SOC/SOM研究最多，而微生物、根系、土壤呼吸等属性研究很少。
  * 许多实验室土壤光谱库基于干燥、研磨、筛分样品，难以直接迁移到田间湿土和结构化土壤。
  * 田间光谱数据库仍不够大，跨仪器、跨作物系统、跨管理方式的数据不足。
* 方法层面不足:
  * 光谱预处理方法种类很多，但缺少明确的选择原则。
  * 模型选择、验证方法和数据划分方式差异很大，导致研究间结果难以比较。
  * 田间光谱与实验室光谱之间的转换方法仍不成熟。
  * 水分校正方法如 EPO 和 DS 有一定潜力，但尚未成为标准流程。
* 实验设计不足:
  * 很多研究只比较田间和实验室预测结果，并没有真正建立两者之间的光谱映射关系。
  * 对不同土壤管理系统的影响考虑不足。
  * 对田间测量目的区分不够清晰，例如农业管理所需的耕层平均属性与遥感校准所需的表层属性并不相同。
  * 自动化测量、分析和解释流程仍较少。
* 泛化能力问题:
  * 田间光谱受土壤水分、结构、粗糙度、植被覆盖和测量几何影响，泛化难度高。
  * 不同传感器之间存在光谱差异，跨设备模型迁移仍是问题。
  * 不同作物系统和土壤管理方式会改变土壤垂向梯度和表层状态，影响模型泛化。
  * 现有SSL模型不能直接用于田间光谱，除非进行校正、spiking 或 domain adaptation。
* 可解释性问题:
  * 大多数模型是经验模型，主要依赖光谱与土壤属性之间的统计关系。
  * 对田间干扰因素如何影响具体波段和预测机制的解释仍不足。
  * 深度学习模型虽有潜力，但在田间土壤光谱中的可解释性和可迁移性问题尚未解决。

## 是否值得复现

* 结论:
  * 不建议将整篇综述作为“模型复现”对象。
  * 非常值得作为研究方向梳理和选题依据。
  * 值得复现其中某些关键问题，例如 Lab-to-Field transfer、moisture correction 或 cross-sensor transfer。
* 理由:
  * 本文不是算法论文，没有提出统一新模型。
  * 其主要价值在于总结田间土壤光谱领域的技术路线、瓶颈和未来方向。
  * 对构建科研问题非常有帮助，尤其适合用于开题、综述和论文引言。
* 复现难度:
  * 完整复现综述工作难度中等偏高。
  * 需要重新检索文献、构建分类体系、提取传感器和测量方式信息。
  * 但复现单个研究方向，如“田间湿土光谱水分校正”，难度较可控。
* 数据可获得性:
  * 论文提供补充材料，包含文献分类信息。
  * 原始光谱数据分散在各个被综述研究中，不一定公开。
  * 可结合公开土壤光谱库和自采田间数据进行后续实验。
* 代码可获得性:
  * 本文没有提供算法代码。
  * 因为其主要是综述和文献分类分析，代码不是核心贡献。
  * 若要复现图表，可自行基于补充材料进行统计绘图。
* 预计复现价值:
  * 对理解领域结构和研究空白价值高。
  * 对直接提升模型性能价值有限。
  * 对设计未来SCI论文选题价值很高，尤其是田间光谱、跨域迁移和水分校正方向。

## 对我的启发

* 对数据处理的启发:
  * 不能默认实验室光谱模型可以直接用于田间数据。
  * 需要显式处理水分、粗糙度、植被残留和测量几何差异。
  * 如果使用SSL训练模型，应考虑 field spectra spiking、EPO、DS 或 domain adaptation。
  * 数据记录中应保留土壤管理方式、作物系统、测量距离、传感器类型和样品状态等元数据。
* 对模型设计的启发:
  * PLSR仍然是强基线，新模型必须与PLSR、RF、SVM、Cubist等传统方法比较。
  * 深度学习研究不应只追求更复杂 backbone，而应关注田间泛化问题。
  * 可考虑设计 moisture-invariant representation learning。
  * 可考虑 cross-sensor calibration 或 domain generalization。
  * 可考虑将实验室光谱库作为源域，田间光谱作为目标域，构建迁移学习框架。
* 对实验设计的启发:
  * 实验设计必须区分：
    * 实验室干土预测
    * 实验室湿土预测
    * 田间表面预测
    * 田间土芯/剖面预测
    * on-the-go 预测
  * 需要明确测量目的：
    * 农业管理需要耕层信息
    * 遥感校准需要表层信息
  * 田间实验应同步记录：
    * 土壤水分
    * 表面粗糙度
    * 植被覆盖
    * 作物系统
    * 土壤管理方式
    * 传感器高度和角度
  * 模型评价应包含跨地块、跨时间、跨设备验证。
* 对后续研究方向的启发:
  * 方向1：Lab-to-Field domain adaptation for soil spectroscopy。
  * 方向2：Moisture correction for in-field Vis–NIR soil spectra。
  * 方向3：Cross-sensor transfer learning between ASD and low-cost MEMS sensors。
  * 方向4：Standardized field measurement protocol for soil spectroscopy。
  * 方向5：Field spectral library construction for agricultural soil monitoring。
  * 方向6：Integration of proximal sensing, UAV imagery and laboratory SSLs for soil property mapping。

## 个人备注

* 需要进一步查证的问题:
  * 论文补充材料中90篇研究的完整分类表。
  * 哪些研究真正实现了 Lab-to-Field 光谱映射，而不仅仅是比较预测结果。
  * EPO、DS、spiking、domain adaptation 在田间土壤光谱中的效果差异。
  * 低成本 MEMS 光谱仪在SOC、TN、pH预测中的精度上限。
  * 不同土壤管理系统对田间光谱模型泛化的影响。
* 可引用的关键观点:
  * 田间 Vis–NIR 土壤光谱具有快速、低成本、多属性预测的潜力。
  * 当前限制田间光谱应用的主要因素不是单纯模型精度，而是测量标准化、土壤水分影响和实验室—田间光谱差异。
  * 实验室SSL基于干燥筛分样品，不能直接迁移到湿润、结构化和异质的田间土壤。
  * 接触式探头可以降低环境光影响，但采样面积较小。
  * on-the-go 测量单点信噪比可能较低，但可通过更高空间采样密度提升整体制图效果。
  * 未来田间土壤光谱应用需要统一测量协议和更大规模跨仪器数据库。
* 可能关联的论文:
  * Ahmadi et al., 2021, Soil Properties Prediction for Precision Agriculture Using Visible and Near-Infrared Spectroscopy: A Systematic Review and Meta-Analysis.
  * Soriano-Disla et al., 2014, The Performance of Visible, Near-, and Mid-Infrared Reflectance Spectroscopy for Prediction of Soil Physical, Chemical, and Biological Properties.
  * Stenberg et al., 2010, Visible and Near Infrared Spectroscopy in Soil Science.
  * Viscarra Rossel et al., 2009, In situ measurements of soil colour, mineral composition and clay content by Vis–NIR spectroscopy.
  * Knadel et al., 2022, Mathematical techniques to remove moisture effects from visible–nearinfrared–shortwave-infrared soil spectra.
  * Metzger et al., 2023, The use of visible and near-infrared spectroscopy for in situ characterization of agricultural soil fertility.
* 后续行动:
  * 将本文作为田间土壤光谱方向的核心综述加入阅读库。
  * 单独整理“Lab-to-Field domain shift in soil spectroscopy”专题笔记。
  * 查找EPO、DS、spiking和domain adaptation相关论文。
  * 对比ASD full-range光谱仪与低成本MEMS光谱仪的研究。
  * 设计后续实验时，必须记录土壤水分、测量距离、传感器类型和土壤管理方式等元数据。
  * 将PLSR、RF、SVM、Cubist作为传统基线，深度学习模型重点验证跨域泛化而不是仅做随机划分精度提升。
