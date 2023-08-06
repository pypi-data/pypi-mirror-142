import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-cloudformation-sysdig-helm-agent",
    "version": "1.8.0.a5",
    "description": "Sysdig Agent EKS cluster deployment.",
    "license": "Apache-2.0",
    "url": "https://github.com/sysdiglabs/cloudformation-resource-providers.git",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdklabs/cdk-cloudformation.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_cloudformation_sysdig_helm_agent",
        "cdk_cloudformation_sysdig_helm_agent._jsii"
    ],
    "package_data": {
        "cdk_cloudformation_sysdig_helm_agent._jsii": [
            "sysdig-helm-agent@1.8.0-alpha.5.jsii.tgz"
        ],
        "cdk_cloudformation_sysdig_helm_agent": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk-lib>=2.16.0, <3.0.0",
        "constructs>=10.0.87, <11.0.0",
        "jsii>=1.55.0, <2.0.0",
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
