from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

class User:
    def __init__(self, user_id: int, name: str):
        self._user_id = user_id
        self._name = name
        self._created_at = datetime.now()
        self._last_login: Optional[datetime] = None
        
    @property
    def user_id(self) -> int:
        return self._user_id
        
    def rename(self, new_name: str) -> None:
        if not new_name.strip():
            raise ValueError("User name cannot be empty")
        self._name = new_name
        
    def record_login(self) -> None:
        self._last_login = datetime.now()
        
    def has_logged_in(self) -> bool:
        return self._last_login is not None

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        """Persists a user"""
        pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        """Finds a user by their identifier"""
        pass

    @abstractmethod
    def find_active_users(self) -> List[User]:
        """Retrieves users who have logged in"""
        pass

    @abstractmethod
    def remove(self, user: User) -> None:
        """Removes a user from the repository"""
        pass

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users = {}

    def save(self, user: User) -> None:
        self._users[user.user_id] = user

    def find_by_id(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)

    def find_active_users(self) -> List[User]:
        return [user for user in self._users.values() if user.has_logged_in()]

    def remove(self, user: User) -> None:
        if user.user_id in self._users:
            del self._users[user.user_id]

# Example usage
if __name__ == "__main__":
    repo = InMemoryUserRepository()
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")

    repo.save(user1)
    repo.save(user2)

    print(repo.find_active_users())  # Output: []
    user1.record_login()
    print(repo.find_active_users())  # Output: [<User object at ...>]
    print(repo.find_by_id(1))  # Output: <User object at ...>
    repo.remove(user1)
    print(repo.find_active_users())  # Output: []
