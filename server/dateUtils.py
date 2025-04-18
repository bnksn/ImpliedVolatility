from datetime import datetime
import constants


def convertMaturityToDays(maturity: str) -> int:
    as_datetime = datetime.strptime(maturity, constants.yfinanceMaturityFormat)
    return (as_datetime - datetime.now()).days
