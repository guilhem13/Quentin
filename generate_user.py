from app.user.domain.entities.user import User
from app.user.services.user_service import  create_new_user, filter_role_and_email


user_dummy = User(last_name="test", first_name="test", phone="test", address="test",email="test",couple="test",enfants="test",allergies="test",regime="test", commentaires="test", gphoto="test")
create_new_user(
        user=user_dummy, 
        last_name="test",
        first_name="test",
        phone="test",
        address="test",
        email="test",
        couple="test",
        enfants="test",
        allergies="test",
        regime="test",
        commentaires="test",
        gphoto="test"
    )
"""user_dummy = User(role="admin", fullname="Dummy",email="Dummy@mail.com", username="userdummy", password="dummy")


user_exists = filter_role_and_email(user=user_dummy, email="admin67@gmail.com", role="")
if not user_exists:
    create_new_user(
        user=user_dummy, 
        fullname="Super Admin",
        email="admin67@gmail.com",
        username="admin",
        password="admin123",
        role="admin"
    )"""