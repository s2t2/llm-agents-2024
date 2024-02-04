# llm-agents-2024

## Setup

Environment setup:

```sh
conda create -n llm-agents-env python=3.10
conda activate llm-agents-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```


Create a [Hugging Face account](https://huggingface.co) as necessary, and obtain a [user access token](https://huggingface.co/docs/hub/security-tokens) for the hugging face hub (i.e. `HUGGING_FACE_TOKEN`).


Setup local ".env" file, with your credentials:

```sh
# example ".env" file contents:
HUGGING_FACE_TOKEN="hf___________"
```

## Usage

Run an example LLM from the hub:

```sh
python -m app.hub

REPO_ID="google/flan-t5-xxl" python -m app.hub
```
