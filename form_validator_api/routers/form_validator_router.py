from datetime import datetime, date
from typing import Optional
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse
from phonenumbers import (
    NumberParseException,
    PhoneNumberFormat,
    PhoneNumberType,
    format_number,
    is_valid_number,
    number_type,
    parse as parse_phone_number,
)
from pydantic import BaseModel, EmailStr, constr, model_validator, validator
import json
from tinydb import TinyDB, Query
import re

from form_validator_api.services.form_validate import form_validate_op


router = APIRouter()


@router.post('/get_form')
async def add_game_router(request: Request):
    params = request.query_params
    form = dict(params)
    result = await form_validate_op(form)
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="form is empty")
    return result
 