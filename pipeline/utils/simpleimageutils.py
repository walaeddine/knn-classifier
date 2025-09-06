import os


class SimpleImageUtils:
    # common image file extensions.
    IMAGE_TYPES = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif",)

    @staticmethod
    def list_files(base_path, valid_exts=None, contains=None):
        # Convert valid extensions to a set for efficient lookup
        valid_exts_set = {ext.lower()
                          for ext in valid_exts} if valid_exts else None

        # Loop over the directory structure using os.walk
        for root_dir, _, filenames in os.walk(base_path):
            # Loop over the filenames in the current directory
            for filename in filenames:
                # If the contains string is specified and not in the filename, skip this file
                if contains and contains not in filename:
                    continue

                # Determine the file extension of the current file
                ext = os.path.splitext(filename)[1].lower()

                # Check if the file's extension is in the set of valid extensions
                if not valid_exts_set or ext in valid_exts_set:
                    # Construct the full path to the file and yield it
                    file_path = os.path.join(root_dir, filename)
                    yield file_path

    @staticmethod
    def list_images(base_path, contains=None):
        # Use a list of common image extensions
        return SimpleImageUtils.list_files(base_path, valid_exts=SimpleImageUtils.IMAGE_TYPES, contains=contains)
