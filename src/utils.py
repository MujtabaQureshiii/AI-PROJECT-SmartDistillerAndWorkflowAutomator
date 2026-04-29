from config import GOOGLE_SERVICE_ACCOUNT_JSON, EMAIL_SENDER

def sheets_configured():
    return bool(GOOGLE_SERVICE_ACCOUNT_JSON.strip())

def email_configured():
    return bool(EMAIL_SENDER.strip())
