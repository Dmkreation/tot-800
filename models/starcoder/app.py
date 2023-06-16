import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "GeorgiaTechResearchInstitute/starcoder-gpteacher-code-instruct"
device = "cuda"

input_prompt = ("Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n"
                "### Instruction:\n"
                "{instruction}\n\n"
                "### Input:\n"
                "{input}\n\n"
                "### Response:")

prompt = "Please explain the following program."
extra_input = "def hello_world\n  puts 'hello'\nend"
prompt = input_prompt.format_map({"instruction": prompt, "input": extra_input})

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(
    checkpoint, trust_remote_code=True, torch_dtype=torch.float16).to(device)

inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
