# mdadm alert twitter

## Usage
* Ubuntu16
* Python3

### Install
```
git clone git@github.com:RASBORA/mdadm-twitter-alert.git
echo PROGRAM "/app/contain/directory/mdadm_alert.py" >> /etc/mdadm/mdadm.conf
systemctl restart mdadm
```

### Create access token
```
./create_token.py
```

### Test 
```
./test.sh
```
