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

### Working with LLAMA-2 model

#### Step 1
[Request download link](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) 

#### Step 2

```
git clone https://github.com/ajithkumar666/Llama2ChatModel.git
```
#### Step 3
Once your request is approved, you will receive a signed URL over email. 
Then run the `download.sh` script, passing the URL provided when prompted to start the download.

Pre-requisites: Make sure you have `wget` and `md5sum` installed. Then to run the script: 
#### 3.1
```
cd Llama2ChatModel/
```
#### 3.2
Change `download.sh` to executable.
```
sudo chmod +x download.sh
```
#### 3.3

```
./download.sh
```
### Execute Chat Completion , example usage

```
torchrun --nproc_per_node 1 chat_completion.py \
    --ckpt_dir /root/Llama2ChatModel/llama-2-7b-chat/ \
    --tokenizer_path /root/Llama2ChatModel/tokenizer.model \
    --max_seq_len 512 \
    --max_batch_size 8 \
    --prompt "what is '(a+b)(a-b)'"
```

### Reference
1. [Lllam2 Meta](https://github.com/facebookresearch/llama)
2. [Model Details](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md)