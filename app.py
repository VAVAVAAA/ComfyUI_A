# import os

# os.system(f"git lfs install")
# os.system(f"git clone https://github.com/comfyanonymous/ComfyUI /home/xlab-app-center/ComfyUI")
# os.chdir(f"/home/xlab-app-center")
# os.system(f"pip install -r requirements.txt")
# os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Manager /home/xlab-app-center/custom_nodes/ComfyUI-Manager")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors?download=true -d /home/xlab-app-center/models/checkpoints -o flux1-dev-fp8.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://civitai.com/api/download/models/782002?type=Model&format=SafeTensor&size=full&fp=fp16 -d /home/xlab-app-center/models/checkpoints -o Jugg_Xl_by_RunDiffusion.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/repos/file/Rnglg2/FLUX.1-Dev/main?filepath=ae.safetensors&sign=28f67ffe6b9eb46266ca3c67d855e344&nonce=1725002929795 -d /home/xlab-app-center/models/checkpoints -o realisticasianthaila_v20.ckpt")
# os.system(f"python main.py --listen 0.0.0.0 --port 7860 --enable-cors-header")
#os.system(f"python main.py --dont-print-server --listen 0.0.0.0 --port 7860 --enable-cors-header")

import subprocess  
import os  
  
def run_command(cmd, cwd=None, check=True, capture_output=False):  
    """  
    运行一个命令并处理输出和错误。  
  
    :param cmd: 要运行的命令，作为列表的字符串（例如：["git", "clone", "url"]）  
    :param cwd: 命令的工作目录  
    :param check: 如果为True，并且命令返回非零退出状态，则引发CalledProcessError  
    :param capture_output: 如果为True，则捕获命令的标准输出和标准错误  
    :return: 如果capture_output为True，则返回CompletedProcess实例；否则返回None  
    """  
    try:  
        result = subprocess.run(cmd, cwd=cwd, check=check, capture_output=capture_output, text=True)  
        if capture_output:  
            return result  
    except subprocess.CalledProcessError as e:  
        print(f"Error running command: {e}")  
        if e.stdout:  
            print("Standard output:")  
            print(e.stdout)  
        if e.stderr:  
            print("Standard error:")  
            print(e.stderr)  
        raise  # 可选：重新抛出异常，或者根据需要处理它  
  
# 确保目标目录存在  
target_dir = "/home/xlab-app-center/custom_nodes"  
os.makedirs(target_dir, exist_ok=True)  
  
# 安装 Git LFS（注意：这可能需要全局安装或在Git仓库中运行）  
# 这里我们假设它已全局安装或不需要在此脚本中安装  
  
# 克隆Git仓库  
run_command(["git", "clone", "https://github.com/ltdrdata/ComfyUI-Manager", os.path.join(target_dir, "ComfyUI-Manager")])  
  
# 下载模型文件  
model_urls = [  
    ("https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors?download=true", "flux1-dev-fp8.safetensors"),  
    ("https://civitai.com/api/download/models/782002?type=Model&format=SafeTensor&size=full&fp=fp16", "Jugg_Xl_by_RunDiffusion.safetensors"),  
    ("https://download.openxlab.org.cn/repos/file/Rnglg2/FLUX.1-Dev/main?filepath=ae.safetensors&sign=28f67ffe6b9eb46266ca3c67d855e344&nonce=1725002929795", "realisticasianthaila_v20.ckpt")  
]  
  
models_dir = "/home/xlab-app-center/models/checkpoints"  
os.makedirs(models_dir, exist_ok=True)  
  
for url, filename in model_urls:  
    run_command(["aria2c", "--console-log-level=error", "-c", "-x", "16", "-s", "16", "-k", "1M", url, "-d", models_dir, "-o", filename])  
  
# 启动Python服务  
run_command(["python3", "main.py", "--listen", "0.0.0.0", "--port", "7860", "--enable-cors-header"], cwd="/home/xlab-app-center")
