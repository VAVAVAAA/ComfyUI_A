import os
import shutil
# 环境
os.system("pip install --upgrade transformers==4.44.2")
os.system("pip install --upgrade torch==2.1.0 torchvision==0.16.0")
# 依赖
os.system("pip install aiohttp_sse")
os.system("pip install segment_anything")
os.system("pip install opencv-python")
os.system("pip install transparent_background")
os.system("pip install aiohttp_sse")
os.system("pip install rembg")

os.chdir(f"/home/xlab-app-center")
# 插件
os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Manager /home/xlab-app-center/custom_nodes/ComfyUI-Manager")
os.system(f"git clone https://github.com/ty0x2333/ComfyUI-Dev-Utils /home/xlab-app-center/custom_nodes/ComfyUI-Dev-Utils") # 显示节点运行时间
os.system(f"git clone https://github.com/Nuked88/ComfyUI-N-Sidebar /home/xlab-app-center/custom_nodes/ComfyUI-N-Sidebar")
os.system(f"git clone https://github.com/AIGODLIKE/AIGODLIKE-ComfyUI-Translation /home/xlab-app-center/custom_nodes/AIGODLIKE-ComfyUI-Translation")
os.system(f"git clone https://github.com/rgthree/rgthree-comfy /home/xlab-app-center/custom_nodes/rgthree-comfy")

os.system(f"git clone https://github.com/MinusZoneAI/ComfyUI-Kolors-MZ /home/xlab-app-center/custom_nodes/ComfyUI-Kolors-MZ") # 可图
os.system(f"git clone https://github.com/SeaArtLab/comfyui_storydiffusion /home/xlab-app-center/custom_nodes/comfyui_storydiffusion") # 可图
os.system(f"git clone https://github.com/yolain/ComfyUI-Easy-Use /home/xlab-app-center/custom_nodes/ComfyUI-Easy-Use")
os.system(f"git clone https://github.com/xinsir6/ControlNetPlus /home/xlab-app-center/custom_nodes/ControlNetPlus") # 全能xl调用
os.system(f"git clone https://github.com/kijai/ComfyUI-segment-anything-2 /home/xlab-app-center/custom_nodes/ComfyUI-segment-anything-2") # 第二代抠图
os.system(f"git clone https://github.com/kijai/ComfyUI-KJNodes /home/xlab-app-center/custom_nodes/ComfyUI-KJNodes")

os.system(f"git clone https://github.com/john-mnz/ComfyUI-Inspyrenet-Rembg /home/xlab-app-center/custom_nodes/ComfyUI-Inspyrenet-Rembg") # 抠背景
os.system(f"git clone https://github.com/Fannovel16/comfyui_controlnet_aux /home/xlab-app-center/custom_nodes/comfyui_controlnet_aux")
os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Impact-Pack /home/xlab-app-center/custom_nodes/ComfyUI-Impact-Pack")
os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Inspire-Pack /home/xlab-app-center/custom_nodes/ComfyUI-Inspire-Pack")
os.system(f"git clone https://github.com/ssitu/ComfyUI_UltimateSDUpscale /home/xlab-app-center/custom_nodes/ComfyUI_UltimateSDUpscale")

os.system(f"git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus /home/xlab-app-center/custom_nodes/ComfyUI_IPAdapter_plus")
os.system(f"git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite /home/xlab-app-center/custom_nodes/ComfyUI-VideoHelperSuite")
os.system(f"git clone https://gitcode.com/gh_mirrors/co/ComfyUI-Allor /home/xlab-app-center/custom_nodes/ComfyUI-Allor") # 硬件性能检测
os.system(f"git clone https://github.com/lucataco/cog-flux-controlnet-union-pro /home/xlab-app-center/custom_nodes/cog-flux-controlnet-union-pro") # flux的全能cn


# 模型
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://hf-mirror.com/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors?download=true -d /home/xlab-app-center/models/checkpoints -o flux1-dev-fp8.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://civitai.com/api/download/models/782002 -d /home/xlab-app-center/models/checkpoints -o Jugg_Xl_by_RunDiffusion.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://download.openxlab.org.cn/models/ninjawick/realistic-vision-5.1/weight//Realistic_Vision_V6.0_NV_B1_inpainting.safetensors -d /home/xlab-app-center/models/checkpoints -o Realistic_Vision_V6.0_NV_B1_inpainting.safetensors")
# lora
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://hf-mirror.com/ByteDance/Hyper-SD/resolve/main/Hyper-FLUX.1-dev-16steps-lora.safetensors?download=true -d /home/xlab-app-center/models/lora -o Hyper-FLUX.1-dev-16steps-lora.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://hf-mirror.com/ByteDance/Hyper-SD/resolve/main/Hyper-FLUX.1-dev-8steps-lora.safetensors?download=true -d /home/xlab-app-center/models/lora -o Hyper-FLUX.1-dev-8steps-lora.safetensors")

# controlnet
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://hf-mirror.com/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro/resolve/main/diffusion_pytorch_model.safetensors?download=true -d /home/xlab-app-center/models/controlnet -o FLUX.1-dev-ControlNet-Union-Pro.safetensors")


os.system(f"python main.py --listen 0.0.0.0 --port 7860 --enable-cors-header")
#os.system(f"python main.py --dont-print-server --listen 0.0.0.0 --port 7860 --enable-cors-header")

