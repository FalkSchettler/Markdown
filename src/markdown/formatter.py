import re


class Formatter:

    @staticmethod
    def remove_empty_lines_and_breaks(row: list) -> list:

        formatted_row = list()
        for col in row:
            formatted_row.append(
                " ".join([line for line in col.splitlines() if line.strip()])
            )

        return formatted_row

    @staticmethod
    def string_to_anchor_id(name):
        # Entferne ungültige Zeichen für HTML-IDs und ersetze Leerzeichen durch Bindestriche
        valid_id = re.sub(r"[^a-zA-Z0-9_\-]", "", name.replace(" ", "-"))
        return valid_id

    @staticmethod
    def remove_line_breaks(text: str) -> str:
        """
        Remove line breaks from the given text.
        Args:
            text (str): The input text from which to remove line breaks.
        Returns:
            str: The text with line breaks removed.
        """

        return " ".join([line for line in text.splitlines() if line.strip()])
