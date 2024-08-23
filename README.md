# GAN Art Generation

This project is focused on generating digital art using Generative Adversarial Networks (GANs). The implementation is based on StyleGAN2, a state-of-the-art GAN architecture that generates high-quality images. The project is containerized using Docker, making it easy to set up and run in any environment.

## Project Structure

GAN-Art-Generation/ ├── data/ │ ├── raw/ │ ├── processed/ ├── models/ │ ├── stylegan2/ # Ignored in the repo ├── notebooks/ ├── scripts/ ├── utils/ ├── discord_bot/ ├── results/ ├── checkpoints/ ├── Dockerfile ├── requirements.txt └── README.md

- **data/**: Contains raw and processed datasets.
- **models/**: Contains model-related code and pre-trained models (StyleGAN2 is excluded from the repo).
- **notebooks/**: Jupyter notebooks for exploration and experiments.
- **scripts/**: Python scripts for data processing, training, etc.
- **utils/**: Utility functions for data handling, visualization, etc.
- **discord_bot/**: Code for a Discord bot to interact with the model.
- **results/**: Generated images and logs.
- **checkpoints/**: Model checkpoints.
- **Dockerfile**: Docker configuration for containerization.
- **requirements.txt**: Python dependencies.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **Docker** (if using the Docker container)
- **NVIDIA GPU** with CUDA support (for GPU-accelerated training)

### Installation

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/yourusername/GAN-Art-Generation.git
    cd GAN-Art-Generation
    ```

2. **Set Up a Virtual Environment**:

    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Download the StyleGAN2 Model** (if necessary):

    Since the `models/stylegan2` directory is ignored in the repo, you need to manually download or clone the StyleGAN2 model into this directory.

    ```sh
    git clone https://github.com/NVlabs/stylegan2.git models/stylegan2
    ```

### Dataset Preparation

Ensure your datasets are located in the `data/processed/digital_art` and `data/processed/met_faces` directories. The datasets should be in a format compatible with StyleGAN2.

### Training the Model

To train the model using the `digital_art` dataset:

```sh
python scripts/train_stylegan2.py
You can modify the train_stylegan2.py script to change the dataset or other training parameters.

Using Docker
Build the Docker Image:

sh
Copy code
docker build -t gan-art-generation .
Run the Docker Container:

sh
Copy code
docker run -it --rm gan-art-generation
This will start the training process inside a Docker container.
```

### Discord Bot Integration
- The project includes a basic Discord bot that interacts with the model. The bot can generate images based on user input. Set up the bot by configuring the discord_bot/ directory and running the bot script.

### Results
- Generated images and logs are stored in the results/ directory. You can explore these results to evaluate the model's performance.

### Contributing
- If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

### License
- This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments

- The StyleGAN2 architecture is based on the work by NVIDIA, and the official implementation can be found [here](https://github.com/NVlabs/stylegan2).
- The PyTorch version of StyleGAN2 can be found [here](https://github.com/rosinality/stylegan2-pytorch).

