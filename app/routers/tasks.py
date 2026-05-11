from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from ..database import get_db
from .. import schemas, crud

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# CREATE
@router.post("/", response_model=schemas.Task)
async def create_task(task: schemas.TaskCreate, db: AsyncSession = Depends(get_db)):

    return await crud.create_task(db, task)


# READ ALL
@router.get("/")
async def read_tasks(
    db: AsyncSession = Depends(get_db),
    search: Optional[str] = None,
    status: Optional[str] = None,
    sort_by: str = "id",
    order: str = "asc",
    limit: int = 10,
    offset: int = 0,
):

    return await crud.get_tasks(db, search, status, sort_by, order, limit, offset)


# READ ONE
@router.get("/{task_id}")
async def read_task(task_id: int, db: AsyncSession = Depends(get_db)):

    task = await crud.get_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# UPDATE
@router.put("/{task_id}")
async def update_task(
    task_id: int, updated_task: schemas.TaskCreate, db: AsyncSession = Depends(get_db)
):

    task = await crud.update_task(db, task_id, updated_task)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# DELETE
@router.delete("/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):

    task = await crud.delete_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}
