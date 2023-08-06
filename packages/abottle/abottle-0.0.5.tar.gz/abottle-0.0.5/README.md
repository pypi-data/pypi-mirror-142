# abottle

trition/tensorrt/onnxruntim/pytorch python server wrapper

put your model into **a bottle** then you get a working server and more.

# Demo
```python

import numpy as np
from transformers import AutoTokenizer


class MiniLM:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    def predict(self, X):
        encode_dict = self.tokenizer(
            X, padding="max_length", max_length=128, truncation=True
        )
        input_ids = np.array(encode_dict["input_ids"], dtype=np.int32)
        attention_mask = np.array(encode_dict["attention_mask"], dtype=np.int32)

        outputs = self.model.infer(
            {"input_ids": input_ids, "attention_mask": attention_mask}, ["y"]
        )

        return outputs['y']


    #you can write config in class or provide it as a yaml file or yaml string
    class Config:
        class model:
            name = "minilm"
            version = "2"
```
you can write a class like this, and then starts with abottle

```shell
abottle main.MiniLM
```

config with shell
```shell
abottle main.MiniLM file_path=test_data.txt batch_size=100 --as tester --config """TritonModel:
        triton_url: localhost
        name: minilm
        version: 2
    """
```

config with file

```shell
abottle main.MiniLM file_path=test_data.txt batch_size=100 --as tester --config <config yaml file path>
```
you can get a http server run at localhost:8081 with a POST url /infer, where your predict function will be called, the X is the json decode content, self.model in your class is a trition client wrapper with a function infer which takes a dictionary as input and a list of str as output

this code is shit, use it carefully.