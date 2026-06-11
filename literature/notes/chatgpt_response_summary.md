
# 一、总体判断

你现在不应该继续堆普通综述，而应该转向  **“可复现实验论文 + 跨库泛化论文 + 方法型论文”** 。你的第一篇 SCI 更适合从：

> **OSSL / LUCAS / KSSL 的 SOC 跨数据集预测 benchmark**

切入，然后再向：

> **spectral harmonization / domain adaptation / self-supervised representation**

扩展。

原因是：纯粹做“1D CNN 或 Transformer 比 PLSR 高一点”创新性不够，而且容易被审稿人质疑 baseline 不公平；但如果你先建立跨数据集 benchmark，再评估 PLSR、Cubist、RF、SVR、GPR、1D CNN、Transformer、harmonization 和 self-supervised encoder，就能形成更扎实的论文逻辑。

---

# 二、优先推荐文献清单

## 2.1 最高优先级：建议立即精读

### 1. Vestergaard et al., 2021

| 项目              | 内容                                                                                                                                                       |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 标题              | *Evaluation of Optimized Preprocessing and Modeling Algorithms for Prediction of Soil Properties Using VIS-NIR Spectroscopy*                             |
| 作者              | Rebecca-Jo Vestergaard et al.                                                                                                                              |
| 年份              | 2021                                                                                                                                                       |
| 期刊              | Sensors                                                                                                                                                    |
| DOI / 链接        | 10.3390/s21206745                                                                                                                                          |
| Zotero collection | `03_Chemometrics_and_ML_Baselines`,`12_Reproducible_Papers`                                                                                            |
| 标签              | `baseline`,`method-paper`,`PLSR`,`RF`,`Cubist`,`reproduce`,`must-read`                                                                       |
| 研究任务          | 不同预处理 × 不同模型组合下的土壤属性预测                                                                                                                 |
| 数据集            | Ontario, Canada 土壤 VIS-NIR 光谱，343–2200 nm                                                                                                            |
| 方法              | 13 种预处理组合；PLSR、Cubist、RF、ELM                                                                                                                     |
| 主要贡献          | 提供了非常适合你复现实验的 baseline 框架；论文比较了 1st derivative、2nd derivative、SG、gap、SNV、detrend 等预处理，并与 PLSR、Cubist、RF、ELM 组合建模。 |
| 主要不足          | 区域性数据集，跨库泛化不是主线。                                                                                                                           |
| 是否值得精读      | 是，第一优先级                                                                                                                                             |
| 是否值得复现      | 非常值得                                                                                                                                                   |
| 对你的启发        | 你的 benchmark 应该先建立 `预处理 × 传统强基线`框架，而不是直接上深度学习。                                                                             |

这篇文章明确报告了 VIS-NIR 光谱范围、预处理组合、PLSR/Cubist/RF/ELM 建模，并指出不同土壤属性需要不同预处理和模型组合。([MDPI](https://www.mdpi.com/1424-8220/21/20/6745 "Evaluation of Optimized Preprocessing and Modeling Algorithms for Prediction of Soil Properties Using VIS-NIR Spectroscopy | MDPI"))

---

### 2. Tsakiridis et al., 2020

| 项目              | 内容                                                                                                                                   |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 标题              | *Simultaneous prediction of soil properties from VNIR-SWIR spectra using a localized multi-channel 1-D convolutional neural network* |
| 作者              | N. L. Tsakiridis, K. D. Keramaris, J. B. Theocharis, G. C. Zalidis                                                                     |
| 年份              | 2020                                                                                                                                   |
| 期刊              | Geoderma                                                                                                                               |
| DOI / 链接        | 10.1016/j.geoderma.2020.114208                                                                                                         |
| Zotero collection | `04_Deep_Learning`,`07_Multitask_Learning`,`12_Reproducible_Papers`                                                              |
| 标签              | `deep-learning`,`cnn`,`multitask-learning`,`soil-organic-carbon`,`soil-texture`,`must-read`,`reproduce`                  |
| 研究任务          | VNIR-SWIR 光谱多土壤属性同步预测                                                                                                       |
| 数据集            | VNIR-SWIR soil spectra                                                                                                                 |
| 方法              | localized multi-channel 1D CNN                                                                                                         |
| 主要贡献          | 这是土壤光谱 1D CNN 和多任务预测方向非常对口的论文。                                                                                   |
| 主要不足          | 如果只在单一数据源上验证，跨库泛化仍不足。                                                                                             |
| 是否值得精读      | 是                                                                                                                                     |
| 是否值得复现      | 非常值得                                                                                                                               |
| 对你的启发        | 可作为你深度学习模型的第一个强基线，而不是一开始就做 Transformer。                                                                     |

> DOI 我较有把握，但本轮检索没有稳定打开出版社页面，建议你导入 Zotero 时再核查一次。

---

### 3. Liu et al., 2018

| 项目              | 内容                                                                                                                                                            |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 标题              | *Transfer Learning for Soil Spectroscopy Based on Convolutional Neural Networks and Its Application in Soil Clay Content Mapping Using Hyperspectral Imagery* |
| 作者              | L. Liu, M. Ji, M. Buchroithner                                                                                                                                  |
| 年份              | 2018                                                                                                                                                            |
| 期刊              | Sensors                                                                                                                                                         |
| DOI / 链接        | 10.3390/s18103169                                                                                                                                               |
| Zotero collection | `05_Transfer_Learning_Domain_Adaptation`,`04_Deep_Learning`,`13_Possible_Research_Gaps`                                                                   |
| 标签              | `transfer-learning`,`domain-adaptation`,`cnn`,`soil-texture`,`classic`,`must-read`                                                                  |
| 研究任务          | CNN 迁移学习用于土壤 clay content mapping                                                                                                                       |
| 数据集            | 土壤高光谱 / hyperspectral imagery                                                                                                                              |
| 方法              | CNN + transfer learning                                                                                                                                         |
| 主要贡献          | 说明 soil spectroscopy 中的 transfer learning 不是空想，而是已有可借鉴路线。                                                                                    |
| 主要不足          | 目标属性是 clay，不是 SOC；更偏成像高光谱。                                                                                                                     |
| 是否值得精读      | 是                                                                                                                                                              |
| 是否值得复现      | 中高                                                                                                                                                            |
| 对你的启发        | 可作为你做 LUCAS → OSSL / KSSL 或 lab → field 迁移时的思想起点。                                                                                              |

> DOI 需要你在 Zotero 中再核查一次；我不建议直接复制进最终参考文献前不核查。

---

### 4. Piccoli et al., 2022

| 项目              | 内容                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 标题              | *A deep scalable neural architecture for soil properties estimation from spectral information*                         |
| 作者              | Flavio Piccoli, Micol Rossini, Roberto Colombo, Raimondo Schettini, Paolo Napoletano                                     |
| 年份              | 2022                                                                                                                     |
| 来源              | arXiv，journal paper 版本                                                                                                |
| DOI / 链接        | 10.48550/arXiv.2210.17314                                                                                                |
| Zotero collection | `04_Deep_Learning`,`07_Multitask_Learning`,`08_Explainability_Band_Selection`,`12_Reproducible_Papers`           |
| 标签              | `deep-learning`,`multitask-learning`,`explainability`,`band-selection`,`LUCAS`,`reproduce`,`sci-potential` |
| 研究任务          | 多土壤属性预测 + 关键波段回溯                                                                                            |
| 数据集            | LUCAS；模拟 PRISMA hyperspectral sensor                                                                                  |
| 方法              | adaptive deep neural architecture                                                                                        |
| 主要贡献          | 同时支持多属性预测、关键波段回溯、不同 spectral library 自适应。                                                         |
| 主要不足          | 预印本，需要确认是否已有正式发表版本。                                                                                   |
| 是否值得精读      | 非常值得                                                                                                                 |
| 是否值得复现      | 中高                                                                                                                     |
| 对你的启发        | 很适合连接你的三个目标：multitask learning、explainability、cross-library prediction。                                   |

该论文明确提出用于多土壤变量预测的自适应深度架构，并强调可回溯贡献波段，实验使用 LUCAS 和模拟 PRISMA 数据。([arXiv](https://arxiv.org/abs/2210.17314 "[2210.17314] A deep scalable neural architecture for soil properties estimation from spectral information"))

---

### 5. Sun et al., 2025

| 项目              | 内容                                                                                                                                    |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| 标题              | *Self-supervised and Multi-fidelity Learning for Extended Predictive Soil Spectroscopy*                                               |
| 作者              | Luning Sun, José L. Safanelli, Jonathan Sanderman 等                                                                                   |
| 年份              | 2025                                                                                                                                    |
| 来源              | arXiv，submitted to Geoderma                                                                                                            |
| DOI / 链接        | 10.48550/arXiv.2511.15965                                                                                                               |
| Zotero collection | `06_Self_Supervised_Learning`,`05_Transfer_Learning_Domain_Adaptation`,`11_Datasets_and_Benchmarks`,`13_Possible_Research_Gaps` |
| 标签              | `self-supervised`,`transfer-learning`,`deep-learning`,`KSSL`,`2022-2025`,`must-read`,`sci-potential`                      |
| 研究任务          | 自监督表征学习；NIR→MIR spectral conversion；多属性预测                                                                                |
| 数据集            | MIR spectral library；KSSL paired NIR/MIR subset                                                                                        |
| 方法              | VAE latent embedding + multi-fidelity learning                                                                                          |
| 主要贡献          | 利用大规模 MIR 光谱库预训练 latent space，再将 NIR 光谱映射到 MIR 表征空间，最后做多土壤属性预测。                                      |
| 主要不足          | 目前是预印本；工程复杂度较高。                                                                                                          |
| 是否值得精读      | 非常值得                                                                                                                                |
| 是否值得复现      | 中等，建议第二阶段再复现                                                                                                                |
| 对你的启发        | 这是你未来做 self-supervised soil spectra 的重要参考，但不建议第一步就直接做。                                                          |

该文提出使用大 MIR 光谱库进行自监督 VAE 表征学习，并用 KSSL 的 paired NIR/MIR 光谱学习 NIR→MIR 映射，再用于 9 个土壤属性预测。([arXiv](https://arxiv.org/abs/2511.15965 "[2511.15965] Self-supervised and Multi-fidelity Learning for Extended Predictive Soil Spectroscopy"))

---

# 三、第二优先级：建议近期加入 Zotero 并阅读

## 3.1 深度学习与多任务学习

### 6. Li et al., 2020

| 项目              | 内容                                                                      |
| ----------------- | ------------------------------------------------------------------------- |
| 标题              | *Simultaneous Prediction of Soil Properties Using Multi_CNN Model*      |
| 作者              | Ruixue Li, Bo Yin, Yanping Cong, Zehua Du                                 |
| 年份              | 2020                                                                      |
| 期刊              | Sensors                                                                   |
| DOI / 链接        | 10.3390/s20216271                                                         |
| Zotero collection | `04_Deep_Learning`,`07_Multitask_Learning`,`12_Reproducible_Papers` |
| 标签              | `deep-learning`,`cnn`,`multitask-learning`,`reproduce`            |
| 研究任务          | 多土壤属性同步预测                                                        |
| 数据集            | 两个不同尺度的 soil NIR spectral datasets                                 |
| 方法              | dual-stream Multi_CNN：1D convolution + 2D convolution                    |
| 主要贡献          | 将光谱序列和光谱图像两种表示融合，实现多属性预测。                        |
| 主要不足          | 更偏工程模型，跨库泛化不是核心。                                          |
| 是否值得精读      | 可读                                                                      |
| 是否值得复现      | 高                                                                        |
| 对你的启发        | 可作为轻量级 multitask CNN baseline。                                     |

该文提出 Multi_CNN，同时从 spectral sequence 和 spectrogram 中提取特征，并进行多属性同步预测。([MDPI](https://www.mdpi.com/1424-8220/20/21/6271 "Simultaneous Prediction of Soil Properties Using Multi_CNN Model"))

---

### 7. Riese & Keller, 2019

| 项目              | 内容                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| 标题              | *Soil Texture Classification with 1D Convolutional Neural Networks based on Hyperspectral Data* |
| 作者              | Felix M. Riese, Sina Keller                                                                       |
| 年份              | 2019                                                                                              |
| 来源              | arXiv / ISPRS Geospatial Week                                                                     |
| DOI / 链接        | 10.48550/arXiv.1901.04846                                                                         |
| Zotero collection | `04_Deep_Learning`,`11_Datasets_and_Benchmarks`,`12_Reproducible_Papers`                    |
| 标签              | `cnn`,`soil-texture`,`LUCAS`,`reproduce`,`must-read`                                    |
| 研究任务          | LUCAS topsoil texture classification                                                              |
| 数据集            | LUCAS topsoil                                                                                     |
| 方法              | LucasCNN、LucasResNet、LucasCoordConv，与 RF 对比                                                 |
| 主要贡献          | 代码可用，适合作为 1D CNN pipeline 起点。                                                         |
| 主要不足          | 分类任务，不是 SOC 连续回归。                                                                     |
| 是否值得精读      | 是                                                                                                |
| 是否值得复现      | 非常值得                                                                                          |
| 对你的启发        | 可用来快速搭建 LUCAS 光谱输入、划分、归一化和 CNN 训练流程。                                      |

论文明确使用 freely available LUCAS topsoil dataset，并实现多个 1D CNN 变体且提供 GitHub 代码。([arXiv](https://arxiv.org/abs/1901.04846 "[1901.04846] Soil Texture Classification with 1D Convolutional Neural Networks based on Hyperspectral Data"))

---

### 8. Miao et al., 2024

| 项目              | 内容                                                                                                                                                            |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 标题              | *Advanced Soil Organic Matter Prediction with a Regional Soil NIR Spectral Library Using Long Short-Term Memory–Convolutional Neural Networks: A Case Study* |
| 作者              | Miao et al.                                                                                                                                                     |
| 年份              | 2024                                                                                                                                                            |
| 期刊              | Remote Sensing                                                                                                                                                  |
| DOI / 链接        | Remote Sensing 16, 1256；DOI 需 Zotero 核查                                                                                                                     |
| Zotero collection | `04_Deep_Learning`,`11_Datasets_and_Benchmarks`                                                                                                             |
| 标签              | `deep-learning`,`cnn`,`soil-organic-carbon`,`2022-2025`                                                                                                 |
| 研究任务          | 区域 NIR spectral library 上的 SOM 预测                                                                                                                         |
| 数据集            | regional soil NIR spectral library                                                                                                                              |
| 方法              | LSTM-CNN                                                                                                                                                        |
| 主要贡献          | 把光谱当作序列建模，适合你比较 CNN、LSTM、Transformer。                                                                                                         |
| 主要不足          | 区域案例，外部泛化仍需验证。                                                                                                                                    |
| 是否值得精读      | 可读                                                                                                                                                            |
| 是否值得复现      | 中等                                                                                                                                                            |
| 对你的启发        | 可作为 Transformer 前的序列模型过渡 baseline。                                                                                                                  |

---

## 3.2 迁移学习、domain adaptation、spiking

### 9. Bogner et al., 2017

| 项目              | 内容                                                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------------------------------- |
| 标题              | *Predicting with limited data – Increasing the accuracy in VIS-NIR diffuse reflectance spectroscopy by SMOTE* |
| 作者              | Christina Bogner, Anna Kühnel, Bernd Huwe                                                                       |
| 年份              | 2017                                                                                                             |
| 来源              | arXiv / workshop final version                                                                                   |
| DOI / 链接        | 10.48550/arXiv.1703.04961                                                                                        |
| Zotero collection | `05_Transfer_Learning_Domain_Adaptation`,`03_Chemometrics_and_ML_Baselines`,`13_Possible_Research_Gaps`    |
| 标签              | `classic`,`baseline`,`domain-adaptation`,`soil-organic-carbon`,`reproduce`                             |
| 研究任务          | field spectra 稀缺时的 synthetic spiking                                                                         |
| 数据集            | air-dried spectra + rare field spectra                                                                           |
| 方法              | PLS + SMOTE                                                                                                      |
| 主要贡献          | 用简单方法解决 lab spectra 与 field spectra 不匹配问题。                                                         |
| 主要不足          | 方法传统，不是深度学习。                                                                                         |
| 是否值得精读      | 是                                                                                                               |
| 是否值得复现      | 非常值得                                                                                                         |
| 对你的启发        | 任何 deep domain adaptation 都应该和这种简单 spiking baseline 比较。                                             |

该文报告了在 field spectra 稀缺情况下，用 SMOTE 生成 synthetic field spectra 并 spiking 到 air-dried calibration set 中，SOC 预测 RMSEP 从 6.18 降到 2.12 mg g⁻¹，R² 从负值提升到 0.82。([arXiv](https://arxiv.org/abs/1703.04961?utm_source=chatgpt.com "Predicting with limited data - Increasing the accuracy in VIS-NIR diffuse reflectance spectroscopy by SMOTE"))

---

### 10. Padarian et al., 2019

| 项目              | 内容                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------ |
| 标题              | *Transfer learning to localise a continental soil vis-NIR calibration model*       |
| 作者              | Padarian et al.                                                                      |
| 年份              | 2019                                                                                 |
| 期刊              | 需核查                                                                               |
| DOI / 链接        | DOI 需核查                                                                           |
| Zotero collection | `05_Transfer_Learning_Domain_Adaptation`,`13_Possible_Research_Gaps`             |
| 标签              | `transfer-learning`,`domain-adaptation`,`global-ssl`,`possible-research-gap` |
| 研究任务          | continental calibration model local adaptation                                       |
| 数据集            | continental soil vis-NIR spectral dataset                                            |
| 方法              | transfer learning / model localization                                               |
| 主要贡献          | 很适合你的 “global / continental SSL → local dataset” 问题。                      |
| 主要不足          | 需要核查全文和具体实现细节。                                                         |
| 是否值得精读      | 值得，但先核查版本                                                                   |
| 是否值得复现      | 中等                                                                                 |
| 对你的启发        | 可作为 OSSL/LUCAS/KSSL 跨库迁移的理论支撑。                                          |

> 这篇题名我高度确信存在，但 DOI 和期刊信息本轮未稳定核实，先放 `99_To_Read`，导入 Zotero 时核查。

---

### 11. Francos et al., 2023

| 项目              | 内容                                                                                                     |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| 标题              | spectral transfer function / harmonizing soil spectral libraries 相关论文                                |
| 作者              | Francos et al.                                                                                           |
| 年份              | 2023                                                                                                     |
| 期刊              | 你已整理                                                                                                 |
| DOI / 链接        | 已在你的已有 summary 中                                                                                  |
| Zotero collection | `05_Transfer_Learning_Domain_Adaptation`,`01_Soil_Spectral_Libraries`,`13_Possible_Research_Gaps`  |
| 标签              | `domain-adaptation`,`spectral-transfer`,`instrument-harmonization`,`must-read`,`sci-potential` |
| 研究任务          | soil spectral library harmonization                                                                      |
| 数据集            | heterogeneous soil spectral libraries                                                                    |
| 方法              | spectral transfer function                                                                               |
| 主要贡献          | 直接对应你的第二条 SCI 潜力路线。                                                                        |
| 主要不足          | 如果只做 transfer function 而没有 downstream SOC benchmark，论文说服力会弱。                             |
| 是否值得精读      | 已读后建议二刷                                                                                           |
| 是否值得复现      | 高                                                                                                       |
| 对你的启发        | 可以作为 benchmark 后的第二篇论文核心方法。                                                              |

---

## 3.3 Self-supervised learning / Transformer

### 12. Kakhani et al., 2023 / 2024

| 项目              | 内容                                                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 标题              | *SSL-SoilNet: A Hybrid Transformer-based Framework with Self-Supervised Learning for Large-scale Soil Organic Carbon Prediction* |
| 作者              | Nafiseh Kakhani et al.                                                                                                             |
| 年份              | 2023；2024 revised                                                                                                                 |
| 来源              | arXiv；accepted to IEEE TGRS                                                                                                       |
| DOI / 链接        | 10.48550/arXiv.2308.03586                                                                                                          |
| Zotero collection | `06_Self_Supervised_Learning`,`04_Deep_Learning`,`10_Soil_Carbon_MRV`,`13_Possible_Research_Gaps`                          |
| 标签              | `self-supervised`,`transformer`,`soil-organic-carbon`,`2022-2025`,`sci-potential`                                        |
| 研究任务          | large-scale SOC prediction                                                                                                         |
| 数据集            | 两个 large-scale datasets                                                                                                          |
| 方法              | self-supervised contrastive learning + ViT + climate Transformer                                                                   |
| 主要贡献          | 把 SSL、Transformer、多模态地理特征和 SOC prediction 结合起来。                                                                    |
| 主要不足          | 更偏 DSM / remote sensing，不是纯 proximal soil spectra。                                                                          |
| 是否值得精读      | 中高                                                                                                                               |
| 是否值得复现      | 中低，作为思想参考更合适                                                                                                           |
| 对你的启发        | 适合你未来把土壤光谱与遥感 / 气候 / 地形变量融合。                                                                                 |

该文使用 self-supervised contrastive learning、pretrained ViT 和 climate Transformer，并在两个 large-scale SOC datasets 上验证，且标注为 accepted to IEEE TGRS。([arXiv](https://arxiv.org/abs/2308.03586 "[2308.03586] SSL-SoilNet: A Hybrid Transformer-based Framework with Self-Supervised Learning for Large-scale Soil Organic Carbon Prediction"))

---

### 13. Ayuba et al., 2025

| 项目              | 内容                                                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- |
| 标题              | *SpecBPP: A Self-Supervised Learning Approach for Hyperspectral Representation and Soil Organic Carbon Estimation* |
| 作者              | Daniel La’ah Ayuba et al.                                                                                           |
| 年份              | 2025                                                                                                                 |
| 来源              | arXiv                                                                                                                |
| DOI / 链接        | 10.48550/arXiv.2507.19781                                                                                            |
| Zotero collection | `06_Self_Supervised_Learning`,`04_Deep_Learning`,`10_Soil_Carbon_MRV`,`13_Possible_Research_Gaps`            |
| 标签              | `self-supervised`,`band-selection`,`soil-organic-carbon`,`2022-2025`,`sci-potential`                       |
| 研究任务          | hyperspectral representation learning + SOC estimation                                                               |
| 数据集            | EnMAP satellite hyperspectral data                                                                                   |
| 方法              | Spectral Band Permutation Prediction, SpecBPP                                                                        |
| 主要贡献          | 设计了非常“光谱原生”的 self-supervised pretext task：打乱 spectral segments，让模型恢复正确顺序。                  |
| 主要不足          | 是 satellite HSI，不是 laboratory SSL；结果需等待同行评审。                                                          |
| 是否值得精读      | 作为创新灵感值得                                                                                                     |
| 是否值得复现      | 暂不建议第一阶段复现                                                                                                 |
| 对你的启发        | 可迁移为 soil spectra 的 band-order prediction / masked-band modeling。                                              |

该文提出 Spectral Band Permutation Prediction，并用于 EnMAP SOC estimation，报告 R²、RMSE 和 RPD 指标，属于很新的高风险高创新方向。([arXiv](https://arxiv.org/abs/2507.19781 "[2507.19781] SpecBPP: A Self-Supervised Learning Approach for Hyperspectral Representation and Soil Organic Carbon Estimation"))

---

### 14. Lei & Bailey, 2024

| 项目              | 内容                                                                                                           |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| 标题              | *A text-based, generative deep learning model for soil reflectance spectrum simulation in the VIS-NIR bands* |
| 作者              | Tong Lei, Brian N. Bailey                                                                                      |
| 年份              | 2024                                                                                                           |
| 来源              | arXiv                                                                                                          |
| DOI / 链接        | 10.48550/arXiv.2405.01060                                                                                      |
| Zotero collection | `06_Self_Supervised_Learning`,`11_Datasets_and_Benchmarks`,`13_Possible_Research_Gaps`                   |
| 标签              | `deep-learning`,`generative-model`,`dataset-paper`,`2022-2025`,`sci-potential`                       |
| 研究任务          | soil reflectance spectra simulation                                                                            |
| 数据集            | 近 180,000 soil spectra–property pairs，来自 17 个数据集                                                      |
| 方法              | diffusion-based soil optics generative model                                                                   |
| 主要贡献          | 可用于数据增强、光谱补全、湿土光谱模拟。                                                                       |
| 主要不足          | 生成模型的真实性与下游预测收益需要严格验证。                                                                   |
| 是否值得精读      | 第二阶段值得                                                                                                   |
| 是否值得复现      | 中等                                                                                                           |
| 对你的启发        | 可作为未来解决小样本、缺失波段、跨仪器差异的数据增强方向。                                                     |

该文使用约 18 万组 soil spectra–property pairs 和 17 个数据集训练生成模型，并提到可做光谱补全与湿土光谱模拟。([arXiv](https://arxiv.org/abs/2405.01060 "[2405.01060] A text-based, generative deep learning model for soil reflectance spectrum simulation in the VIS-NIR (400-2499 nm) bands"))

---

## 3.4 Cross-dataset / harmonization / strong baseline

### 15. Chiniadis & Tamvakis, 2023

| 项目              | 内容                                                                                                                                            |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 标题              | *Rapid detection of soil carbonates by means of NIR spectroscopy, deep learning methods and phase quantification by powder X-ray diffraction* |
| 作者              | Chiniadis, Tamvakis                                                                                                                             |
| 年份              | 2023                                                                                                                                            |
| 来源              | arXiv                                                                                                                                           |
| DOI / 链接        | 10.48550/arXiv.2307.12341                                                                                                                       |
| Zotero collection | `04_Deep_Learning`,`11_Datasets_and_Benchmarks`,`12_Reproducible_Papers`                                                                  |
| 标签              | `deep-learning`,`baseline`,`KSSL`,`LUCAS`,`reproduce`                                                                                 |
| 研究任务          | soil carbonates prediction                                                                                                                      |
| 数据集            | KSSL + LUCAS                                                                                                                                    |
| 方法              | MLP / CNN 与 PLSR / Cubist / SVM 等对比                                                                                                         |
| 主要贡献          | 很适合参考其 KSSL + LUCAS 跨库实验设计。                                                                                                        |
| 主要不足          | 目标属性是 carbonates，不是 SOC。                                                                                                               |
| 是否值得精读      | 可读                                                                                                                                            |
| 是否值得复现      | 中高                                                                                                                                            |
| 对你的启发        | 虽然目标不是 SOC，但它是“跨库 + deep learning + 强 baseline”的好模板。                                                                        |

---

### 16. Vohland et al., 2014

| 项目              | 内容                                                                                                                             |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 标题              | *Determination of soil properties with visible to near- and mid-infrared spectroscopy: Effects of spectral variable selection* |
| 作者              | Vohland et al.                                                                                                                   |
| 年份              | 2014                                                                                                                             |
| 期刊              | Geoderma                                                                                                                         |
| DOI / 链接        | DOI 需核查；可能为 10.1016/j.geoderma.2014.01.013                                                                                |
| Zotero collection | `08_Explainability_Band_Selection`,`03_Chemometrics_and_ML_Baselines`                                                        |
| 标签              | `classic`,`band-selection`,`baseline`,`must-read`                                                                        |
| 研究任务          | spectral variable selection 对土壤属性预测的影响                                                                                 |
| 数据集            | Vis-NIR / MIR soil spectra                                                                                                       |
| 方法              | variable selection + chemometric models                                                                                          |
| 主要贡献          | band selection 经典文献。                                                                                                        |
| 主要不足          | 年代较早，无深度学习。                                                                                                           |
| 是否值得精读      | 是                                                                                                                               |
| 是否值得复现      | 中等                                                                                                                             |
| 对你的启发        | 可作为 explainable band selection 的传统基线。                                                                                   |

---

### 17. Pouladi et al., 2019

| 项目              | 内容                                                                                           |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| 标题              | *Mapping soil organic matter contents at field level with Cubist, Random Forest and kriging* |
| 作者              | Pouladi et al.                                                                                 |
| 年份              | 2019                                                                                           |
| 期刊              | Geoderma                                                                                       |
| DOI / 链接        | DOI 需核查                                                                                     |
| Zotero collection | `03_Chemometrics_and_ML_Baselines`,`09_Digital_Soil_Mapping`,`12_Reproducible_Papers`    |
| 标签              | `baseline`,`Cubist`,`RF`,`soil-organic-carbon`,`reproduce`                           |
| 研究任务          | field-level SOM mapping                                                                        |
| 数据集            | field-level soil data                                                                          |
| 方法              | Cubist、RF、kriging                                                                            |
| 主要贡献          | 可把 soil spectroscopy prediction 与 digital soil mapping 连接起来。                           |
| 主要不足          | 非深度学习。                                                                                   |
| 是否值得精读      | 可读                                                                                           |
| 是否值得复现      | 高                                                                                             |
| 对你的启发        | 可作为你后续从“光谱预测”走向“空间制图”的桥梁文献。                                         |

---

# 四、暂时收藏，不急读

| 论文                                                                                                                                                                   | Collection                                                                   | 标签                                                    | 为什么先收藏                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------- |
| Wang et al., 2024,*Non-linear memory-based learning for predicting soil properties using a regional vis-NIR spectral library*                                        | `03_Chemometrics_and_ML_Baselines`,`12_Reproducible_Papers`              | `baseline`,`local-learning`,`2022-2025`           | local / memory-based learning 是很强 baseline，但先读 Vestergaard 更基础。 |
| Liu et al., 2023,*Simultaneous estimation of multiple soil properties under moist conditions using fractional-order derivative of vis-NIR spectra and deep learning* | `04_Deep_Learning`,`07_Multitask_Learning`,`13_Possible_Research_Gaps` | `deep-learning`,`moist-soil`,`multitask-learning` | 很贴近 lab-to-field，但应在基线框架建立后读。                              |
| Wang et al., 2025,*Multi-gate mixture-of-experts with data augmentation*                                                                                             | `04_Deep_Learning`,`07_Multitask_Learning`                               | `deep-learning`,`multitask-learning`,`2022-2025`  | 方法较复杂，适合第二阶段方法创新。                                         |
| Datta et al., 2025,*ReflectGAN*                                                                                                                                      | `10_Soil_Carbon_MRV`,`13_Possible_Research_Gaps`                         | `deep-learning`,`domain-cleaning`,`sci-potential` | 更偏遥感 SOC，可作为后续 EO 融合方向。                                     |
| Dey et al., 2025,*DeepSalt*                                                                                                                                          | `05_Transfer_Learning_Domain_Adaptation`                                   | `domain-adaptation`,`knowledge-distillation`        | 属性是 salinity，但 lab-to-satellite adaptation 思路值得借鉴。             |

---

# 五、优先阅读列表

## 5.1 最高优先级 5 篇

| 顺序 | 论文                     | 为什么先读                                                  |
| ---: | ------------------------ | ----------------------------------------------------------- |
|    1 | Vestergaard et al., 2021 | 建立预处理 × baseline 的公平实验框架                       |
|    2 | Tsakiridis et al., 2020  | 1D CNN + 多任务 soil spectra prediction 核心文献            |
|    3 | Liu et al., 2018         | transfer learning 在 soil spectroscopy 中的早期代表         |
|    4 | Piccoli et al., 2022     | 多任务 + band traceability + LUCAS                          |
|    5 | Sun et al., 2025         | self-supervised / multi-fidelity soil spectroscopy 最新方向 |

## 5.2 第二优先级 10 篇

| 顺序 | 论文                                                                   |
| ---: | ---------------------------------------------------------------------- |
|    1 | Li et al., 2020, Multi_CNN                                             |
|    2 | Riese & Keller, 2019, 1D CNN texture classification                    |
|    3 | Bogner et al., 2017, SMOTE / spiking                                   |
|    4 | Vohland et al., 2014, spectral variable selection                      |
|    5 | Chiniadis & Tamvakis, 2023, KSSL + LUCAS carbonates                    |
|    6 | Padarian et al., 2019, transfer learning to localise continental model |
|    7 | Miao et al., 2024, LSTM-CNN SOM                                        |
|    8 | Wang et al., 2024, memory-based learning                               |
|    9 | Kakhani et al., 2023/2024, SSL-SoilNet                                 |
|   10 | Lei & Bailey, 2024, generative soil spectra simulation                 |

## 5.3 暂时只收藏，不急读

* Ayuba et al., 2025, SpecBPP
* Wang et al., 2025, multi-gate mixture-of-experts
* Liu et al., 2023, moist soil + FOD + DL
* Datta et al., 2025, ReflectGAN
* Dey et al., 2025, DeepSalt
* Pouladi et al., 2019, Cubist/RF/kriging SOM mapping

---

# 六、研究路线判断

## 6.1 六个方向对比

| 方向                                            | 稳妥性 | 创新性 | 复现难度 | SCI 潜力 | 我的判断                                          |
| ----------------------------------------------- | -----: | -----: | -------: | -------: | ------------------------------------------------- |
| 1. OSSL/LUCAS/KSSL SOC 跨数据集 benchmark       |   很高 |   中高 |       中 |     很高 | **第一篇最推荐**                            |
| 2. spectral transfer function / harmonization   |     高 |     高 |     中高 |     很高 | **第二篇最推荐**                            |
| 3. 1D CNN / Transformer soil spectra prediction |     中 |     中 |       中 |       中 | 只能作为 benchmark 中的一部分                     |
| 4. Self-supervised pretraining for soil spectra |     中 |   很高 |       高 |     很高 | 第三阶段做，不适合一开始                          |
| 5. Multitask learning for SOC, texture, pH, CEC |   中高 |   中高 |       中 |       高 | 可作为 benchmark 扩展                             |
| 6. Explainable band selection                   |     高 |   中高 |     低中 |       高 | 最容易快速出结果，但要避免只做传统 band selection |

---

## 6.2 最稳妥方向

**方向 1：OSSL/LUCAS/KSSL 上的 SOC 跨数据集预测 benchmark。**

理由：

* 数据可获得性相对最好；
* 科学问题清楚：跨库、跨仪器、跨协议、跨区域泛化；
* baseline 明确：PLSR、Cubist、RF、SVR、GPR；
* 深度学习也可以纳入，但不是唯一卖点；
* 很适合做成 reproducible benchmark paper。

建议论文题目可以暂定为：

> **A reproducible cross-library benchmark for soil organic carbon prediction from Vis–NIR spectra**

---

## 6.3 创新性最高方向

**方向 4：Self-supervised pretraining for soil spectra。**

但前提是你不能简单套 MAE / SimCLR，而要设计光谱原生任务，例如：

* masked wavelength reconstruction；
* spectral segment order prediction；
* dry-to-moist spectrum prediction；
* NIR-to-MIR latent alignment；
* cross-instrument contrastive learning。

Sun et al. 的 self-supervised + multi-fidelity 思路和 Ayuba et al. 的 SpecBPP 思路都说明，这个方向正在变热，但还没有完全成熟。([arXiv](https://arxiv.org/abs/2511.15965 "[2511.15965] Self-supervised and Multi-fidelity Learning for Extended Predictive Soil Spectroscopy"))

---

## 6.4 最容易复现方向

**方向 6：Explainable band selection。**

最容易起步的组合是：

* 数据：LUCAS / OSSL
* 任务：SOC prediction
* 模型：PLSR、RF、Cubist、SVR、1D CNN
* 解释：VIP、permutation importance、SHAP、integrated gradients、attention
* 输出：关键波段稳定性分析

但要注意：如果只做“哪个波段重要”，创新性不够。你要把它升级为：

> **跨数据集关键波段稳定性分析**

也就是看 LUCAS、KSSL、OSSL 中 SOC 的关键波段是否一致。

---

## 6.5 最有 SCI 潜力方向

我建议你采用组合路线：

### 第一篇 SCI

**方向 1 + 方向 6：跨库 benchmark + 可解释波段稳定性**

核心问题：

> 不同 soil spectral libraries 上，SOC 预测模型的泛化能力如何？传统强基线、1D CNN 和解释性波段选择在跨库条件下是否稳定？

这是最稳的。

---

### 第二篇 SCI

**方向 2：spectral library harmonization**

核心问题：

> spectral transfer function / harmonization 能否显著提升 LUCAS、KSSL、OSSL 之间的 SOC 跨库泛化？

这篇更有方法深度。

---

### 第三篇 SCI

**方向 4 + 方向 5：self-supervised + multitask**

核心问题：

> 自监督光谱表征能否提升 SOC、texture、pH、CEC 多任务跨库泛化？

这篇创新性最高，但最好在你已有 benchmark 之后做。

---

# 七、下一步最具体的阅读顺序

## 7.1 第一周

* Vestergaard et al., 2021
* Riese & Keller, 2019
* Li et al., 2020

目标：搭建 baseline 和 1D CNN 代码思路。

## 7.2 第二周

* Tsakiridis et al., 2020
* Piccoli et al., 2022
* Vohland et al., 2014

目标：形成 multitask + explainability 思路。

## 7.3 第三周

* Liu et al., 2018
* Bogner et al., 2017
* Francos et al., 2023

目标：形成 transfer / harmonization 方案。

## 7.4 第四周

* Sun et al., 2025
* Kakhani et al., 2023/2024
* Ayuba et al., 2025

目标：判断 self-supervised 是否作为第二阶段创新路线。

---

# 八、最终建议

你的路线不要从 “Transformer for soil spectra” 开始，而应该从：

> **cross-library benchmark → harmonization → self-supervised / multitask / explainable deep learning**

开始。

这条路线更像科研问题，而不是模型替换。第一篇论文的最优形态是：

> **OSSL / LUCAS / KSSL 上的 SOC 跨数据集预测 benchmark，比较 PLSR、Cubist、RF、SVR、GPR、1D CNN，并分析关键波段稳定性与跨库误差来源。**

这是目前最稳、最容易落地、最有连续产出潜力的主线。
