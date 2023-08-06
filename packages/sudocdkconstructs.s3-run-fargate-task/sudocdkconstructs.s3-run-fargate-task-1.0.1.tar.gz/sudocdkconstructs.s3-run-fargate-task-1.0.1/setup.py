import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "sudocdkconstructs.s3-run-fargate-task",
    "version": "1.0.1",
    "description": "Run Fargate task with S3 upload event",
    "license": "MIT",
    "url": "https://github.com/sudopla/cdk-constructs.git",
    "long_description_content_type": "text/markdown",
    "author": "Jorge Pla",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/sudopla/cdk-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "sudocdkconstructs.s3_run_fargate_task",
        "sudocdkconstructs.s3_run_fargate_task._jsii"
    ],
    "package_data": {
        "sudocdkconstructs.s3_run_fargate_task._jsii": [
            "s3-run-fargate-task@1.0.1.jsii.tgz"
        ],
        "sudocdkconstructs.s3_run_fargate_task": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk-lib>=2.0.0, <3.0.0",
        "constructs>=10.0.0, <11.0.0",
        "jsii>=1.54.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
