from collections import UserDict

from .record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def show_all(self, book):
        for name, record in book.data.items():
            print(record)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
