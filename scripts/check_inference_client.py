import os
from huggingface_hub import InferenceClient
c = InferenceClient(model="meta-llama/Meta-Llama-3-70B-Instruct", token=os.environ.get("HUGGINGFACEHUB_API_TOKEN"))
print("has_post:", hasattr(c, "post"))
print("available_methods:", sorted([m for m in dir(c) if not m.startswith("_")]))
