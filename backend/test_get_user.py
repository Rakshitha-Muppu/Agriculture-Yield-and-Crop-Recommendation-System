from services.user_service import get_user_by_email

user = get_user_by_email("testuser@gmail.com")

print(user)