# Remote Sensing Techniques for Soil Organic Carbon Estimation: A Review

## 基本信息

* 标题: Remote Sensing Techniques for Soil Organic Carbon Estimation: A Review
* 作者: Theodora Angelopoulou, Nikolaos Tziolas, Athanasios Balafoutis, George Zalidis, Dionysis Bochtis
* 年份: 2019
* 期刊: Remote Sensing
* DOI/链接: [https://doi.org/10.3390/rs11060676](https://doi.org/10.3390/rs11060676)

## 研究问题

* 研究目标:
  * 综述 VNIR–SWIR 范围内遥感技术用于 SOC 估算的研究进展。
  * 比较 satellite、airborne、UAS 三类平台在 SOC 估算中的优势、局限和应用表现。
  * 总结近十年 SOC 遥感估算中使用的数据源、光谱范围、建模方法和预测结果。
  * 为不熟悉土壤光谱的读者提供土壤光谱学入门说明。
  * 讨论未来 SOC 遥感估算中需要解决的关键挑战，如大气校正、辐射校正、几何校正、植被覆盖、土壤水分和粗糙度。
* 预测的土壤属性:
  * Soil Organic Carbon, SOC
  * Soil Organic Matter, SOM
  * 文章主要聚焦 SOC / SOM。
  * 部分研究使用遥感变量或辅助变量进行 SOC stocks / SOC spatial variability 估计。
* 任务类型:
  * Review paper
  * SOC 遥感估算综述
  * 遥感平台比较
  * VNIR–SWIR 土壤光谱应用总结
  * 多变量回归与机器学习方法比较
* 应用场景:
  * SOC 大尺度制图
  * 农田 SOC 空间变异监测
  * 土壤碳储量评估
  * 可持续农业与土地退化监测
  * SDG 土壤相关指标支持
  * 精准农业中的土壤属性快速监测
  * 土壤光谱库与遥感影像融合

## 数据集

* 数据集名称:
  * 非单一实验数据集。
  * 本文综述了 2008–2018 年为主、并补充部分 2019 年研究的 SOC 遥感估算论文。
* 数据来源:
  * Scopus
  * 关键词：
    * “Remote sensing”
    * “Airborne”
    * “Satellite”
    * “UAS”
    * “Soil Organic Carbon”
    * “Soil Organic Matter”
  * 作者还检查了已有综述和选中文章的参考文献。
* 样本数量:
  * 初始检索得到 382 篇文章。
  * 限制引用次数后减少到 340 篇。
  * 预读标题、摘要、图形摘要、highlights 和关键词后减少到 37 篇。
  * 全文评估后最终纳入 28 篇 journal articles。
  * 各原始研究样本量不同，例如：
    * UAS 研究使用 161 个土样。
    * Hyperion 研究中使用不同 SOC 类别和 in situ 测量。
    * APEX + LUCAS bottom-up 研究使用 LUCAS topsoil database。
* 光谱范围:
  * VNIR–SWIR: 400–2500 nm。
  * 文章涉及多类传感器：
    * Hyperion: 400–2500 nm
    * Sentinel-2: 440–2200 nm
    * EnMAP: 420–2500 nm
    * PRISMA: 400–2500 nm
    * HyspIRI: 380–2510 nm
    * AHS-160: 430–2540 nm
    * HyMap: 450–2500 nm
    * ProSpecTIR V-S: 400–2500 nm
    * Mini-MCA6: 450–1050 nm
  * 文章图 1 展示了砂壤土在 350–2500 nm 的反射光谱，并用灰色区域标出与 SOC 估算相关的重要波长区间。
* 波段数量:
  * 不同传感器差异较大。
  * Hyperion 原始 242 个波段，经过去除低信噪比波段和大气吸收波段后保留 152 个波段。
  * Sentinel-2 为多光谱 / superspectral 数据，波段少于高光谱传感器。
  * Airborne 和 UAS 平台可搭载高光谱或多光谱传感器。
* 标签类型:
  * SOC / SOM 实测值。
  * 通常来自实地土壤采样与实验室分析。
  * 标签为连续变量，属于回归任务。
* 数据划分方式:
  * 本文为综述，没有统一数据划分。
  * 被综述研究常见方式包括：
    * calibration / validation
    * cross-validation
    * local calibration
    * global calibration
    * independent validation dataset
  * 部分研究按土壤类型、区域或图像编号进行分组建模。
* 是否公开:
  * 本文没有提供统一数据集。
  * 部分数据源公开，例如 Landsat、Sentinel-2、LUCAS。
  * APEX、HyMap、AHS-160、UAS 等数据通常取决于具体项目是否公开。

## 方法

* 输入数据:
  * Satellite data:
    * Hyperion
    * Landsat ETM+
    * Sentinel-2
    * 模拟 EnMAP、PRISMA、HyspIRI
  * Airborne data:
    * AHS-160
    * HyMap
    * ProSpecTIR V-S
    * AISA-Eagle
    * AISA Dual
    * APEX
  * UAS data:
    * Mini-MCA6
  * 辅助变量:
    * DEM 派生变量
    * brightness / wetness / vegetation indices
    * bare soil composite
    * soil spectral libraries
* 光谱预处理:
  * 大气校正
  * 几何校正
  * 辐射校正
  * 去除低 SNR 波段
  * 去除大气吸收波段
  * 重采样到目标传感器波段
  * bare soil composite
  * spectral unmixing
  * residual spectral unmixing, RSU
  * green vegetation masking
  * bare soil fractional cover estimation
  * spectral variable selection:
    * CARS
    * Genetic Algorithm, GA
  * 作者指出预处理方法差异很大，目前没有统一标准。
* 模型结构:
  * PLSR, Partial Least Squares Regression
  * SVM / SVMR, Support Vector Machine Regression
  * RF, Random Forest
  * PSR, Penalized Spline Regression
  * SLR, Simple Linear Regression
  * SMLR, Stepwise Multiple Linear Regression
  * ANN / ANNSK
  * Stochastic Gradient Treeboost
  * Stacking ensemble
  * Genetic algorithm-based stacking
  * 文章图 4 显示 PLSR 是使用最多的校准技术，机器学习方法逐渐增多。
* 损失函数:
  * 本文为综述，没有统一讨论损失函数。
  * 各模型通常以最小化 SOC / SOM 预测误差为目标。
* 训练策略:
  * 常见策略：
    * 使用实测 SOC 样点校准遥感光谱模型。
    * 将实验室 / 田间光谱重采样到卫星波段。
    * 使用 bare soil composite 增加裸土像元。
    * 按土壤类型、区域、图像编号构建局部模型。
    * 使用大型土壤光谱库进行 bottom-up 遥感建模。
    * 结合同步 field spectra 与 airborne / satellite imagery。
  * 作者强调从点尺度到空间显式指标存在尺度转换挑战。
* 对比方法:
  * 平台比较：
    * Spaceborne
    * Airborne
    * UAS
  * 传感器比较：
    * Hyperion、Sentinel-2、Landsat、EnMAP、PRISMA、HyspIRI、AHS-160、HyMap、APEX、Mini-MCA6 等
  * 模型比较：
    * PLSR、SVM、RF、PSR、ANN、SMLR 等
  * 数据策略比较：
    * laboratory spectroscopy
    * in situ spectroscopy
    * airborne hyperspectral
    * satellite hyperspectral / multispectral
    * bare soil composite
    * spectral unmixing
    * SSL bottom-up approach
* 评价指标:
  * R²
  * RMSE
  * RPD
  * RPIQ
  * 部分研究报告 g C kg⁻¹ 或百分比单位 RMSE。

## 创新点

* 创新点 1:
  * 从 satellite、airborne、UAS 三个平台层级系统梳理 SOC 遥感估算研究，明确不同平台在空间、光谱、时间、成本和适用尺度上的权衡。
* 创新点 2:
  * 总结近十年 28 篇 SOC 遥感研究的传感器、波段、模型和预测结果，并通过表格分别呈现 spaceborne、airborne 和 UAS 结果。
* 创新点 3:
  * 提出未来需要整合 proximal sensing、soil spectral libraries 和 remote sensing imagery，发展高空间分辨率、低成本、可用于决策的 SOC 监测方案。

## 实验结果

* 主要结果:
  * 作者观察到预测精度通常从 UAS 到 satellite 平台降低。
  * UAS 研究数量极少，但已有研究显示很高精度。
  * Airborne 平台具有较高空间和光谱分辨率，但成本高、操作复杂、需要良好天气和校正流程。
  * Satellite 平台覆盖范围广、可免费获取、时间序列能力强，但受混合像元、植被、大气和空间分辨率限制。
  * PLSR 是最常用的校准方法，但机器学习方法如 SVM、RF、ANN、stacking 等有潜力提升模型性能。
* 最优指标:
  * Spaceborne:
    * Hyperion: R² 约 0.51，RPD 约 1.43。
    * Sentinel-2 + SVM: RPD 约 1.60–1.92。
    * Sentinel-2 + PLSR/RF: RPD 范围约 1.0–2.6。
    * 模拟 PRISMA / EnMAP / HyspIRI 在不同数据集上 R² 变化较大。
  * Airborne:
    * AHS-160: R² 约 0.53–0.89，RPD 约 1.47–3.15。
    * HyMap: R² 约 0.34–0.83，RPD 约 1.14–2.32。
    * APEX + LUCAS bottom-up approach: RMSE 约 4.3 g C kg⁻¹，RPD 约 2.5。
    * HyMap + variable selection: R² 约 0.73–0.85，RPD 约 1.94–2.62。
  * UAS:
    * Mini-MCA6 + SVM: R² = 0.95，RMSE = 0.21。
    * 但该结果来自单一研究，不能直接推广到所有 UAS 场景。
* 与基线相比的提升:
  * 相比普通 kriging，仅加入遥感辅助变量的地统计方法可提升 SOC 空间变异预测。
  * 相比全光谱模型，CARS 和 GA 等变量选择方法可提升部分 airborne SOC 预测。
  * 相比直接使用混合像元，bare soil composite、vegetation masking、spectral unmixing 可以改善 SOC 估算。
  * 机器学习方法在部分场景优于 PLSR，但不是所有场景稳定优于 PLSR。
* 消融实验:
  * 本文没有传统消融实验。
  * 但综述中比较了：
    * 不同平台
    * 不同传感器
    * 不同模型
    * 不同波段范围
    * 不同裸土提取 / 植被去除策略
* 外部验证:
  * 本文没有进行新实验。
  * 多数被综述研究外部验证有限。
  * 部分研究使用 independent validation dataset。
  * 作者指出模型多具有局地性，transferability 较弱。

## 不足

* 数据层面不足:
  * 只纳入 28 篇文章，且筛选时排除了部分低引用文章，可能遗漏新兴或重要研究。
  * UAS 方向仅有极少研究。
  * 卫星 SOC 直接估算研究数量较少。
  * 遥感数据常受植被覆盖、土壤水分、粗糙度和混合像元影响。
* 方法层面不足:
  * 各研究预处理方法差异很大，没有统一方法。
  * PLSR 使用最多，但 SOC 与光谱之间关系不一定线性。
  * 机器学习方法虽有潜力，但模型解释和泛化仍不足。
  * 不同研究评价指标不完全一致，结果可比性受限。
* 实验设计不足:
  * 很多研究需要同步 ground observations，但实际获取困难。
  * 大面积裸土影像难以获得。
  * airborne / UAS 飞行受天气、法规、成本和任务规划限制。
  * 表层遥感只能估算土壤最上层几厘米，难以代表耕层或剖面 SOC。
* 泛化能力问题:
  * 局部校准模型 transferability 较弱。
  * 小尺度模型迁移到大尺度会出现尺度效应和不确定性。
  * 不同平台、不同传感器之间存在空间、光谱和辐射差异。
  * 植被、秸秆、土壤水分和粗糙度造成 domain shift。
* 可解释性问题:
  * 机器学习方法可能提升精度，但对 SOC 光谱机制解释不足。
  * 遥感变量与 SOC 可能是间接相关，而非直接光谱吸收。
  * 需要结合土壤光谱机理和模型解释方法。

## 是否值得复现

* 结论:
  * 不建议完整复现整篇综述。
  * 非常值得复现其中的代表性技术路线，尤其是 Sentinel-2 / Landsat / APEX / UAS 与 SOC 的建模流程。
* 理由:
  * 本文是 SOC 遥感综述中较早系统比较平台的文章。
  * 对构建遥感 SOC 研究框架非常有帮助。
  * 其中的裸土提取、spectral unmixing、bottom-up SSL 方法仍有研究价值。
* 复现难度:
  * 复现综述：中等。
  * 复现单个遥感 SOC 流程：中等到较高。
  * 难点在于同步土壤样点、遥感影像预处理、裸土像元筛选和外部验证。
* 数据可获得性:
  * Sentinel-2、Landsat 公开可得。
  * LUCAS 土壤数据库部分可用。
  * Airborne / UAS 数据多数不公开或难获取。
  * EnMAP / PRISMA 现在已逐步有真实数据可用，值得更新研究。
* 代码可获得性:
  * 本文没有统一代码。
  * 可用 Google Earth Engine、Python、R、QGIS / SNAP 等工具复现部分流程。
* 预计复现价值:
  * 高。
  * 尤其适合复现：
    * Sentinel-2 bare soil composite + SOC
    * LUCAS SSL + satellite bottom-up approach
    * spectral unmixing 去除植被影响
    * UAS 高分辨率 SOC 制图
    * PLSR vs RF vs SVM 比较

## 对我的启发

* 对数据处理的启发:
  * SOC 遥感估算必须先解决裸土像元问题。
  * 植被覆盖、秸秆、水分和粗糙度是遥感 SOC 的核心干扰源。
  * 不同平台的空间、光谱、时间分辨率决定了适用尺度。
  * 仅靠单景影像可能不够，bare soil composite 和多时相策略很重要。
* 对模型设计的启发:
  * PLSR 是传统强基线，但 SVM、RF、stacking 等机器学习方法值得比较。
  * 变量选择方法如 CARS、GA 对高光谱 airborne 数据有价值。
  * 使用 SSL 与遥感影像结合的 bottom-up 方法可能比纯遥感模型更有机制基础。
  * 不应只做模型替换，应重点解决尺度、裸土、迁移和数据融合问题。
* 对实验设计的启发:
  * 应明确区分 satellite、airborne、UAS、proximal sensing。
  * 应设计跨尺度验证：
    * lab spectra
    * field spectra
    * airborne / UAV imagery
    * satellite imagery
  * 应报告植被覆盖、水分、粗糙度和裸土比例。
  * 应使用 independent validation 或 spatial validation。
* 对后续研究方向的启发:
  * 方向1：Sentinel-2 / Landsat 多时相裸土合成 SOC 预测。
  * 方向2：SSL + satellite imagery 的 bottom-up SOC 估算。
  * 方向3：UAS 高分辨率 SOC 制图与卫星尺度迁移。
  * 方向4：vegetation / straw spectral unmixing。
  * 方向5：跨平台 SOC 模型迁移。
  * 方向6：EnMAP / PRISMA 真实高光谱卫星 SOC 预测。

## 个人备注

* 需要进一步查证的问题:
  * 2019 年以后 EnMAP、PRISMA、Sentinel-2 SOC 真实应用进展。
  * UAS SOC 估算是否仍然只有少量研究，还是已明显增长。
  * Sentinel-2 红边、SWIR 对 SOC 的贡献是否稳定。
  * bare soil composite 的最优构建策略。
  * spectral unmixing 在不同作物和残茬条件下是否稳定。
* 可引用的关键观点:
  * SOC 是陆地碳循环和土壤质量的重要指标。
  * VNIR–SWIR 遥感可以以快速、非破坏、低成本方式支持 SOC 估算。
  * SOC 遥感估算精度通常受平台、传感器、植被覆盖、水分、粗糙度和混合像元影响。
  * UAS 具有高空间分辨率，但受续航、载荷和传感器范围限制。
  * Satellite 平台覆盖范围广，但需要严格大气、几何、辐射校正。
  * Proximal sensing、SSL 和 remote sensing 融合是未来方向。
* 可能关联的论文:
  * Chinilin et al., 2023
  * Shin et al., 2025
  * Lima et al., 2025
  * Odebiri et al., 2021
  * Castaldi et al., 2018 / 2019
  * Gomez et al., 2008
  * Vaudour et al., 2016
  * Stevens et al., 2010 / 2013
* 后续行动:
  * 将本文作为 SOC 遥感估算平台综述加入文献库。
  * 单独整理“Satellite-Airborne-UAS SOC Estimation Comparison”笔记。
  * 复现 Sentinel-2 bare soil composite + SOC baseline。
  * 查找 PRISMA / EnMAP 实际 SOC 估算研究。
