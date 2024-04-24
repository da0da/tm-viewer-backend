import datetime
import io
from tempfile import NamedTemporaryFile
from time import gmtime, strftime

from fastapi import HTTPException, UploadFile
from pygbx import (CGameChallenge, CGameCtnGhost, CGameReplayRecord, Gbx,
                   GbxType)

from app.api.gbx.schemas import UploadFileResponse
from app.utils.time import time_to_str


class LoadRunUseCase:
    async def __call__(self, file: UploadFile) -> UploadFileResponse:
        with NamedTemporaryFile() as tmp_file:
            tmp_file.write(file.file.read())
            tmp_file.seek(0)
            gbx = Gbx(tmp_file.name)

        ghost: CGameCtnGhost = gbx.get_class_by_id(GbxType.CTN_GHOST)
        replay: CGameReplayRecord = gbx.get_class_by_id(GbxType.REPLAY_RECORD)
        challenge: CGameChallenge = replay.track.get_class_by_id(GbxType.CHALLENGE)

        race_time = time_to_str(ghost.race_time)

        cp_times = []
        for cp_time in ghost.cp_times:
            cp_times.append(time_to_str(cp_time))

        return UploadFileResponse(
            map_uid=ghost.uid,
            map_name=challenge.map_name,
            nick_name=replay.nickname,
            race_time=race_time,
            respawns=ghost.num_respawns,
            cp_times=cp_times,
        )
