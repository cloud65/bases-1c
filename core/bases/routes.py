# pylint: disable=missing-function-docstring, unused-argument
"""
Routes
"""
from uuid import UUID

from fastapi import APIRouter, Query, Request, Response

from core.bases.bases import Infobases
from core.config import setting

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
    #headers = {'WWW-Authenticate': 'Basic'}
    #return Response(status_code=status.HTTP_401_UNAUTHORIZED, headers=headers)
    return result


@router.get('/GetInfoBases/')
async def get_infobases(
        request: Request,
        response: Response,
        client_id: UUID = Query(alias='ClientID'),
        check_code: UUID = Query(alias='InfoBasesCheckCode')

):
    response.headers["Cache-Control"] = "no-cache"
    ib = Infobases(request.client.host)
    result = {
        'root': {
            "ClientID": client_id,
            "InfoBasesCheckCode": check_code,
            'InfoBases': ib.get_list()
        }
    }
    return result
