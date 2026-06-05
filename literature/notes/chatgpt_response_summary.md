# ChatGPT 回复总结

说明：当前环境没有直接调用另一个 ChatGPT 对话并读取其回复的独立通道。因此本文件先根据项目现状和拟发送提示词，整理一份“预期回复应提炼出的行动清单”。等拿到外部 ChatGPT 的实际回复后，可将本文件更新为真实回复总结。

## 预期应从 ChatGPT 回复中提取的信息

### 1. 新增文献候选

重点从回复中筛选以下类型文献：

- soil spectral library 数据集论文
- OSSL、LUCAS、KSSL、global SSL 相关论文
- calibration transfer / spectral transfer function 论文
- domain adaptation / transfer learning for soil spectroscopy
- self-supervised learning for spectral 或 hyperspectral data
- multitask learning for soil property prediction
- explainability / band selection 论文
- 1D CNN / Transformer for soil spectra 论文
- PLSR、Cubist、RF、SVR、GPR 强基线论文

### 2. Zotero 归档原则

如果 ChatGPT 推荐数据集或光谱库论文：

- 放入 `01_Soil_Spectral_Libraries`
- 同时视情况放入 `11_Datasets_and_Benchmarks`
- 若数据/代码可用，放入 `12_Reproducible_Papers`

如果推荐深度学习模型论文：

- 放入 `04_Deep_Learning`
- 若涉及 Transformer，加 `transformer`
- 若涉及 CNN，加 `cnn`

如果推荐跨域或迁移论文：

- 放入 `05_Transfer_Learning_Domain_Adaptation`
- 若有明确研究 gap，同时放入 `13_Possible_Research_Gaps`

如果推荐解释性或波段选择论文：

- 放入 `08_Explainability_Band_Selection`

### 3. 当前最应优先补的文献类型

当前不是继续补普通综述，而是补以下原始论文：

1. OSSL / LUCAS / KSSL 数据集和 benchmark 论文。
2. Cubist、PLSR、RF、SVR 等强基线论文。
3. 跨数据集 soil spectra prediction 论文。
4. calibration transfer / instrument harmonization 论文。
5. self-supervised 或 domain adaptation 在光谱数据中的方法论文。

### 4. 推荐的研究路线判断

从目前已有文献看，最稳妥路线是：

```text
OSSL/LUCAS/KSSL 上的 SOC 跨数据集预测 benchmark
```

原因：

- 数据和应用场景清晰。
- SOC 文献基础最成熟。
- 有强基线可比较。
- 可自然引出 domain adaptation、harmonization、uncertainty 和 explainability。

创新性更高的路线是：

```text
基于 spectral transfer function / domain adaptation 的 soil spectral library harmonization
```

原因：

- 直接面对不同光谱库协议不一致的问题。
- 比单纯换模型更接近真实研究 gap。
- 可结合 OSSL、LUCAS、BSSL、KSSL 等数据。

最容易复现的路线是：

```text
OSSL 上复现 Cubist / RF / PLSR baseline，然后加入 1D CNN 或 Transformer 对比
```

原因：

- OSSL 是开放资源。
- 传统模型 baseline 明确。
- 后续可以逐步扩展深度学习。

### 5. 下一步执行清单

1. 建立 `literature/papers/paper_index.md`。
2. 把 ChatGPT 推荐的每篇论文录入 paper index。
3. 先筛出 10 篇最高优先级论文。
4. 优先精读 OSSL 2025 和 Spectral Transfer Function 2023。
5. 针对 OSSL 建立第一个复现实验计划。
6. 查找并补充 LUCAS、KSSL、global SSL 的原始数据论文。
7. 查找 soil spectra 上的 domain adaptation / transfer learning 原始论文。

## 待外部 ChatGPT 回复后补充

收到外部 ChatGPT 的实际回复后，应补充：

- 推荐论文列表
- 每篇论文的 DOI/链接
- 对应 Zotero collection
- 推荐标签
- 精读优先级
- 复现优先级
- 是否可能形成 SCI 方向
