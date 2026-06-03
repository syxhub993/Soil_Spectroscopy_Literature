# 土壤高光谱深度学习文献研究库

本仓库用于管理“土壤高光谱 × 深度学习 × 土壤属性预测”项目的文献调研资料。

本项目的定位是：**Zotero 管理论文本体，本仓库管理研究过程和研究产出**。

## 研究方向

- 土壤光谱学
- 高光谱遥感
- 深度学习
- 土壤属性预测

## 仓库结构

```text
literature/
  papers/
  notes/
  summaries/
  reading_plan/
  research_map/
zotero_setup/
  setup_zotero_collections.py
  .env.example
README.md
requirements.txt
.gitignore
.gitattributes
```

## 目录说明

- `literature/`: 本地文献研究工作区。
- `literature/papers/`: 后续可放论文索引，不建议大量存放 PDF。
- `literature/notes/`: 阅读笔记、想法、术语解释、研究问题。
- `literature/summaries/`: 论文精读总结和统一阅读模板。
- `literature/reading_plan/`: 文献阅读路线和阶段计划。
- `literature/research_map/`: 研究地图、方向树、研究缺口分析。
- `zotero_setup/`: Zotero collection 初始化脚本。

## Zotero 与本仓库的分工

Zotero 用来管理：

- 论文条目
- PDF
- DOI、期刊、作者等元数据
- 引用信息
- 标签
- 文献分类 collection

本仓库用来管理：

- 阅读计划
- 论文总结
- 研究地图
- 复现判断
- 研究 gap
- 后续写论文或建模时需要用到的研究思考

推荐工作流：

1. 新论文先放入 Zotero 的 `99_To_Read`。
2. 筛选后在 Zotero 中分类并打标签。
3. 精读总结写到 `literature/summaries/`。
4. 阅读过程中的想法写到 `literature/notes/`。
5. 值得复现的论文放入 Zotero 的 `12_Reproducible_Papers`。
6. 有研究空白启发的论文放入 Zotero 的 `13_Possible_Research_Gaps`。

## Zotero 初始化脚本

脚本位置：

```bash
zotero_setup/setup_zotero_collections.py
```

安装依赖：

```bash
pip install -r requirements.txt
```

在仓库根目录创建 `.env` 文件，参考 `zotero_setup/.env.example`：

```env
ZOTERO_API_KEY=your_zotero_api_key_here
ZOTERO_USER_ID=your_zotero_user_id_here
ZOTERO_LIBRARY_TYPE=user
```

运行脚本：

```bash
python zotero_setup/setup_zotero_collections.py
```

脚本会先检查 Zotero 中是否已经存在 collection：

- 已存在则跳过。
- 不存在则创建。
- 不会修改、移动或删除已有 Zotero 文献。

## Zotero Collection 结构

脚本会创建以下 Zotero collection 层级：

```text
Soil_Hyperspectral_DL_Research
  00_Reviews
  01_Soil_Spectral_Libraries
  02_Soil_Properties
  03_Chemometrics_and_ML_Baselines
  04_Deep_Learning
  05_Transfer_Learning_Domain_Adaptation
  06_Self_Supervised_Learning
  07_Multitask_Learning
  08_Explainability_Band_Selection
  09_Digital_Soil_Mapping
  10_Soil_Carbon_MRV
  11_Datasets_and_Benchmarks
  12_Reproducible_Papers
  13_Possible_Research_Gaps
  99_To_Read
```

## 建议标签体系

后续给论文打标签时，建议使用：

```text
classic
review
dataset-paper
method-paper
baseline
deep-learning
cnn
transformer
transfer-learning
domain-adaptation
self-supervised
multitask-learning
explainability
band-selection
soil-organic-carbon
soil-texture
pH
CEC
LUCAS
KSSL
global-ssl
must-read
reproduce
possible-research-gap
2022-2025
sci-potential
```

## 安全注意事项

- 不要提交 `.env` 文件。
- 不要把 Zotero API key 写进代码或 Markdown 文档。
- `.gitignore` 已经忽略 `.env`、Python 缓存和编辑器配置。
- 如果以后使用 Zotero group library，需要把 `ZOTERO_LIBRARY_TYPE` 改成 `group`，并使用 groupID。

## 当前阶段目标

未来一周主要做文献调研，暂不继续模型开发。

重点任务：

- 梳理土壤高光谱深度学习研究地图。
- 建立论文阅读路线。
- 找到 3 到 5 篇值得复现的核心论文。
- 总结可行的研究 gap。
- 为后续模型设计提供依据。
