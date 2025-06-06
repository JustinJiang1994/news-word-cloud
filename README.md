# News Word Cloud

一个用于生成中文新闻词云的工具，支持文本预处理、分词、停用词过滤，为生成词云提供高质量的数据支持。

## 功能特点

- 使用jieba进行中文分词
- 自动过滤停用词
- 清理文本（去除URL、HTML标签、标点符号等）
- 支持大规模文本处理
- 保留原始数据，新增处理后的文本列
- 为词云生成提供标准化的文本数据
- 支持自定义词云形状和样式
- 生成高质量词云图片

## 项目结构

```
.
├── README.md
├── requirements.txt
├── process_news.py          # 文本处理脚本
├── generate_wordcloud.py    # 词云生成脚本
├── data/
│   ├── entertainment_news.csv    # 原始新闻数据
│   ├── stopwords.txt            # 停用词列表
│   └── mask.png                 # 词云形状图片（可选）
└── output/
    └── news_wordcloud.png       # 生成的词云图片
```

## 环境要求

- Python 3.6+
- pandas >= 1.5.0
- jieba >= 0.42.1
- wordcloud >= 1.9.2
- matplotlib >= 3.7.0
- numpy >= 1.24.0
- Pillow >= 10.0.0

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
   - 可选：准备词云形状图片（mask.png）放在 `data` 目录下

2. 处理文本：
```bash
python process_news.py
```

3. 生成词云：
```bash
python generate_wordcloud.py
```

4. 查看结果：
   - 处理后的数据保存在 `data/processed_news.csv` 中
   - 词云图片保存在 `output/news_wordcloud.png` 中
   - 如果提供了mask图片，还会生成形状词云 `output/news_wordcloud_circle.png`

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

4. 词云生成：
   - 支持自定义词云形状
   - 可调整词云大小、颜色、字体等参数
   - 生成高质量图片

## 词云示例

![新闻词云示例](output/news_wordcloud.png)

### 词云分析结果

通过对娱乐新闻数据的分析，生成的词云展示了以下特点：

1. 高频词汇：
   - 明星名字（如：周杰伦、王力宏等）
   - 娱乐活动（如：演唱会、电影、综艺等）
   - 热门话题（如：热搜、话题、关注等）

2. 词云特点：
   - 字体大小：根据词频自动调整，突出重要内容
   - 颜色分布：采用渐变色系，视觉效果丰富
   - 布局方式：采用随机布局，避免词语重复
   - 图片质量：高分辨率（300dpi）输出，适合各种场景使用

3. 数据规模：
   - 处理文本：约12MB原始新闻数据
   - 词云词汇：最多显示2000个高频词
   - 字体大小：10-100像素动态调整

4. 应用场景：
   - 新闻热点分析
   - 娱乐话题追踪
   - 社交媒体内容分析
   - 舆情监测

## 注意事项

- 确保输入CSV文件的编码为UTF-8
- 如果新闻文本的列名不是'content'，需要修改 `process_news.py` 中的 `text_column` 变量
- 处理大文件时可能需要较长时间，请耐心等待
- 可以根据需要修改 `stopwords.txt` 来自定义停用词列表
- 词云生成时使用的字体需要根据系统环境调整

## 许可证

MIT License 