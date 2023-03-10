# Practicing NanoGPT 🤖
 Trying out nanoGPT for the first time. </br>
 These are just some notes that I wanted to write down...

👉Following the two, Simon Willison blog posts on setting up nanoGPT
> https://til.simonwillison.net/llms/nanogpt-shakespeare-m2
> https://til.simonwillison.net/llms/training-nanogpt-on-my-blog
___
</br>

### Summary of the **setup** steps that I took

1. Clone from Andrej Karpathy's nanoGPT repo
    ```py
    git clone https://github.com/karpathy/nanoGPT
    ```
    
2.  Create a venv
    ```py
    python -m venv venv
    ```
    
3. Install some libraries in that venv
    ```py
    pip install transformers datasets tiktoken tqdm wandb numpy httpx
    ```
    **+PLUS** install PyTorch according to the setup that
    </br>
        works for you https://pytorch.org/get-started/locally/
    
    I personally ran the following for system with **windows, pip, python and cpu**:
    ```py
    pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
    ```

And that should be it for the initial setup..

___
</br>

### How I understand it...

**First**, you'll most likely run
```py
python prepare.py
```
> (in the correct directory; otherwise it won't work)

Basically what prepare.py does, is that it downloads the data you want to feed it, and splits it into training and validation sets, creating the train.bin & val.bin files.
____
**Next**, start training! You might want to change the options </br> of train.py to fit your system. you could do this by either changing them straight in the file, or by overriding them like this (e.g)
```py
python train.py --dataset=simonwillisonblog --n_layer=4 --n_head=4 --n_embd=64 --compile=False --eval_iters=1 --block_size=64 --batch_size=8 --device=cpu
```
> (In my case, in the nanoGPT folder)

Output looking something like this
```py
step 0: train loss 10.8340, val loss 10.8173
iter 0: loss 10.8320, time 472.43ms
iter 1: loss 10.8206, time 137.21ms
iter 2: loss 10.8160, time 244.42ms
iter 3: loss 10.8250, time 145.10ms
iter 4: loss 10.8312, time 140.41ms
iter 5: loss 10.8306, time 135.30ms
```
