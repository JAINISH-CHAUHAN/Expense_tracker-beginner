from fastapi import APIRouter
from exptracker_api.models.expense import Expense,ExpenseIn

router = APIRouter()

expense_table = {}




@router.post('/expense', response_model=Expense, status_code=201)
async def create_expense(expense : ExpenseIn):
    last_record_id = len(expense_table)
    data = expense.model_dump()
    new_expense = {**data, "id":last_record_id}
    expense_table[last_record_id] = new_expense
    return new_expense


