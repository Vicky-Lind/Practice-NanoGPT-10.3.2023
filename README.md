# Practicing NanoGPT 🤖
 Trying out nanoGPT for the first time...

:point_right: 👉Following the two, Simon Willison blog posts on setting up nanoGPT
> https://til.simonwillison.net/llms/nanogpt-shakespeare-m2
> https://til.simonwillison.net/llms/training-nanogpt-on-my-blog


___
### Summary of the steps I took

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
    ```py
    
    ```
    fixing this soon...
