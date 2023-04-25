<h1 align="center">
    <img src="https://github.com/mscaudill/datarig/blob/master/docs/imgs/logo.png" 
    style="width:700px;height:auto;"/>
</h1>

<h2 align="center">
<p align="center">
  <a href="https://github.com/mscaudill/datarig/blob/master/LICENSE"><img
    src="https://img.shields.io/badge/License-BSD%203--Clause-teal" 
    alt="DataRig is released under the BSD 3-Clause license." />
  </a>
  <a href="https://github.com/mscaudill/datarig/tree/master#Dependencies"><img 
    src="https://img.shields.io/pypi/pyversions/openseize?logo=python&logoColor=gold" 
    alt="Python versions supported." />
  </a>
 <a href="https://github.com/mscaudill/datarig/pulls"><img 
    src="https://img.shields.io/badge/PRs-welcome-F8A3A3"
    alt="Pull Request Welcomed!" />
  </a>
</p>
</h2>

<p align="center"  style="font-size: 20px">
<a href="#Key-Features">Key Features</a>   |  
<a href="#Installation">Installation</a>   |  
<a href="#Dependencies">Dependencies</a>   |  
<a href="#Documentation">Documentation</a>   |  
<a href="#Attribution">Attribution</a>   |  
<a href="#Contributions">Contributions</a>   |  
<a href="#Issues">Issues</a>   |  
<a href="#License">License</a> |
<a href="#Acknowledgements">Acknowledgements</a> 
</p>


## THIS PROJECT HAS YET TO BE RELEASED. PLEASE CHECK BACK SOON!

# Key Features
Providing large testing and demo data alongside your package releases is
challenging for two reasons. First, code repositories have strict limits on file
sizes. Second, you don't want your users to wait forever to download your cool
package because you've included large data files.  If you're a python developer
and have hit these issues then <b><a href=https://github.com/mscaudill/datarig
target=_blank>DataRig</a></b> is for you.  DataRig allows you to
move data from several data repositories into the users local directories
post-installation. This "just-in-time" data fetching is perfect for users to
test or run your packages demos.

# Installation
DataRig can be installed into your projects environment using pip:

1. Activate the virtual or conda environment of your package
```Shell
$ source <YOUR_ENV>/bin/activate # python virtual environment
```

```Shell
$ conda activate <YOUR_ENV>
```

2. Install DataRig to your active environment
```Shell
(<YOUR_ENV>)$ pip install datarig
```

# Dependencies

DataRig is super lightweight requiring just <b>Python <span>&#8805;</span>
3.9</b> and the request library available here:

<table>

<tr>
    <th>package</th>
    <th>pypi</th>
    <th>conda</th>
  </tr>

<tr>
    <td><a href="https://requests.readthedocs.io/en/latest/" 
        target=_blank>requests</a></td>
    <td>https://pypi.org/project/requests/</td>
    <td align='center'><span>&#10003;</span></td>
  </tr>

</table>

# Documentation

# Attribution
If you find DataRig useful, please cite the Zenodo archive of this repository.

If you really like DataRig, you can also star the <a
href=https://github.com/mscaudill/datarig>repository</a> 
<span>&#11088;</span>!

# Contributions
Contributions are what makes open-source fun and we would love for you to
contribute. Please check out our [contribution guide](
https://github.com/mscaudill/datarig/blob/master/.github/CONTRIBUTING.md)
to get started.

# Issues

DataRig provides custom issue templates for filing bugs, requesting
feature enhancements, suggesting documentation changes, or just asking
questions. *Ready to discuss?* File an issue <a
href=https://github.com/mscaudill/datarig/issues/new/choose>here</a>. 

# License

DataRig is licensed under the terms of the 3-Clause BSD License.

# Acknowledgements

**This work is generously supported through the Ting Tsung and Wei Fong Chao 
Foundation and the National Institute of Neurological Disorders and Stroke 
(Grant 2R01 NS100738-05A1).**



