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
$ sudo docker run -d --name fmlserv-042 -p 8877:8765 fishmlserv:0.4.2  # Run Docker
$ sudo docker ps   # Check Container

# Into Docker Container
$ sudo docker exec -it fml043 bash
```

### Fly.io
```bash
# Launch
$ flyctl launch --name esther-fishmlserv

# Deploy
$ flyctl deploy
```

### Ref
- https://curlconverter.com/python
