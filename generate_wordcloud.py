import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import os

def generate_wordcloud(text, output_path, mask_path=None, width=1200, height=800):
    """
    生成词云图片
    
    参数:
        text (str): 处理好的文本，词语用空格分隔
        output_path (str): 输出图片路径
        mask_path (str, optional): 词云形状图片路径
        width (int): 图片宽度
        height (int): 图片高度
    """
    # 设置中文字体，需要根据系统安装的字体来设置
    font_path = '/System/Library/Fonts/PingFang.ttc'  # MacOS系统字体
    
    # 词云参数设置
    params = {
        'font_path': font_path,
        'width': width,
        'height': height,
        'background_color': 'white',
        'max_words': 2000,
        'min_font_size': 10,
        'max_font_size': 100,
        'random_state': 42,  # 固定随机状态，使结果可复现
        'collocations': False  # 避免词语重复
    }
    
    # 如果提供了mask图片，则使用mask
    if mask_path and os.path.exists(mask_path):
        mask = np.array(Image.open(mask_path))
        params['mask'] = mask
    
    # 生成词云
    wordcloud = WordCloud(**params)
    wordcloud.generate(text)
    
    # 保存图片
    plt.figure(figsize=(width/100, height/100), dpi=100)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(output_path, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close()
    
    print(f"词云图片已保存到: {output_path}")

def main():
    # 读取处理好的数据
    print("正在读取处理好的数据...")
    df = pd.read_csv('data/processed_news.csv')
    
    # 合并所有文本
    print("正在合并文本...")
    all_text = ' '.join(df['processed_text'].dropna())
    
    # 创建输出目录
    os.makedirs('output', exist_ok=True)
    
    # 生成基础词云
    print("正在生成基础词云...")
    generate_wordcloud(
        all_text,
        'output/news_wordcloud.png',
        width=1600,
        height=1200
    )
    
    # 生成圆形词云（如果有mask图片）
    mask_path = 'data/mask.png'  # 可以准备一个圆形或其他形状的mask图片
    if os.path.exists(mask_path):
        print("正在生成圆形词云...")
        generate_wordcloud(
            all_text,
            'output/news_wordcloud_circle.png',
            mask_path=mask_path,
            width=1600,
            height=1200
        )

if __name__ == '__main__':
    main() 