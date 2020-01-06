# mdadm alert twitter

## Usage
* Ubuntu16
* Python3

### Install
```
git clone git@github.com:RASBORA/mdadm-twitter-alert.git
pip install -r mdadm-twitter-alert/requirements.txt
echo PROGRAM "/app/contain/directory/mdadm_alert.py" >> /etc/mdadm/mdadm.conf
systemctl restart mdadm
```

### Create access token
```
./create_token.py
```

### Test 
```
mdadm --monitor --scan --oneshot --test
```

## Blog entry
[mdadmの警告をTwitterに通知する](http://blog.ivy-box.net/mdadm-twitter-alert/)
