# DNA-RWE-project
DNA Disk: Achieving Read-Write-Erase Operations via Confined Enzymatic Control

# Data Encoding and Sequencing Depth Calculation for Research Project

This repository contains Python scripts used in our research paper for data encoding (images and text) and sequencing depth calculation. All scripts are compatible with **Python 3.x**.

## Overview

The repository provides:
- Image data encoding using Huffman coding.
- Text data encoding using simple mapping methods.
- Image preprocessing (resizing and sampling reduction).
- Sequencing depth calculation required for reliable data recovery.

These scripts were directly utilized in the experiments described in our research work.

## Scripts Description

### 1. Resize photo.py
Preprocess images by resizing them to reduce sampling resolution and file size before encoding. Run this script to prepare input images before Huffman encoding.

### 2. data encoding1.py
Performs Huffman encoding on preprocessed image files. Encodes image data into compressed binary format for efficient storage and recovery.

### 3. data encoding2.py
Encodes text (.txt) documents using a simple mapping-based encoding strategy. Maps characters to predefined binary or numerical codes, suitable for plain text storage.

### 4. Calculation of Sequencing Depth Required for Data Recovery.py
Computes the minimum sequencing depth required to reliably recover encoded data from experimental reads. Implements statistical models for depth calculation and provides guidance for experimental design.

## Requirements

- Python 3.x
- Recommended libraries:
  - numpy
  - pillow (for image handling)
  - collections (standard library)

