from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextBrowser, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QDialog, QHBoxLayout, QMessageBox, QStackedWidget, QApplication
)
from PySide6.QtGui import QPixmap
import requests
import os
import json

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(850, 500)

        background_image = QLabel(self)
        background_image.setGeometry(0, 0, 850, 500)
        background_image.setPixmap(QPixmap(os.path.expanduser("../assets/landing.jpg")))
        background_image.setScaledContents(True)
        background_image.setStyleSheet("background: transparent;")

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 280, 40)

        label1 = QLabel("Enter the Pokémon name", self)
        label1.setGeometry(50, 5, 600, 70)
        label1.setStyleSheet("color: white;")

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)

        self.info_browser = QTextBrowser(self)
        self.info_browser.setGeometry(350, 50, 450, 300)
        self.info_browser.setStyleSheet("color: white; background: transparent;")

        self.image_view = QGraphicsView(self)
        self.image_view.setGeometry(350, 350, 150, 150)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)

        enter_button.clicked.connect(self.search_pokemon)
        capture_button.clicked.connect(self.capture_pokemon)
        display_button.clicked.connect(self.display_pokemon)

        self.captured_pokemon_info = []

        self.load_captured_images()

    def search_pokemon(self):
        pokemon_name = self.textbox.text().lower()
        api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
        response = requests.get(api_url)

        if response.status_code == 200:
            pokemon_data = response.json()
            name = pokemon_data['name'].capitalize()
            abilities = " ".join([ability['ability']['name'].title() for ability in pokemon_data['abilities']])
            types = " ".join([type_info['type']['name'].capitalize() for type_info in pokemon_data['types']])
            stats = "\n".join([f"{stat['stat']['name'].title()}: {stat['base_stat']}" for stat in pokemon_data['stats']])

            pokemon_info = f"Name: {name}\nAbilities: {abilities}\nTypes: {types}\nStats:\n{stats}"
            self.info_browser.setPlainText(pokemon_info)

            image_url = pokemon_data['sprites']['front_default']
            pixmap = self.download_image(image_url)  
            if pixmap:
                scene = QGraphicsScene()
                item = QGraphicsPixmapItem(pixmap)
                scene.addItem(item)
                self.image_view.setScene(scene)
        else:
            self.info_browser.setPlainText("Pokémon not found")

    def capture_pokemon(self):
        if self.info_browser.toPlainText() != "Pokémon not found":
            pokemon_name = self.textbox.text().lower()
            api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
            response = requests.get(api_url)

            if response.status_code == 200:
                pokemon_data = response.json()
                image_url = pokemon_data['sprites']['front_default']
                pixmap = self.download_image(image_url, save=True) 
                if pixmap:
                    self.captured_pokemon_info.append((pokemon_name.capitalize(), pixmap))
                    QMessageBox.information(self,"Capture Success","Pokémon successfully captured!")


    def next_pokemon(self):
        self.stacked_widget.setCurrentIndex((self.stacked_widget.currentIndex() + 1) % len(self.captured_pokemon_info))

    def prev_pokemon(self):
        self.stacked_widget.setCurrentIndex((self.stacked_widget.currentIndex() - 1) % len(self.captured_pokemon_info))


    def display_pokemon(self):
        if self.captured_pokemon_info:
            display_dialog = QDialog(self)
            display_dialog.setWindowTitle("Captured Pokémon")

            layout = QVBoxLayout()
            self.stacked_widget = QStackedWidget()

            for i, (pokemon_name, pixmap) in enumerate(self.captured_pokemon_info):
                pokemon_widget = QWidget()
                layout_inner = QVBoxLayout()

                label_name = QLabel(f"Name: {pokemon_name}")
                layout_inner.addWidget(label_name)

                if pixmap:
                    scene = QGraphicsScene()
                    item = QGraphicsPixmapItem(pixmap)
                    scene.addItem(item)
                    image_view = QGraphicsView()
                    image_view.setScene(scene)
                    layout_inner.addWidget(image_view)

                pokemon_widget.setLayout(layout_inner)
                self.stacked_widget.addWidget(pokemon_widget)

            layout.addWidget(self.stacked_widget)

            button_layout = QHBoxLayout()
            next_button = QPushButton("Next >")
            prev_button = QPushButton("< Previous")
            next_button.clicked.connect(self.next_pokemon)
            prev_button.clicked.connect(self.prev_pokemon)            
            button_layout.addWidget(prev_button)
            button_layout.addWidget(next_button)

            layout.addLayout(button_layout)
            display_dialog.setLayout(layout)

            display_dialog.exec()

    def download_image(self, image_url, save=False):  
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = response.content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)

            if save:
                save_directory = "pokemon_images/"
                os.makedirs(save_directory, exist_ok=True)
                filename = os.path.join(save_directory, f"{self.textbox.text().lower()}.png")
                pixmap.save(filename)

            return pixmap
        return None

    def load_captured_images(self):
        image_directory = "pokemon_images/"
        if os.path.exists(image_directory):
            for filename in os.listdir(image_directory):
                if filename.endswith(".png"):
                    filepath = os.path.join(image_directory, filename)
                    pixmap = QPixmap(filepath)
                    self.captured_pokemon_info.append((filename.split('.')[0].capitalize(), pixmap))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
