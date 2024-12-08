import json

DATA_FILE = "books.json"

def load_books():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)

def add_book(books, title, author, category, year):
    book = {
        "title": title,
        "author": author,
        "category": category,
        "year": year
    }
    books.append(book)
    print(f"书籍《{title}》已添加！")

def view_books(books):
    if books:
        print("\n所有图书：")
        for idx, book in enumerate(books, 1):
            print(f"{idx}. 书名：{book['title']} | 作者：{book['author']} | 类别：{book['category']} | 出版年份：{book['year']}")
    else:
        print("没有任何图书记录。")

def search_books(books, keyword):
    search_results = [book for book in books if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower()]
    
    if search_results:
        print(f"\n搜索结果：")
        for idx, book in enumerate(search_results, 1):
            print(f"{idx}. 书名：{book['title']} | 作者：{book['author']} | 类别：{book['category']} | 出版年份：{book['year']}")
    else:
        print("没有找到相关图书。")

if __name__ == "__main__":
    books = load_books()
    print("欢迎使用图书管理系统！")

    while True:
        print("\n请选择一个操作：")
        print("1. 添加新图书")
        print("2. 查看所有图书")
        print("3. 搜索图书")
        print("4. 退出")

        choice = input("请输入选项（1/2/3/4）：")

        if choice == "1":
            title = input("请输入书名：")
            author = input("请输入作者：")
            category = input("请输入类别：")
            year = input("请输入出版年份：")
            add_book(books, title, author, category, year)
            save_books(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            keyword = input("请输入搜索关键词（书名或作者）：")
            search_books(books, keyword)
        elif choice == "4":
            print("感谢使用图书管理系统，再见！")
            break
        else:
            print("无效选项，请重新选择。")
