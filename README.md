# Python Kavithai and Quotes Maker  

Simple python Script to Generate a Tamil Kavithai and English Quotes image in Square Format for Social Media Posts and Status.  

## Modules

- Python Pillow for Generate Quotes image - <https://github.com/python-pillow/Pillow>
- textwrap - <https://docs.python.org/3/library/textwrap.html>

## Usage

- `full.py` - Create Quotes in English with 140 to 200 words
- `single.py` - Create Quotes in English with Below 100 Words
- `short.py` - Generate Tamil Kavithai image Below 100 words
- `medium.py` - Generate Tamil Kavithai image Below 150 words
- `long.py` - Generate Tamil Kavithai image Below 200 words

**For More :** refer Python Pillow Module docs for advance usage  

```sh
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

**For Termux** Refer  - <https://stackoverflow.com/questions/62956054/how-to-install-pillow-on-termux>

```bash

pip install wheel

$ pkg install libjpeg-turbo

#If you are using aarch64

$ LDFLAGS="-L/system/lib64/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install Pillow

#If you are using an non aarch64 

$ LDFLAGS="-L/system/lib/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install Pillow

```

I use this Method to Create Quotes and Kavithai image for My Social Pages and Status  

![Hello](https://raw.githubusercontent.com/mskian/py-tamil-text/main/images/example.png)  

## LICENSE

MIT
