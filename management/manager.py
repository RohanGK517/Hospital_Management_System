from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations=True


    def create_user(self,username,password=None,**extra_fields):
        user=self.model(username=username)
        user.set_password(password)
        user.save(user=self._db)
        return user