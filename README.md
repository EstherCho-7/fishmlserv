# fishmlserv

### Deploy
![deploy_image](https://github.com/user-attachments/assets/ea46447a-0c40-42fa-843d-519b9ca2b013)

### Run
- dev
```bash
# uvicorn --help
$ uvicorn src.fishmlserv.main:app --reload
```

- prd
```bash
$ uvicorn src.fishmlserv.main:app --host 0.0.0.0 --port 8765 
```

### Docker
```bash
$ sudo docker images   # Check images
$ sudo docker build -t fishmlserv:0.4.X .   # build image
$ sudo docker run -d --name fmlserv-042 -p 8877:8765 fishmlserv:0.4.2  # Run Docker
$ sudo docker ps   # Check Container

# Into Docker Container
$ sudo docker exec -it fml043 bash

# exit
$ exit

# log 확인
$ sudo docker logs -f <container ID | Name>
```

### Command
```bash
# get model path
$ sudo docker exec -it f084 get-model-path

# prediction by fire
$ sudo docker exec -it f084 prediction-f -l <length> -w <weight>

# prediction by typer
$ sudo docker exec -it f084 prediction-t -l <length> -w <weight>
```

#### prediction_help
```bash
# for typer
$ prediction-t --help
```
![typer_help](https://github.com/user-attachments/assets/f7e703cb-ba50-43ac-9fff-0d4a71db8354)


```bash
# for fire
$ prediction-f --help
```
![fire_help](https://github.com/user-attachments/assets/d149e90c-810a-4678-847f-4c65e718e3a8)



### Fly.io
```bash
# Launch
$ flyctl launch --name esther-fishmlserv

# Deploy
$ flyctl deploy
```

### Ref
- https://curlconverter.com/python
