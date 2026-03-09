import base64
from logger import logger
import os


class Analizer:

    def __init__(self):

        self.negative_word_list = self.Get_decoded_word_list(os.path.join(".", "negative_word_list.txt"))
        self.less_negative_word_list = self.Get_decoded_word_list(os.path.join(".", "less_negative_word_list.txt"))

    def Get_decoded_word_list(self, file_path):
        with open(file_path, "r") as f:
            data = f.read().strip()

        decoded_bytes = base64.b64decode(data)

        try:
            decoded_string = decoded_bytes.decode("utf-8")
            return decoded_string.lower().split(",")
        except UnicodeDecodeError:
            logger.error("Decoded data is binary, not UTF-8 text.")

    def bds_percent(self, object):

        text = object.get("file_text", "").lower()

        negative_word = sum(text.count(word) for word in self.negative_word_list)
        less_negative_word = (sum(text.count(word) for word in self.less_negative_word_list) / 2)

        bds_percent = ((negative_word + less_negative_word) / len(text.split())) * 100
        object["bds_percent"] = bds_percent

        threshold = (100 / 3) 
        object["is_bds"] = True if object["bds_percent"] >= threshold else False

        object["bds_threat_level"] = (
            "none" if object["bds_percent"] <= (100 / 3)
            else "medium" if object["bds_percent"] <= ((100 / 3) * 2) 
            else "high"
        )

        return object



