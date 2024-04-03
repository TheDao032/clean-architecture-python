from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from internal.api.deps import get_db
from internal.domain.dtos.dumpuser import DumpUserCreate, DumpUserGet, DumpUserResponse
from internal.domain.entities.dumpuser import DumpUser

from internal.infrastructure.persistent.dumpuser.command_repository import (
    DumpUserCommandRepository as dumpusercommandrepo
)
from internal.infrastructure.persistent.dumpuser.query_repository import (
    DumpUserQueryRepository as dumpuserqueryrepo
)


router = APIRouter()


@router.post("", status_code=status.HTTP_200_OK, response_model=DumpUserResponse)
async def create_user(
    *,
    user_in: DumpUserCreate,
    db: Session = Depends(get_db),
) -> DumpUserResponse:
    """
        Get a specific user by id
    """

    user_input_db = DumpUser(**user_in.__dict__)
    commandrepo = dumpusercommandrepo()
    user_db_output = commandrepo.create_user(db=db, obj_in=user_input_db)
    # convert_output_dict = user_db_output.__dict__
    dumpuser_output = DumpUserGet(
        userId=user_db_output.userId,
        name=user_db_output.name,
        phone=user_db_output.phone,
        isActivate=user_db_output.isActivate
    )

    return DumpUserResponse(
        code=status.HTTP_200_OK,
        message="",
        data=dumpuser_output
    )
