## Run Locally

```bash
git clone <your-repo>
cd bank_api
python -m venv venv
venv\Scripts\activate       
pip install -r requirements.txt
python -m app.seed          
uvicorn app.main:app --reload

CTRL+C  #(to stop the server)#
```