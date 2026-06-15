import json


class Okims_JSON_Builder:
    """ComfyUI node that outputs the JSON prompt created by the visual builder."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_prompt": (
                    "STRING",
                    {
                        "multiline": False,
                        "default": json.dumps(
                            {
                                "high_level_description": "",
                                "style_description": {
                                    "medium": "photograph",
                                    "aesthetics": "",
                                    "lighting": "",
                                    "photo": ""
                                },
                                "compositional_deconstruction": {
                                    "background": "",
                                    "elements": []
                                }
                            },
                            ensure_ascii=False,
                            indent=2,
                        ),
                    },
                )
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("json_prompt",)
    FUNCTION = "build"
    CATEGORY = "Okims/JSON"

    def build(self, json_prompt: str):
        if json_prompt is None:
            json_prompt = ""
        return (str(json_prompt),)


NODE_CLASS_MAPPINGS = {
    "Okims_JSON_Builder": Okims_JSON_Builder,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Okims_JSON_Builder": "Okims_JSON_Builder",
}
