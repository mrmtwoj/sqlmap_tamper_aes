# SqlMap Tamper AES Encrypt 
## Install Pip For Python
``` bash
 pip install Padding
 pip install crypto
 pip install cryptography
```

## How Find AES KEY and VI in Android 
Use aes.js in Github my Project [aes_finder_method_two.js]
https://github.com/mrmtwoj/frida_list

## How Use sqlmap_tamper_aes
easy peasy 😎😎

## One
``` bash
sqlmap -r request.txt -p uid --tamper ~/Desktop/sqlmap_tamper_aes.py -- dbs
```
## Two
``` bash
sqlmap -u "http://example.com/index.php" -D "username,password" --tamper ~/Desktop/sqlmap_tamper_aes.py -- dbs
```

## Hint
If the file sqlmap_tamper_aes does not run, you can go to the following address and run the code

``` bash
cp sqlmap_tamper_aes.py /usr/share/sqlmap/tamper/
sqlmap -r request.txt -p uid --tamper sqlmap_tamper_aes -- dbs
```
## ❤🙌
You needed help again, send me a message
mr.mtwoj[at].gmail.com
