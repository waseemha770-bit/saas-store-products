import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# الصلاحيات التي نريدها (قراءة وتعديل الشيتس، وقراءة وتعديل الدرايف)
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file'
]

def main():
    creds = None
    # التحقق مما إذا كان لدينا ملف token.json مسبقاً
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # إذا لم يكن هناك صلاحيات، أو كانت منتهية، نطلب من المستخدم تسجيل الدخول
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # هنا سيستخدم ملف credentials.json الذي قمت بتجهيزه
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            # سيفتح المتصفح ليطلب منك الموافقة
            creds = flow.run_local_server(port=0)
        
        # حفظ الصلاحيات في ملف token.json لاستخدامه لاحقاً في المشروع
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())
            print("\n✅ تم بنجاح! تم إنشاء ملف token.json")
            print("الآن يمكننا استخدام هذا الملف في تطبيق Flask للاتصال بخدمات جوجل.")

if __name__ == '__main__':
    main()
