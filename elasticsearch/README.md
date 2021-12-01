<div dir=”rtl”>

# مقدمه
  
برای اجرای elasticsearch، نیازمند چند دستور ابتدایی در ماشین‌ها هستیم. برای تنظیمات ssl، به پوشه ssl در همین مسیر مراجعه کنید. 

--------------------------------------------------------

# تنظیمات VM

با استفاده از دستور زیر، مقدار max_map را افزایش می‌دهیم.

```bash
  
sudo sysctl -w vm.max_map_count=262144
  
```

برای افزایش توانایی elasticsearch در بهره برداری از memory، با استفاده از دستورات زیر، swap را حذف می‌کنیم.

```bash
  
sudo swapoff /dev/mapper/centos-swap 

sudo swapoff -a
  
```
سپس وارد مسیر /ect/fstab شده و swap رو به صورت comment قرار می‌دهیم.
  
  
--------------------------------------------------------
# تنظیمات elasticsearch
در این قسمت، تنظیمات درونی مربوط به elasticsearch، بیان شده است.
## bootstrap.memory_lock

این گزینه به صورت پیش فرض در حالت false قرار دارد. در این حالت، اجرای container ها به صورت docker-compose و swarm بدون مشکل می باشد. در صورتی که این گزینه به صورت true قرار گیرد، اجرا container در هر دو صورت، به مشکل می‌انجامد. در حالتی که از دستور docker-compose استفاده می‌کنیم، برای رفع این مشکل، موارد زیر را به compose file خود اضافه می‌کنیم. توجه داریم که این موارد به صورت پیش فرض نیس در فایل اصلی شرکت elasticsearch، وجود دارد و نیازی به صورت دستی نمی‌باشد.

```docker
  
ulimits:
  memlock:
    soft: -1
    hard: -1
  
```

در حالت swarm، موارد بالا به صورت ignore  قرار می‌گید. Ignore در swarm به این معنی می‌باشد که موارد تعیین شده در compose file، در حالت swarm نادیده گرفته می‌شود و تا ثیری در اجرای container ندارد. برای حل این مشکل، باید وارد مسیر /usr/lib/systemd/system/ شده و سرویس docker.service را ویرایش می‌کنیم. با استفاده از یک ویرایشگر، موارد زیر را تغییر می‌دهیم. خط پایین به  صورت پیش فرض قرار داد. --default-ulimit memlock=-1:-1 را اضافه می‌کنیم.


```bash
  
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
  
```

خط نهایی به صورت زیر می‌شود.

```bash
  
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock --default-ulimit memlock=-1:-1
  
```

با دستور زیر، سرویس را reload می‌کنیم.

```bash
  
sudo systemctl daemon-reload
  
sudo systemctl restart docker.service
  
```
 
 # منابع
 در این قسمت منابع مورد استفاده برای ایجاد ssl، بیان شده است.
 
- [youtube](https://www.youtube.com/watch?v=Y4v1Rqopz6s)
- [github](https://github.com/linuxxstart/docker-cluster-elastic)
</div>
