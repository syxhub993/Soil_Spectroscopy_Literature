# Basic and deep learning models in remote sensing of soil organic carbon estimation: A brief review

## 基本信息

* 标题: Basic and deep learning models in remote sensing of soil organic carbon estimation: A brief review
* 作者: Omosalewa Odebiri, John Odindi, Onisimo Mutanga
* 年份: 2021
* 期刊: International Journal of Applied Earth Observation and Geoinformation
* DOI/链接: [https://doi.org/10.1016/j.jag.2021.102389](https://doi.org/10.1016/j.jag.2021.102389)

## 研究问题

* 研究目标:
  * 简要综述传统神经网络（Traditional Neural Networks, TNN）和深度学习（Deep Learning, DL）在遥感土壤有机碳（SOC）估算中的应用。
  * 梳理从基础神经网络模型向深度学习模型发展的技术路线。
  * 总结 BPNN、MLP、RBF、ELM、CNN、RNN 等模型在 SOC / SOM 遥感估算中的作用、优势和局限。
  * 分析深度学习在 SOC 遥感制图中尚未广泛应用的原因。
  * 提出未来 SOC 遥感深度学习研究方向，包括多光谱数据、图像融合、UAV、Autoencoder、DBN 和迁移学习。
* 预测的土壤属性:
  * Soil Organic Carbon, SOC
  * Soil Organic Matter, SOM
  * 文章主要围绕 SOC / SOM 遥感估算展开，少量讨论也涉及其他土壤属性预测经验。
* 任务类型:
  * 简短综述，brief review
  * 遥感 SOC 估算方法综述
  * 传统神经网络与深度学习模型对比
  * 技术发展路线梳理
  * 未来研究方向讨论
* 应用场景:
  * 大尺度 SOC 遥感估算
  * 土壤碳储量监测
  * 气候变化缓解研究
  * 农业、生态和可持续发展研究
  * 遥感影像驱动的 SOC / SOM 制图
  * 土壤属性非破坏性估算

## 数据集

* 数据集名称:
  * 本文不是实验论文，没有构建或使用单一数据集。
  * 文章综述了已有 SOC / SOM 遥感估算研究中使用的神经网络和深度学习模型。
* 数据来源:
  * 已发表文献。
  * 涉及的遥感数据来源包括：
    * Hyperion
    * AVHRR
    * MODIS
    * LUCAS 光谱库
    * Vis–NIR 光谱仪数据
    * 卫星高光谱和多光谱数据
    * 潜在 UAV 数据源
  * 文章没有使用系统综述式检索流程，也没有给出 PRISMA 筛选步骤。
* 样本数量:
  * 不适用。
  * 本文为 brief review，不报告统一样本数量。
  * 被引用的原始研究样本数量各不相同。
* 光谱范围:
  * 文中涉及多个光谱范围：
    * Hyperion: 约 400–2500 nm
    * Vis–NIR: 约 305–2200 nm 或 350–2500 nm
    * MODIS: 约 400–2300 nm
    * LUCAS 光谱库: 400–2500 nm
  * 文章同时讨论高光谱、多光谱和潜在雷达数据在 SOC 遥感估算中的应用。
* 波段数量:
  * 不统一。
  * 高光谱数据通常具有连续窄波段。
  * 多光谱数据波段较少，但作者认为新一代多光谱卫星如 Sentinel-2、Sentinel-3、WorldView-2/3、RapidEye 具有更好的 SOC 估算潜力。
  * 本文没有统计各数据源具体波段数量。
* 标签类型:
  * SOC / SOM 实测值。
  * 通常来自实验室化学测定或已有土壤数据库。
  * 标签为连续数值，因此任务本质是回归预测。
* 数据划分方式:
  * 不适用。
  * 本文为综述论文，没有统一训练集、验证集或测试集划分。
  * 被引用研究中具体划分方式取决于原始论文。
* 是否公开:
  * 本文没有提供统一数据集。
  * 被引用数据如 LUCAS 光谱库具有一定公开性。
  * 其他原始研究中的遥感影像和土壤样点数据是否公开取决于具体论文。

## 方法

* 输入数据:
  * 遥感影像：
    * 高光谱影像
    * 多光谱影像
    * 潜在雷达影像
  * 土壤光谱数据：
    * Vis–NIR 光谱
    * 实验室或原位光谱
  * 环境变量：
    * 土壤相关变量
    * 地形变量
    * 气候变量
    * 土地覆盖变量
  * 文章重点不是具体输入变量组合，而是不同神经网络模型如何处理遥感数据。
* 光谱预处理:
  * 本文没有系统总结光谱预处理方法。
  * 讨论中涉及遥感数据的高维性、多波段连续性和复杂预处理需求。
  * 文中提到遥感数据处理受模型类型影响较大。
  * 对未来方向，作者提出图像融合可作为提升空间—光谱信息质量的重要方法。
* 模型结构:
  * Traditional Neural Network, TNN:
    * BPNN, Backpropagation Neural Network
    * MLP, Multilayer Perceptron
    * RBF, Radial Basis Function Network
    * ELM, Extreme Learning Machine
  * Deep Learning, DL:
    * CNN, Convolutional Neural Network
    * RNN, Recurrent Neural Network
    * LSTM, Long Short-Term Memory Network
    * GRU, Gated Recurrent Unit
    * AE, Autoencoder
    * DBN, Deep Belief Network
    * GAN, Generative Adversarial Network
  * 作者指出，截至该文写作时，SOC / SOM 遥感研究中真正广泛应用的主流 DL 模型仍较少，主要集中在 CNN 和 RNN / LSTM 方向。
* 损失函数:
  * 本文没有系统讨论损失函数。
  * 被综述模型多属于回归任务，通常目标是最小化 SOC / SOM 预测误差。
  * 对深度学习模型，常见损失可能是 MSE 或类似回归误差，但本文未展开。
* 训练策略:
  * TNN:
    * BPNN 通过前向传播和反向传播训练网络。
    * MLP 通过隐藏层和权重参数学习输入与 SOC 之间的非线性关系。
    * RBF 使用径向基函数进行函数逼近。
    * ELM 随机生成隐藏层参数，并解析求解输出权重，以加快训练。
  * DL:
    * CNN 通过卷积层、池化层和全连接层自动提取空间 / 波段特征。
    * RNN 通过循环结构处理序列数据。
    * LSTM / GRU 用于缓解普通 RNN 的长期依赖问题。
    * Transfer learning 被作者提出为未来解决小样本 SOC 遥感建模的重要策略。
* 对比方法:
  * 传统神经网络之间的比较：
    * BPNN
    * MLP
    * RBF
    * ELM
  * 传统神经网络与深度学习模型比较：
    * TNN vs CNN
    * TNN vs RNN / LSTM
  * 与传统机器学习或统计模型的关系：
    * PLSR
    * PCA
    * SVM
    * RF
  * 作者主要进行概念性比较，没有进行统一实验或定量性能比较。
* 评价指标:
  * 本文没有统一汇总评价指标。
  * 被引用原始研究一般使用 SOC 回归预测常见指标：
    * R²
    * RMSE
    * MAE
    * prediction accuracy
  * 文章更关注模型结构、应用潜力和局限，而非指标排名。

## 创新点

* 创新点 1:
  * 将 SOC 遥感估算中的神经网络方法按 TNN 和 DL 进行梳理。
  * 对 BPNN、MLP、RBF、ELM、CNN、RNN 等模型的基本结构和适用性进行了简明解释。
* 创新点 2:
  * 明确指出 SOC 遥感研究正从传统神经网络和传统机器学习逐步转向深度学习。
  * 强调 DL 能够从复杂遥感数据中自动学习特征表示，适合处理高维、多波段和非线性的 SOC 估算问题。
* 创新点 3:
  * 提出多个未来研究方向：
    * 多光谱传感器 + DL
    * 图像融合
    * UAV 平台
    * Autoencoder
    * DBN
    * transfer learning
  * 这些方向后来在 SOC 遥感研究中逐渐成为热点，因此本文具有较强的前瞻性。

## 实验结果

* 主要结果:
  * 本文没有开展新实验。
  * 作者通过文献回顾认为，传统神经网络已经在 SOC / SOM 遥感估算中取得一定成功，但存在训练困难、收敛慢、对权重敏感、浅层结构表达能力有限等问题。
  * DL 模型相比 TNN 具有更强的特征学习能力，能够更好处理遥感数据中的复杂非线性关系。
  * CNN 被认为是遥感任务中最强大且最常见的 DL 模型之一，适合多波段遥感影像和土壤光谱数据。
  * RNN / LSTM 适合处理序列数据，具有应用于多时相遥感 SOC 估算的潜力。
  * 多光谱卫星、图像融合和迁移学习被认为是未来 SOC 遥感深度学习的重要方向。
* 最优指标:
  * 不适用。
  * 本文没有进行统一实验比较，因此没有报告最优 R²、RMSE 或 MAE。
  * 文章的主要价值在于模型谱系总结和研究方向判断。
* 与基线相比的提升:
  * 不适用。
  * 本文没有提出新模型或新实验。
  * 但从综述角度看，作者认为 DL 相比传统 ML / TNN 在复杂非线性建模和自动特征提取方面具有潜在优势。
* 消融实验:
  * 无。
  * 本文为 brief review，没有消融实验。
* 外部验证:
  * 无。
  * 本文没有开展模型训练和外部验证。
  * 对模型泛化、跨区域验证和空间块验证的讨论较少。

## 不足

* 数据层面不足:
  * 本文没有系统文献检索流程，也没有报告纳入文献数量。
  * 没有构建统一文献数据库。
  * 没有统计不同研究的数据源、样本数量、空间分辨率和采样密度。
  * 对数据可得性、样本空间分布和标签质量的讨论较少。
  * 对 SOC 遥感中样本稀缺问题有讨论，但不够定量。
* 方法层面不足:
  * 文章主要是概念性综述，缺少定量比较。
  * 没有系统分析不同模型在不同数据源下的性能差异。
  * 对深度学习模型的讲解较基础，缺少更深入的网络结构、训练细节和优化策略比较。
  * 对自监督学习、Transformer、domain adaptation 等新兴方法没有涉及，因为文章发表时间较早。
* 实验设计不足:
  * 本文不是实验论文，因此没有统一实验设计。
  * 没有对不同模型进行同一数据集上的公平比较。
  * 没有讨论随机划分、空间块验证、跨区域验证等验证策略对 SOC 估算结果的影响。
  * 没有提供可复现的实验框架。
* 泛化能力问题:
  * 作者提到 SOC 具有动态性，不同研究区之间差异较大，会导致模型精度不一致。
  * 但文章没有深入展开跨区域泛化问题。
  * 没有系统讨论 domain shift、transfer learning 的具体实现路径和评价方式。
  * 对遥感数据尺度不匹配问题讨论不足。
* 可解释性问题:
  * 作者指出 DL 存在 interpretability 问题。
  * 但没有详细介绍解释方法，例如 SHAP、saliency map、attention visualization 或 feature importance。
  * 对 SOC 形成机制和模型预测机制之间的关系讨论较少。

## 是否值得复现

* 结论:
  * 不值得作为实验论文完整复现。
  * 值得作为 SOC 遥感深度学习方向的入门综述和理论背景文献。
  * 值得基于本文提出的未来方向设计后续实验。
* 理由:
  * 本文没有提出新数据集、新模型或新实验结果。
  * 其主要价值是梳理模型谱系和指出未来方向。
  * 对理解 TNN 到 DL 的技术演化很有帮助。
  * 对写论文引言和研究背景有较高引用价值。
* 复现难度:
  * 完整复现不适用。
  * 若复现文中提到的典型模型路线，难度如下：
    * BPNN / MLP / RBF / ELM: 低到中等
    * CNN / RNN / LSTM: 中等
    * Autoencoder / DBN / GAN / Transfer learning: 中等到较高
  * 主要难点不在模型代码，而在获取高质量 SOC 样本和遥感数据匹配。
* 数据可获得性:
  * 本文没有数据集。
  * 可结合公开数据进行后续实验：
    * Sentinel-2
    * Sentinel-3
    * Landsat
    * MODIS
    * LUCAS
    * SoilGrids
    * ISRIC / WoSIS
  * 高质量地面 SOC 样本仍是主要限制。
* 代码可获得性:
  * 本文没有代码。
  * 所述模型可用常见工具实现：
    * scikit-learn
    * TensorFlow
    * Keras
    * PyTorch
    * Google Earth Engine
  * 文章提到的深度学习工具包括 TensorFlow、Keras、Microsoft Cognitive Toolkit 等。
* 预计复现价值:
  * 直接复现价值较低。
  * 作为后续研究路线设计的价值较高。
  * 建议复现或扩展以下方向：
    * Sentinel-2 + CNN / MLP 预测 SOC
    * 多光谱 + 高光谱融合预测 SOC
    * UAV 多光谱 SOC 制图
    * Autoencoder 进行 SOC 输入变量选择
    * Transfer learning 解决小样本区域 SOC 预测

## 对我的启发

* 对数据处理的启发:
  * 遥感 SOC 估算面临高维、多波段、多时相和大数据量挑战，需要合理的数据预处理和特征选择。
  * 多光谱传感器并非不能用于 SOC 预测，新一代 Sentinel-2 / Sentinel-3 等数据具有较大潜力。
  * 图像融合值得关注，可以弥补单一遥感数据空间分辨率或光谱分辨率不足的问题。
  * UAV 数据适合田块尺度和高分辨率 SOC 研究，但需要注意标定和泛化问题。
* 对模型设计的启发:
  * 传统神经网络模型如 BPNN、MLP、RBF、ELM 可以作为早期基线方法。
  * CNN 适合处理多波段遥感影像和空间邻域信息。
  * RNN / LSTM 适合处理多时相遥感数据和光谱序列。
  * Autoencoder 可用于特征选择、降维和无监督表示学习。
  * Transfer learning 可用于缓解 SOC 样本不足问题。
  * 后续模型创新不应只停留在换模型名称，而应围绕小样本、跨区域泛化、多源融合和可解释性展开。
* 对实验设计的启发:
  * 应将传统 ML、TNN 和 DL 放在同一数据集上公平比较。
  * 应设置强基线：
    * RF
    * SVM
    * XGBoost
    * PLSR
    * MLP
    * CNN
  * 应避免只使用随机划分，应增加：
    * spatial block validation
    * leave-region-out validation
    * temporal validation
  * 对多时相数据，应考虑 LSTM、GRU、Temporal CNN 或 Temporal Transformer。
  * 对小样本区域，应考虑迁移学习或自监督预训练。
* 对后续研究方向的启发:
  * 方向1：多光谱遥感 + DL 的 SOC 估算。
  * 方向2：Sentinel-1 / Sentinel-2 / DEM 多源融合。
  * 方向3：UAV 多光谱或高光谱 SOC 田块尺度制图。
  * 方向4：Autoencoder 用于 SOC 预测变量选择与降维。
  * 方向5：Transfer learning 用于小样本 SOC 遥感估算。
  * 方向6：RNN / LSTM / Temporal Transformer 用于多时相 SOC 建模。
  * 方向7：可解释深度学习揭示 SOC 遥感预测机制。

## 个人备注

* 需要进一步查证的问题:
  * 文中提到的 CNN 和 RNN 在 SOC 遥感中的早期应用具体数据集和性能。
  * Autoencoder、DBN、GAN 在 2021 年以后是否已经被用于 SOC 预测。
  * Sentinel-2 / Sentinel-3 多光谱数据在 SOC 估算中相较高光谱数据的性能差距。
  * Transfer learning 在 SOC 遥感中的实际效果。
  * UAV 平台 SOC 制图是否能有效迁移到卫星尺度。
  * 深度学习模型在 spatial block validation 下是否仍优于 RF / XGBoost 等传统模型。
* 可引用的关键观点:
  * SOC 是重要的陆地碳库，对气候变化缓解和土壤质量评价具有重要意义。
  * 遥感数据具有高维、多时空、大数据量特点，因此需要先进的分析方法。
  * 深度学习能够从数据中自动学习复杂特征表示，适合处理非线性的 SOC 遥感估算问题。
  * 传统神经网络在 SOC / SOM 预测中已有应用，但受限于浅层结构、收敛速度、权重敏感性和训练难度。
  * CNN 是遥感应用中最常见和最强大的深度学习模型之一。
  * RNN / LSTM 对多时相 SOC 遥感估算具有潜力。
  * 深度学习在 SOC 遥感中的主要障碍包括样本需求大、计算成本高、可解释性弱、云覆盖、地面样本不足和过拟合。
  * 多光谱传感器、图像融合、UAV、Autoencoder、DBN 和迁移学习是未来值得探索的方向。
* 可能关联的论文:
  * Lima et al., 2025, Soil Organic Carbon Assessment Using Remote-Sensing Data and Machine Learning: A Systematic Literature Review.
  * Odebiri et al., 2023, Mapping soil organic carbon distribution across South Africa’s major biomes using remote sensing-topo-climatic covariates and Concrete Autoencoder-Deep neural networks.
  * Odebiri et al., 2022, Deep learning-based national scale soil organic carbon mapping with Sentinel-3 data.
  * Padarian et al., 2019, Using deep learning to predict soil properties from regional spectral data.
  * Tsakiridis et al., 2020, Simultaneous prediction of soil properties from VNIR-SWIR spectra using a localized multi-channel 1-D CNN.
  * Veres et al., 2015, Deep learning architectures for soil property prediction.
  * Wadoux et al., 2019, Multi-source data integration for soil mapping using deep learning.
  * Ahmadi et al., 2021, Soil Properties Prediction for Precision Agriculture Using Visible and Near-Infrared Spectroscopy.
  * Piccini et al., 2024, In-field soil spectroscopy in Vis–NIR range for fast and reliable soil analysis.
* 后续行动:
  * 将本文作为 SOC 遥感深度学习方向的早期综述加入阅读库。
  * 与 Lima et al. 2025 对照阅读，分析 2021 年提出的未来方向在 2025 年前哪些已经发展、哪些仍是空白。
  * 单独整理 TNN 与 DL 在 SOC 遥感中的模型谱系笔记。
  * 查找 Autoencoder、Transfer Learning、CNN-LSTM 和 Sentinel-2 SOC 预测相关论文。
  * 后续实验可优先设计：
    * Sentinel-2 + DEM + RF / XGBoost / CNN 基线比较
    * 多时相 Sentinel-2 + LSTM / Temporal Transformer
    * Autoencoder 特征选择 + DNN
    * 小样本区域 SOC 迁移学习
    * random split 与 spatial block split 对比
