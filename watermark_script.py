import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

# 视频文件夹路径
video_folder_path = "C:\\Users\\YouUsername\\Desktop\\video"
# 水印图片路径
logo_path = "C:\\Users\\YouUsername\\Desktop\\logo.png"
# 输出文件夹路径
output_folder_path = 'C:\\Users\\YouUsername\\Desktop\\watermarked_videos'

# 如果输出文件夹不存在，创建它
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# 加载水印图片
logo = ImageClip(logo_path).set_duration(None).set_opacity(0.5)
# 设置水印在屏幕上的位置
logo = logo.set_position(('right', 'bottom'))

# 遍历视频文件夹中的所有视频文件
for filename in os.listdir(video_folder_path):
    if filename.endswith('.mp4'):  # 确保文件是MP4格式
        # 完整视频路径
        video_path = os.path.join(video_folder_path, filename)
        # 输出视频的路径
        output_path = os.path.join(output_folder_path, filename)

        # 加载视频文件
        clip = VideoFileClip(video_path)

        # 设置水印的持续时间与视频一致
        logo = logo.set_duration(clip.duration)

        # 将水印添加到视频上
        watermarked_clip = CompositeVideoClip([clip, logo])

        # 输出最终的视频
        watermarked_clip.write_videofile(output_path, codec='libx264', fps=24)

print("水印添加完成！")