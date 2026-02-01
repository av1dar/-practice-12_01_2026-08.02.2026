from abc import ABC, abstractmethod
import datetime

# 1.АБСТРАКЦІЯ

class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self._is_available = True 

    @abstractmethod
    def get_loan_period(self):
        pass
    def checkout(self):
        if self._is_available:
            self._is_available = False
            return True
        return False
    def return_item(self):
        self._is_available = True

    def __str__(self):
        status = "Доступно" if self._is_available else "Видано"
        return f"[{self.item_id}] {self.title} ({status})"
    
# 2.СПАДКУВАННЯ ТА ПОЛІМОРФІЗМ

class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
    def get_loan_period(self):
        return 14
    def __str__(self):
        return f"Книга: {super().__str__()} | Автор: {self.author}"
class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue):
        super().__init__(title, item_id)
        self.issue = issue
    def get_loan_period(self):
        return 7
    def __str__(self):
        return f"🗞 Журнал: {super().__str__()} | Випуск №{self.issue}"
    
# 3. КЛАС ЧИТАЧА (Actor)

class Reader:
    def __init__(self, name, ticket_id):
        self.name = name
        self.__ticket_id = ticket_id 
        self.borrowed_items = []

    def get_ticket_id(self):
        return self.__ticket_id

    def show_items(self):
        print(f"\n Читач {self.name} має на руках:")
        if not self.borrowed_items:
            print("   (пусто)")
        else:
            for item in self.borrowed_items:
                days = item.get_loan_period()
                due_date = datetime.date.today() + datetime.timedelta(days=days)
                print(f"   - {item.title} (Повернути до: {due_date})")

# 4. СИСТЕМА (Взаємодія об'єктів)

class Library:
    def __init__(self):
        self.catalog = []

    def add_item(self, item):
        self.catalog.append(item)

    def lend_item(self, reader, item_id):
        target_item = None
        for item in self.catalog:
            if item.item_id == item_id:
                target_item = item
                break
        
        if target_item:
            if target_item.checkout():
                reader.borrowed_items.append(target_item)
                print(f"Успіх! {reader.name} взяв '{target_item.title}'.")
            else:
                print(f"Халепа: '{target_item.title}' зараз недоступна.")
        else:
            print(f"Похибка: Предмет з ID {item_id} не знайдено.")

    def show_catalog(self):
        print("\n--- Каталог Бібліотеки ---")
        for item in self.catalog:
            print(item)
        print("-" * 30)
city_library = Library()

city_library.add_item(Book("Гаррі Поттер", "B01", "Дж. Роулінг"))
city_library.add_item(Book("Кобзар", "B02", "Т. Шевченко"))
city_library.add_item(Magazine("National Geographic", "M01", 105))

student = Reader("Данило", "Ticket-777")
city_library.show_catalog()
city_library.lend_item(student, "B01")
city_library.lend_item(student, "M01")
city_library.lend_item(student, "B01")
student.show_items()
city_library.show_catalog()