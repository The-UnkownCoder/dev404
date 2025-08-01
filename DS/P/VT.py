import sys
import os
import pygame
import speech_recognition as sr
from gtts import gTTS
from deep_translator import GoogleTranslator

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton,
    QTextEdit, QComboBox, QMessageBox, QFileDialog, QHBoxLayout, QCheckBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont


class VoiceTranslator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎙️ Voice Translator")
        self.setGeometry(100, 100, 900, 700)
        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.languages = ["english", "spanish", "french", "german", "hindi", "italian"]
        self.dst_lang = "german"

        self.dark_mode = False

        self.init_ui()
        pygame.mixer.init()

    def init_ui(self):
        layout = QVBoxLayout()

        self.header = QLabel("🎙️ Voice Translator")
        self.header.setStyleSheet(
            "background-color:#6200ea; color:whit                                                                   e; font-size:24px; font-weight:bold; padding:15px;"
        )
        self.header.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.header)

        # language selection
        lang_layout = QHBoxLayout()
        lang_label = QLabel("🌐 Target Language:")
        lang_label.setStyleSheet("font-weight:bold; font-size:14px;")
        lang_layout.addWidget(lang_label)

        self.lang_combo = QComboBox()
        self.lang_combo.addItems(self.languages)
        self.lang_combo.setCurrentText(self.dst_lang)
        lang_layout.addWidget(self.lang_combo)
        layout.addLayout(lang_layout)

        # theme toggle
        self.theme_checkbox = QCheckBox("🌙 Dark Mode")
        self.theme_checkbox.stateChanged.connect(self.toggle_theme)
        layout.addWidget(self.theme_checkbox)

        # buttons
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("🎧 Start Translating")
        self.start_button.setStyleSheet("background-color:#03dac5; font-weight:bold; padding:10px;")
        self.start_button.clicked.connect(self.start_translation)
        button_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("⏹️ Stop")
        self.stop_button.setStyleSheet("background-color:#ff0266; color:white; font-weight:bold; padding:10px;")
        self.stop_button.clicked.connect(self.stop_translation)
        button_layout.addWidget(self.stop_button)

        self.save_button = QPushButton("💾 Save Transcript")
        self.save_button.setStyleSheet("background-color:#ffd600; font-weight:bold; padding:10px;")
        self.save_button.clicked.connect(self.save_transcript)
        button_layout.addWidget(self.save_button)

        layout.addLayout(button_layout)

        # text area
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setFont(QFont("Consolas", 11))
        self.text_area.setStyleSheet(
            "background-color:#ffffff; color:#212121; border: 1px solid #ccc; padding:5px;"
        )
        layout.addWidget(self.text_area)

        # status
        self.status = QLabel("✅ Ready to translate")
        self.status.setStyleSheet("background-color:#6200ea; color:white; padding:5px;")
        layout.addWidget(self.status)

        self.central.setLayout(layout)

    def start_translation(self):
        recognizer = sr.Recognizer()
        dst_lang = self.lang_combo.currentText()

        try:
            with sr.Microphone() as source:
                self.status.setText("🎧 Listening... please speak")
                self.text_area.append("🎧 Listening...")
                QApplication.processEvents()

                audio = recognizer.listen(source)
                self.status.setText("📝 Recognizing speech...")
                QApplication.processEvents()

                text = recognizer.recognize_google(audio)
                self.status.setText("✅ Speech recognized")
                self.text_area.append(f"🌐 You said: {text}")
                QApplication.processEvents()

                target_code = self.lang_to_code(dst_lang)
                self.status.setText(f"🌐 Translating to {dst_lang}...")
                QApplication.processEvents()

                translated = GoogleTranslator(source='auto', target=target_code).translate(text)
                final = self.preserve_names(text, translated)

                self.text_area.append(f"✅ Translated: {final}")
                self.text_area.append("-" * 70)
                self.status.setText("🔊 Generating audio...")
                QApplication.processEvents()

                tts = gTTS(final, lang=target_code)
                tts.save("translated.mp3")

                self.status.setText("🔊 Playing translation...")
                pygame.mixer.music.load("translated.mp3")
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    QApplication.processEvents()

                os.remove("translated.mp3")
                self.status.setText("✅ Translation completed")
                
        except sr.UnknownValueError:
            QMessageBox.critical(self, "Error", "Could not understand the audio.")
            self.status.setText("⚠️ Audio could not be recognized.")
        except sr.RequestError as e:
            QMessageBox.critical(self, "Error", f"Request error: {e}")
            self.status.setText("⚠️ Request error.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unexpected: {e}")
            self.status.setText("⚠️ Unexpected error occurred.")

    def stop_translation(self):
        pygame.mixer.music.stop()
        self.status.setText("⏹️ Playback stopped")

    def save_transcript(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save Transcript", "transcript.txt", "Text Files (*.txt)")
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self.text_area.toPlainText())
                QMessageBox.information(self, "Saved", f"Transcript saved to {path}")
                self.status.setText("💾 Transcript saved.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save: {e}")
                self.status.setText("⚠️ Error saving transcript.")

    def toggle_theme(self):
        if self.theme_checkbox.isChecked():
            self.dark_mode = True
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor("#121212"))
            palette.setColor(QPalette.WindowText, QColor("#ffffff"))
            palette.setColor(QPalette.Base, QColor("#1e1e1e"))
            palette.setColor(QPalette.Text, QColor("#ffffff"))
            self.setPalette(palette)
            self.text_area.setStyleSheet(
                "background-color:#1e1e1e; color:#ffffff; border: 1px solid #333; padding:5px;"
            )
            self.status.setStyleSheet("background-color:#333333; color:white; padding:5px;")
            self.header.setStyleSheet(
                "background-color:#212121; color:white; font-size:24px; font-weight:bold; padding:15px;"
            )
            self.status.setText("🌙 Dark mode enabled")
        else:
            self.dark_mode = False
            self.setPalette(QApplication.style().standardPalette())
            self.text_area.setStyleSheet(
                "background-color:#ffffff; color:#212121; border: 1px solid #ccc; padding:5px;"
            )
            self.status.setStyleSheet("background-color:#6200ea; color:white; padding:5px;")
            self.header.setStyleSheet(
                "background-color:#6200ea; color:white; font-size:24px; font-weight:bold; padding:15px;"
            )
            self.status.setText("☀️ Light mode enabled")

    def preserve_names(self, original, translated):
        names = [w for w in original.split() if w.istitle()]
        for name in names:
            if name not in translated:
                translated += f" {name}"
        return translated

    def lang_to_code(self, name):
        codes = {
            "english": "en",
            "spanish": "es",
            "french": "fr",
            "german": "de",
            "hindi": "hi",
            "italian": "it"
        }
        return codes.get(name.lower(), "en")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = VoiceTranslator()
    translator.show()
    sys.exit(app.exec_())
