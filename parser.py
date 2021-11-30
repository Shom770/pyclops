from types import GenericAlias


class PyclopsParser:
    """Parses the command-line arguments given the annotations of each function."""

    def __init__(self, command_line_args: list) -> None:
        self.__args__ = command_line_args
        self.grouping = {}

        for argument in self.__args__:
            if argument.startswith("-") or argument.startswith("--"):
                self.grouping[argument] = []
            else:
                last_key = list(self.grouping.keys())
                self.grouping[last_key].append(argument)

    def convert(self, annotations: dict) -> dict:
        """
        Converts the command-line arguments into their respective annotations.

        If the conversion fails, it'll return an empty dictionary.

        Returns:
            dict

        Arguments:
            annotations: a dictionary representing the annotations of the callback function
        """
        for param, annotation in annotations.items():
            if isinstance(annotation, GenericAlias):
                if len(annotation.__args__) > 1:
                    raise TypeError(
                        f"class '{annotation.__origin__.__name__}' should only have one argument for the"
                        f" type hint."
                    )
