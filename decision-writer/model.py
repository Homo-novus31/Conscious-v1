from huggingface_hub import login
login()

from transformers import AutoTokenizer as at
from transformers import AutoModelForCausalLM as am
import torch

MODEL_NAME = "meta-llama/Llama-3.2-1B"
tokeniser = at.from_pretrained(MODEL_NAME)
model = am.from_pretrained(
    MODEL_NAME,
    torch_dtype = torch.float16,
    device_map = 'auto'
)
model.eval()