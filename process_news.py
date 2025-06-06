import pandas as pd
import jieba
import re

def load_stopwords(file_path):
    """加载停用词列表"""
    with open(file_path, 'r', encoding='utf-8') as f:
        stopwords = set([line.strip() for line in f])
    return stopwords

def clean_text(text):
    """清理文本，去除特殊字符"""
    if not isinstance(text, str):
        return ""
    # 去除URL
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    # 去除HTML标签
    text = re.sub(r'<[^>]+>', '', text)
    # 去除标点符号和特殊字符
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def process_text(text, stopwords):
    """处理文本：清理、分词、去停用词"""
    # 清理文本
    text = clean_text(text)
    # 分词
    words = jieba.cut(text)
    # 去停用词
    words = [word for word in words if word not in stopwords and len(word.strip()) > 0]
    return ' '.join(words)

def main():
    # 加载停用词
    stopwords = load_stopwords('data/stopwords.txt')
    
    # 读取新闻数据
    print("正在读取新闻数据...")
    df = pd.read_csv('data/entertainment_news.csv')
    
    # 假设文本列名为'content'，如果不是请修改
    text_column = 'content'
    if text_column not in df.columns:
        print(f"错误：找不到列 '{text_column}'")
        print("可用的列名：", df.columns.tolist())
        return
    
    # 处理文本
    print("正在处理文本...")
    df['processed_text'] = df[text_column].apply(lambda x: process_text(x, stopwords))
    
    # 保存结果
    output_file = 'data/processed_news.csv'
    print(f"正在保存处理后的数据到 {output_file}...")
    df.to_csv(output_file, index=False, encoding='utf-8')
    print("处理完成！")

if __name__ == '__main__':
    main() 