from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, asc, desc

from . import models, schemas


# CREATE
async def create_task(db: AsyncSession, task: schemas.TaskCreate):
    db_task = models.Task(title=task.title, status=task.status, owner_id=1)

    db.add(db_task)

    await db.commit()
    await db.refresh(db_task)

    return db_task


# READ ALL
async def get_tasks(
    db: AsyncSession,
    search: str = None,
    status: str = None,
    sort_by: str = "id",
    order: str = "asc",
    limit: int = 10,
    offset: int = 0,
):

    query = select(models.Task)

    if search:
        query = query.where(models.Task.title.ilike(f"%{search}%"))

    if status:
        query = query.where(models.Task.status == status)

    col = getattr(models.Task, sort_by, models.Task.id)

    query = query.order_by(desc(col) if order == "desc" else asc(col))

    query = query.offset(offset).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()


# READ ONE
async def get_task(db: AsyncSession, task_id: int):

    result = await db.execute(select(models.Task).where(models.Task.id == task_id))

    return result.scalar_one_or_none()


# UPDATE
async def update_task(db: AsyncSession, task_id: int, updated_task: schemas.TaskCreate):

    task = await get_task(db, task_id)

    if not task:
        return None

    task.title = updated_task.title
    task.status = updated_task.status

    await db.commit()
    await db.refresh(task)

    return task


# DELETE
async def delete_task(db: AsyncSession, task_id: int):

    task = await get_task(db, task_id)

    if not task:
        return None

    await db.delete(task)

    await db.commit()

    return task
