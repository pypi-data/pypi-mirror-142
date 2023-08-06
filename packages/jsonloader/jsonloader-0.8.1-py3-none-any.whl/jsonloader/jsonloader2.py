from typing import Dict, Any, Type


def JSONclass(
        cls=None,
        *,
        annotations: bool = False,
        annotations_strict: bool = False,
        annotations_type: bool = False):

    if cls is not None:
        class Child(JSONWrapper, cls):
            pass

        return Child

    else:
        return lambda c: JSONclass(c,
                                   annotations=annotations,
                                   annotations_strict=annotations_strict,
                                   annotations_type=annotations_type)

def _get_attribute(
        value: Any,
        expected_type: Type,
        annotations: bool,
        annotations_strict: bool,
        annotations_type: bool) -> Any:
    """
    Return a built JSONWrapper if expected_type is a JSONWrapper,
    """


class JSONWrapper:
    def __init__(self,
                 data: Dict[str, Any],
                 *,
                 annotations: bool = False,
                 annotations_strict: bool = False,
                 annotations_type: bool = False):
        annotations_c: Dict[str, Type]
        if hasattr(self, '__annotations__'):
            annotations_c = self.__annotations__.copy()
        else:
            annotations_c = {}

        data_c = data.copy()
        for k, v in data.items():
            if k in data_c:
                del data_c[k]
            if k in annotations_c:
                if annotations_type and not isinstance():
                    pass
