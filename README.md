bb# Practicing NanoGPT 🤖
 Trying out nanoGPT for the first time...

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
