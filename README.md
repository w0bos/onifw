# **ONIFW**

###### *A console based framework for Pentesting. Based on the work of [Manisso's Fsociety framework](https://github.com/Manisso/fsociety)*

![](https://img.shields.io/badge/License-MIT-blue.svg?longCache=true&style=popout-square)
![](https://img.shields.io/badge/Tested_On-Linux-orange.svg?longCache=true&style=popout-square)
![](https://img.shields.io/badge/Version-1.10-dark_green.svg?longCache=true&style=popout-square)
![](https://img.shields.io/badge/Python-3-purple.svg?longCache=true&style=popout-square)

## Description
**onifw** is a console-based framework for pentester. It comes with some common tools. You can either install all the recommended tools or install some of them. **onifw** is also able to use custom tools.

## Installation

Clone this repository and start the installer or `curl` the installer

```bash
curl 'https://raw.githubusercontent.com/w0bos/onifw/master/install.sh' > install.sh

./install.sh
```


## Required dependencies

- `python2.7`

- `python 3.7+`

- `packaging`
    
    with ```pip install packaging```


## Usage

From a terminal use 
```bash 
onifw
```

Use the `help` command in order to see all the available commands

## Configuration
onifw comes with some options that you can edit in the `src/onirc` file. These options with their default value are:
```ini
show_ascii_art = true
show_version = true
check_connectivity = true
check_version = false
show_options = false
delete_cache_on_exit = true
remove_tools_on_exit = false
save_session = false
prompt = onifw >
debug = false
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Feel free to contact me at w0bos@protonmail.com if you have any questions

## License
[MIT](https://choosealicense.com/licenses/mit/)
