from typing import Optional
import fire
from llama import Llama


def main(
    ckpt_dir: str = "/home/ubuntu/llama/Llama2ChatModel/llama-2-7b-chat/",
    tokenizer_path: str = "/home/ubuntu/llama/Llama2ChatModel/tokenizer.model",
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 8,
    max_gen_len: Optional[int] = None,
    prompt: str = "",
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    if len(prompt)==0:
        print("ImmiResult:Prompt is empty",)
    else:
        pass

    dialogs = [
        [{"role": "user", "content": prompt}],

    ]
    results = generator.chat_completion(
        dialogs,  # type: ignore
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )

    for dialog, result in zip(dialogs, results):
        # for msg in dialog:
        #     print(f"{msg['role'].capitalize()}: {msg['content']}\n")
        # print(
        #     f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}"
        # )
        # print("\n==================================\n")
        print("ImmiResult:",result['generation']['content'].strip())

if __name__ == "__main__":
    fire.Fire(main)