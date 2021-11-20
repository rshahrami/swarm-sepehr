FROM nginx:1.20.0

RUN rm /etc/nginx/conf.d/default.conf
ADD your_pem_ssl.pem /root
ADD your_cert_ssl.crt /root
# EXPOSE 80

# CMD ["nginx", "-g", "daemon off;"]