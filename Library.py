class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
    
    def __del__(self):
        self.file.close()
    
    def list_books(self):
        self.file.seek(0)  
        lines = self.file.read().splitlines()
        for line in lines:
            parts = line.split(',')
            # Kitap adı, yazarı ve ek olarak bir kitaptan kaç adet olduğunu yazdırdım.
            print(f"{parts[0]}, {parts[1]}, Quantity: {parts[4]}")
            
    
    def add_book(self):
        title = input("Enter the title of the book: ").upper()
        author = input("Enter the author of the book: ").upper()
        release_year = input("Enter the release year of the book: ")
        num_pages = input("Enter the number of pages of the book: ")
        
        book_found = False
        #Eğer aynı kitap tekrar girildiyse o kitabın listede yada books.txt dosyasında yeniden görünmesini istemedim.
        #O yüzden aynı kitabın eklendiğinin gözükmesi için adet miktarını eklettirdim.
        self.file.seek(0)
        lines = self.file.readlines()
        new_lines = []
        for line in lines:
            if title.lower() in line.lower():
                book_found = True
                parts = line.strip().split(',')
                parts[4] = str(int(parts[4]) + 1)  # Adet bilgisini bir arttırmak için
                line = ','.join(parts) + '\n'
            new_lines.append(line)
        
        if not book_found:
            book_informatıon = f"{title},{author},{release_year},{num_pages},1\n"
            self.file.write(book_informatıon)
        
        else:
            self.file.seek(0)
            self.file.truncate()  
            self.file.writelines(new_lines)

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ").upper()
        self.file.seek(0)
        lines = self.file.readlines()
        new_books = []
        for line in lines:
            if title_to_remove in line.upper():
                parts = line.strip().split(',')
                if int(parts[4]) > 1:                  # Eğer Bir kitaptan birden fazla varsa  
                    parts[4] = str(int(parts[4]) - 1)  # Adet bilgisini bir azaltma
                    line = ','.join(parts) + '\n'
                else:
                    continue  # Eğer sadece bir adet varsa satırı silme
            new_books.append(line)
        #Birden fazla aynı kitaptan varsa silme işlemi yapmak istediğimde adet sayısını bir düşürmek istedim.
        #Yani bir kitap silindi o yüzden 1 adet azaldı mantığıyla ilerledim.     
        self.file.seek(0)
        self.file.truncate()  
        self.file.writelines(new_books)

lib = Library()

while True:
    print("\n*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book\nq) Exit")
    
    choice = input("Please enter your choice: ")
    
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "q":
        del lib  
        break
    else:
        print("Invalid choice. Please enter a valid option.")

