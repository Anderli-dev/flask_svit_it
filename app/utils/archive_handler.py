import os
import tarfile
import zipfile


class ArchiveHandler:
    def __init__(self, save_directory="uploads", extracted_directory="uploads/extracted_logs"):
        self.save_directory = save_directory
        self.extracted_directory = extracted_directory
        os.makedirs(self.save_directory, exist_ok=True)
        os.makedirs(self.extracted_directory, exist_ok=True)
    
    def save_file(self, file):
        save_path = os.path.join(self.save_directory, file.filename)
        file.save(save_path)
        return save_path
    
    def extract_archive(self, file_path):
        print(file_path)
        filename:str = os.path.basename(file_path)
        os.makedirs(self.extracted_directory, exist_ok=True)

        if filename.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(self.extracted_directory)
        elif filename.endswith('.tar'):
            with tarfile.open(file_path, 'r:') as tar_ref:
                tar_ref.extractall(self.extracted_directory)
        else:
            return file_path
        
        return os.path.join(self.extracted_directory, filename.split(".", 1)[0] + ".txt")
    
    def process_file(self, file):
        save_path = self.save_file(file)
        extracted_path = self.extract_archive(save_path)
        return extracted_path