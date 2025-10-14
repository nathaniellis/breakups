'''
To run this properly, you need to use the virtual environment 

./.venv/Scripts/pip3.exe install torch torchvision torchaudio

'''
import numpy as np
import pandas as pd
import matplotlib as plt
import torch
from transformers import XLNetTokenizer, XLNetForQuestionAnsweringSimple


tokenizer = XLNetTokenizer.from_pretrained('xlnet-base-cased')
model = XLNetForQuestionAnsweringSimple.from_pretrained("xlnet/xlnet-base-cased")

question = 'why did we break up'
text_to_compare = ['my wife left me', 'she broke up with me 2 months ago', 'we made spaghetti']

# get output/hidden layer of initial question
q_inputs = torch.tensor(tokenizer.encode(question, add_special_tokens=True)).unsqueeze(0)
outputs = model(q_inputs)
hidden_states = outputs[0][:,-1]

#compare to all other text
for i in range(len(text_to_compare)):

    t_inputs = torch.tensor(tokenizer.encode(text_to_compare[i], add_special_tokens=True)).unsqueeze(0)
    t_outputs = model(t_inputs)
    hidden_states1 = t_outputs[0][:,-1]

    cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
    sim = cos(hidden_states, hidden_states1)
    print(f"{sim} why did we break up x {text_to_compare[i]}")





#answer_start_index = outputs.start_logits.argmax()
#answer_end_index = outputs.end_logits.argmax()

#predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]

# target is "nice puppet"
#target_start_index = torch.tensor([14])
#target_end_index = torch.tensor([15])

#outputs = model(**inputs, start_positions=target_start_index, end_positions=target_end_index)
#loss = outputs.loss

# i am out of it or something- not sure what i'm doing. should probably take some time to review neural networks and stuff. 

# what is this supposed to do? 
# primary function: take a sentence, classify it as 
# Take a sentence