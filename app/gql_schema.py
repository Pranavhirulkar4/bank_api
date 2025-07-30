import strawberry
from typing import List, Optional
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Branch as BranchModel, Bank as BankModel


@strawberry.type
class Bank:
    id: int
    name: str

@strawberry.type
class Branch:
    ifsc: str
    branch: Optional[str]
    address: Optional[str]
    city: Optional[str]
    district: Optional[str]
    state: Optional[str]
    bank: Bank

# 🔹 Relay-style edge wrapper
@strawberry.type
class BranchEdge:
    node: Branch

@strawberry.type
class BranchConnection:
    edges: List[BranchEdge]

# 🔧 Query
@strawberry.type
class Query:
    @strawberry.field
    def branches(
        self,
        city: Optional[str] = None,
        state: Optional[str] = None,
        district: Optional[str] = None,
        bankName: Optional[str] = None,
        ifscStartsWith: Optional[str] = None,
        branch: Optional[str] = None,
        addressContains: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> BranchConnection:
        db: Session = SessionLocal()
        query = db.query(BranchModel).join(BankModel)

        # Filters
        if city:
            query = query.filter(BranchModel.city.ilike(f"%{city}%"))
        if state:
            query = query.filter(BranchModel.state.ilike(f"%{state}%"))
        if district:
            query = query.filter(BranchModel.district.ilike(f"%{district}%"))
        if bankName:
            query = query.filter(BankModel.name.ilike(f"%{bankName}%"))
        if ifscStartsWith:
            query = query.filter(BranchModel.ifsc.ilike(f"{ifscStartsWith}%"))
        if branch:
            query = query.filter(BranchModel.branch.ilike(f"%{branch}%"))
        if addressContains:
            query = query.filter(BranchModel.address.ilike(f"%{addressContains}%"))

        # Pagination
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)

        results = query.all()

        # Wrap in edges
        edges = [
            BranchEdge(node=Branch(
                ifsc=b.ifsc,
                branch=b.branch,
                address=b.address,
                city=b.city,
                district=b.district,
                state=b.state,
                bank=Bank(id=b.bank.id, name=b.bank.name)
            )) for b in results
        ]

        return BranchConnection(edges=edges)

# 📦 Final schema
schema = strawberry.Schema(Query)
