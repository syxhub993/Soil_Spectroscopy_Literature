import os
import re
import sys
from typing import Dict, Iterable, List, Optional, Tuple

from dotenv import load_dotenv
from pyzotero import zotero


ROOT_COLLECTION = "Soil_Hyperspectral_DL_Research"

SUBCOLLECTIONS = [
    "00_Reviews",
    "01_Soil_Spectral_Libraries",
    "02_Soil_Properties",
    "03_Chemometrics_and_ML_Baselines",
    "04_Deep_Learning",
    "05_Transfer_Learning_Domain_Adaptation",
    "06_Self_Supervised_Learning",
    "07_Multitask_Learning",
    "08_Explainability_Band_Selection",
    "09_Digital_Soil_Mapping",
    "10_Soil_Carbon_MRV",
    "11_Datasets_and_Benchmarks",
    "12_Reproducible_Papers",
    "13_Possible_Research_Gaps",
    "99_To_Read",
]

ZOTERO_TAGS = [
    "classic",
    "review",
    "dataset-paper",
    "method-paper",
    "baseline",
    "deep-learning",
    "cnn",
    "transformer",
    "transfer-learning",
    "domain-adaptation",
    "self-supervised",
    "multitask-learning",
    "explainability",
    "band-selection",
    "soil-organic-carbon",
    "soil-texture",
    "pH",
    "CEC",
    "LUCAS",
    "KSSL",
    "global-ssl",
    "must-read",
    "reproduce",
    "possible-research-gap",
    "2022-2025",
    "sci-potential",
]

COLLECTION_GUIDES = {
    "00_Reviews": {
        "put": "综述、系统综述、meta-analysis、领域路线图论文。",
        "avoid": "只提出单一模型且没有系统梳理的普通方法论文。",
        "keywords": ["review", "soil spectroscopy", "hyperspectral", "soil property prediction", "digital soil mapping"],
        "questions": [
            "该综述如何划分 soil spectroscopy 研究方向？",
            "哪些数据集、方法和评价指标被反复提及？",
            "作者认为主要研究缺口是什么？",
        ],
    },
    "01_Soil_Spectral_Libraries": {
        "put": "土壤光谱库、光谱数据库、跨区域光谱样本构建与校准论文。",
        "avoid": "只使用某个光谱库做模型实验、但不讨论数据集本身的论文。",
        "keywords": ["soil spectral library", "SSL", "LUCAS", "KSSL", "global soil spectral library"],
        "questions": [
            "光谱范围、样本量、土壤属性标签是什么？",
            "是否公开？是否适合复现实验？",
            "不同仪器或地区之间如何校准？",
        ],
    },
    "02_Soil_Properties": {
        "put": "围绕具体土壤属性预测的论文，如 SOC、SOM、pH、CEC、texture、moisture、nitrogen。",
        "avoid": "没有明确土壤属性标签或只做传感器工程的论文。",
        "keywords": ["SOC", "SOM", "pH", "CEC", "clay", "sand", "silt", "moisture", "nitrogen"],
        "questions": [
            "目标属性是直接光谱响应还是间接相关？",
            "标签测量方式和误差来源是什么？",
            "不同属性之间是否适合多任务学习？",
        ],
    },
    "03_Chemometrics_and_ML_Baselines": {
        "put": "PLSR、SVR、Random Forest、Cubist、GBDT、GPR 等传统基线和化学计量学方法。",
        "avoid": "只报告深度学习模型且没有强基线对照的论文。",
        "keywords": ["PLSR", "SVR", "Random Forest", "Cubist", "chemometrics", "baseline"],
        "questions": [
            "哪些传统方法是该任务的强基线？",
            "预处理与基线组合是否公平？",
            "深度学习是否真正超过这些基线？",
        ],
    },
    "04_Deep_Learning": {
        "put": "使用 CNN、RNN、Transformer、attention、autoencoder 等深度学习模型的土壤光谱论文。",
        "avoid": "仅使用传统机器学习、没有深度模型的论文。",
        "keywords": ["deep learning", "1D CNN", "CNN", "Transformer", "attention", "autoencoder"],
        "questions": [
            "模型如何利用光谱序列结构？",
            "样本量是否足以支持深度学习？",
            "是否有防止过拟合的清晰策略？",
        ],
    },
    "05_Transfer_Learning_Domain_Adaptation": {
        "put": "迁移学习、域适应、跨仪器、跨区域、跨数据集泛化论文。",
        "avoid": "只在单一数据集随机划分上验证的普通模型论文。",
        "keywords": ["transfer learning", "domain adaptation", "domain shift", "cross-site", "cross-dataset"],
        "questions": [
            "源域和目标域分别是什么？",
            "域偏移来自地区、仪器、尺度还是水分状态？",
            "是否有外部验证？",
        ],
    },
    "06_Self_Supervised_Learning": {
        "put": "自监督、对比学习、掩码建模、无标签光谱表征学习论文。",
        "avoid": "没有无标签预训练或表征学习机制的普通监督学习论文。",
        "keywords": ["self-supervised", "contrastive learning", "masked modeling", "pretraining", "representation learning"],
        "questions": [
            "预训练任务是否符合光谱数据结构？",
            "无标签数据规模和来源是什么？",
            "下游任务收益是否稳定？",
        ],
    },
    "07_Multitask_Learning": {
        "put": "同时预测多个土壤属性或利用属性相关性的多任务学习论文。",
        "avoid": "只是分别训练多个单任务模型的论文。",
        "keywords": ["multitask learning", "multi-output regression", "joint prediction", "soil properties"],
        "questions": [
            "哪些土壤属性被联合预测？",
            "任务之间是互相增益还是互相干扰？",
            "是否分析属性相关性？",
        ],
    },
    "08_Explainability_Band_Selection": {
        "put": "模型解释、关键波段识别、变量重要性、attention 解释、波段选择论文。",
        "avoid": "只给出预测精度、不讨论可解释性或波段贡献的论文。",
        "keywords": ["explainability", "interpretability", "band selection", "wavelength selection", "feature importance"],
        "questions": [
            "识别出的关键波段是否有土壤学解释？",
            "解释方法是否稳定？",
            "波段选择是否提高泛化能力？",
        ],
    },
    "09_Digital_Soil_Mapping": {
        "put": "数字土壤制图、区域尺度预测、遥感高光谱影像制图论文。",
        "avoid": "只做实验室点光谱、没有空间制图目标的论文。",
        "keywords": ["digital soil mapping", "DSM", "hyperspectral image", "soil mapping", "remote sensing"],
        "questions": [
            "是否解决裸土像元识别？",
            "空间验证方式是否合理？",
            "模型如何处理光谱-空间信息？",
        ],
    },
    "10_Soil_Carbon_MRV": {
        "put": "土壤碳监测、SOC 估计、MRV、碳汇评估相关论文。",
        "avoid": "与 SOC 或碳监测无关的一般土壤属性论文。",
        "keywords": ["soil organic carbon", "SOC", "MRV", "carbon monitoring", "carbon stock"],
        "questions": [
            "是否支持监测、报告和核证场景？",
            "精度是否满足区域碳核算需求？",
            "不确定性如何估计？",
        ],
    },
    "11_Datasets_and_Benchmarks": {
        "put": "公开数据集、benchmark、评价协议、复现实验基准论文。",
        "avoid": "不提供数据或没有明确 benchmark 设置的普通应用论文。",
        "keywords": ["dataset", "benchmark", "open data", "reproducibility", "evaluation protocol"],
        "questions": [
            "数据和代码是否公开？",
            "划分协议是否能避免数据泄漏？",
            "是否适合成为项目基准？",
        ],
    },
    "12_Reproducible_Papers": {
        "put": "数据、方法、代码或实验设置足够清晰，值得优先复现的论文。",
        "avoid": "结果有趣但数据不可得、方法描述不清或复现成本过高的论文。",
        "keywords": ["reproduce", "open-source", "code available", "benchmark", "implementation"],
        "questions": [
            "复现需要哪些数据和依赖？",
            "最小可复现实验是什么？",
            "复现后能直接服务当前项目吗？",
        ],
    },
    "13_Possible_Research_Gaps": {
        "put": "暴露明确研究空白、方法缺陷、数据限制或未来工作机会的论文。",
        "avoid": "只作为背景引用、没有启发研究问题的论文。",
        "keywords": ["research gap", "limitation", "future work", "uncertainty", "generalization"],
        "questions": [
            "论文暴露了什么尚未解决的问题？",
            "这个 gap 是否有可操作实验？",
            "是否具备 SCI 论文潜力？",
        ],
    },
    "99_To_Read": {
        "put": "尚未阅读、待筛选、临时收集的候选论文。",
        "avoid": "已经精读并明确归类的论文。",
        "keywords": ["to-read", "candidate", "screening", "priority"],
        "questions": [
            "是否与土壤高光谱深度学习直接相关？",
            "优先级是高、中还是低？",
            "应归入哪个正式目录？",
        ],
    },
}


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def collection_parent_key(collection: dict) -> Optional[str]:
    parent = collection.get("data", {}).get("parentCollection")
    return parent or None


def load_all_collections(zot: zotero.Zotero) -> List[dict]:
    return zot.everything(zot.collections())


def build_collection_index(collections: Iterable[dict]) -> Dict[Tuple[str, Optional[str]], dict]:
    index = {}
    for collection in collections:
        data = collection.get("data", {})
        index[(data.get("name"), collection_parent_key(collection))] = collection
    return index


def create_collection(zot: zotero.Zotero, name: str, parent_key: Optional[str] = None) -> dict:
    template = {"name": name}
    if parent_key:
        template["parentCollection"] = parent_key
    created = zot.create_collections([template])
    if not created.get("success"):
        raise RuntimeError(f"Failed to create collection {name}: {created}")
    created_key = next(iter(created["success"].values()))
    return zot.collection(created_key)


def normalize_html_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", value).strip().lower()


def note_exists(zot: zotero.Zotero, collection_key: str, title: str) -> bool:
    try:
        items = zot.everything(zot.collection_items(collection_key))
    except Exception:
        items = []

    title_norm = title.lower()
    for item in items:
        data = item.get("data", {})
        if data.get("itemType") != "note":
            continue
        note_text = normalize_html_text(data.get("note", ""))
        if title_norm in note_text:
            return True
    return False


def html_list(values: List[str]) -> str:
    return "<ul>" + "".join(f"<li>{value}</li>" for value in values) + "</ul>"


def collection_note_html(collection_name: str) -> str:
    guide = COLLECTION_GUIDES[collection_name]
    return f"""
<h1>README - {collection_name}</h1>
<h2>这个目录放什么类型的论文</h2>
<p>{guide["put"]}</p>
<h2>不应该放什么</h2>
<p>{guide["avoid"]}</p>
<h2>典型关键词</h2>
{html_list(guide["keywords"])}
<h2>未来阅读时需要记录的问题</h2>
{html_list(guide["questions"])}
""".strip()


def root_note_html() -> str:
    return f"""
<h1>README - {ROOT_COLLECTION}</h1>
<p>本 collection 用于管理 Soil Spectroscopy × Hyperspectral Remote Sensing × Deep Learning × Soil Property Prediction 项目的文献。</p>
<h2>使用原则</h2>
<ul>
  <li>不移动或删除已有 Zotero 文献。</li>
  <li>新论文先放入 99_To_Read，精读后再归类。</li>
  <li>值得复现的论文同时放入 12_Reproducible_Papers。</li>
  <li>有研究缺口启发的论文同时放入 13_Possible_Research_Gaps。</li>
</ul>
<h2>建议标签体系</h2>
{html_list(ZOTERO_TAGS)}
""".strip()


def create_note(zot: zotero.Zotero, collection_key: str, note_html: str, tags: Optional[List[str]] = None) -> dict:
    template = zot.item_template("note")
    template["note"] = note_html
    template["collections"] = [collection_key]
    template["tags"] = [{"tag": tag} for tag in (tags or [])]
    return zot.create_items([template])


def print_result(action: str, name: str, key: str = "") -> None:
    suffix = f" ({key})" if key else ""
    print(f"{action}: {name}{suffix}")


def main() -> int:
    load_dotenv()

    api_key = require_env("ZOTERO_API_KEY")
    user_id = require_env("ZOTERO_USER_ID")
    library_type = os.getenv("ZOTERO_LIBRARY_TYPE", "user")

    if library_type != "user":
        print("This script currently expects ZOTERO_USER_ID with ZOTERO_LIBRARY_TYPE=user.", file=sys.stderr)
        print("For a group library, adapt the library id to the groupID and set library_type='group'.", file=sys.stderr)
        return 2

    zot = zotero.Zotero(user_id, library_type, api_key)

    collections = load_all_collections(zot)
    index = build_collection_index(collections)

    root = index.get((ROOT_COLLECTION, None))
    if root:
        root_key = root["key"]
        print_result("SKIP collection", ROOT_COLLECTION, root_key)
    else:
        root = create_collection(zot, ROOT_COLLECTION)
        root_key = root["key"]
        print_result("CREATE collection", ROOT_COLLECTION, root_key)
        collections = load_all_collections(zot)
        index = build_collection_index(collections)

    root_note_title = f"README - {ROOT_COLLECTION}"
    if note_exists(zot, root_key, root_note_title):
        print_result("SKIP note", root_note_title)
    else:
        response = create_note(zot, root_key, root_note_html(), tags=["sci-potential"])
        print_result("CREATE note", root_note_title, str(response))

    for name in SUBCOLLECTIONS:
        collection = index.get((name, root_key))
        if collection:
            collection_key = collection["key"]
            print_result("SKIP collection", name, collection_key)
        else:
            collection = create_collection(zot, name, root_key)
            collection_key = collection["key"]
            print_result("CREATE collection", name, collection_key)
            collections = load_all_collections(zot)
            index = build_collection_index(collections)

        note_title = f"README - {name}"
        if note_exists(zot, collection_key, note_title):
            print_result("SKIP note", note_title)
        else:
            response = create_note(zot, collection_key, collection_note_html(name))
            print_result("CREATE note", note_title, str(response))

    print("\nSuggested Zotero tags:")
    for tag in ZOTERO_TAGS:
        print(f"- {tag}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
