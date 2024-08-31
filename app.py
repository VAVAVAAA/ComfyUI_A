import os
import shutil

os.system("pip install --upgrade transformers==4.44.2")
os.system("pip install --upgrade torch==2.1.0 torchvision==0.16.0")

os.chdir(f"/home/xlab-app-center")
# os.system("git pull https://github.com/comfyanonymous/ComfyUI.git main")
# 插件
os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Manager /home/xlab-app-center/custom_nodes/ComfyUI-Manager")
os.system(f"git clone https://github.com/ty0x2333/ComfyUI-Dev-Utils /home/xlab-app-center/custom_nodes/ComfyUI-Dev-Utils")
os.system(f"git clone https://github.com/Nuked88/ComfyUI-N-Sidebar /home/xlab-app-center/custom_nodes/ComfyUI-N-Sidebar")
os.system(f"git clone https://github.com/AIGODLIKE/AIGODLIKE-ComfyUI-Translation /home/xlab-app-center/custom_nodes/AIGODLIKE-ComfyUI-Translation")


# 模型
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://hf-mirror.com/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors?download=true -d /home/xlab-app-center/models/checkpoints -o flux1-dev-fp8.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://civitai.com/api/download/models/782002 -d /home/xlab-app-center/models/checkpoints -o Jugg_Xl_by_RunDiffusion.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false https://download.openxlab.org.cn/models/ninjawick/realistic-vision-5.1/weight//Realistic_Vision_V6.0_NV_B1_inpainting.safetensors -d /home/xlab-app-center/models/checkpoints -o Realistic_Vision_V6.0_NV_B1_inpainting.safetensors")
os.system(f"python main.py --listen 0.0.0.0 --port 7860 --enable-cors-header")
#os.system(f"python main.py --dont-print-server --listen 0.0.0.0 --port 7860 --enable-cors-header")

