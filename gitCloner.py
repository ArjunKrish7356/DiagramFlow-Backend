import os
import shutil
from git import Repo
from logger_config import logger

def clear_directory(directory_path):
    """
    Clear all files and subdirectories from the specified directory.
    Creates the directory if it doesn't exist.
    """
    try:
        # Check if directory exists
        if os.path.exists(directory_path):
            # Remove all contents
            for item in os.listdir(directory_path):
                item_path = os.path.join(directory_path, item)
                if os.path.isfile(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            logger.info(f"Directory {directory_path} has been cleared")
        else:
            # Create directory if it doesn't exist
            os.makedirs(directory_path)
            logger.info(f"Directory {directory_path} has been created")
        return True
    except Exception as e:
        logger.error(f"Error clearing directory {directory_path}: {e}")
        return False

def fetch_repo_from_git_link(link):
    if link.endswith(".git"):
        try:
            if clear_directory("./DirectoryToConvert"):
                Repo.clone_from(link, "./DirectoryToConvert")
                logger.info(f"The repo -- {link} has been cloned...")
                return True
            else:
                return False
        except Exception as e:
            logger.error(f"Error cloning repository: {e}")
            return False
    else:
        logger.warning(f"Invalid git URL: {link} (must end with .git)")
        return False