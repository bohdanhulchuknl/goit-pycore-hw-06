from collections import UserDict
import re
from typing import List, Optional

class Field:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value: str) -> None:
        if not re.fullmatch(r'\d{10}', value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: List[Phone] = []

    def add_phone(self, phone: str) -> None:
        """Add a phone number to the record."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        """Remove a phone number from the record."""
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Edit an existing phone number in the record."""
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone: str) -> Optional[Phone]:
        """Find a phone number in the record."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        """Add a record to the address book."""
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        """Find a record by name in the address book."""
        return self.data.get(name, None)

    def delete(self, name: str) -> None:
        """Delete a record by name from the address book."""
        if name in self.data:
            del self.data[name]

# Приклад використання
if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    book.delete("Jane")