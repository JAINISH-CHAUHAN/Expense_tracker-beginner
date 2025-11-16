import pytest
from httpx import AsyncClient
from typing import Optional, Literal

async def create_expense(
    amount: float, 
    category: Literal[
        "Groceries",
        "Leisure",
        "Electronics",
        "Utilities",
        "Clothing",
        "Health",
        "Others"
    ], 
    payment_method: Literal[
        "Cash",
        "UPI/Debit Card",
        "Credit Card"
    ],
    description: Optional[str],

    async_client : AsyncClient
):
        response = await async_client.post("/expense", json={
            "amount": amount,
            "category":category,
            "payment_method":payment_method,
            "description":description
        })
        return response.json()
        

@pytest.fixture()
async def created_expense(async_client:AsyncClient):
    return await create_expense(
    amount= 40,
    category="Leisure",
    payment_method="Cash",
    description="Pool and drinks"
)
    
@pytest.mark.anyio
async def test_create_expense(async_client: AsyncClient):
    amount= 40
    category="Leisure"
    payment_method="Cash"
    description="Pool and drinks"
    response = await async_client.post("/expense", json={
        "amount": amount,
        "category":category,
        "payment_method":payment_method,
        "description":description
    })
    assert response.status_code == 201
    assert {
        "id" : 0,
        "amount": amount,
        "category":category,
        "payment_method":payment_method,
        "description":description
    }.items() <= response.json().items()


@pytest.mark.anyio
async def test_create_post_missing_amount(async_client: AsyncClient):
    
    category="Leisure"
    payment_method="Cash"
    description="Pool and drinks"
    response = await async_client.post("/expense", json={
        "category":category,
        "payment_method":payment_method,
        "description":description
    })
    assert response.status_code == 422

@pytest.mark.anyio
async def test_create_expense_missing_category(async_client: AsyncClient):
    amount= 40
    payment_method="Cash"
    description="Pool and drinks"
    response = await async_client.post("/expense", json={
        "amount": amount,
        "payment_method":payment_method,
        "description":description
    })
    assert response.status_code == 422

@pytest.mark.anyio
async def test_create_expense_missing_payment_method(async_client: AsyncClient):
    amount= 40
    category="Leisure"
    description="Pool and drinks"
    response = await async_client.post("/expense", json={
        "amount": amount,
        "category":category,
        "description":description
    })
    assert response.status_code == 422

@pytest.mark.anyio
async def test_create_expense_missing_description(async_client: AsyncClient):
    amount= 40
    category="Leisure"
    payment_method="Cash"
    response = await async_client.post("/expense", json={
        "amount": amount,
        "category":category,
        "payment_method":payment_method
    })
    assert response.status_code == 201
