# 视频水印工具 Video Watermarking Tool

该项目提供了一个Python脚本，用于批量向视频中添加图片水印。它旨在处理指定目录中的多个视频，为每个视频应用水印图片。水印的位置和透明度可以自定义。

### 系统要求

- Python 3.x
- moviepy 库

### 安装

1. 确保系统已安装 Python 3.x。
2. 使用pip安装`moviepy`库：

```bash
pip install moviepy
```

3. 克隆此仓库或下载脚本到您的本地机器。

### 使用方法

1. 将视频放置在指定的`video`目录下。
2. 将水印图片（例如，`logo.png`）放置在已知位置。
3. 运行脚本：

```bash
python watermark_script.py
```

4. 处理后的视频将保存在指定的输出目录中。


This project provides a Python script for batch adding image watermarks to videos. It's designed to process multiple videos located in a specified directory, applying a watermark image to each. The watermark position and opacity can be customized.

### Prerequisites

- Python 3.x
- moviepy library

### Installation

1. Ensure Python 3.x is installed on your system.
2. Install the `moviepy` library using pip:

```bash
pip install moviepy
```

3. Clone this repository or download the script to your local machine.

### Usage

1. Place your videos in the specified `video` directory.
2. Place your watermark image (e.g., `logo.png`) in the known location.
3. Run the script:

```bash
python watermark_script.py
```

4. Processed videos will be saved in the specified output directory.

