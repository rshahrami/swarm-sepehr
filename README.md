# swarm-sepehr


## monitoring
### grafana-promatheus

image repository address is in .env file. use typical .env file in docker compose. use below command for docker swarm. add --with-registry-auth option for use private regestry.
```
env $(cat .env | grep ^[A-Z] | xargs) docker stack deploy -c docker-compose-grafana-prometheus-swarm.yml <<stack_name>> --with-registry-auth
``` 

create network overly with below command for docker swarm and in docker compose not used.
```
docker networl create --attachable --driver overly monitoring
```

prometheus config file is below directory for docker compose 
```
monitoring/prometheus/compose/prometheus.yml
```

prometheus config file is below directory for docker swarm 
```
monitoring/prometheus/compose/prometheus.yml
```

using below link for dashboards:

[grafana_dashboard_cadvisor](https://grafana.com/grafana/dashboards/193-docker-monitoring/)

[grafana_dashboard_node-exporter](https://grafana.com/grafana/dashboards/193-docker-monitoring/)