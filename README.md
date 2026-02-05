# AI Watermark Remover Pro

![License](https://img.shields.io/badge/license-GPLv3-green.svg?style=flat)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20MacOS%20%7C%20Linux-lightgrey.svg)
![AI](https://img.shields.io/badge/AI-Deep%20Learning-orange.svg)

## Overview

Professional-grade video watermark removal tool powered by advanced AI inpainting algorithms. Remove logos, text watermarks, and overlays from videos while maintaining visual quality through deep learning-based content restoration.

## Key Features

- 🎯 **AI-Powered Detection** - Automatic watermark detection and localization
- 🖼️ **Smart Inpainting** - Neural network-based content restoration
- ⚡ **GPU Acceleration** - CUDA-optimized processing for speed
- 🎬 **Batch Processing** - Remove watermarks from multiple videos
- 🔧 **Customizable** - Adjust detection sensitivity and quality settings
- 📊 **Real-time Preview** - See results before final processing

## How It Works

1. **Detection Phase**: AI model scans video frames to locate watermark patterns
2. **Analysis Phase**: Determines watermark boundaries and opacity levels  
3. **Removal Phase**: Deep learning inpainting removes watermark pixel by pixel
4. **Restoration Phase**: Content-aware fill reconstructs the original scene
5. **Encoding Phase**: Outputs clean video with original quality preserved

## Technology Stack

- **Deep Learning**: PyTorch-based inpainting models
- **Computer Vision**: OpenCV for frame processing
- **GPU Computing**: CUDA/TensorRT acceleration
- **Video Processing**: FFmpeg for encoding/decoding

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.10+ | 3.11+ |
| OS | Windows 10 / MacOS 11 / Linux | Windows 11 / MacOS 13 |
| RAM | 4GB | 8GB+ |
| GPU | GTX 1660 (6GB VRAM) | RTX 3060+ (12GB VRAM) |
| Storage | 2GB free | 10GB free |
| Dependencies | FFmpeg, CUDA 11.8+ | FFmpeg, CUDA 12.0+ |

**Note**: CPU-only mode available but 10-50x slower than GPU processing.

## Supported Watermark Types

| Type | Description | Success Rate |
|------|-------------|--------------|
| **Static Logo** | Fixed position logos/branding | 95%+ |
| **Text Overlay** | Static text watermarks | 90%+ |
| **Semi-transparent** | Partially transparent overlays | 80-90% |
| **Animated** | Moving/fading watermarks | 70-85% |
| **Complex Patterns** | Intricate designs | 60-75% |

**Best Results**: Clean, high-contrast watermarks on uniform backgrounds

## Installation

Clone the repository using Git:

```bash
git clone https://github.com/uedk9p/sora2-watermark-remover.git
cd sora2-watermark-remover
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

```
ai-watermark-remover/
├── main.py              # Desktop GUI application
├── server.py            # REST API server
├── requirements.txt     # Python dependencies
├── config.json          # Configuration file
├── src/
│   └── processor.py     # Video processing engine
├── models/
│   └── inpainting.py    # AI inpainting models
├── utils/
│   └── validators.py    # Input validation
├── presets/             # Watermark detection presets
│   ├── logo.json        # Logo watermark preset
│   └── text.json        # Text watermark preset
├── templates/           # Web UI templates (API mode)
├── static/              # Static assets
└── output/              # Processed videos
```

## Usage

### Quick Start (GUI)

Launch the desktop application:

```bash
python main.py
```

**Steps:**
1. Click "Browse" to select video file
2. Adjust detection settings (Auto/Manual/AI-Enhanced)
3. Set inpainting quality (Low/Medium/High/Ultra)
4. Click "Process Video"
5. Wait for watermark detection and removal
6. Find output in `output/` folder

### CLI Mode

Process video from command line:

```bash
python main.py --input video.mp4 --output clean.mp4 --mode auto --quality high
```

### API Server Mode

For integration with other applications:

```bash
python server.py --port 8000 --gpu
```

## API Documentation

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/detect` | POST | Detect watermark in video |
| `/remove` | POST | Remove detected watermark |
| `/upload` | POST | Upload and process video |
| `/status/{job_id}` | GET | Check processing status |
| `/download/{job_id}` | GET | Download processed video |

### Example: Detect Watermark

```python
import requests

files = {'video': open('watermarked.mp4', 'rb')}
data = {'mode': 'auto', 'threshold': 0.8}

response = requests.post('http://localhost:8000/detect', 
                        files=files, 
                        data=data)

result = response.json()
# {'watermark_found': True, 'position': [100, 50, 200, 100], 'confidence': 0.95}
```

### Example: Remove Watermark

```python
import requests

files = {'video': open('watermarked.mp4', 'rb')}
data = {
    'quality': 'high',
    'method': 'ai-inpainting',
    'preserve_quality': True
}

response = requests.post('http://localhost:8000/remove', 
                        files=files, 
                        data=data)

job_id = response.json()['job_id']

# Check status
status = requests.get(f'http://localhost:8000/status/{job_id}')

# Download when complete
if status.json()['status'] == 'complete':
    result = requests.get(f'http://localhost:8000/download/{job_id}')
    with open('output.mp4', 'wb') as f:
        f.write(result.content)
```

## Best Practices

### For Best Results

1. **Source Quality**: Use highest quality source video
2. **Watermark Type**: Static watermarks work best
3. **Position**: Corner watermarks easier than centered
4. **Contrast**: High contrast between watermark and background
5. **Resolution**: 1080p recommended (4K may be slower)

### Processing Workflow

```
Input Video → Watermark Detection → Position Verification → 
AI Inpainting → Quality Check → Output Clean Video
```

### Manual Mode

For difficult watermarks:
1. Use manual mode in GUI
2. Specify exact watermark coordinates
3. Adjust inpainting strength (0.5-1.0)
4. Preview before full processing

## Configuration

Create a `config.json` file in the root directory:

```json
{
  "model_path": "models/weights.pth",
  "output_dir": "output",
  "temp_dir": "temp",
  "quality": 23,
  "gpu_enabled": true
}
```

## Troubleshooting

### Common Errors

**Error: "No watermark detected"**
- Watermark may be too faint or transparent
- Try manual mode and specify watermark location
- Increase detection threshold in settings

**Error: "CUDA not available"**
- Install NVIDIA CUDA Toolkit 11.8 or later
- Verify GPU drivers: `nvidia-smi`
- Use `--cpu` flag for CPU-only mode (slower)

**Error: "Inpainting failed"**
- Watermark overlaps critical content
- Video resolution too high (reduce to 1080p)
- Try lower quality setting first

**Error: "Out of VRAM"**
- Reduce video resolution
- Process shorter segments
- Lower batch size in config.json
- Use CPU mode as fallback

**Error: "Unsupported format"**
- Convert to MP4: `ffmpeg -i input.avi -c:v libx264 output.mp4`
- Ensure video uses H.264 codec

### Performance Tips

- **GPU Mode**: 30-60 FPS processing (RTX 3060+)
- **CPU Mode**: 2-5 FPS processing
- **Batch Processing**: Process multiple videos overnight
- **Presets**: Use built-in presets for common watermark types

## Support the Project

If you find this tool helpful, consider supporting continued development:

| Currency | Address |
|----------|---------|
| BTC | `bc1q8grhtxdw37npcdadm7xa848vquqgurj9ecvpex` |
| ERC20 | `0x2d19c72fb8b3a7cdc7fa4970b5c777966f547854` |

**Thank you for your support! 🙏**

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under GPLv3 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV team for computer vision tools
- PyTorch community for deep learning framework
- FFmpeg project for video processing

## Disclaimer

This tool is for educational and research purposes. Users are responsible for ensuring they have the right to process and modify video content.

---

**Built with ❤️ by the open source community**