<div dir=”rtl”>

# مقدمه

# ایجاد venv
  
در مسیر مورد نظر، با استفاده از دستور زیر، یک venv ایجاد می کنیم. به جای کلمه venv_name، می توانیم نام دلخواه خود را قرار دهیم
  
```bash
  
python -m venv venv_name
  
```

با استفاده از دستور زیر، venv را فعال می‌کنیم. این دستور برای محیط لینوکسی می‌باشد.  
  

```bash
  
source path/to/directory/venv_name/bin/activate
  
```

با استفاده از دستور زیر، package های مورد نیاز برای اتصال را، نصب می‌کنیم.
  
```bash
pip install --upgrade pip  
pip install -r requrement
  
```  
در اینجا برای kafka producer، یک image ایجاد شده است. برای هر یک از موارد، می‌توان image جداگانه ای را ایجاد کرد.
# docker
با استفاده از Dockerfile، می‌توانیم image برای هر کدام از قابلیت ها، ایجاد کنیم. با استفاده از دستور زیر، image مورد نظر را ایجاد می‌کنیم. به جای کلمه image_tag:v1، می‌توان هر کلمه ی دیگری را قرار داد

```docker
  
docker build -t image_tag:v1 .
  
```

## image base:
python:3.6-alpine
  
- [x] kafka producer!
- [x] kafka consumer!
- [x] kafka topic!
- [x] send data with key value!
  
- [ ] get offset per partition!

</div>
