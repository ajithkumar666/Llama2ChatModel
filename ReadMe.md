## Llama 2: Open Foundation and Fine-Tuned Chat Models 

`NOTE: Verfied and working in Google Colab A100 GPU`


### Install following

```
sudo apt-get update
```

```
sudo apt-get -y install python3-pip
```

### Clone repository 

```
python3 -m pip install -r requirements.txt

```

### Download Llama model

#### step 1
[Request download link](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) 

#### step 2
Once your request is approved, you will receive a signed URL over email. 
Then run the `download.sh` script, passing the URL provided when prompted to start the download.

Pre-requisites: Make sure you have `wget` and `md5sum` installed. Then to run the script: `./download.sh`.

### Execute Chat Completion 
```
torchrun --nproc_per_node 1 chat_completion.py \
    --ckpt_dir llama-2-7b-chat/ \
    --tokenizer_path tokenizer.model \
    --max_seq_len 512 --max_batch_size 6
```

### Reference
1. [Lllam2 Meta](https://github.com/facebookresearch/llama)
2. [Model Details](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md)