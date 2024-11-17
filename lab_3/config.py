PATH_RESULT = 'lab_3/result.json'
PATH_CSV = 'lab_3/68.csv'
VARIANT = 68
PATTERNS = {
    "telephone": r"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "height": r"^\d\.\d{2}$",
    "snils": r"^\d{11}$",
    "identifier": r"^\d{2}-\d{2}/\d{2}$",
    "occupation": r"^(?:[a-za-я]+(?:-|\b|\s))+$",
    "longitude": r"^-?(180(\.0*)*|1[0-7]\d(\.\d*)*|[1-9]*\d(\.\d*)*)$",
    "blood_type": r"^(?:AB|A|B|O)(?:\+|\u2212)$",
    "issn": r"^\d{4}-\d{4}$",
    "locale_code": r"^(?:\w{2}-\w{2}|\w{2})$",
    "date": r"^(?:19|20)\d{2}-(?:0[1-9]|1[012])-(?:0[1-9]|[12]\d|3[01])$"
}
 