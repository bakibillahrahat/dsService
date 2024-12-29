from typing import Optional
from langchain_mistralai import ChatMistralAI
from langchain_core.pydantic_v1 import BaseModel, Field

class Expense(BaseModel):
    amount: Optional[str] = Field(title="expense", description= "Expense made in the transaction")
    merchant: Optional[str] = Field(title="merchant", description= "Marchant name of the transaction has been made")
    currency: Optional[str] = Field(title="currency", description= "Currency of the transaction")
