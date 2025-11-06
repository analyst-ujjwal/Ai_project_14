from diffusers import StableDiffusionPipeline
import torch

def generate_meme_image(prompt: str, output_path: str = "outputs/memes/meme.png"):
    """
    Generates an image based on the meme caption or topic.
    """
    pipe = StableDiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-1", torch_dtype=torch.float16
    )
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    image = pipe(prompt).images[0]
    image.save(output_path)
    return output_path
