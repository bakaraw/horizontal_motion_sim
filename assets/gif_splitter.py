
from PIL import Image
import os

def split_gif_to_frames(gif_path, output_folder):
    """
    Splits a GIF into individual PNG frames.

    :param gif_path: Path to the GIF file.
    :param output_folder: Directory to save the frames.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    frame_number = 0

    try:
        # Open the GIF file
        gif = Image.open(gif_path)

        # Loop through each frame in the GIF
        while True:
            # Save the current frame as a PNG
            frame_path = os.path.join(output_folder, f"frame{frame_number:03d}.png")
            gif.save(frame_path, format="PNG")
            print(f"Saved: {frame_path}")
            frame_number += 1

            # Move to the next frame
            gif.seek(gif.tell() + 1)

    except EOFError:
        # End of frames
        print(f"GIF split into {frame_number} frames in folder: {output_folder}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
gif_path = "assets/VanOne-export.gif"  # Replace with your GIF file path
output_folder = "sprite_frames"  # Replace with your desired output directory
split_gif_to_frames(gif_path, output_folder)
