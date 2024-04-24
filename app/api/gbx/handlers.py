from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, UploadFile

from app.api.gbx.schemas import UploadFileResponse
from app.dependencies.webapp import WebAppContainer
from app.use_cases.gbx.load_file import LoadRunUseCase

router = APIRouter()


@router.post("/gbx")
@inject
async def load_gbx(
    file: UploadFile,
    use_case: LoadRunUseCase = Depends(Provide[WebAppContainer.load_gbx_file_use_case]),
) -> UploadFileResponse:
    result = await use_case(file=file)
    return result
