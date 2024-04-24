from app.utils.models import ApiCamelModel


class UploadFileResponse(ApiCamelModel):
    map_uid: str
    map_name: str
    nick_name: str
    race_time: str
    respawns: int
    cp_times: list
