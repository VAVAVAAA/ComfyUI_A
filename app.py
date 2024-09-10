import os
import shutil
import openxlab
from openxlab.dataset import download
import subprocess
# 环境
os.system("pip install --upgrade transformers==4.44.2")
# os.system("pip install --upgrade torch==2.1.2")
os.system("pip install torchvision")
os.system("pip install packaging==23.0")


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


# os.chdir(f"/home/xlab-app-center")
# 插件
os.system(f"git clone https://git.homegu.com/ltdrdata/ComfyUI-Manager /home/xlab-app-center/custom_nodes/ComfyUI-Manager")
os.system(f"git clone https://git.homegu.com/ty0x2333/ComfyUI-Dev-Utils /home/xlab-app-center/custom_nodes/ComfyUI-Dev-Utils") # 显示节点运行时间
os.system(f"git clone https://git.homegu.com/Nuked88/ComfyUI-N-Sidebar /home/xlab-app-center/custom_nodes/ComfyUI-N-Sidebar")
os.system(f"git clone https://git.homegu.com/AIGODLIKE/AIGODLIKE-ComfyUI-Translation /home/xlab-app-center/custom_nodes/AIGODLIKE-ComfyUI-Translation")
os.system(f"git clone https://git.homegu.com/rgthree/rgthree-comfy /home/xlab-app-center/custom_nodes/rgthree-comfy")

os.system(f"git clone https://git.homegu.com/MinusZoneAI/ComfyUI-Kolors-MZ /home/xlab-app-center/custom_nodes/ComfyUI-Kolors-MZ") # 可图
os.system(f"git clone https://git.homegu.com/SeaArtLab/comfyui_storydiffusion /home/xlab-app-center/custom_nodes/comfyui_storydiffusion") # 可图
os.system(f"git clone https://git.homegu.com/yolain/ComfyUI-Easy-Use /home/xlab-app-center/custom_nodes/ComfyUI-Easy-Use")
# os.system(f"git clone https://git.homegu.com/xinsir6/ControlNetPlus /home/xlab-app-center/custom_nodes/ControlNetPlus") # 全能xl调用
os.system(f"git clone https://git.homegu.com/kijai/ComfyUI-segment-anything-2 /home/xlab-app-center/custom_nodes/ComfyUI-segment-anything-2") # 第二代抠图
os.system(f"git clone https://git.homegu.com/kijai/ComfyUI-KJNodes /home/xlab-app-center/custom_nodes/ComfyUI-KJNodes")

os.system(f"git clone https://git.homegu.com/john-mnz/ComfyUI-Inspyrenet-Rembg /home/xlab-app-center/custom_nodes/ComfyUI-Inspyrenet-Rembg") # 抠背景
os.system(f"git clone https://git.homegu.com/Fannovel16/comfyui_controlnet_aux /home/xlab-app-center/custom_nodes/comfyui_controlnet_aux")
os.system(f"git clone https://git.homegu.com/ltdrdata/ComfyUI-Impact-Pack /home/xlab-app-center/custom_nodes/ComfyUI-Impact-Pack")
os.system(f"git clone https://git.homegu.com/ltdrdata/ComfyUI-Inspire-Pack /home/xlab-app-center/custom_nodes/ComfyUI-Inspire-Pack")
os.system(f"git clone https://git.homegu.com/ssitu/ComfyUI_UltimateSDUpscale /home/xlab-app-center/custom_nodes/ComfyUI_UltimateSDUpscale")

os.system(f"git clone https://git.homegu.com/cubiq/ComfyUI_IPAdapter_plus /home/xlab-app-center/custom_nodes/ComfyUI_IPAdapter_plus")
os.system(f"git clone https://git.homegu.com/Kosinkadink/ComfyUI-VideoHelperSuite /home/xlab-app-center/custom_nodes/ComfyUI-VideoHelperSuite")
os.system(f"git clone https://git.homegu.com/Nourepide/ComfyUI-Allor /home/xlab-app-center/custom_nodes/ComfyUI-Allor") # 硬件性能检测
os.system(f"git clone https://git.homegu.com/StartHua/Comfyui_CXH_joy_caption  /home/xlab-app-center/custom_nodes/Comfyui_CXH_joy_caption") # 支持多个视觉反推模型
os.system(f"git clone https://git.homegu.com/miaoshouai/ComfyUI-Miaoshouai-Tagger /home/xlab-app-center/custom_nodes/ComfyUI-Miaoshouai-Tagger") # 全新的视觉反推模型，显存更小

os.system(f"git clone https://git.homegu.com/pythongosssss/ComfyUI-Custom-Scripts /home/xlab-app-center/custom_nodes/ComfyUI-Custom-Scripts")
os.system(f"git clone https://git.homegu.com/melMass/comfy_mtb /home/xlab-app-center/custom_nodes/comfy_mtb")
os.system(f"git clone https://git.homegu.com/chflame163/ComfyUI_LayerStyle /home/xlab-app-center/custom_nodes/ComfyUI_LayerStyle")
os.system(f"git clone https://git.homegu.com/cubiq/ComfyUI_essentials /home/xlab-app-center/custom_nodes/ComfyUI_essentials")
os.system(f"git clone https://git.homegu.com/chrisgoringe/cg-use-everywhere /home/xlab-app-center/custom_nodes/cg-use-everywhere")
os.system(f"git clone https://git.homegu.com/chrisgoringe/cg-image-picker /home/xlab-app-center/custom_nodes/cg-image-picker")


# unet模型
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/models/unet/{file_name}') 
 for file_name in [
     'ketu_fp16.safetensors', 
 ]]
# lora
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/models/loras/{file_name}') 
 for file_name in [
     'Hyper-FLUX.1-dev-8steps-lora.safetensors', 
 ]]
# vae
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/models/vae/{file_name}') 
 for file_name in [
     'ketu_vae_fp16.safetensors', 
     'flux_vae.safetensors'
 ]]
# clip模型
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/models/clip/{file_name}') 
 for file_name in [
     'ViT-L-14-TEXT-detail-improved-hiT-GmP-TE-only-HF.safetensors', 
     'clip_l.safetensors',
     't5xxl_fp8_e4m3fn.safetensors'
 ]]
# 视觉识别模型&大语言模型
[download(dataset_repo='mofashi/comfy', 
          source_path=file_name, 
          target_path=f'/home/xlab-app-center/models/LLM/{file_name}') 
 for file_name in [
     'Florence_2_large_PromptGen.safetensors'
 ]]

# 大模型
os.chdir(f"/home/xlab-app-center/models/checkpoints") #文件夹

os.chdir(f"/home/xlab-app-center/models/unet") # 文件夹
subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/flux1-dev-fp8.safetensors?ref=main&nonce=1725931610381 -o flux1-dev-fp8.safetensors")


os.chdir(f"/home/xlab-app-center/models/LLM") # 文件夹
subprocess.run("aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://code.openxlab.org.cn/api/v1/repos/mofashi/comfy/media/chatglm3-8bit.safetensors?ref=main&nonce=1725936486503 -o chatglm3-8bit.safetensors")

os.chdir(f"/home/xlab-app-center")# 文件夹
os.system(f"python main.py --listen 0.0.0.0 --port 7860 --enable-cors-header")
#os.system(f"python main.py --dont-print-server --listen 0.0.0.0 --port 7860 --enable-cors-header")

