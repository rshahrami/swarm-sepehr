<div dir=”rtl”>

# مقدمه


# kibana.yml

این فایل شامل تنظیمات درونی kibana می باشد. این تنظیمات شامل آدرس اتصال به elasticsearch و نام کاربری و کلمه ی عبور آن، می‌باشد.


# docker-compose

فایل kibana.yml را به صورت یک volume در مسیر /usr/share/kibana/config/ قرار می‌دهیم. با استفاده از یک dockerfile می‌توان فایل را در مسیر مورد نظر قرار داد.

## environment

برای اینکه مسیر url در kibana، یک مسیر مشخصی باشد، می‌توان خط SERVER_BASEPATH را پیکربندی کرد.


</div>
