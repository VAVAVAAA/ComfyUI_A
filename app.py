import os
import shutil
import openxlab
from openxlab.dataset import download
import subprocess
import zipfile
import requests

# 环境
os.system("pip install --upgrade transformers==4.44.2")
os.system("pip install --upgrade torch==2.4.1")
os.system("pip install --upgrade torchvision")
os.system("pip install --upgrade packaging")
os.system("pip install diffusers==0.30.3")

os.system("pip install openxlab")
os.system("pip install -U openxlab")
openxlab.login(ak='xa5ag8yyvwpqkxw839pw', sk='l8njwnadbjgdwxe1zn83olme31xpparlo2q7vkmo')

# 依赖
os.system("pip install aiohttp_sse")
os.system("pip install segment_anything")
os.system("pip install opencv-python")
os.system("pip install transparent_background")
os.system("pip install rembg")
os.system("pip install piexif")
os.system("pip install accelerate>=0.25.0")
os.system("pip install blend_modes")
os.system("pip install diffusers")
os.system("pip install insightface")
os.system("pip install deepdiff")
os.system("pip install ultralytics") # Impact-Pack的依赖
os.system("pip install py-cpuinfo")
os.system("pip install pynvml")
os.system("pip install iopath")
os.system("pip install webcolors")
os.system("pip install loguru")
os.system(f"git lfs install")

# os.chdir(f"/home/xlab-app-center")
# 插件
base_url = "https://github.com"
os.system(f"git clone {base_url}/ltdrdata/ComfyUI-Manager /home/xlab-app-center/custom_nodes/ComfyUI-Manager")
os.system(f"git clone {base_url}/ty0x2333/ComfyUI-Dev-Utils /home/xlab-app-center/custom_nodes/ComfyUI-Dev-Utils") # 显示节点运行时间
# os.system(f"git clone https://git.homegu.com/Nuked88/ComfyUI-N-Sidebar /home/xlab-app-center/custom_nodes/ComfyUI-N-Sidebar")
os.system(f"git clone {base_url}/AIGODLIKE/AIGODLIKE-ComfyUI-Translation /home/xlab-app-center/custom_nodes/AIGODLIKE-ComfyUI-Translation")
os.system(f"git clone {base_url}/rgthree/rgthree-comfy /home/xlab-app-center/custom_nodes/rgthree-comfy")

os.system(f"git clone {base_url}/MinusZoneAI/ComfyUI-Kolors-MZ /home/xlab-app-center/custom_nodes/ComfyUI-Kolors-MZ") # 可图
os.system(f"git clone {base_url}/SeaArtLab/comfyui_storydiffusion /home/xlab-app-center/custom_nodes/comfyui_storydiffusion") # 可图
#os.system(f"git clone https://git.homegu.com/yolain/ComfyUI-Easy-Use /home/xlab-app-center/custom_nodes/ComfyUI-Easy-Use")
os.system(f"git clone {base_url}/VAVAVAAA/ComfyUI-Easy-Use-A /home/xlab-app-center/custom_nodes/ComfyUI-Easy-Use-A") # 自己fork仓库的
#os.system(f"git clone https://git.homegu.com/xinsir6/ControlNetPlus /home/xlab-app-center/custom_nodes/ControlNetPlus") # 全能xl调用
os.system(f"git clone {base_url}/kijai/ComfyUI-segment-anything-2 /home/xlab-app-center/custom_nodes/ComfyUI-segment-anything-2") # 第二代抠图
os.system(f"git clone {base_url}/kijai/ComfyUI-KJNodes /home/xlab-app-center/custom_nodes/ComfyUI-KJNodes")

os.system(f"git clone {base_url}/john-mnz/ComfyUI-Inspyrenet-Rembg /home/xlab-app-center/custom_nodes/ComfyUI-Inspyrenet-Rembg") # 抠背景
os.system(f"git clone {base_url}/Fannovel16/comfyui_controlnet_aux /home/xlab-app-center/custom_nodes/comfyui_controlnet_aux")
os.system(f"git clone {base_url}/ltdrdata/ComfyUI-Impact-Pack /home/xlab-app-center/custom_nodes/ComfyUI-Impact-Pack impact_subpack")
# os.system(f"git clone https://git.homegu.com/ltdrdata/ComfyUI-Impact-Subpack /home/xlab-app-center/custom_nodes/ComfyUI-Impact-Subpack")
os.system(f"git clone {base_url}/ltdrdata/ComfyUI-Inspire-Pack /home/xlab-app-center/custom_nodes/ComfyUI-Inspire-Pack")

os.system(f"git clone {base_url}/cubiq/ComfyUI_IPAdapter_plus /home/xlab-app-center/custom_nodes/ComfyUI_IPAdapter_plus")
os.system(f"git clone {base_url}/Kosinkadink/ComfyUI-VideoHelperSuite /home/xlab-app-center/custom_nodes/ComfyUI-VideoHelperSuite")
os.system(f"git clone {base_url}/EvilBT/ComfyUI_SLK_joy_caption_two  /home/xlab-app-center/custom_nodes/ComfyUI_SLK_joy_caption_two ") # joy_caption2代
# os.system(f"git clone https://git.homegu.com/miaoshouai/ComfyUI-Miaoshouai-Tagger /home/xlab-app-center/custom_nodes/ComfyUI-Miaoshouai-Tagger") # 全新的视觉反推模型，显存更小
os.system(f"git clone {base_url}/siliconflow/BizyAir /home/xlab-app-center/custom_nodes/BizyAir") # 满血版反推

os.system(f"git clone {base_url}/pythongosssss/ComfyUI-Custom-Scripts /home/xlab-app-center/custom_nodes/ComfyUI-Custom-Scripts")
os.system(f"git clone {base_url}/melMass/comfy_mtb /home/xlab-app-center/custom_nodes/comfy_mtb")
os.system(f"git clone {base_url}/chflame163/ComfyUI_LayerStyle /home/xlab-app-center/custom_nodes/ComfyUI_LayerStyle")
os.system(f"git clone {base_url}/cubiq/ComfyUI_essentials /home/xlab-app-center/custom_nodes/ComfyUI_essentials")
os.system(f"git clone {base_url}/chrisgoringe/cg-use-everywhere /home/xlab-app-center/custom_nodes/cg-use-everywhere")
os.system(f"git clone {base_url}/chrisgoringe/cg-image-picker /home/xlab-app-center/custom_nodes/cg-image-picker")
os.system(f"git clone {base_url}/ssitu/ComfyUI_UltimateSDUpscale /home/xlab-app-center/custom_nodes/ComfyUI_UltimateSDUpscale --recursive")

os.system(f"git clone {base_url}/M1kep/ComfyLiterals /home/xlab-app-center/custom_nodes/ComfyLiterals") # 字符串节点
os.system(f"git clone {base_url}/lquesada/ComfyUI-Inpaint-CropAndStitch /home/xlab-app-center/custom_nodes/ComfyUI-Inpaint-CropAndStitch") # 重绘
os.system(f"git clone {base_url}/erosDiffusion/ComfyUI-enricos-nodes /home/xlab-app-center/custom_nodes/ComfyUI-enricos-nodes") # 自定义构图
os.system(f"git clone {base_url}/WASasquatch/was-node-suite-comfyui /home/xlab-app-center/custom_nodes/was-node-suite-comfyui") 
os.system(f"git clone {base_url}/Fannovel16/ComfyUI-Frame-Interpolation /home/xlab-app-center/custom_nodes/ComfyUI-Frame-Interpolation") # 视频补帧
os.system(f"git clone {base_url}/MinusZoneAI/ComfyUI-CogVideoX-MZ /home/xlab-app-center/custom_nodes/ComfyUI-CogVideoX-MZ") # 图生视频
os.system(f"git clone {base_url}/kijai/ComfyUI-CogVideoXWrapper /home/xlab-app-center/custom_nodes/ComfyUI-CogVideoXWrapper") # 图生视频，与上面搭配使用
os.system(f"git clone {base_url}/TTPlanetPig/Comfyui_TTP_Toolset /home/xlab-app-center/custom_nodes/Comfyui_TTP_Toolset") # flux放大
os.system(f"git clone {base_url}/kijai/ComfyUI-Florence2 /home/xlab-app-center/custom_nodes/ComfyUI-Florence2")
os.system(f"git clone {base_url}/shiimizu/ComfyUI-PhotoMaker-Plus /home/xlab-app-center/custom_nodes/ComfyUI-PhotoMaker-Plus") # 换脸
os.system(f"git clone {base_url}/cubiq/ComfyUI_InstantID /home/xlab-app-center/custom_nodes/ComfyUI_InstantID") # 换脸
os.system(f"git clone {base_url}/crystian/ComfyUI-Crystools /home/xlab-app-center/custom_nodes/ComfyUI-Crystools") # 性能检测
os.system(f"git clone {base_url}/tatookan/comfuinoda-Navyblue /home/xlab-app-center/custom_nodes/comfuinoda-Navyblue") # sigme分离加细节
os.system(f"git clone {base_url}/kijai/ComfyUI-FluxTrainer /home/xlab-app-center/custom_nodes/ComfyUI-FluxTrainer") # lora训练
os.system(f"git clone {base_url}/logtd/ComfyUI-Fluxtapoz /home/xlab-app-center/custom_nodes/ComfyUI-Fluxtapoz") #类风格迁移
os.system(f"git clone {base_url}/mutek/Cryptocat /home/xlab-app-center/custom_nodes/Cryptocat") #工作流加密
os.system(f"git clone {base_url}/stormcenter/ComfyUI-AutoSplitGridImage /home/xlab-app-center/custom_nodes/ComfyUI-AutoSplitGridImage") #一张图的切割，与下面的插件搭配
os.system(f"git clone {base_url}/kinfolk0117/ComfyUI_GridSwapper /home/xlab-app-center/custom_nodes/ComfyUI_GridSwapper") #网格技术生成的面部一致性保持
os.system(f"git clone {base_url}/leadbreak/comfyui-faceaging /home/xlab-app-center/custom_nodes/comfyui-faceaging") #年龄变化-50到100岁
os.system(f"git clone {base_url}/chflame163/ComfyUI_LayerStyle_Advance /home/xlab-app-center/custom_nodes/ComfyUI_LayerStyle_Advance")




# ai去水印，lama
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/ComfyUI/models/lama/{file_name}') 
 for file_name in [
     'big-lama.pt'
 ]]


# 大模型
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/models/checkpoints/{file_name}') 
 for file_name in [
     'MYHuman-墨幽人造人15.safetensors'
 ]]

# unet模型
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/models/unet/{file_name}') 
#  for file_name in [
#      'ketu_fp16.safetensors'
     
#  ]]
# lora
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/models/loras/{file_name}') 
 for file_name in [
     # 'Hyper-FLUX.1-dev-8steps-lora.safetensors', 
     # 'xl_99art写实摄影·光影光斑光晕增强.safetensors',
     # '绘梦摄影Flux复古胶片摄影时尚写真电影质感.safetensors',
     # '墨幽-F.1-Lora-网图-MYH-1.1.safetensors',
     # '墨幽Flux-Lora-网图.safetensors',
     # 'flux_realism_lora-写实主义.safetensors',
     # 'Flux_小红书真实风格.safetensors',
     # '万物调FluxTexture质感增强器06.safetensors',
     # 'ASKOLORS可图绘风.safetensors',
     # 'ASKOLORS绘本插画风格.safetensors',
     # 'kolors国风描金插画.safetensors',
     # 'Zenpainting禅意插画08.safetensors',
     # 'UIA插画古风山水艺术06.safetensors',
     # 'FLUX-Turbo-Alpha.safetensors',
     # '美学艺术Aestheticsart.safetensors',
     # 'aidmaFLUXpro1.1-FLUX-V0.2.safetensors'
 ]]
# vae
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/models/vae/{file_name}') 
 for file_name in [
     'ketu_vae_fp16.safetensors', 
     'flux_vae.safetensors',
 ]]
# clip模型
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/models/clip/{file_name}') 
#  for file_name in [
#      'ViT-L-14-TEXT-detail-improved-hiT-GmP-TE-only-HF.safetensors', 
#      'clip_l.safetensors',
#      't5xxl_fp8_e4m3fn.safetensors'
#  ]]

# 放大模型
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/models/upscale_models/{file_name}') 
#  for file_name in [
#      '4xNomos8kSCHAT-L.pth', 
#      'RealESRGAN_x4plus.pth',
#      '4x_NMKD-Siax_200k.pth'
#  ]]

# SAM检测加载器
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/models/sams/{file_name}') 
 for file_name in [
     'sam_vit_b_01ec64.pth'
 ]]

# SAM2检测加载器
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/models/sam2/{file_name}') 
 for file_name in [
     'sam2_hiera_base_plus.safetensors'
 ]]

# bbox检测面部模型
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/models/ultralytics/bbox/{file_name}') 
 for file_name in [
     'face_yolov8m.pt'
 ]]
# controlnet
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/models/controlnet/{file_name}') 
#  for file_name in [
#      'InstantID-controlnet.safetensors'
#  ]]


# 数据集2- lora
# [download(dataset_repo='mofashi/comfy2', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/models/loras/{file_name}') 
#  for file_name in [
#      'Flux-小红书真实写真.safetensors',
#      '山水诗行_flux版',
#      '极氪白白酱Flux-人像V6MAX'
#  ]]

# id换脸模型
# [download(dataset_repo='mofashi/comfy', 
#           source_path=file_name, 
#           target_path=f'/home/xlab-app-center/models/instantid/{file_name}') 
#  for file_name in [
#      'ip-adapter.bin'
#  ]]


# # 设置目标目录
# target_dir = '/home/xlab-app-center/custom_nodes/ComfyUI-Impact-Pack/'
# source_file_path = os.path.join(target_dir, 'mofashi___comfy', 'impact_subpack.zip')
# target_file_path = os.path.join(target_dir, 'impact_subpack.zip')

# # 下载数据集
# download(dataset_repo='mofashi/comfy', source_path='impact_subpack.zip', target_path=target_dir)

# # 确认下载结果并移动文件
# if os.path.exists(source_file_path):
#     shutil.move(source_file_path, target_file_path)
#     print(f"文件已成功移动到: {target_file_path}")
# else:
#     print("下载的文件不存在，请检查下载过程。")
     
# # os.chdir(f"/home/xlab-app-center/custom_nodes/ComfyUI-Impact-Pack")
# # directory = '/home/xlab-app-center/custom_nodes/ComfyUI-Impact-Pack'

# # # 尝试获取目录中的所有文件和文件夹
# # try:
# #     files_and_dirs = os.listdir(directory)
# #     # 打印所有文件和文件夹
# #     for item in files_and_dirs:
# #         print(item)
# # except FileNotFoundError:
# #     print(f"目录 '{directory}' 不存在。请检查路径是否正确。")

# # 查找压缩包并解压
# os.chdir(f"/home/xlab-app-center/custom_nodes/ComfyUI-Impact-Pack")
# zip_file_path = "impact_subpack.zip"
# if os.path.exists(zip_file_path):
#     subprocess.run(f"unzip {zip_file_path}", shell=True)
#     print("文件解压完成")

#     # 删除压缩包
#     os.remove(zip_file_path)
#     print(f"已删除压缩包 {zip_file_path}")
# else:
#     print(f"{zip_file_path} 不存在或者解压失败")

#---------------------------------------------------------------------------
# # 设置目标目录
# target_dir = '/home/xlab-app-center/models/Joy_caption_two/'
# source_file_path = os.path.join(target_dir, 'mofashi___comfy', 'text_model.zip')
# target_file_path = os.path.join(target_dir, 'text_model.zip')

# # 下载数据集
# download(dataset_repo='mofashi/comfy', source_path='text_model.zip', target_path=target_dir)

# # 确认下载结果并移动文件
# if os.path.exists(source_file_path):
#     shutil.move(source_file_path, target_file_path)
#     print(f"文件已成功移动到: {target_file_path}")
# else:
#     print("下载的文件不存在，请检查下载过程。")
     
# # 查找压缩包并解压
# os.chdir(f"/home/xlab-app-center/models/Joy_caption_two")
# zip_file_path = "text_model.zip"
# if os.path.exists(zip_file_path):
#     subprocess.run(f"unzip {zip_file_path}", shell=True)
#     print("文件解压完成")

#     # 删除压缩包
#     os.remove(zip_file_path)
#     print(f"已删除压缩包 {zip_file_path}")
# else:
#     print(f"{zip_file_path} 不存在或者解压失败")

# # 定义文件路径
# old_file = "/home/xlab-app-center/models/Joy_caption_two/cgrkzexw-599808_config.yaml"
# new_file = "/home/xlab-app-center/models/Joy_caption_two/config.yaml"

# # 检查文件是否存在并重命名
# if os.path.exists(old_file):
#     os.rename(old_file, new_file)
#     print(f"文件已重命名为: {new_file}")
# else:
#     print(f"文件未找到: {old_file}")

#------------------------------------------------------------
# # 设置目标目录
# target_dir = '/home/xlab-app-center/models/clip'
# source_file_path = os.path.join(target_dir, 'mofashi___comfy', 'siglip-so400m-patch14-384.zip')
# target_file_path = os.path.join(target_dir, 'siglip-so400m-patch14-384.zip')

# # 下载数据集
# download(dataset_repo='mofashi/comfy', source_path='siglip-so400m-patch14-384.zip', target_path=target_dir)

# # 确认下载结果并移动文件
# if os.path.exists(source_file_path):
#     shutil.move(source_file_path, target_file_path)
#     print(f"文件已成功移动到: {target_file_path}")
# else:
#     print("下载的文件不存在，请检查下载过程。")
     
# # 查找压缩包并解压
# os.chdir(f"/home/xlab-app-center/models/clip/")
# zip_file_path = "siglip-so400m-patch14-384.zip"
# if os.path.exists(zip_file_path):
#     subprocess.run(f"unzip {zip_file_path}", shell=True)
#     print("文件解压完成")

#     # 删除压缩包
#     os.remove(zip_file_path)
#     print(f"已删除压缩包 {zip_file_path}")
# else:
#     print(f"{zip_file_path} 不存在或者解压失败")
          
# os.chdir(f"/home/xlab-app-center/models/clip")
# directory = '/home/xlab-app-center/models/clip'

# # 尝试获取目录中的所有文件和文件夹
# try:
#     files_and_dirs = os.listdir(directory)
#     # 打印所有文件和文件夹
#     for item in files_and_dirs:
#         print(item)
# except FileNotFoundError:
#     print(f"目录 '{directory}' 不存在。请检查路径是否正确。")

# 大模型
os.chdir(f"/home/xlab-app-center/models/checkpoints") #模型仓库，大模型文件夹
#subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/MYHuman-%E5%A2%A8%E5%B9%BD%E4%BA%BA%E9%80%A0%E4%BA%BAXL_v2010-Flux-RF.safetensors?ref=main&nonce=1726399393393 -o MYHuman-墨幽人造人XL-v2010-Flux-RF.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('MYHuman-墨幽人造人XL-v2010-Flux-RF下载完成')
#subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://www.modelscope.cn/models/AI-ModelScope/stable-diffusion-3.5-large/resolve/master/sd3.5_large.safetensors -o sd3.5_large.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('sd3.5_large下载完成')


#os.chdir(f"/home/xlab-app-center/models/unet") # 模型仓库，unet文件夹
#subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/flux1-dev-fp8原始.safetensors?ref=main&nonce=1725931610381 -o flux1-dev-fp8原始.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('flux1-dev-fp8原始下载完成')
#subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/MYHuman-F.1-%E5%8E%9F%E5%A2%A8%E5%B9%BD%E9%9A%8F%E6%8B%8D-v1-%E9%9A%8F%E6%8B%8D.safetensors?ref=main&nonce=1726204698330 -o MYHuman-F.1-原墨幽随拍-v1-随拍.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('原墨幽随拍-v1-随拍下载完成')
#subprocess.run('aria2c -c -x 16 -s 16 -k 1M --async-dns=false --check-certificate=false "https://download.openxlab.org.cn/repos/file/mofashi/comfy2/main?filepath=pixelwave_flux1Dev03.safetensors&sign=f145bbad6a3f5271bacd8dd7c3fb219f&nonce=1730166831451" -o pixelwave_flux1Dev03.safetensors', shell=True);print('pixelwave_flux1Dev03风格模型下载完成')

#os.chdir(f"/home/xlab-app-center/models/clip") # clip
#subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://www.modelscope.cn/models/Comfy-Org/stable-diffusion-3.5-fp8/resolve/master/text_encoders/clip_g.safetensors -o clip_g.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('clip_g下载完成')


#os.chdir(f"/home/xlab-app-center/models/loras") #模型仓库，lora文件夹
#subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/%E7%AD%91%E6%A2%A6F.1_INS%E6%BB%A4%E9%95%9C_v1.0.safetensors?ref=main&nonce=1726186206302 -o 筑梦F.1_INS滤镜_v1.0.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('筑梦F.1_INS滤镜下载完成')

#os.makedirs("/home/xlab-app-center/models/LLM", exist_ok=True) # 目录不存在则自动创建
#os.chdir(f"/home/xlab-app-center/models/LLM") # 模型仓库，LLM文件夹
# subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/Florence-2-large-PromptGen-v1.5.safetensors?ref=main&nonce=1727138430530 -o Florence-2-large-PromptGen-v1.5.safetensors",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);print('Florence-2-large-PromptGen-v1.5下载完成')

#-------------------------------------------------------------
os.chdir(f"/home/xlab-app-center")# 启动文件（勿动！）
#os.system(f"python main.py --listen 0.0.0.0 --port 7860 --enable-cors-header")
#os.system(f"python main.py --cpu --listen 0.0.0.0 --port 7860 --enable-cors-header")

def has_gpu():
    try:
        # 尝试运行 nvidia-smi 命令，检查是否有显卡
        result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0  # 如果返回码为0，表示有显卡
    except FileNotFoundError:
        return False  # 如果找不到命令，则表示没有显卡

if has_gpu():
    command = "python main.py --listen 0.0.0.0 --port 7860 --enable-cors-header"
else:
    command = "python main.py --cpu --listen 0.0.0.0 --port 7860 --enable-cors-header"

os.system(command)


