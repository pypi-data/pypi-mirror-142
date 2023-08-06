from setuptools import setup, find_packages
import os

current_file_path = os.path.abspath(os.path.dirname(__file__))

def get_readme():
    readme_file_path = os.path.join(current_file_path, 'README.md')
    with open(readme_file_path, 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name='enaptorch',
    version="v1.0",
    author='Swanand Katdare',
    author_email='swanand@edgeneural.ai',
    url='https://enaptorch.org',
    download_url='https://github.com/SwanandkEN/enaptorch/archive/refs/tags/v1.0.zip',
    packages=find_packages(),
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
        ],
        install_requires=['numpy', 'torch', 'torchmetrics'],
        python_requires='>=3.6.1',
        description='A simplified framework and utilities for PyTorch.',
        long_description=get_readme(),
        long_description_content_type='text/plain',
        extras_require={
            "colorama": "colorama>=0.4.3",
            "scikit-learn": "scikit-learn>=0.23.2",
            "tensorboard": "tensorboard>=2.4.0",
            "tensorboardX": "tensorboardX>=2.1",
            "torchvision": "torchvision>=0.8.1",
            "pandas": "pandas>=2.0.0.0",
            "mlflow": "mlflow>=1.12.1",
        },

)