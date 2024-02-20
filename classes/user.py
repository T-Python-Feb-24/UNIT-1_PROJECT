from dataclasses import dataclass, field
from login import Login
from typing import Optional
import sys
from getpass import getpass


@dataclass()
class User:
    user_name: str
    user_type: bool = field(init=False, default=False)
    phone_number: Optional[str] = field(init=False, default=False)
    __password: Optional[str] = field(init=False)

    def __post_init__(self):
        try:
            if sys.argv[1] == "-a":
                self.__password = getpass(
                    f"Enter password for {self.user_name}: ")
                if Login().login(self.user_name, self.__password):
                    self.user_type = True
        except IndexError:
            pass


def main():
    print(sys.argv)
    u = User("wissam")
    if u.user_type:
        print(f"Login as {u.user_name} successful.")


if __name__ == '__main__':
    main()
