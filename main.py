import flet as ft
import dbh # currently redundant
import mysql.connector # currently redundant

sql_server = dbh.db_server()
sql_username = dbh.db_username()
sql_password = dbh.db_password()
sql_db = dbh.db_name()

# Connect to the SQL database (currently redundant)
def connect_database():
    conn = mysql.connector.connect(user=sql_username,
                                   password=sql_password,
                                   host=sql_server,
                                   database=sql_db
                                   )
    c = conn.cursor()
    return conn, c

# Create a table called users (currently redundant)
def create_users_table():
    conn, c = connect_database()
    c.execute("CREATE TABLE users (id int(11) NOT NULL AUTO_INCREMENT, username VARCHAR(50) UNIQUE, email VARCHAR(50) UNIQUE, password VARCHAR(300), PRIMARY KEY(id))")
    conn.commit()
    c.close()

# App Function
def main(page: ft.Page):
    page.title = "Login Page"
    page.window_width = 600
    page.window_height = 800

    headder = ft.Container(
        padding = ft.padding.only(top=40),
        content=(
            ft.Divider(color="white")
        ), expand=False
    )

    username_text_input = ft.Container(
        padding = ft.padding.symmetric(horizontal=40),
        content=(
            ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                    controls=[ft.TextField(width=page.window_width/1.5, expand=True, label="Username / Email")]
                    )
        )
    )

    password_text_input = ft.Container(
        padding = ft.padding.symmetric(horizontal=40),
        content =(
            ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                controls=[ft.TextField(width=page.window_width/2, expand=True, label="Password", password=True)]
            )

        )
    )

    sign_in_button = ft.Container(
        padding = ft.padding.only(right=40),
        content = (
            ft.Row(alignment=ft.MainAxisAlignment.END,
            controls=[ft.OutlinedButton("Sign In", icon="login", style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)))]
            )
        )
    )

    divider = ft.Container(
        padding = ft.padding.only(top=400),
        content=(
            ft.Divider(color="white")
        ), expand=True
    )

    sign_in_page_footer = ft.Container(
        padding = ft.padding.only(left=40, top=0, right=40, bottom=40),
        content = (
    
            ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(
                        controls=[
                            ft.OutlinedButton("Forgot Password", icon="lock_reset", style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)))
                        ]
                    ),
                    ft.Column(
                        controls=[
                            ft.OutlinedButton("Register", icon="account_circle", style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)))
                        ]
                    )
                ]
            )
        )
    )

    page.add(headder, username_text_input, password_text_input, sign_in_button, divider, sign_in_page_footer)


ft.app(target=main)
