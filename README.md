# News Word Cloud

一个用于生成中文新闻词云的工具，支持文本预处理、分词、停用词过滤，为生成词云提供高质量的数据支持。

## 功能特点

- 使用jieba进行中文分词
- 自动过滤停用词
- 清理文本（去除URL、HTML标签、标点符号等）
- 支持大规模文本处理
- 保留原始数据，新增处理后的文本列
- 为词云生成提供标准化的文本数据

## 项目结构

```
.
├── README.md
├── requirements.txt
├── process_news.py
└── data/
    ├── entertainment_news.csv    # 原始新闻数据
    ├── stopwords.txt            # 停用词列表
    └── processed_news.csv       # 处理后的数据
```

## 环境要求

- Python 3.6+
- pandas >= 1.5.0
- jieba >= 0.42.1

## 安装

1. 克隆项目到本地
2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 准备数据：
   - 将新闻数据保存为CSV格式，放在 `data` 目录下
   - 确保CSV文件中包含文本列（默认为'content'列）
   - 停用词列表已包含在 `data/stopwords.txt` 中

2. 运行处理脚本：
```bash
python process_news.py
```

3. 处理结果：
   - 处理后的数据将保存在 `data/processed_news.csv` 中
   - 原始数据保持不变，新增 `processed_text` 列存储处理后的文本
   - 处理后的文本中词语之间用空格分隔

## 处理流程

1. 文本清理：
   - 去除URL
   - 去除HTML标签
   - 去除标点符号和特殊字符

2. 分词处理：
   - 使用jieba进行中文分词
   - 自动加载jieba词典

3. 停用词过滤：
   - 使用预定义的停用词列表
   - 过滤掉停用词和空字符

## 注意事项

- 确保输入CSV文件的编码为UTF-8
- 如果新闻文本的列名不是'content'，需要修改 `process_news.py` 中的 `text_column` 变量
- 处理大文件时可能需要较长时间，请耐心等待
- 可以根据需要修改 `stopwords.txt` 来自定义停用词列表

## 输出示例

原始文本：
```
新华社北京3月15日电（记者张三）今天，某公司发布了新产品。
```

处理后的文本：
```
新华社 北京 电 记者 张三 今天 公司 发布 新产品
```

## 许可证

MIT License 