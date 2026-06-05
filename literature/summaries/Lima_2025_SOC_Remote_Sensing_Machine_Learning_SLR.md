# Soil Organic Carbon Assessment Using Remote-Sensing Data and Machine Learning: A Systematic Literature Review

## 基本信息

* 标题: Soil Organic Carbon Assessment Using Remote-Sensing Data and Machine Learning: A Systematic Literature Review
* 作者: Arthur A. J. Lima, Júlio Castro Lopes, Rui Pedro Lopes, Tomás de Figueiredo, Eva Vidal-Vázquez, Zulimar Hernández
* 年份: 2025
* 期刊: Remote Sensing
* DOI/链接: [https://doi.org/10.3390/rs17050882](https://doi.org/10.3390/rs17050882)

## 研究问题

* 研究目标:
  * 系统梳理 2021–2023 年间使用遥感数据和机器学习 / 深度学习估算土壤有机碳（SOC）的研究进展。
  * 分析 SOC 遥感估算中常用的数据源、输入变量、卫星平台、空间分辨率、光谱分辨率和 AI 模型。
  * 比较 Deep Learning（DL）、Traditional Neural Network（TNN）和 Other Machine Learning（O-ML）在 SOC 预测中的表现。
  * 识别 SOC 大尺度估算中的关键影响因素，包括采样密度、输入变量质量、空间分布代表性和多时相数据使用情况。
* 预测的土壤属性:
  * Soil Organic Carbon, SOC
  * Soil Organic Matter, SOM
  * 部分被综述文献也涉及土壤养分、土壤理化属性或植被覆盖等辅助预测目标，但本文核心聚焦 SOC / SOM。
* 任务类型:
  * 系统文献综述，Systematic Literature Review, SLR
  * PRISMA 流程文献筛选
  * SOC 遥感估算方法比较
  * 遥感数据 + 机器学习 / 深度学习的应用综述
  * 大尺度数字土壤制图方法总结
* 应用场景:
  * 大尺度 SOC 监测
  * 农业土壤肥力评价
  * 土壤碳储量估算
  * 气候变化缓解与碳循环监测
  * 土壤退化与荒漠化评价
  * 区域尺度 / 国家尺度数字土壤制图
  * 遥感辅助精准农业管理

## 数据集

* 数据集名称:
  * 非单一实验数据集。
  * 本文构建的是一个关于“遥感数据 + AI 方法估算 SOC”的系统综述文献数据库。
* 数据来源:
  * Scopus
  * Web of Science, WoS
  * 检索时间范围主要为 2021–2023 年。
  * 选择该时间范围的原因是已有相关综述覆盖到 2020 年左右，本文意在更新近年研究进展。
* 样本数量:
  * 初始检索得到 125 篇文章：
    * WoS: 47 篇
    * Scopus: 78 篇
  * 删除重复文献 49 篇后，剩余 76 篇。
  * Screening 阶段保留 43 篇。
  * Eligibility 阶段排除 7 篇。
  * 最终纳入 36 篇文献进行系统综述。
  * 被综述研究中的 SOC 样本数量差异很大：
    * 平均样本数约 1513
    * 中位数约 249
    * 标准差约 6115
    * 有个别研究使用超过 3 万个土壤样本点
  * 多数研究的采样密度低于 1 个样本 / km²。
* 光谱范围:
  * 主要包括遥感影像中的可见光、近红外、短波红外和少量热红外波段。
  * 常见光谱区域：
    * VIS: 400–700 nm
    * NIR: 700–1200 nm
    * SWIR: 1200–2500 nm
    * TIR: 8000–14,000 nm
  * SOC 建模中最常使用的是 VIS、NIR 和 SWIR 区域。
  * 本文不局限于实验室土壤光谱，而是更关注卫星、无人机、航空和野外光谱仪等遥感平台。
* 波段数量:
  * 不同遥感平台波段数量不同。
  * Sentinel-2 和 Landsat 系列是最常用的数据源。
  * Sentinel-2 包含多个可见光、红边、近红外和短波红外波段。
  * Landsat 8 常用 30 m 多光谱波段。
  * 部分研究使用高光谱数据，例如 UAV 高光谱、航空高光谱或 PRISMA 数据。
  * 多光谱数据更易获取，高光谱数据在光谱细节上更强，但应用成本和数据处理复杂度更高。
* 标签类型:
  * 土壤采样点对应的 SOC / SOM 实测值。
  * 实验室测定通常作为模型训练与验证的参考标签。
  * 标签一般为连续型变量，因此主要是回归任务。
* 数据划分方式:
  * 本文为系统综述，没有统一实验数据划分。
  * 被综述研究中常见的数据划分方式包括：
    * 训练集 / 测试集划分
    * 交叉验证
    * 随机划分
    * 不同模型间性能比较
  * 论文对验证方式的统计不如对数据源、模型类型、采样密度和输入变量的统计详细。
  * 从科研角度看，很多 SOC 遥感研究仍可能存在随机划分导致空间泛化能力被高估的问题。
* 是否公开:
  * 本文综述的文献列表和质量评价表在论文附录中提供。
  * 原始 SOC 样点数据、遥感影像和模型代码是否公开取决于各被综述论文。
  * 本文自身不提供统一的 SOC 遥感训练数据集。

## 方法

* 输入数据:
  * 遥感光谱数据：
    * 卫星影像
    * 野外光谱仪数据
    * 航空影像
    * UAV 影像
  * 植被指数和土壤指数：
    * NDVI
    * EVI
    * RVI
    * SAVI
    * DVI
    * TVI
    * BI
  * 地形变量：
    * DEM
    * Elevation
    * Slope
    * Aspect
    * Topographic Wetness Index, TWI
    * Valley Depth
    * Topographic Position Index, TPI
    * Profile Curvature
  * 气候变量：
    * 降水
    * 温度
    * 蒸散相关变量
  * 其他辅助变量：
    * 土地利用
    * 土壤类型
    * 地质信息
    * 森林类型
    * 植被参数
    * 土壤属性
* 光谱预处理:
  * 本文不是单一模型实验论文，因此没有统一的光谱预处理流程。
  * 被综述研究常见处理包括：
    * 卫星影像重采样
    * 波段统一空间分辨率
    * 植被指数计算
    * 土壤指数计算
    * 遥感影像与土壤样点空间匹配
    * DEM 派生地形因子计算
    * 多源数据融合
    * 高光谱波段选择
  * 部分研究将不同空间分辨率的数据重采样到 10 m、20 m、30 m 或 300 m。
  * Sentinel-2、Landsat、MODIS、DEM 等多源数据常被融合使用。
* 模型结构:
  * 本文将模型分为三大类：
    * Deep Learning, DL
    * Traditional Neural Network, TNN
    * Other Machine Learning, O-ML
  * DL 模型包括：
    * DNN
    * CNN
    * 1D-CNN
    * LSTM
    * CNN-LSTM
    * CAE-DNN
    * SA-DNN
    * Hybrid CNN-RNN
    * LSM-ResNet
    * Semi-DNNR
  * TNN 模型包括：
    * ANN
    * MLP
    * BPNN
  * O-ML 模型包括：
    * Random Forest, RF
    * Support Vector Machine / Regression, SVM / SVR
    * Partial Least Squares, PLS
    * XGBoost, XGB
    * Cubist
    * GBDT
    * KNN
    * Lasso
    * Gaussian Process Regression, GPR
    * Kriging-based methods
    * Multiple Linear Regression, MLR
    * Ordinary Least Squares, OLS
* 损失函数:
  * 本文为系统综述，没有统一讨论各模型的损失函数。
  * 大多数 SOC 估算模型属于回归模型，通常以最小化预测误差为优化目标。
  * 对深度学习模型而言，常见损失函数可能是 MSE 或 RMSE 相关目标，但本文未系统统计。
* 训练策略:
  * 被综述研究通常基于实测 SOC 样点训练模型，再使用遥感变量进行空间预测。
  * 常见训练策略包括：
    * 多源遥感变量融合
    * 特征选择
    * 高光谱波段筛选
    * 训练集 / 测试集划分
    * 交叉验证
    * 深度网络训练
    * 传统机器学习模型调参
  * 部分代表性策略：
    * CAE-DNN: 先用 Concrete Autoencoder 选择关键变量，再用 DNN 预测 SOC。
    * CNN-LSTM: CNN 提取空间特征，LSTM 提取时间序列特征。
    * SA-DNN: 使用模拟退火优化 DNN，并结合高光谱变量选择。
    * Semi-DNNR: 半监督深度神经网络回归，用于样本有限场景。
* 对比方法:
  * 模型层面对比：
    * DL vs TNN vs O-ML
    * CNN / DNN / LSTM 与 RF / SVM / PLS 等传统模型比较
  * 数据源层面对比：
    * Sentinel
    * Landsat
    * MODIS
    * Gaofen
    * PRISMA
    * DEM
    * UAV
    * 航空影像
    * 野外光谱仪
  * 输入变量层面对比：
    * 光谱波段
    * 植被指数
    * 地形指数
    * 气候变量
    * 土壤属性
    * 土地利用
  * 空间分辨率层面对比：
    * <10 m
    * 10–30 m
    * > 30 m
      >
    * 250–300 m
* 评价指标:
  * R²
  * RMSE
  * 部分研究还使用 MAE、Bias 或其他回归评价指标。
  * 本文主要使用 R² 和 RMSE 总结模型性能。
  * 作者重点比较不同模型类别在 R² 上的整体表现。

## 创新点

* 创新点 1:
  * 聚焦 2021–2023 年最新研究，补充已有 SOC 遥感深度学习综述之后的进展。
  * 文章反映了近几年 SOC 遥感估算从野外光谱仪逐渐转向卫星遥感数据的趋势。
* 创新点 2:
  * 系统比较 DL、TNN 和 O-ML 三类模型在 SOC 估算中的表现。
  * 文章不仅列举模型，还进一步分析不同模型类别的 R² 分布，指出 DL 模型总体表现更强。
* 创新点 3:
  * 将采样密度、遥感平台、空间分辨率、植被指数、地形指数和模型性能联系起来分析。
  * 论文强调样本空间分布和环境异质性代表性比单纯样本数量更重要，这对 SOC 遥感制图实验设计有较强启发。

## 实验结果

* 主要结果:
  * 最终纳入 36 篇文献，其中 2022 年和 2023 年相关研究数量明显增加。
  * 研究国家分布不均，中国相关研究最多，其次为伊朗、南非、美国和摩洛哥等。
  * 卫星数据已成为 SOC 遥感估算的主流数据源，在被综述研究中使用比例约为 80%。
  * 野外光谱仪使用比例约为 19%，UAV 使用比例较低，约为 3%。
  * Sentinel 系列，尤其 Sentinel-2，是最常用的卫星数据源之一。
  * Landsat 8 也是常用数据源。
  * 常用空间分辨率集中在 10–30 m。
  * 常见输入变量包括 NDVI、SAVI、EVI、RVI 等植被指数，以及 DEM 派生的 elevation、slope、aspect、TWI 等地形因子。
  * 多数研究采样密度低于 1 个样本 / km²。
  * 采样密度对模型 R² 有影响，但只能解释约 36% 的 R² 变异，剩余部分由输入变量、地形、气候、模型结构和数据质量等因素决定。
  * DL 模型整体上表现优于 TNN 和 O-ML，但在部分研究中 RF、SVR、GBDT、OLS、Lasso 等传统模型仍可能取得更好结果。
* 最优指标:
  * 本文没有给出统一最优模型的单一数值。
  * Figure 14 显示 DL 模型的 R² 中位数和平均水平整体高于 TNN 和 O-ML。
  * DL 模型在多个研究中表现出更高稳定性和预测能力。
  * 但 O-ML 模型结果分散较大，在部分数据集上也可能表现很好。
* 与基线相比的提升:
  * 本文为综述论文，不提出新的统一算法，因此没有单一基线提升值。
  * 从文献趋势看，DL 模型通常比传统神经网络和传统机器学习模型具有更强 SOC 估算能力。
  * 代表性研究显示：
    * CAE-DNN 优于普通 DNN 和 Boruta-DNN。
    * CNN-LSTM 能同时利用空间和时间特征，在 SOC 预测中表现较好。
    * CNN、DNN、Hybrid CNN-RNN 等模型在多篇研究中优于 RF、SVM、PLS 等传统方法。
  * 但作者也指出，数据量、样本空间分布和输入变量质量对模型性能有重要影响，不能简单认为 DL 在所有情况下都必然最优。
* 消融实验:
  * 本文没有传统意义上的消融实验。
  * 但系统综述中分析了多个影响维度：
    * 样本数量
    * 采样密度
    * 输入变量类型
    * 遥感平台
    * 空间分辨率
    * 光谱区域
    * 模型类别
    * 是否使用多时相数据
  * 多数被综述论文并未进行严格消融，因此不同变量对 SOC 预测的独立贡献仍需要进一步研究。
* 外部验证:
  * 本文没有开展新的外部验证实验。
  * 被综述论文覆盖 13 个国家，具有一定文献层面的外部性。
  * 但不同研究的数据集、区域、验证方式、空间尺度和模型设置差异很大，不能等同于统一标准下的外部验证。
  * 作者指出样本空间分布和异质性覆盖对模型性能很关键，未来应加强跨区域、跨时间和跨传感器验证。

## 不足

* 数据层面不足:
  * 多数研究采样密度偏低，通常低于 1 个样本 / km²。
  * SOC 样本数量差异极大，少数大样本研究会显著影响总体统计。
  * 原始样点数据和代码并不统一公开，降低了可复现性。
  * 不同研究使用的遥感平台、空间分辨率、输入变量和研究区尺度差异明显。
  * 样本总数不是唯一关键，样本是否覆盖地形、气候、土地利用和土壤类型异质性更重要。
* 方法层面不足:
  * 不同论文模型评价方式不完全一致，R² 和 RMSE 的可比性有限。
  * 许多研究仍可能使用随机划分训练集和测试集，存在空间自相关导致精度高估的风险。
  * 深度学习模型表现较好，但部分结果可能受输入变量数量、数据预处理、调参程度和验证方式影响。
  * 对特征选择、变量冗余和输入变量之间的共线性讨论仍不足。
  * 多时相数据潜力较大，但实际使用研究很少。
* 实验设计不足:
  * 很多研究没有充分讨论采样设计对模型性能的影响。
  * 对 spatial block validation、leave-region-out validation、temporal validation 等严格验证方式关注不足。
  * 遥感像元与土壤样点之间存在尺度不匹配问题，但综述对这一问题的深入讨论有限。
  * 多源变量融合常被使用，但缺少系统分析哪些变量组合最稳定、最可泛化。
* 泛化能力问题:
  * SOC 遥感模型容易受研究区特定地形、气候、土地利用和植被条件影响。
  * 在一个区域训练的模型未必能迁移到另一个区域。
  * 遥感变量与 SOC 的关系很多是间接关系，例如 NDVI、EVI、DEM 只是环境协变量，不一定直接反映 SOC 光谱特征。
  * 跨区域、跨年份、跨传感器的泛化能力仍是关键挑战。
* 可解释性问题:
  * DL 模型总体效果较好，但解释性不足。
  * 很多研究仍停留在模型精度比较，缺少对 SOC 形成机制和环境驱动因素的解释。
  * 遥感变量与 SOC 之间可能存在相关性而非因果关系。
  * 未来需要结合 SHAP、变量重要性、敏感性分析和不确定性评估增强模型解释能力。

## 是否值得复现

* 结论:
  * 不建议完整复现整篇系统综述。
  * 值得将其作为 SOC 遥感 + 深度学习方向的基础综述文献。
  * 值得选择其中的代表性技术路线进行复现实验，例如 Sentinel-2 + DEM + vegetation indices + RF / XGBoost / CNN / DNN。
* 理由:
  * 本文不是提出新算法的实验论文，而是系统总结近年研究趋势。
  * 其价值主要在于帮助确定研究空白、数据源选择和模型比较框架。
  * 对后续开题、写综述、设计 SOC 预测实验有较高参考价值。
  * 复现某个具体被综述模型比复现整篇综述更有意义。
* 复现难度:
  * 完整复现系统综述：中等偏高。
  * 复现单个 SOC 遥感预测流程：中等。
  * 难点主要包括：
    * 获取一致的 SOC 样点数据
    * 遥感影像预处理
    * 多源数据空间匹配
    * 采样密度与空间验证设计
    * 模型调参和公平比较
* 数据可获得性:
  * Sentinel-2、Landsat、MODIS、SRTM DEM 等遥感数据公开可得。
  * SOC 样点数据不一定公开。
  * 可使用公开土壤数据库或区域调查数据作为标签。
  * 高光谱 UAV 或航空数据获取难度较高。
* 代码可获得性:
  * 本文没有提供统一代码。
  * 具体代码取决于被综述论文。
  * 但基于 Google Earth Engine、Python、scikit-learn、PyTorch 或 TensorFlow 可自行复现常见 SOC 遥感建模流程。
* 预计复现价值:
  * 高。
  * 尤其适合复现以下方向：
    * Sentinel-2 + DEM + RF / XGBoost baseline
    * Sentinel-2 + multi-temporal indices + CNN-LSTM
    * 多源变量选择与冗余消除
    * 随机划分 vs 空间块验证对模型性能的影响
    * 小样本 SOC 预测中的 DL 与传统 ML 比较

## 对我的启发

* 对数据处理的启发:
  * SOC 遥感预测不能只依赖单一影像，应融合光谱、地形、气候、土地利用等多源变量。
  * NDVI、SAVI、EVI、RVI 等植被指数是常见有效输入，但它们主要是 SOC 的间接代理变量。
  * DEM 派生变量非常重要，因为地形影响水分、侵蚀、沉积和有机质积累。
  * 样本空间分布比样本总数更关键，应优先覆盖不同地形、土地利用、气候和土壤类型。
  * 未来实验中应避免只使用随机划分，应增加空间块验证。
* 对模型设计的启发:
  * DL 模型在文献中整体表现较好，但必须与 RF、SVM、XGBoost、PLS、Cubist 等强基线公平比较。
  * CNN 适合处理空间局部特征，LSTM 适合处理时间序列，CNN-LSTM 或 Temporal Transformer 可能适合多时相 SOC 预测。
  * CAE-DNN 的变量选择思想值得借鉴，可用于减少输入变量冗余。
  * 对小样本 SOC 数据，不能盲目使用复杂深度模型，应重视正则化、特征选择和空间验证。
  * 模型创新不应只是换 backbone，而应围绕空间泛化、多时相建模和不确定性估计展开。
* 对实验设计的启发:
  * 实验至少应设计：
    * Random split
    * Spatial block split
    * Leave-region-out split
    * Temporal split
  * 应比较单时相与多时相遥感数据。
  * 应比较仅光谱变量、光谱 + DEM、光谱 + DEM + 气候、光谱 + DEM + 气候 + 土地利用等组合。
  * 应报告 R²、RMSE、MAE、Bias 和空间误差分布。
  * 应分析采样密度和样本空间代表性对模型性能的影响。
* 对后续研究方向的启发:
  * 方向1：基于 Sentinel-2 多时相数据的 SOC 预测。
  * 方向2：SOC 遥感建模中的空间块验证与泛化能力评估。
  * 方向3：样本空间代表性与主动采样设计。
  * 方向4：多源数据融合下的变量选择与冗余控制。
  * 方向5：CNN-LSTM / Temporal Transformer 用于长期 SOC 预测。
  * 方向6：跨区域 SOC 迁移学习。
  * 方向7：SOC 遥感预测中的可解释性分析和不确定性估计。

## 个人备注

* 需要进一步查证的问题:
  * 36 篇被综述论文中，哪些使用了严格的空间验证？
  * DL 模型表现更好是否受到随机划分和空间自相关影响？
  * Sentinel-2 红边波段在 SOC 预测中的实际贡献有多大？
  * 多时相遥感变量相比单时相变量能提升多少？
  * 样本密度、样本空间分布和研究区异质性之间如何共同影响模型性能？
  * 高光谱数据相比 Sentinel-2 / Landsat 多光谱数据在 SOC 预测中是否具有稳定优势？
* 可引用的关键观点:
  * SOC 是土壤肥力、土壤健康、碳储量和气候变化缓解的重要指标。
  * 实验室 SOC 测定昂贵、耗时且可能产生化学废弃物，因此遥感和 AI 方法具有重要应用价值。
  * 近年来卫星数据已成为 SOC 遥感估算的主流数据源，尤其是 Sentinel-2 和 Landsat 8。
  * NDVI、SAVI、EVI 等植被指数和 DEM 派生地形变量是 SOC 预测中常用且重要的输入。
  * DL 模型整体上表现优于传统神经网络和其他机器学习模型，但其优势依赖于数据质量和验证方式。
  * 样本空间分布和环境异质性代表性比单纯样本数量更重要。
  * 多时相和高光谱数据仍有较大研究潜力。
* 可能关联的论文:
  * Odebiri et al., 2021, Deep learning approaches in remote sensing of soil organic carbon: A review of utility, challenges, and prospects.
  * Odebiri et al., 2022, Deep learning-based national scale soil organic carbon mapping with Sentinel-3 data.
  * Odebiri et al., 2023, Mapping soil organic carbon distribution across South Africa’s major biomes using remote sensing-topo-climatic covariates and Concrete Autoencoder-Deep neural networks.
  * Zhang et al., 2022, A CNN-LSTM model for soil organic carbon content prediction with long time series of MODIS-based phenological variables.
  * Meng et al., 2022, An advanced SOC prediction model via fused temporal-spatial-spectral information.
  * Padarian et al., 2019, Transfer learning to localise a continental soil vis-NIR calibration model.
  * Ahmadi et al., 2021, Soil Properties Prediction for Precision Agriculture Using Visible and Near-Infrared Spectroscopy: A Systematic Review and Meta-Analysis.
* 后续行动:
  * 将本文作为 SOC 遥感 + AI 方向的核心综述加入文献库。
  * 单独整理“Sentinel-2 + DEM + vegetation indices for SOC prediction”的方法笔记。
  * 复现一个基线流程：Sentinel-2 + DEM + RF / XGBoost。
  * 进一步设计严格实验：Random split vs Spatial block split。
  * 查找 CNN-LSTM、多时相 SOC 预测和 CAE-DNN 变量选择相关论文。
  * 后续若做深度学习模型，应把研究重点放在空间泛化、多时相建模、变量选择和可解释性，而不是单纯提高随机划分下的 R²。
