# pylint: disable=missing-function-docstring, unused-argument
"""
Routes
"""
from uuid import UUID

from fastapi import APIRouter, Query, Request, Response

from core.bases.bases import Infobases
from core.config import logger, setting

router = APIRouter(prefix=f'{setting.prefix}/WebCommonInfoBases')


@router.head('')
async def get_head(response: Response):
    response.headers["Cache-Control"] = "no-cache"
    return None


@router.get('/CheckInfoBases/')
async def check_infobases(
        request: Request,
        response: Response,
        client_id: UUID = Query(alias='ClientID'),
        check_code: UUID = Query(alias='InfoBasesCheckCode')
):
    response.headers["Cache-Control"] = "no-cache"
    result = {'root': {"InfoBasesChanged": True, 'URL': request.base_url}}
    return result


@router.get('/GetInfoBases/')
async def get_infobases(
        request: Request,
        response: Response,
        client_id: UUID = Query(alias='ClientID'),
        check_code: UUID = Query(alias='InfoBasesCheckCode')

):
    response.headers["Cache-Control"] = "no-cache"
    ib = Infobases()
    result = {
        'root': {
            "ClientID": client_id,
            "InfoBasesCheckCode": check_code,
            'InfoBases': ib.get_list(request.client.host)
        }
    }
    logger.info('GetInfoBases')
    return result
