# Okims_JSON_Builder

ComfyUI custom node for building structured JSON prompts visually.

## Install

Place this folder here:

```text
ComfyUI/custom_nodes/ComfyUI-Okims_JSON_Builder/
```

Restart ComfyUI.

## Node

```text
Okims/JSON > Okims_JSON_Builder
```

The node shows only:

```text
Open Builder
Copy JSON
```

Open Builder launches the full visual editor. Use **Confirm & Send JSON Prompt** to send the generated JSON prompt back to the ComfyUI node. The node outputs the prompt as a STRING.

## Included editor features

- Visual bbox layout canvas
- Impact Guide and Impact Box creation
- Fixed 10px base grid
- Object/text boxes
- Four-corner resize handles
- Drag, pan, zoom, snap, and impact-grid snap tools
- Layer/order controls
- JSON copy/load/paste/save
- Preset save/load
- User memo tables in help panels
- Multilingual interface
- Theme skins

This node only builds JSON prompts. It does not run an image model by itself.
