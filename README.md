Mini GPT PyTorch
A lightweight implementation of the GPT (Generative Pre-trained Transformer) architecture built from scratch with PyTorch. This project provides a minimal yet complete transformer-based language model for educational purposes.
Features

Complete transformer architecture implementation
Self-attention mechanism with multi-head attention
Auto-regressive text generation
Simple training pipeline
Easily configurable hyperparameters

Overview
This project implements a small-scale GPT model that demonstrates the core principles of transformer-based language models. Despite its compact size, it includes all essential components:

Token and positional embeddings
Multi-head self-attention
Feed-forward networks
Layer normalization
Transformer blocks
Auto-regressive text generation

The model is trained on a tiny dataset ("hello world") for demonstration purposes, making it easy to understand the entire pipeline from data processing to text generation.
Requirements

Python 3.6+
PyTorch 1.0+

bashpip install torch
Usage
Simply run the script to train the model and generate text:
bashpython model.py
The script will:

Create a tokenizer from the dataset
Initialize the model
Train for the specified number of iterations
Generate new text using the trained model

Architecture
The implementation follows the standard transformer architecture with:

Self-Attention Head: Implements key-query-value attention mechanism
Multi-Head Attention: Combines multiple attention heads
Feed-Forward Network: Two-layer neural network with ReLU activation
Transformer Block: Combines attention and feed-forward networks with residual connections
Complete Model: Includes token embeddings, positional embeddings, and output projection

Hyperparameters
The model's behavior can be customized by modifying these hyperparameters:
ParameterDefaultDescriptionblock_size8Context length for predictionsbatch_size4Number of sequences per batchn_embd32Embedding dimensionn_heads4Number of attention headsn_layers2Number of transformer blocksmax_iters500Training iterationseval_interval100Steps between loss reportinglearning_rate1e-3Learning rate for AdamW optimizer
Extending the Model
You can enhance this implementation by:

Training on larger text datasets
Adding dropout for regularization
Implementing learning rate scheduling
Supporting larger vocabulary (e.g., BPE tokenization)
Adding model checkpointing

License
MIT
Acknowledgements
This implementation is inspired by the architecture described in the "Attention Is All You Need" paper and the GPT models by OpenAI.
