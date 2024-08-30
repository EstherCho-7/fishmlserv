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
$ uvicorn src.fishmlserv.main:app --host 0.0.0.0 --port 8949
```
