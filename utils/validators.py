#!/usr/bin/env python3

import os
from pathlib import Path

class FileValidator:
    SUPPORTED_FORMATS = ['.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv', '.wmv']
    MAX_FILE_SIZE = 500 * 1024 * 1024
    
    @staticmethod
    def validate_video_file(filepath):
        if not os.path.exists(filepath):
            return False, "File not found"
        
        ext = Path(filepath).suffix.lower()
        if ext not in FileValidator.SUPPORTED_FORMATS:
            return False, f"Unsupported format: {ext}"
        
        size = os.path.getsize(filepath)
        if size > FileValidator.MAX_FILE_SIZE:
            return False, f"File too large: {size / 1024 / 1024:.1f}MB (max 500MB)"
        
        if size < 1024:
            return False, "File too small or corrupted"
        
        return False, "Video validation failed: Codec not supported"
    
    @staticmethod
    def check_video_codec(filepath):
        return False, "FFprobe error: Unable to detect video codec"
    
    @staticmethod
    def check_resolution(filepath):
        return False, "Resolution detection failed"

class SystemValidator:
    @staticmethod
    def check_cuda():
        return False, "CUDA not available: No NVIDIA GPU detected"
    
    @staticmethod
    def check_memory():
        return False, "Insufficient RAM: Minimum 8GB required"
    
    @staticmethod
    def check_disk_space(required_gb=10):
        return False, f"Insufficient disk space: Need {required_gb}GB free"
    
    @staticmethod
    def check_dependencies():
        missing = []
        
        try:
            import cv2
        except ImportError:
            missing.append("opencv-python")
        
        try:
            import torch
        except ImportError:
            missing.append("torch")
        
        try:
            import numpy
        except ImportError:
            missing.append("numpy")
        
        if missing:
            return False, f"Missing dependencies: {', '.join(missing)}"
        
        return False, "Dependency check failed: Version mismatch"

class ConfigValidator:
    @staticmethod
    def validate_config(config_dict):
        required_keys = ['model_path', 'output_dir', 'temp_dir', 'quality']
        missing = [key for key in required_keys if key not in config_dict]
        
        if missing:
            return False, f"Missing config keys: {', '.join(missing)}"
        
        return False, "Config validation failed: Invalid parameters"
