<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">MALAYALAM-MNIST</h1></p>
<p align="center">
	<em><code>❯ REPLACE-ME</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/MarcGeorgeML/malayalam-mnist?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/MarcGeorgeML/malayalam-mnist?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/MarcGeorgeML/malayalam-mnist?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/MarcGeorgeML/malayalam-mnist?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

<p>❯ This repository is focused on recognizing handwritten Malayalam characters, drawing inspiration from the MNIST dataset for handwritten digit recognition. The repository contains several Jupyter notebooks, including model.ipynb, model_symbols.ipynb, and preprocessing.ipynb, which detail the processes of data preprocessing, model development, and training. Additionally, files such as label_2_letter.csv and label_2_symbol.csv are mappings between labels and corresponding Malayalam letters or symbols. Model files like mal_model.pth and mal_model_symbols.pth are trained models that are included in the repository. This can be used to create a malayalam HCR (Handwritten character Recognition).​</p>

---

##  Features

- Malayalam Handwritten Recognition: Inspired by the MNIST dataset, this project is designed to recognize handwritten Malayalam characters and symbols.

- Comprehensive Data Preprocessing: Contains Jupyter notebooks that handle data cleaning, transformation, and preparation tailored for Malayalam script.

- Model Training and Evaluation: Provides interactive notebooks (e.g., model.ipynb and model_symbols.ipynb) that guide users through the process of building, training, and evaluating deep learning models.

- Pre-trained Models Included: Comes with ready-to-use pre-trained models (mal_model.pth and mal_model_symbols.pth), enabling quick inference without retraining.

- Label Mapping Files: Includes CSV files (label_2_letter.csv and label_2_symbol.csv) for mapping numeric labels to their corresponding Malayalam letters and symbols.

- PyTorch-based Implementation: Utilizes PyTorch as the underlying framework for constructing and training neural networks.

- Reproducibility and Experimentation: Designed with reproducibility in mind, allowing researchers and developers to replicate experiments or fine-tune models for further improvements.

---

##  Project Structure

```sh
└── malayalam-mnist/
    ├── __pycache__
    │   └── conversion.cpython-37.pyc
    ├── conversion.py
    ├── directory.ipynb
    ├── label_2_letter.csv
    ├── label_2_symbol.csv
    ├── labels.csv
    ├── labels_symbols.csv
    ├── mal_model.pth
    ├── mal_model_symbols.pth
    ├── merge_datasets.ipynb
    ├── model.ipynb
    ├── model_symbols.ipynb
    ├── preprocessing.ipynb
    ├── test_values.csv
    ├── train_values.csv
    └── valid_values.csv
```


###  Project Index
<details open>
	<summary><b><code>MALAYALAM-MNIST/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/MarcGeorgeML/malayalam-mnist/blob/master/directory.ipynb'>directory.ipynb</a></b></td>
				<td><code>❯ Code that creates csv files that helps the model to track of input data and its labels</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MarcGeorgeML/malayalam-mnist/blob/master/model.ipynb'>model.ipynb</a></b></td>
				<td><code>❯ Training and testing of the letter model</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MarcGeorgeML/malayalam-mnist/blob/master/preprocessing.ipynb'>preprocessing.ipynb</a></b></td>
				<td><code>❯ Testing of all preprocessing and transforms to be applied to images</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MarcGeorgeML/malayalam-mnist/blob/master/merge_datasets.ipynb'>merge_datasets.ipynb</a></b></td>
				<td><code>❯ Code that merged all the datasets to one as well as convert pixel values to .jpg images and stored them</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MarcGeorgeML/malayalam-mnist/blob/master/mal_model_symbols.pth'>mal_model_symbols.pth</a></b></td>
				<td><code>❯ The final symbol model saved state for letters</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MarcGeorgeML/malayalam-mnist/blob/master/conversion.py'>conversion.py</a></b></td>
				<td><code>❯ Converts all images from rgba to rgb files</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MarcGeorgeML/malayalam-mnist/blob/master/model_symbols.ipynb'>model_symbols.ipynb</a></b></td>
				<td><code>❯ Training and testing of the symbol model</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/MarcGeorgeML/malayalam-mnist/blob/master/mal_model.pth'>mal_model.pth</a></b></td>
				<td><code>❯ The final symbol model saved state for symbols</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with malayalam-mnist, ensure your runtime environment meets the following requirements:

- **Programming Language:** JupyterNotebook


###  Installation

Install malayalam-mnist using one of the following methods:

**Build from source:**

1. Clone the malayalam-mnist repository:
```sh
❯ git clone https://github.com/MarcGeorgeML/malayalam-mnist
```

2. Navigate to the project directory:
```sh
❯ cd malayalam-mnist
```

3. Install the project dependencies:
'pip install -r requirements.txt'



###  Usage
Run malayalam-mnist using the following command:
'jupyter notebook model.ipynb'
'jupyter notebook model_symbols.ipynb'

##  Project Roadmap

- [X] **`Task 1`**: <strike>Create and train letter model.</strike>
- [X] **`Task 2`**: <strike>Create and train symbol model.</strike>
- [X] **`Task 3`**: <strike>Implement in apps.</strike>

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/MarcGeorgeML/malayalam-mnist/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/MarcGeorgeML/malayalam-mnist/issues)**: Submit bugs found or log feature requests for the `malayalam-mnist` project.
- **💡 [Submit Pull Requests](https://github.com/MarcGeorgeML/malayalam-mnist/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/MarcGeorgeML/malayalam-mnist
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/MarcGeorgeML/malayalam-mnist/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=MarcGeorgeML/malayalam-mnist">
   </a>
</p>
</details>

---


##  Acknowledgments

- I thank [@tims-exe](www.github.com/tims-exe) for the immense support
#### 📊 Datasets Used

- **Dataset 1**: [Malayalam Handwritten Letters (Kaggle)](https://www.kaggle.com/datasets/manikantanrnair/malayalam-hand-written-letters)  
  Contains a collection of handwritten Malayalam characters for classification tasks.

- **Dataset 2**: [Amrita Malayalam Character Database (TC11)](https://tc11.cvc.uab.es/datasets/Amrita_MalCharDb_1)  
  A comprehensive dataset of isolated Malayalam handwritten characters from Amrita University.

- **Dataset 3**: *(Add link or description here when available)*
 
---
