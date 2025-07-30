import pandas as pd
from app.models import Bank, Branch
from app.database import SessionLocal, init_db

init_db()
db = SessionLocal()

df = pd.read_csv("bank_branches.csv")

df = df.dropna(subset=["ifsc", "branch", "bank_id", "bank_name"])


for bank_id, name in df[['bank_id', 'bank_name']].drop_duplicates().values:
    db.merge(Bank(id=int(bank_id), name=name))
db.commit()


for _, row in df.iterrows():
    db.merge(Branch(
        ifsc=row['ifsc'],
        branch=row['branch'],
        address=row['address'],
        city=row['city'],
        district=row['district'],
        state=row['state'],
        bank_id=int(row['bank_id'])
    ))
db.commit()
db.close()
