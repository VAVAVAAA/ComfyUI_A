import os
import shutil

os.chdir(f"/home/xlab-app-center")
# os.system(f"git lfs install")
# os.system(f"git lfs update")
# os.system(f"git clone https://github.com/comfyanonymous/ComfyUI /home/xlab-app-center/ComfyUI")
# os.system(f"pip install -r requirements.txt")
os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Manager /home/xlab-app-center/custom_nodes/ComfyUI-Manager")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors?download=true -d /home/xlab-app-center/models/checkpoints -o flux1-dev-fp8.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://civitai.com/api/download/models/782002?type=Model&format=SafeTensor&size=full&fp=fp16 -d /home/xlab-app-center/models/checkpoints -o Jugg_Xl_by_RunDiffusion.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/repos/file/Rnglg2/FLUX.1-Dev/main?filepath=ae.safetensors&sign=28f67ffe6b9eb46266ca3c67d855e344&nonce=1725002929795 -d /home/xlab-app-center/models/checkpoints -o realisticasianthaila_v20.ckpt")
os.system(f"python main.py --listen 0.0.0.0 --port 7860 --enable-cors-header")
#os.system(f"python main.py --dont-print-server --listen 0.0.0.0 --port 7860 --enable-cors-header")
